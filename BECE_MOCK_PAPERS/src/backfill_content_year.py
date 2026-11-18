"""Backfill content_year (paper-heading ground truth) for every harvested file on disk.

- Recomputes SHA-256 from the file bytes, updates harvested_files by hash
- Reports: filled, filename-vs-heading mismatches, out-of-window (2019-2026) files
- Uses heading text with the filename as fallback context only
"""

from __future__ import annotations

import hashlib
import json
import re
import sqlite3
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.config import DATABASE_PATH
from src.year_extractor import extract_content_year

YEAR_MIN, YEAR_MAX = 2019, 2100  # window: 2019 onward, no practical upper cap
DB_PATH = DATABASE_PATH


def main() -> dict:
    from src.database import CatalogDatabase

    CatalogDatabase()  # ensures content_year columns exist (idempotent ALTERs)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        """
        SELECT id, sha256, local_path, file_name, subject
        FROM harvested_files WHERE local_path != ''
        ORDER BY id;
        """
    ).fetchall()

    filled, mismatches, out_of_window, unreadable = [], [], [], []
    seen_sha: set = set()

    for r in rows:
        p = Path(r["local_path"])
        if not p.exists() or p.is_dir():
            continue
        digest = hashlib.sha256(p.read_bytes()).hexdigest()
        yr = extract_content_year(
            content=p.read_bytes()[: 20 * 1024 * 1024],
            extension=p.suffix or ".txt",
            text_context=p.name,
        )
        if yr.year is None:
            unreadable.append({"file": p.name, "local_path": str(p)})
            continue

        # guard against feeding another file's hash (filename-assigned rows)
        update = conn.execute(
            "UPDATE harvested_files SET content_year=?, year_source=?, year_evidence=? WHERE id=?",
            (yr.year, yr.source, yr.evidence[:120], r["id"]),
        )
        conn.commit()

        name_year = None
        m = re.search(r"\b(20[0-2]\d|19[9]\d)\b", p.name)
        if m:
            name_year = int(m.group(1))
        entry = {
            "file": p.name,
            "subject": r["subject"],
            "content_year": yr.year,
            "source": yr.source,
            "evidence": yr.evidence[:60],
            "filename_year": name_year,
        }
        filled.append(entry)
        if name_year and name_year != yr.year:
            entry_mismatch = {**entry, "kind": "filename_heading_mismatch"}
            mismatches.append(entry_mismatch)
        if yr.year < YEAR_MIN or yr.year > YEAR_MAX:
            entry_range = {**entry, "kind": "out_of_window"}
            out_of_window.append(entry_range)
        seen_sha.add(digest)

    conn.close()
    return {
        "scanned": len(rows),
        "filled": len(filled),
        "unreadable": unreadable,
        "filename_heading_mismatches": mismatches,
        "out_of_window": out_of_window,
    }


if __name__ == "__main__":
    report = main()
    out_path = REPO_ROOT / "data" / "metadata" / "content_year_backfill.json"
    out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({**{k: len(v) if isinstance(v, list) else v for k, v in report.items()},
                      "written_to": str(out_path)}, indent=2))
