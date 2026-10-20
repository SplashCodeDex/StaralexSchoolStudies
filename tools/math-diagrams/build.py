#!/usr/bin/env python3
"""Compile TikZ maths diagram sources to PNG for lesson folders.

Usage:
  python build.py                          # rebuild every catalog entry
  python build.py --only number_line_x_gt_4
  python build.py --tex path/to/file.tex --out path/to/file.png
  python build.py --check                  # list stale/missing outputs

Source layout:
  templates/<id>.tex          standalone TikZ figure (uses styles/mathdiagrams.sty)
  catalog.json                maps id -> output PNG path (absolute or cwd-relative)

Output: PNG at --dpi (default 200), white background, trimmed margins.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
TEMPLATES = ROOT / "templates"
STYLES = ROOT / "styles"
CATALOG = ROOT / "catalog.json"
DEFAULT_DPI = 200


def _ensure_path_env() -> None:
    """Make sure MiKTeX bin is reachable even if launched from a bare shell."""
    miktex = Path(r"C:\Program Files\MiKTeX\miktex\bin\x64")
    if miktex.exists() and str(miktex) not in os.environ.get("PATH", ""):
        os.environ["PATH"] = str(miktex) + os.pathsep + os.environ.get("PATH", "")


def compile_tex(tex_path: Path, out_png: Path, dpi: int = DEFAULT_DPI, also_svg: bool = True) -> None:
    """pdflatex standalone → PDF → trimmed PNG (+ SVG via dvisvgm)."""
    _ensure_path_env()
    tex_path = tex_path.resolve()
    out_png = out_png.resolve()
    if not tex_path.exists():
        raise FileNotFoundError(tex_path)

    with tempfile.TemporaryDirectory(prefix="mdtikz_") as tmp:
        tmp_path = Path(tmp)
        # local copies so \usepackage{mathdiagrams} resolves without TEXINPUTS hacks
        shutil.copy2(tex_path, tmp_path / "figure.tex")
        shutil.copy2(STYLES / "mathdiagrams.sty", tmp_path / "mathdiagrams.sty")

        r = subprocess.run(
            [
                "pdflatex",
                "-interaction=nonstopmode",
                "-halt-on-error",
                "figure.tex",
            ],
            cwd=tmp_path,
            capture_output=True,
            text=True,
            timeout=90,
        )
        pdf = tmp_path / "figure.pdf"
        if r.returncode != 0 or not pdf.exists():
            log = (tmp_path / "figure.log").read_text(encoding="utf-8", errors="replace")
            tail = "\n".join(log.splitlines()[-40:])
            raise RuntimeError(f"pdflatex failed for {tex_path.name}:\n{tail}")

        import pypdfium2 as pdfium

        doc = pdfium.PdfDocument(str(pdf))
        try:
            page = doc[0]
            # pypdfium2 scale is relative to 72 dpi
            bitmap = page.render(scale=dpi / 72.0)
            pil = bitmap.to_pil().convert("RGB")
        finally:
            doc.close()

        out_svg = out_png.with_suffix(".svg")
        if also_svg:
            svg_r = subprocess.run(
                [
                    "dvisvgm",
                    "--pdf",
                    "--no-fonts",
                    "--exact-bbox",
                    f"--output={tmp_path / 'figure.svg'}",
                    str(pdf),
                ],
                cwd=tmp_path,
                capture_output=True,
                text=True,
                timeout=60,
            )
            svg_file = tmp_path / "figure.svg"
            if svg_r.returncode != 0 or not svg_file.exists():
                # keep PNG working even if SVG conversion fails
                print(f"  warn: dvisvgm failed for {tex_path.name}: {svg_r.stderr[-200:]}")
            else:
                out_svg.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(svg_file, out_svg)

    # trim white border
    gray = pil.convert("L")
    mask = gray.point(lambda p: 255 if p < 250 else 0)
    bbox = mask.getbbox()
    if bbox:
        pad = 6
        left = max(0, bbox[0] - pad)
        top = max(0, bbox[1] - pad)
        right = min(pil.width, bbox[2] + pad)
        bottom = min(pil.height, bbox[3] + pad)
        pil = pil.crop((left, top, right, bottom))

    out_png.parent.mkdir(parents=True, exist_ok=True)
    pil.save(out_png, "PNG", optimize=True)


def load_catalog() -> list[dict]:
    if not CATALOG.exists():
        return []
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        data = data.get("diagrams", [])
    return data


def build_entry(entry: dict, dpi: int) -> Path:
    tid = entry["id"]
    tex = ROOT / entry.get("tex", f"templates/{tid}.tex")
    out = Path(entry["out"])
    if not out.is_absolute():
        out = (ROOT.parents[1] / out).resolve()
    print(f"  [{tid}] -> {out} (+ .svg)")
    compile_tex(tex, out, dpi=dpi, also_svg=True)
    return out


def cmd_build(only: str | None, dpi: int) -> int:
    entries = load_catalog()
    if only:
        entries = [e for e in entries if e["id"] == only]
        if not entries:
            print(f"No catalog entry id={only}", file=sys.stderr)
            return 1
    if not entries:
        print("catalog.json is empty — nothing to build", file=sys.stderr)
        return 1
    failed = 0
    for e in entries:
        try:
            build_entry(e, dpi)
        except Exception as exc:  # noqa: BLE001 — report each failure, keep going
            failed += 1
            print(f"  FAIL {e['id']}: {exc}", file=sys.stderr)
    print(f"Done. {len(entries) - failed} ok, {failed} failed.")
    return 1 if failed else 0


def cmd_check() -> int:
    entries = load_catalog()
    missing = []
    for e in entries:
        out = Path(e["out"])
        if not out.is_absolute():
            out = (ROOT.parents[1] / out).resolve()
        tex = ROOT / e.get("tex", f"templates/{e['id']}.tex")
        if not tex.exists():
            missing.append((e["id"], "no tex"))
        elif not out.exists():
            missing.append((e["id"], "no png"))
        elif out.stat().st_mtime < tex.stat().st_mtime:
            missing.append((e["id"], "stale"))
    if not missing:
        print(f"All {len(entries)} catalog outputs up to date.")
        return 0
    for tid, why in missing:
        print(f"  {tid}: {why}")
    return 1


def cmd_build_tex(tex: Path, out: Path, dpi: int) -> int:
    compile_tex(tex, out, dpi=dpi)
    print(f"Wrote {out}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--only", help="build a single catalog id")
    ap.add_argument("--dpi", type=int, default=DEFAULT_DPI)
    ap.add_argument("--check", action="store_true", help="list missing/stale outputs")
    ap.add_argument("--tex", type=Path, help="compile one .tex source")
    ap.add_argument("--out", type=Path, help="output PNG for --tex")
    args = ap.parse_args()

    if args.check:
        return cmd_check()
    if args.tex:
        if not args.out:
            print("--tex requires --out", file=sys.stderr)
            return 2
        return cmd_build_tex(args.tex, args.out, args.dpi)
    return cmd_build(args.only, args.dpi)


if __name__ == "__main__":
    raise SystemExit(main())
