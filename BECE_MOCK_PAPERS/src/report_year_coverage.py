"""Print CAD/ICT content-year coverage from heading ground truth."""

import sqlite3
from pathlib import Path

DB = Path(__file__).resolve().parent.parent / "data" / "metadata" / "catalog.db"

conn = sqlite3.connect(DB)
rows = conn.execute(
    """
    SELECT subject, content_year, year_source, COUNT(*)
    FROM harvested_files
    WHERE subject IN ('CAD','Computing_ICT')
      AND local_path LIKE '%harvested%'
      AND local_path NOT LIKE '%OutOfRange%'
      AND content_year IS NOT NULL
    GROUP BY subject, content_year
    ORDER BY subject, content_year;
    """
).fetchall()

print("CONTENT-YEAR coverage (heading ground truth, 2019-onward policy):")
for subject, year, source, n in rows:
    print(f"  {subject:<15} {str(year):<5} n={n:<2} src={source}")

null_n = conn.execute(
    """
    SELECT COUNT(*) FROM harvested_files
    WHERE subject IN ('CAD','Computing_ICT')
      AND local_path LIKE '%harvested%'
      AND local_path NOT LIKE '%OutOfRange%'
      AND content_year IS NULL;
    """
).fetchone()[0]
print(f"no heading year yet (scanned-image PDFs, future OCR): {null_n}")
conn.close()
