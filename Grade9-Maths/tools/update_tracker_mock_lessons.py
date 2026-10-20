#!/usr/bin/env python3
"""Mark delivered mock-driven lesson packages in LESSON_TRACKER.md."""
from pathlib import Path

TRACKER = Path(r"W:\StaralexSchoolStudies\Grade9-Maths\LESSON_TRACKER.md")
text = TRACKER.read_text(encoding="utf-8")

# (unique substring after which the Status line sits, new status block)
REPLACEMENTS = [
    (
        "Place value deduction problems and numerical puzzles.",
        "  - Status: [x] Lesson 1 Delivered (Place Value & Standard Form — 40 Exercises & Worked Solutions)",
        "  - Status: [x] Lesson 1 Delivered (Place Value & Standard Form — PDF live, 40 Exercises & Worked Solutions)",
    ),
    (
        "Constructing and populating 2-set and 3-set Venn diagrams with factor sets and subsets.\n    - Word problems on set relationships (e.g., dual-category surveys, overlapping groups).",
        "  - Status: [ ] Not Started",
        "  - Status: [x] Lesson 2 Delivered (Number Systems & Venn Diagrams — PDF live, 40 Exercises & Worked Solutions)",
    ),
    (
        "Rapid conversion among benchmark fractions, terminating decimals, and percentages (e.g., halves, thirds, quarters, fifths, eighths, tenths).",
        "  - Status: [ ] Not Started",
        "  - Status: [x] Lesson 3 Delivered (Indices, Decimals & Number Operations — PDF live, 40 Exercises & Worked Solutions)",
    ),
    (
        "Rapid conversion among benchmark fractions, terminating decimals, and percentages (e.g., halves, thirds, quarters, fifths, eighths, tenths).",
        "  - Exercise Quota: 8 exercises x 5 questions + worked solutions.",
        "  - Exercise Quota: 8 exercises x 5 questions + worked solutions.",
    ),
]

# Simpler: add a delivery register at the end if not present, and patch known Status lines by day header.
DAY_PATCH = {
    "Day 2: Strand 1, Sub-strand 1 (Part 2)": (
        "  - Status: [ ] Not Started",
        "  - Status: [x] Lesson 2 Delivered (Number Systems & Venn Diagrams — PDF live, 40 Exercises & Worked Solutions)",
    ),
    "Day 3: Strand 1, Sub-strand 2 (Part 1)": (
        "  - Status: [ ] Not Started",
        "  - Status: [x] Lesson 3 Delivered (Indices, Decimals & Number Operations — PDF live, 40 Exercises & Worked Solutions)",
    ),
    "Day 10: Strand 1, Sub-strand 3 (Part 1)": (
        "  - Status: [ ] Not Started",
        "  - Status: [x] Lesson 4 Delivered (Fractions, Decimals & Percentages — PDF live, 40 Exercises & Worked Solutions)",
    ),
    "Day 15: Strand 1, Sub-strand 4 (Part 1)": (
        "  - Status: [ ] Not Started",
        "  - Status: [x] Lesson 5 Delivered (Ratio, Proportion & Financial Maths — PDF live, 40 Exercises & Worked Solutions)",
    ),
    "Day 25: Strand 2, Sub-strand 1 (Part 1)": (
        "  - Status: [ ] Not Started",
        "  - Status: [x] Lesson 6 Delivered (Linear Relations & Gradient — PDF live, 40 Exercises & Worked Solutions)",
    ),
    "Day 29: Strand 2, Sub-strand 2 (Part 1)": (
        "  - Status: [ ] Not Started",
        "  - Status: [x] Lesson 7 Delivered (Algebraic Expressions & Modelling — PDF live, 40 Exercises & Worked Solutions)",
    ),
    "Day 36: Strand 2, Sub-strand 3 (Part 1)": (
        "  - Status: [ ] Not Started",
        "  - Status: [x] Lesson 8 Delivered (Equations & Inequalities — PDF live, 40 Exercises & Worked Solutions)",
    ),
    "Day 45: Strand 3, Sub-strand 2 (Part 1)": (
        "  - Status: [ ] Not Started",
        "  - Status: [x] Lesson 10 Delivered (Circles, Scale & Measurement — PDF live, 40 Exercises & Worked Solutions)",
    ),
    "Day 51: Strand 4, Sub-strand 1 (Part 1)": (
        "  - Status: [ ] Not Started",
        "  - Status: [x] Lesson 12 Delivered (Data & Statistics — PDF live, 40 Exercises & Worked Solutions)",
    ),
    "Day 55: Strand 4, Sub-strand 2 (Part 1)": (
        "  - Status: [ ] Not Started",
        "  - Status: [x] Lesson 13 Delivered (Probability — PDF live, 40 Exercises & Worked Solutions)",
    ),
}

