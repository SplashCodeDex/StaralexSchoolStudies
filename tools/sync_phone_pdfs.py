#!/usr/bin/env python3
"""Incrementally sync StaralexSchoolStudies PDFs to an Android phone over ADB.

Usage:
    .venv\\Scripts\\python.exe tools\\sync_phone_pdfs.py
    .venv\\Scripts\\python.exe tools\\sync_phone_pdfs.py --dry-run
    .venv\\Scripts\\python.exe tools\\sync_phone_pdfs.py --export-mocks
    .venv\\Scripts\\python.exe tools\\sync_phone_pdfs.py --target 10.79.49.188:5555
"""
from __future__ import annotations

import argparse
import hashlib
import os
import pathlib
import shlex
import subprocess
import tempfile

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_TARGET = "10.79.49.188:5555"
DEFAULT_REMOTE_ROOT = "/sdcard/StaralexSchoolStudies"
SKIP_DIRS = {".venv", ".git", "__pycache__", "node_modules"}

DUPLICATE_CURRICULUM: dict[str, str] = {}

HARVESTED_SUBJ_MAP = {
    "Mathematics": "Mathematics",
    "Computing_ICT": "Computing-ICT",
    "CAD": "CAD",
}

MOCK_DOCX_SOURCES = [
    "BECE_MOCK_PAPERS/data/sample_mock_paper/computing/Staralex_Computing_Mock_2027_Paper1_and_2.docx",
    "BECE_MOCK_PAPERS/data/sample_mock_paper/creative_arts_and_design/CDT_CAD_Staralex_Mock_Oct2026_Paper1and2.docx",
    "BECE_MOCK_PAPERS/data/sample_mock_paper/maths_topic_mock_set1/Staralex_Mathematics_Mock_2027_Paper1_and_2.docx",
]


