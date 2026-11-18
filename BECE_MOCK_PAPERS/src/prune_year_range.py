"""Quarantine CAD / Computing_ICT files outside the year window (2019 → ∞).

Current policy: papers must be from 2019 onward; 2027, 2028, ... future seasons
are all valid. Only pre-2019 content is quarantined.

- Moves flagged files to data/harvested/OutOfRange/
- Updates harvested_files.local_path in catalog.db
- Tombstones their SHA-256 in rejected_content (reason=out_of_year_range) so the
  harvester never re-downloads identical bytes
- Deduplicates near-identical .txt articles within range (normalized body hash),
  keeping the oldest and tombstoning the rest as duplicates
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import sqlite3
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
HARVESTED = REPO_ROOT / "data" / "harvested"
OUTDIR = HARVESTED / "OutOfRange"
DB_PATH = REPO_ROOT / "data" / "metadata" / "catalog.db"

# Year window: 2019 onward, NO upper cap (2027, 2028... all valid seasons).
YEAR_MIN = 2019
YEAR_MAX = None  # unrestricted future years are allowed

# Files whose *content* year is outside the window (matched by filename substring)
OUT_OF_RANGE_PATTERNS = [
    "2010-2017-home-economics",      # CDT_CAD compilation of 2010-2017 HE papers
    "2010-2017-pretech-skills",      # CDT_CAD compilation of 2010-2017 PreTech papers
    "Computing_ICT_2012_",           # ICT 2012 pasco txt
    "Computing_ICT_Computing_2013_", # Computing 2013 txt
    "Computing_ICT_Computing_2015_", # Computing 2015 txt
    "ICT_2014_Qu_and_Ans",           # ICT 2014 document + docx conversion
]

REJECT_REASON = "out_of_year_range"


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main(out: dict) -> None:
    conn = sqlite3.connect(DB_PATH)
    moved, deduped = [], []

    # DB content-year ground truth per local_path (backfill / pipeline hook)
    path_year: dict[str, int] = {}
    try:
        for row in conn.execute(
            "SELECT local_path, content_year FROM harvested_files WHERE content_year IS NOT NULL;"
        ).fetchall():
            path_year[row[0]] = row[1]
    except sqlite3.OperationalError:
        pass

    # ---- 1. Move out-of-range files ----
    for subject in ("CAD", "Computing_ICT"):
        subject_dir = HARVESTED / subject
        if not subject_dir.exists():
            continue
        for f in subject_dir.rglob("*"):
            if not f.is_file():
                continue
            # Heading year (DB content_year) wins; filename pattern as fallback
            yr = path_year.get(str(f))
            if yr is not None:
                triggered = yr < YEAR_MIN or (YEAR_MAX is not None and yr > YEAR_MAX)
                out_reason = (
                    f"heading year {yr} outside {YEAR_MIN}-{YEAR_MAX if YEAR_MAX else '∞'}"
                )
            else:
                triggered = any(pat in f.name for pat in OUT_OF_RANGE_PATTERNS)
                out_reason = "filename year-pattern"
            if not triggered:
                continue
            dest_dir = OUTDIR / subject / f.parent.name
            dest_dir.mkdir(parents=True, exist_ok=True)
            dest = dest_dir / f.name
            if dest.exists():
                dest = dest_dir / f"{f.stem}_{f.suffix}"
            shutil.move(str(f), dest)
            digest = sha256_file(dest)
            conn.execute("UPDATE harvested_files SET local_path = ? WHERE local_path = ?;", (str(dest), str(f)))
            conn.execute(
                "INSERT OR IGNORE INTO rejected_content (sha256, original_url, file_name, file_type, reason, details, decided_at)"
                " VALUES (?, ?, ?, ?, ?, ?, datetime('now'));",
                (digest, "", f.name, f.suffix, REJECT_REASON, out_reason),
            )
            moved.append({"file": f.name, "from": subject, "reason": out_reason})

    # ---- 2. In-range duplicate detection for .txt articles ----
    by_body: dict[str, list[Path]] = {}
    for f in (HARVESTED / "Computing_ICT" / "txt").rglob("*.txt"):
        text = f.read_text(encoding="utf-8", errors="ignore")
        # strip pipeline header (SOURCE URL / TITLE / SUBJECT) then normalize
        body = re.sub(r"^(SOURCE URL|TITLE|SUBJECT|={5,}).*$", "", text, flags=re.M)
        body = re.sub(r"\s+", " ", body).lower().strip()
        digest_sha = hashlib.sha256(body.encode("utf-8")).hexdigest()
        by_body.setdefault(digest_sha, []).append(f)

    for group in by_body.values():
        if len(group) < 2:
            continue
        group.sort(key=lambda p: p.stat().st_mtime)
        for dup in group[1:]:
            digest = sha256_file(dup)
            if conn.execute("SELECT 1 FROM rejected_content WHERE sha256 = ?;", (digest,)).fetchone():
                continue
            dest = OUTDIR / "Computing_ICT" / "txt" / dup.name
            dest.parent.mkdir(parents=True, exist_ok=True)
            if dest.exists():
                dest = dest.with_suffix(f".{_dup_id(dup)}{dup.suffix}")
            shutil.move(str(dup), dest)
            conn.execute("UPDATE harvested_files SET local_path = ? WHERE local_path = ?;", (str(dest), str(dup)))
            conn.execute(
                "INSERT OR IGNORE INTO rejected_content (sha256, original_url, file_name, file_type, reason, details, decided_at)"
                " VALUES (?, ?, ?, ?, 'duplicate', 'normalized-text identical to earlier txt', datetime('now'));",
                (digest, "", dup.name, ".txt"),
            )
            deduped.append(dup.name)

    conn.commit()
    conn.close()
    out["moved_out_of_range"] = moved
    out["deduped"] = deduped


def _dup_id(p: Path) -> str:
    return hashlib.sha256(p.name.encode()).hexdigest()[:6]


if __name__ == "__main__":
    result = {}
    main(result)
    print(json.dumps(result, indent=2))
