#!/usr/bin/env python3
"""Backfill exam year for Computing_ICT questions whose source year was never tagged.

Evidence-based mapping source_file -> exam year:
 - Titled past-question pages ("Computing 2013 — BECE Past Questions") -> that title year.
 - Folder-convention files ("Computing_ICT_<batch>_<exam YEAR detail>") -> the exam year
   named inside the label (e.g. 2021_ICT-2019 = 2019 paper, 2021_BECE-ICT-2020 = 2020 paper).
 - Content-identified PDFs (uc_d45488d0 header says "2022 SAMPLE MOCK QUESTIONS") -> that year.
Files with no reliable year evidence (uc_3582a795, BestBrain aggregate, etc.) stay untagged.

Flow: extracted_questions.year -> question_occurrences.year (join original_id)
                             -> questions.year (only where year IS NULL).
"""
from __future__ import annotations

import sqlite3
from pathlib import Path

DB_PATH = Path(r"W:\StaralexSchoolStudies\BECE_MOCK_PAPERS\data\metadata\catalog.db")

# suffix of source_file (hash tail) -> exam year
YEAR_BY_SUFFIX: dict[str, int] = {
    "fae362a3": 2012,  # 2012 BECE ICT Pasco questions with answers
    "15e6f5de": 2013,  # Computing 2013 — BECE Past Questions
    "95d92336": 2015,  # Computing 2015 — BECE Past Questions
    "f2cdf945": 2019,  # 2021 batch docx holding the ICT-2019 paper
    "3963716f": 2021,  # Computing 2021 — BECE Past Questions
    "6c7dde33": 2022,  # ICT-BECE-2022 pdf (harvest batch 2023) — not yet extracted, harmless
    "b6754594": 2022,  # GhLearner Download 2022 BECE Computing Questions
    "d45488d0": 2022,  # uc pdf: header "GHANA EDUCATION NEWS 2022 SAMPLE MOCK QUESTIONS"
    "e5e552b7": 2023,  # 2023 BECE ICT Objective Test Questions
    "d7b8b699": 2023,  # 2023 Likely BECE ICT Questions And Answers
    "e1044fc8": 2020,  # BECE-ICT-2020-QUESTIONS pdf (harvest batch 2021) — not yet extracted
    "735229ee": 2021,  # ICT-BECE-private-2021 pdf — not yet extracted
    "16039b45": 2021,  # 2021-BECE-ICT pdf (harvest batch 2022) — not yet extracted
    "01ac21ac": 2025,  # 2025 SUPER MOCK B marking scheme
}


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    with conn:
        # 1) Tag extracted_questions rows
        tagged_eq = 0
        rows = conn.execute(
            "SELECT id, year, source_file FROM extracted_questions WHERE subject='Computing_ICT'"
        ).fetchall()
        for r in rows:
            if r["year"] is not None:
                continue
            src = r["source_file"] or ""
            hit = next((y for sfx, y in YEAR_BY_SUFFIX.items() if src.endswith(sfx) or sfx in src), None)
            if hit is not None:
                conn.execute("UPDATE extracted_questions SET year=? WHERE id=?", (hit, r["id"]))
                tagged_eq += 1

        # 2) Tag question_occurrences (join through original_id)
        conn.execute(
            """
            UPDATE question_occurrences
            SET year = (SELECT eq.year FROM extracted_questions eq WHERE eq.id = question_occurrences.original_id)
            WHERE question_id IN (SELECT id FROM questions WHERE subject='Computing_ICT')
              AND year IS NULL
              AND (SELECT eq.year FROM extracted_questions eq WHERE eq.id = question_occurrences.original_id) IS NOT NULL
            """
        )

        # 3) Backfill canonical questions.year only where still unknown
        cur = conn.execute(
            """
            UPDATE questions
            SET year = (
                SELECT qo.year FROM question_occurrences qo
                WHERE qo.question_id = questions.id
                ORDER BY (qo.year IS NULL) ASC, qo.year DESC
                LIMIT 1
            )
            WHERE subject='Computing_ICT'
              AND year IS NULL
              AND EXISTS (
                SELECT 1 FROM question_occurrences qo
                WHERE qo.question_id = questions.id AND qo.year IS NOT NULL
              )
            """
        )
        tagged_q = cur.rowcount

    # report
    print("extracted_questions newly tagged:", tagged_eq)
    print("questions backfilled:", tagged_q)
    for r in conn.execute(
        "SELECT year, count(*) FROM questions WHERE subject='Computing_ICT' GROUP BY year ORDER BY year"
    ):
        print("questions.year", r[0], r[1])


if __name__ == "__main__":
    main()