lines = text.splitlines(keepends=True)
out = []
i = 0
n = len(lines)
current_day = None
while i < n:
    line = lines[i]
    out.append(line)
    for key in DAY_PATCH:
        if key in line:
            current_day = key
    if current_day and line.strip().startswith("- Status: [ ] Not Started"):
        old, new = DAY_PATCH[current_day]
        out[-1] = line.replace(old, new)
        current_day = None
    i += 1

text2 = "".join(out)

# Append delivery register
register = """

---

## Mock-Driven Lesson Packages — Delivery Register (October 2026 Mock 0201026/27)

All packages below were produced from the user-supplied BECE Mathematics mock
(`0201026/27`, Paper 2 Essay + Paper 1 Objective). Each package contains a lesson
PDF with ~20 worked examples, 8 exercise sections × 5 questions (all authentic
mock items included, generated questions top up to 40), and full step-by-step
solutions. Generated questions are in the BECE question bank.

| # | Package | Strand / Sub-strand | Mock Qs covered | Status |
| :---: | :--- | :--- | :---: | :---: |
| 1 | Place Value & Standard Form | S1 / Numeration | P2 Q1(a) | Done |
| 2 | Number Systems & Venn Diagrams | S1 / Numeration | P1 Q15, P2 Q5(d) | Done |
| 3 | Indices, Decimals & Number Ops | S1 / Number Operations | P1 Q1/3/9/14/32/33/40, P2 Q5(b)/7(c) | Done |
| 4 | Fractions, Decimals & Percentages | S1 / FDP | P1 Q12/26, P2 Q2(a)/4(c) | Done |
| 5 | Ratio, Proportion & Financial Maths | S1 / Ratio | P1 Q6/22/23, P2 Q1(b)/3(a)/5(c) | Done |
| 6 | Linear Relations & Gradient | S2 / Patterns | P1 Q20/35–37, P2 Q4(b) | Done |
| 7 | Algebraic Expressions & Modelling | S2 / Expressions | P1 Q10/16/17/19/29, P2 Q4(d)/6(a)/6(c) | Done |
| 8 | Equations & Inequalities | S2 / Variables | P1 Q2/4/8/18/25/39, P2 Q3(c)/6(b) | Done |
| 9 | Angles, Parallel Lines & Trigonometry | S3 / Shapes | P1 Q11/27/30/31, P2 Q3(b) | Done |
| 10 | Circles, Scale & Measurement | S3 / Measurement | P1 Q5/24, P2 Q3(d) | Done |
| 11 | Vectors | S3 / Measurement & Vectors | P1 Q13/21/38, P2 Q6(d) | Done |
| 12 | Data & Statistics | S4 / Data | P1 Q7/28/34, P2 Q1(c)/1(d)/2(b)/2(d)/4(a) | Done |
| 13 | Probability | S4 / Probability | P2 Q5(a) | Done |

**Lessons 1 & 2 of Sub-strand 1 Shapes (Polygons; Congruence & Similarity) remain
delivered from the earlier Strand 3 run. Lesson 3 (Angles / Trig) was added for the
mock's parallel-line and right-triangle items.**
"""

if "Mock-Driven Lesson Packages — Delivery Register" not in text2:
    text2 = text2.rstrip() + "\n" + register

TRACKER.write_text(text2, encoding="utf-8")
print("Tracker updated.")