def sha256_file(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def map_dest(rel: pathlib.Path) -> pathlib.Path | None:
    """Map a repo-relative PDF path to its organized destination under remote root."""
    parts = rel.parts
    name = rel.name
    if len(parts) == 2 and parts[0] in ("CAD", "Computing", "Mathematics"):
        return pathlib.Path("01-Lesson-Plans-and-Trackers") / name
    if parts[:2] == ("curriculum", "Upper-Primary"):
        return pathlib.Path("02-Curriculum-NaCCA/Upper-Primary-Maths") / name
    if parts[:2] == ("curriculum", "JHS-B7-B9"):
        return pathlib.Path("02-Curriculum-NaCCA/JHS-B7-B9") / name
    if parts[:3] == ("BECE_MOCK_PAPERS", "data", "curriculum"):
        return pathlib.Path("02-Curriculum-NaCCA/JHS-B7-B9") / name
    if parts[0] == "Upper-Primary" and "Lessons" in parts:
        return pathlib.Path("03-Mathematics-Lessons/Upper-Primary") / parts[1] / name
    if parts[0] == "Mathematics" and len(parts) >= 5:
        # Mathematics/<Strand>/Grade<7|8|9>/<Substrand>/<Lesson>/<file>.pdf
        strand, grade, substrand = parts[1], parts[2], parts[3]
        return pathlib.Path("03-Mathematics-Lessons") / strand / grade / substrand / name
    if parts[0] == "Computing" and len(parts) >= 4:
        # Computing/<Strand>/Grade<7|8|9>/<Lesson>/<file>.pdf
        strand, grade = parts[1], parts[2]
        return pathlib.Path("04-Computing-Lessons") / strand / grade / name
    if parts[0] == "CAD" and len(parts) >= 4:
        # CAD/<Section>/Grade<7|8|9>/<Lesson>/<file>.pdf
        section, grade = parts[1], parts[2]
        return pathlib.Path("05-CAD-Lessons") / section / grade / name
    if parts[:3] == ("BECE_MOCK_PAPERS", "data", "sample_mock_paper"):
        return pathlib.Path("06-BECE-and-Mock-Exams/Staralex-Sample-Mock") / name
    if parts[:3] == ("BECE_MOCK_PAPERS", "data", "harvested"):
        return pathlib.Path("06-BECE-and-Mock-Exams") / HARVESTED_SUBJ_MAP[parts[3]] / name
    raise ValueError(f"Unmapped PDF in repo: {rel}")


def build_manifest(repo_root: pathlib.Path, remote_root: str) -> dict[str, pathlib.Path]:
    """Discover all repo PDFs and return {remote_path: local_path}, verifying deduplication."""
    manifest: dict[str, pathlib.Path] = {}
    for root, dirs, files in os.walk(repo_root):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        for fname in sorted(files):
            if not fname.lower().endswith(".pdf"):
                continue
            local = pathlib.Path(root) / fname
            rel = local.relative_to(repo_root)
            dst_rel = map_dest(rel)
            if dst_rel is None:
                rel_posix = rel.as_posix()
                dup_target = DUPLICATE_CURRICULUM.get(rel_posix)
                if not dup_target or sha256_file(local) != sha256_file(repo_root / dup_target):
                    raise ValueError(f"Unexpected or mismatched duplicate curriculum PDF: {rel_posix}")
                continue
            remote_path = f"{remote_root.rstrip('/')}/{dst_rel.as_posix()}"
            if remote_path in manifest:
                raise ValueError(f"Destination path collision: {remote_path}")
            manifest[remote_path] = local
    return manifest


def export_mocks_via_word(repo_root: pathlib.Path, out_dir: pathlib.Path, remote_root: str) -> dict[str, pathlib.Path]:
    """Export the 3 Staralex mock .docx files to PDF in out_dir using Microsoft Word COM."""
    src_list = [str(repo_root / rel) for rel in MOCK_DOCX_SOURCES if (repo_root / rel).exists()]
    if not src_list:
        return {}
    ps = r"""
$ErrorActionPreference = 'Stop'
$outDir = $env:MOCK_OUT_DIR
$srcs = $env:MOCK_SRCS -split '\|'
$w = New-Object -ComObject Word.Application
$w.Visible = $false
$w.DisplayAlerts = 0
$w.AutomationSecurity = 3
try {
    foreach ($src in $srcs) {
        $dst = Join-Path $outDir ([System.IO.Path]::GetFileNameWithoutExtension($src) + '.pdf')
        $doc = $w.Documents.Open($src, $false, $true, $false, '', '', $false, '', '', 0, 0, $false, $false, 0, $true)
        $doc.ExportAsFixedFormat($dst, 17)
        $doc.Close($false)
    }
} finally {
    $w.Quit()
}
"""
    env = os.environ.copy()
    env["MOCK_OUT_DIR"] = str(out_dir)
    env["MOCK_SRCS"] = "|".join(src_list)
    subprocess.run(["powershell", "-NoProfile", "-Command", ps], env=env, check=True, timeout=60)
    return {
        f"{remote_root.rstrip('/')}/06-BECE-and-Mock-Exams/Staralex-Sample-Mock/{p.name}": p
        for p in sorted(out_dir.glob("*.pdf"))
    }


def ensure_connected(target: str | None) -> str:
    r_devs = subprocess.run(["adb", "devices"], check=True, capture_output=True, text=True)
    online = [
        line.split("\t", 1)[0].strip()
        for line in r_devs.stdout.splitlines()[1:]
        if "\tdevice" in line
    ]
    if target and target in online:
        return target
    if not target and online:
        return online[0]
    cand = target or DEFAULT_TARGET
    if ":" in cand:
        subprocess.run(["adb", "connect", cand], capture_output=True, text=True, timeout=8)
    r = subprocess.run(["adb", "-s", cand, "get-state"], capture_output=True, text=True)
    if r.returncode == 0 and r.stdout.strip() == "device":
        return cand
    if online:
        return online[0]
    raise RuntimeError(f"ADB target {cand} not ready: {r.stderr.strip() or r.stdout.strip()}")


def fetch_phone_hashes(target: str, remote_root: str) -> dict[str, str]:
    cmd = f"mkdir -p {shlex.quote(remote_root)} && find {shlex.quote(remote_root)} -type f -print0 | xargs -0 -r sha256sum"
    r = subprocess.run(["adb", "-s", target, "shell", cmd], check=True, capture_output=True, text=True, encoding="utf-8")
    hashes: dict[str, str] = {}
    for line in r.stdout.splitlines():
        if "  " in line:
            h, path = line.split("  ", 1)
            hashes[path] = h
    return hashes


def main() -> None:
    p = argparse.ArgumentParser(description="Sync StaralexSchoolStudies PDFs incrementally over ADB.")
    p.add_argument("--target", default=None, help=f"ADB serial or IP:port (auto-detects active device, fallback: {DEFAULT_TARGET})")
    p.add_argument("--remote-root", default=DEFAULT_REMOTE_ROOT, help=f"Remote folder (default: {DEFAULT_REMOTE_ROOT})")
    p.add_argument("--export-mocks", action="store_true", help="Also export and sync the 3 Staralex mock .docx papers via Word")
    p.add_argument("--no-prune", action="store_true", help="Do not delete stale remote files or empty directories")
    p.add_argument("--dry-run", action="store_true", help="Print pending relocations, pushes, and prunes without modifying the phone")
    args = p.parse_args()

    manifest = build_manifest(REPO_ROOT, args.remote_root)
    preserved_mocks = {
        f"{args.remote_root.rstrip('/')}/06-BECE-and-Mock-Exams/Staralex-Sample-Mock/{pathlib.Path(s).stem}.pdf"
        for s in MOCK_DOCX_SOURCES
    }

    with tempfile.TemporaryDirectory(prefix="staralex_mocks_") as tmp:
        if args.export_mocks:
            manifest.update(export_mocks_via_word(REPO_ROOT, pathlib.Path(tmp), args.remote_root))

        target = ensure_connected(args.target)
        phone_hashes = fetch_phone_hashes(target, args.remote_root)
        hash_to_existing: dict[str, str] = {}
        for rpath, rhash in phone_hashes.items():
            hash_to_existing.setdefault(rhash, rpath)

        to_relocate: list[tuple[str, str, str]] = []
        to_push: list[tuple[pathlib.Path, str, str]] = []
        for remote_path, local_path in sorted(manifest.items()):
            local_hash = sha256_file(local_path)
            if phone_hashes.get(remote_path) == local_hash:
                continue
            existing_remote = hash_to_existing.get(local_hash)
            if existing_remote and existing_remote != remote_path:
                to_relocate.append((existing_remote, remote_path, local_hash))
            else:
                to_push.append((local_path, remote_path, local_hash))

        allowed_remote = set(manifest.keys()) | preserved_mocks
        to_prune = [] if args.no_prune else sorted(rp for rp in phone_hashes if rp not in allowed_remote)

        up_to_date = len(manifest) - len(to_relocate) - len(to_push)
        print(
            f"Target: {target} | Manifest: {len(manifest)} PDFs | Up-to-date: {up_to_date} | "
            f"On-device relocate: {len(to_relocate)} | To push: {len(to_push)} | To prune: {len(to_prune)}"
        )
        if args.dry_run:
            for src_rp, dst_rp, _ in to_relocate:
                print(f"  [RELOCATE] {src_rp} -> {dst_rp}")
            for local_path, remote_path, _ in to_push:
                print(f"  [PUSH] {local_path} -> {remote_path}")
            for rp in to_prune:
                print(f"  [PRUNE] {rp}")
            return

        all_target_dirs = sorted(
            {rp.rsplit("/", 1)[0] for _, rp, _ in to_relocate}
            | {rp.rsplit("/", 1)[0] for _, rp, _ in to_push}
        )
        if all_target_dirs:
            subprocess.run(
                ["adb", "-s", target, "shell", "mkdir -p " + " ".join(shlex.quote(d) for d in all_target_dirs)],
                check=True,
            )

        if to_relocate:
            cp_cmds = " && ".join(f"cp -f {shlex.quote(src)} {shlex.quote(dst)}" for src, dst, _ in to_relocate)
            subprocess.run(["adb", "-s", target, "shell", cp_cmds], check=True)
            for _, dst_rp, _ in to_relocate:
                print(f"  [RELOCATED] {dst_rp}")

        for local_path, remote_path, _ in to_push:
            rel_arg = os.path.relpath(local_path, REPO_ROOT) if local_path.is_relative_to(REPO_ROOT) else str(local_path)
            r = subprocess.run(["adb", "-s", target, "push", rel_arg, remote_path], cwd=REPO_ROOT, capture_output=True, text=True)
            if r.returncode != 0:
                raise RuntimeError(f"Push failed for {local_path}: {r.stderr.strip() or r.stdout.strip()}")
            print(f"  [PUSHED] {remote_path}")

        if to_prune:
            rm_cmd = "rm -f " + " ".join(shlex.quote(rp) for rp in to_prune)
            subprocess.run(["adb", "-s", target, "shell", rm_cmd], check=True)
            for rp in to_prune:
                print(f"  [PRUNED] {rp}")

        # Always sweep empty directories inside remote_root when pruning is enabled
        if not args.no_prune:
            empty_cmd = f"find {shlex.quote(args.remote_root)} -depth -type d -empty -delete"
            subprocess.run(["adb", "-s", target, "shell", empty_cmd], check=True)

        if to_relocate or to_push or to_prune:
            updated_hashes = fetch_phone_hashes(target, args.remote_root)
            mismatched = [
                rp
                for _, rp, lh in ([(None, d, h) for _, d, h in to_relocate] + to_push)
                if updated_hashes.get(rp) != lh
            ]
            if mismatched:
                raise RuntimeError(f"Checksum mismatch after sync: {mismatched}")
            print(
                f"Verified {len(to_relocate)} relocated + {len(to_push)} pushed file(s) by SHA-256 "
                f"(pruned {len(to_prune)} stale file(s))."
            )


if __name__ == "__main__":
    main()
