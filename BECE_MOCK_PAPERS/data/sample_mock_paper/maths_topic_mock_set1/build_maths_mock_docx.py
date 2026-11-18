# -*- coding: utf-8 -*-
"""
Build the Staralex BECE Mathematics Mock (Paper 2 & Paper 1) as .docx.

Visual formatting mirrors the approved Computing mock
(data/sample_mock_paper/computing/build_computing_mock_docx.py) and the CDT/CAD mock
(creative_arts_and_design/build_cad_mock_docx.py) — A4, Times New Roman, letterhead
cover with logo box + dotted candidate fields + shaded heading bar, PAPER 2 on the
cover page, Paper 1 two-column newspaper body, header page number, footer code stamp,
marking scheme at the end.

Maths-specific authenticity (framing study data/taxonomy/maths_paper_framing_2023_2026.md):
  - Real BECE Mathematics 2&1 timings: Paper 2 = 1 hour, Paper 1 = 1 hour, 2-hour booklet.
  - Paper 2: eight questions (user choice: two added topic questions — transversals
    hard, Pythagoras), answer four, EQUAL marks — NO per-part mark tags
    and NO dotted answer lines (answers go into the answer booklet, as on the real June
    2022/2026 scans). Header carries the authentic three-line instruction block.
  - Paper 1: WAEC rubric with the authentic worked example (3n + 2 = 8 -> D), 40 x 1-mark
    items, options A-D, linked pair (Q33/Q34), diagram items carrying
    'Diagram not drawn to scale'.
  - Diagrams: the 8 approved PNGs from this folder's diagrams/ subfolder (.tex sources
    in data/diagrams/math_redrawn/). No .pdf/.svg intermediates exist.
  - Answer key is FIXED (identical to the companion markdown paper): balanced spread
    A7 B11 C12 D10; the script asserts this exact distribution.

Content: only the topics taught (+ 5 plain-arithmetic filler items) — algebraic
expressions, equations, pattern & sequence, perimeter, construction & bisection of
angles, angles/transversals, properties of triangles, percentages, ratio & proportion,
inequalities, Pythagoras theorem. 12 of the 40 objective items = exactly 30% word
problems. All money in GH₵ to 2 decimal places.
"""
from __future__ import annotations

import re
import shutil
from collections import Counter
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt

HERE = Path(__file__).resolve().parent
FIQ = HERE / "diagrams"
LOGO = HERE / "assets" / "logo_staralex.png"
OUT = HERE / "Staralex_Mathematics_Mock_2027_Paper1_and_2.docx"

if not LOGO.exists():
    # sibling logo lives at ../creative_arts_and_design/assets/logo_staralex.png
    src = HERE.parent / "creative_arts_and_design" / "assets" / "logo_staralex.png"
    LOGO.parent.mkdir(exist_ok=True)
    shutil.copyfile(src, LOGO)

# ----------------------------------------------------------------------------- helpers
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")


def add_runs(par, text: str, italic=False):
    """Render text with **bold** markers as alternating runs."""
    pos = 0
    for m in BOLD_RE.finditer(text):
        if m.start() > pos:
            r = par.add_run(text[pos:m.start()])
            if italic:
                r.italic = True
        rb = par.add_run(m.group(1))
        rb.bold = True
        if italic:
            rb.italic = True
        pos = m.end()
    if pos < len(text):
        r = par.add_run(text[pos:])
        if italic:
            r.italic = True


def line(doc, text="", bold=False, italic=False, align=None, indent=None,
         space_before=0, space_after=2, size=None):
    p = doc.add_paragraph()
    if align:
        p.alignment = align
    pf = p.paragraph_format
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    if indent is not None:
        pf.left_indent = Cm(indent)
    if text:
        if bold:
            r = p.add_run(text)
            r.bold = True
            if italic:
                r.italic = True
        else:
            add_runs(p, text, italic=italic)
    if size:
        for run in p.runs:
            run.font.size = Pt(size)
    return p


def centered(doc, text, bold=True, italic=False, space_before=6, space_after=6, size=None, shaded=False):
    p = line(doc, text, bold=bold, italic=italic, align=WD_ALIGN_PARAGRAPH.CENTER,
             space_before=space_before, space_after=space_after, size=size)
    if shaded:  # grey bar behind the heading, like the approved mock covers
        pPr = p._p.get_or_add_pPr()
        shd = OxmlElement("w:shd")
        shd.set(qn("w:val"), "clear")
        shd.set(qn("w:fill"), "D9D9D9")
        pPr.append(shd)
    return p


def set_cols(section, num):
    sectPr = section._sectPr
    cols = sectPr.find(qn("w:cols"))
    if cols is None:
        cols = OxmlElement("w:cols")
        sectPr.append(cols)
    cols.set(qn("w:num"), str(num))
    cols.set(qn("w:space"), "480")


def nil_borders(cell):
    tcPr = cell._tc.get_or_add_tcPr()
    borders = OxmlElement("w:tcBorders")
    for edge in ("top", "left", "bottom", "right"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "nil")
        borders.append(el)
    tcPr.append(borders)


def box_borders(cell):
    tcPr = cell._tc.get_or_add_tcPr()
    borders = OxmlElement("w:tcBorders")
    for edge in ("top", "left", "bottom", "right"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), "6")
        borders.append(el)
    tcPr.append(borders)


def page_number_header(section):
    """Centered real PAGE field in the page header (later sections inherit)."""
    p = section.header.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    b = OxmlElement("w:fldChar"); b.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText"); instr.set(qn("xml:space"), "preserve"); instr.text = " PAGE "
    e = OxmlElement("w:fldChar"); e.set(qn("w:fldCharType"), "end")
    run._r.append(b); run._r.append(instr); run._r.append(e)


def footer_code(section, code="26/030019/2&1/stx/oct/bece"):
    p = section.footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r = p.add_run(code)
    r.font.size = Pt(9)


def page_break(doc):
    p = doc.add_paragraph()
    p.add_run().add_break(WD_BREAK.PAGE)


def picture(doc, path, width_cm, space_before=4, space_after=6):
    """Centered image in its own paragraph, sized for the current column."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pf = p.paragraph_format
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    p.add_run().add_picture(str(path), width=Cm(width_cm))
    return p


# ----------------------------------------------------------------------------- build
p1_key: list[tuple[int, str]] = []

doc = Document()
normal = doc.styles["Normal"]
normal.font.name = "Times New Roman"
normal.font.size = Pt(11.5)
for section in doc.sections:
    section.page_width, section.page_height = Cm(21.0), Cm(29.7)   # A4 like the real papers
    section.top_margin, section.bottom_margin = Cm(1.8), Cm(1.8)
    section.left_margin, section.right_margin = Cm(2.0), Cm(2.0)

# ------------------------------------------------------------------ cover (CDT letterhead style)
if LOGO.exists():
    head = doc.add_table(rows=1, cols=2)
    head.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_logo, c_school = head.rows[0].cells
    c_logo.width, c_school.width = Cm(6.2), Cm(10.8)
    nil_borders(c_school)
    box_borders(c_logo)
    pl = c_logo.paragraphs[0]
    pl.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pl.add_run().add_picture(str(LOGO), width=Cm(4.6))
    pb = c_logo.add_paragraph()
    pb.alignment = WD_ALIGN_PARAGRAPH.CENTER
    rb = pb.add_run("OCTOBER 2026  ·  MOCK")
    rb.bold = True
    rb.font.size = Pt(10)
    t1 = c_school.paragraphs[0]
    r1 = t1.add_run("STARALEX SCHOOL COMPLEX")
    r1.bold = True
    r1.font.size = Pt(20)
    r1.font.name = "Old English Text MT"
    for t in ("MOTTO: Education is Power. Slogan: Happy Parents Our Pride.",
              "For more info. About the school, please call: 026-2535-502/054-8028-300"):
        p_ = c_school.add_paragraph()
        rr = p_.add_run(t)
        rr.font.size = Pt(10.5)
else:
    centered(doc, "STARALEX SCHOOL COMPLEX", size=20)

line(doc, "", space_after=4)
for label in ["Full Name:", "Index Number:", "Signature:", "Date of Examination:"]:
    line(doc, label + "  " + "." * (84 - len(label)), space_after=2)

centered(doc, "Basic Education Certificate Mock Examination",
                          space_before=10, space_after=2, size=13, shaded=True)
centered(doc, "MATHEMATICS  2&1", space_after=2)
centered(doc, "Essay and Objective: 2 hours", bold=False, space_after=8)

centered(doc, "INSTRUCTIONS TO CANDIDATES", space_before=14, space_after=4)
line(doc, "**Do not** open this booklet until you are told to do so. While you are waiting, read and "
          "observe the following instructions carefully.", italic=True, space_after=6)
line(doc, "Write your **name**, **index number** and **date of examination** in **ink** in the spaces "
          "provided above.", italic=True, space_after=6)
line(doc, "This booklet consists of **two papers**. Answer **Paper 2, which comes first**, in "
          "**your answer booklet** and **Paper 1** on your Objective Test answer sheet. "
          "**Paper 2** will last **1 hour** after which the answer booklet will be collected. "
          "**Do not start Paper 1** until you are told to do so. **Paper 1** will last **1 hour**.",
     italic=True, space_after=6)
line(doc, "The use of calculators is **not** allowed. Rough work may be done on the back of this "
          "booklet.", italic=True, space_after=6)
line(doc, "Any candidate who tears off **any** part of this question paper will be severely penalized. "
          "Whether you answer all the questions in this paper or not, hand in the **entire** question "
          "paper to the invigilator.", italic=True, space_after=6)

# ------------------------------------------------------------------ PAPER 2
centered(doc, "PAPER 2", space_before=16, space_after=0, size=13)
centered(doc, "ESSAY  ·  [60 MARKS]  ·  1 HOUR", space_after=6)
line(doc, "**Answer four questions only.**", space_after=1)
line(doc, "**All questions carry equal marks.**", space_after=1)
line(doc, "**All** working must be clearly shown. Marks will **not** be awarded for **correct** "
          "answers without corresponding working.", space_after=6)


def essay_q(doc, num, intro_or_None, parts, picture_part=None, number=True,
            image_name="diagram_mockset1_straight_line_2x10_3x5.png"):
    """parts = list of (letter, text, subs) with subs = None or [(tag, text), ...].
    NO per-part mark tags, NO answer lines (answers go in the answer booklet).
    number=False continues the same question (used when a table sits between
    its parts) without repeating the question number."""
    first_p = line(doc, "", space_before=14, space_after=2)
    if number:
        r = first_p.add_run(f"{num}.  ")
        r.bold = True
        if intro_or_None:
            add_runs(first_p, intro_or_None)
    for letter, text, subs in parts:
        p = line(doc, "", indent=0.6, space_before=10, space_after=0)
        add_runs(p, f"({letter}) {text}" if text else f"({letter})")
        if subs is not None:
            for tag, stext in subs:
                sp = line(doc, "", indent=1.6, space_before=5, space_after=0)
                add_runs(sp, f"({tag}) {stext}")
        if picture_part == letter:
            line(doc, "", space_after=2)
            picture(doc, FIQ / image_name, 9.6)
            line(doc, "Diagram **not** drawn to scale.", italic=True, align=WD_ALIGN_PARAGRAPH.CENTER,
                 space_after=4)


essay_q(doc, 1, None, [
    ("a", "Expand and simplify: (2y + 1)(y − 4).", None),
    ("b", "Factorise **completely**: 3xy − 6xz − 4y + 8z.", None),
    ("c", "The volume V of a box with a square base of side 2x is given by the relation V = 4x²h.",
     [("i", "Make h the subject of the relation."),
      ("ii", "Find the value of h when V = 108 and x = 3.")]),
])

essay_q(doc, 2, None, [
    ("a", "Solve: (2x + 5)/3 = (x + 7)/2", None),
    ("b", "Solve the inequality 5x − 3 > 2x + 9 and **illustrate** your answer on a number line.", None),
    ("c", "Kofi is three times as old as Esi. In eight years' time, Kofi will be twice as old as Esi. "
          "Find their present ages.", None),
])

essay_q(doc, 3, None, [
    ("a", "Given the relation y = 4x − 1, copy and complete the table of values below:", None),
])

# the y = 4x - 1 table as a bordered grid, like the real essay papers
tab = doc.add_table(rows=2, cols=6)
tab.style = "Table Grid"
tab.alignment = WD_TABLE_ALIGNMENT.CENTER
hdr = ("x", "1", "2", "3", "4", "5")
val = ("y", "3", "**m**", "11", "15", "**n**")
for row, data in ((0, hdr), (1, val)):
    for j, t in enumerate(data):
        cell = tab.rows[row].cells[j]
        cell.width = Cm(2.4 if j == 0 else 1.9)
        p_ = cell.paragraphs[0]
        p_.alignment = WD_ALIGN_PARAGRAPH.CENTER
        add_runs(p_, t)

essay_q(doc, 3, None, [
    ("b", "The first four terms of a sequence are 1, 4, 9, 16, …",
     [("i", "Write down the 5th term."),
      ("ii", "Find the 10th term."),
      ("iii", "State the rule for the sequence.")]),
    ("c", "Yaw reads 15 pages of a storybook on the first day. Each day after that, he reads 4 more "
          "pages than the previous day. How many pages does he read on the 10th day?", None),
], number=False)

essay_q(doc, 4, None, [
    ("a", "In the diagram, PQR is a straight line.",
     [("i", "Find the value of x."),
      ("ii", "Find the larger of the two angles.")]),
    ("b", "The exterior angle of a triangle is 4x° and the two interior opposite angles are "
          "(x + 30)° and (2x − 10)°.",
     [("i", "Find the value of x."),
      ("ii", "Hence, find the size of the exterior angle.")]),
    ("c", "The base angles of an isosceles triangle are (3y − 6)° each, and the apex angle is 30°.",
     [("i", "Find the value of y."),
      ("ii", "Calculate the size of each base angle.")]),
], picture_part="a")

essay_q(doc, 5, None, [
    ("a", "Using a ruler and a pair of compasses only,",
     [("i", "construct an angle of 60° at a point Q;"),
      ("ii", "construct the bisector of this angle.")]),
])

line(doc, "What is the size of each of the two equal parts?", indent=1.6, space_before=6, space_after=0)

essay_q(doc, 5, None, [
    ("b", "A ladder leans against a vertical wall. The foot of the ladder is 5 m from the base of the "
          "wall, and the top of the ladder reaches a window 12 m above the ground.",
     [("i", "Illustrate the information in a diagram."),
      ("ii", "Calculate the length of the ladder.")]),
    ("c", "Calculate the perimeter of the triangle formed by the ladder, the wall and the ground.", None),
], number=False)

essay_q(doc, 6, None, [
    ("a", "In the diagram, AC and DF are parallel lines, and BT and ET form a V-shape between them.",
     [("i", "Calculate the value of the reflex angle y."),
      ("ii", "State one angle relationship you used in (i).")]),
    ("b", "In the diagram, the angle marked (3x − 5)° is the angle between TE and the line DF on the side of F.",
     [("i", "Find the value of x."),
      ("ii", "Calculate the size of the angle FET.")]),
    ("c", "In the diagram, the angle marked (5u − 20)° is the angle between TB and TE on the side facing A and D.",
     [("i", "Find the value of u."),
      ("ii", "Calculate the size of the angle BTE.")]),
], picture_part="a", image_name="diagram_mockset1_transversal_zigzag_algebra.png")

essay_q(doc, 7, None, [
    ("a", "The top of a vertical mast is 26 m above the ground. A support wire runs from the top of "
          "the mast to a peg on the ground 10 m from the foot of the mast.",
     [("i", "Illustrate the information in a diagram."),
      ("ii", "Calculate the length of the wire.")]),
    ("b", "A boat sails 12 km due east from a harbour H to a point P, and then 9 km due north from "
          "P to Q. Calculate the distance from H to Q.", None),
    ("c", "Show that a triangle with sides 7 cm, 24 cm and 25 cm is right-angled.", None),
])

essay_q(doc, 8, None, [
    ("a", "Asana is paid **GH₵ 25.00** per day for picking cashew nuts. If her daily wage increased "
          "by **10%** and she worked for **30** days, how much will she be paid?", None),
    ("b", "Two brothers, Kojo and Yaw, shared **GH₵ 8,100.00** from the sale of their produce in the "
          "ratio 4 : 5.",
     [("i", "Calculate each brother's share."),
      ("ii", "How much more did Yaw receive than Kojo?")]),
    ("c", "A trader bought a bag of rice for **GH₵ 2,500.00** and sold it for **GH₵ 3,250.00**. "
          "Calculate the percentage profit.", None),
])

centered(doc, "END OF ESSAY TEST", bold=True, space_before=16)

# ------------------------------------------------------------------ PAPER 1
page_break(doc)
centered(doc, "PAPER 1", space_after=0, size=13)
centered(doc, "OBJECTIVE TEST  ·  [40 MARKS]  ·  1 HOUR", space_after=10)
line(doc, "**Answer all the questions.**", space_after=4)
line(doc, "Each question is followed by **four** options lettered **A to D**. Find the **correct** "
          "option for **each** question and **shade in pencil** on your answer sheet the answer "
          "space which bears the same letter as the option you have chosen. Give only **one** "
          "answer to **each** question. An example is given below.", space_after=6)
line(doc, "If 3n + 2 = 8, find the value of n.", space_after=2)
line(doc, "A. 10       B. 6       C. 3       D. 2", indent=1.0, space_after=2)
line(doc, "The correct answer is 2, which is lettered **D**, and therefore answer space **D** would "
          "be shaded.", space_after=2)
line(doc, "A ☐      B ☐      C ☐      D ☑", indent=1.0, space_after=6)
line(doc, "**Think carefully before you shade** the answer spaces. **Erase your first answer "
          "completely** and shade the appropriate space for the new answer. **Do all rough work in "
          "this paper.** **Now answer the following questions.**", space_after=12)


def objective(num, stem, opts, image_name=None, ndts=False, width=7.3):
    stem_p = line(doc, "", space_before=8, space_after=2)
    num_run = stem_p.add_run(f"{num}.")
    num_run.bold = True
    add_runs(stem_p, f"  {stem}")
    if image_name:
        picture(doc, FIQ / image_name, width, space_before=2, space_after=2)
        if ndts:
            line(doc, "Diagram **not** drawn to scale.", italic=True, size=10,
                 align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    for j2, opt in enumerate("ABCD"):
        line(doc, f"{opt}. {opts[j2]}", indent=0.5, space_after=1, size=11)
    p1_key.append((num, KEY[num - 1]))


# ---- objective items, options in EXACT display order; key fixed to match the .md paper
# authoritative key, identical to the .md paper (md table: A7 B11 C12 D10)
KEY = list("CBDA CDCB CBDC DCDD BCDD BBAB ACAB DCCD BCBA BCAA".replace(" ", ""))
assert len(KEY) == 40, KEY

ITEMS = []
ITEMS.append(("A trader sold a school bag for **GH₵ 48.00** and made a profit of **20%** on the cost. Find the cost of the bag.",
              ["GH₵ 9.60", "GH₵ 38.40", "GH₵ 40.00", "GH₵ 57.60"]))
ITEMS.append(("Evaluate: −15 − (−20) + (−10)",
              ["−15", "−5", "5", "15"]))
ITEMS.append(("Evaluate: 8.4 × 0.25 ÷ 0.6",
              ["0.35", "14", "35", "3.5"]))
ITEMS.append(("The numbers −9, −5, m, 3, 7, 11 form a pattern in which each number is 4 more than the one before it. Find the value of m.",
              ["−1", "−3", "1", "5"]))
ITEMS.append(("Evaluate: 3¼ + 1⅚",
              ["2⅖", "4 11/12", "5 1/12", "4 1/12"]))
ITEMS.append(("Evaluate: 2⅖ − 1⅔",
              ["8/15", "7/8", "1 4/15", "11/15"]))
ITEMS.append(("If 0.03 × k = 2.4, find k.",
              ["0.072", "0.08", "80", "800"]))
ITEMS.append(("If p = 2 and q = ¾, evaluate p²(q − 1).",
              ["−3", "−1", "1", "3"]))
ITEMS.append(("Express 12.5% as a fraction in its lowest terms.",
              ["1/80", "1/12", "1/8", "1/4"]))
ITEMS.append(("Ama and Kwame shared **GH₵ 45.00** in the ratio 2 : 3. Find **Kwame's** share.",
              ["GH₵ 18.00", "GH₵ 27.00", "GH₵ 45.00", "GH₵ 54.00"]))
ITEMS.append(("Expand and simplify: (x − 2)(x + 4)",
              ["x² + 2x + 8", "x² + 6x − 8", "x² − 2x − 8", "x² + 2x − 8"]))
ITEMS.append(("Simplify: x − 5(3 − 2x) − 12x + 7",
              ["−21x − 8", "3x − 8", "−x − 8", "23x − 8"]))
ITEMS.append(("Factorise: 2pq + 6p − 6q − 18",
              ["2(p + 3)(q − 3)", "(p − 3)(q + 3)", "2(q − 3)(p + 3)", "2(q + 3)(p − 3)"]))
ITEMS.append(("Factorise: 3a²b − 9ab²",
              ["3ab(a − 9b)", "3ab(a + 3b)", "3ab(a − 3b)", "3a²b(1 − 3b)"]))
ITEMS.append(("If m = b² − t, make t the subject of the relation.",
              ["t = m − b²", "t = b² + m", "t = −b² − m", "t = b² − m"]))
ITEMS.append(("Solve: ¾x = 2¼",
              ["9/16", "1⅓", "27/16", "3"]))
ITEMS.append(("Solve: 2(x + 3) − 4 = 12",
              ["4", "5", "7", "11"]))
ITEMS.append(("Ama is three times as old as Kofi. The sum of their ages is 40 years. How old is Ama?",
              ["8 years", "10 years", "30 years", "32 years"]))
ITEMS.append(("Find the 8th term of the sequence 3, 7, 11, …",
              ["29", "33", "35", "31"]))
ITEMS.append(("A relation maps x onto y as follows: 1 → 4, 2 → 2, 3 → 0, 4 → −2, 5 → −4. Which of the following is the rule of the mapping?",
              ["y = −2x + 2", "y = 2x + 2", "y = 6 − x", "y = −2x + 6"]))
ITEMS.append(("Kwaku saves **GH₵ 800.00** in the first month and increases his savings by **GH₵ 50.00** each month. How much will he save in the 6th month?",
              ["GH₵ 1,100.00", "GH₵ 1,050.00", "GH₵ 1,000.00", "GH₵ 1,150.00"]))
ITEMS.append(("A rectangular garden has a perimeter of **66 m**. If the length is twice the width, find the width.",
              ["9 m", "11 m", "22 m", "33 m"]))
ITEMS.append(("The line which intersects two or more parallel lines at different points is called",
              ["a transversal", "a perpendicular", "a bisector", "a median"]))
ITEMS.append(("In the diagram below, the construction shown is for",
              ["constructing a perpendicular", "bisecting an angle", "bisecting a line segment", "constructing 60°"]))
ITEMS.append(("In the diagram, LM and PQ are parallel lines cut by a transversal. Find the value of u.",
              ["40°", "50°", "140°", "220°"]))
ITEMS.append(("When a transversal intersects two parallel lines, the corresponding angles are",
              ["supplementary", "complementary", "equal", "alternate"]))
ITEMS.append(("In the diagram, |AB| = |AC|. Find the value of y.",
              ["36°", "54°", "72°", "108°"]))
ITEMS.append(("In the diagram, PQR is a straight line. Find the value of x.",
              ["32", "34", "36", "38"]))
ITEMS.append(("Kofi marked out a triangular vegetable plot ABC. If angle A = 38° and angle B = 54°, what is the size of angle C?",
              ["78°", "92°", "98°", "88°"]))
ITEMS.append(("Three women contributed money towards a business in the ratio 2 : 3 : 4. The total contribution was **GH₵ 5,400.00**. How much did the woman who contributed the **largest** share pay?",
              ["GH₵ 1,200.00", "GH₵ 1,800.00", "GH₵ 2,400.00", "GH₵ 2,700.00"]))
ITEMS.append(("Two complementary angles are in the ratio 2 : 3. Find the larger angle.",
              ["36°", "45°", "54°", "60°"]))
ITEMS.append(("The cross-section of the roof of a kiosk is an isosceles triangle with apex angle 40°. Find each base angle.",
              ["50°", "60°", "140°", "70°"]))
ITEMS.append(("Find the length |MO|.",
              ["13 cm", "15 cm", "16 cm", "21 cm"]))
ITEMS.append(("Calculate the perimeter of triangle MNO.",
              ["24 cm", "27 cm", "36 cm", "45 cm"]))
ITEMS.append(("Adwoa walked **12 km** due north from her home to the market, and then **5 km** due east to the school. Calculate the shortest distance between her home and the school.",
              ["12 km", "13 km", "17 km", "30 km"]))
ITEMS.append(("Solve: 7 − 2x > 15 − 4x",
              ["x > 4", "x < 4", "x > 11", "x < 8"]))
ITEMS.append(("Which of the following inequalities is represented by the number line below?",
              ["x < 2", "x ≤ 2", "x > 2", "x ≥ 2"]))
ITEMS.append(("A trader bought a basket containing 20 mangoes. **20%** of the mangoes were rotten. How many mangoes were **not** rotten?",
              ["4", "5", "16", "80"]))
ITEMS.append(("A mason mixed sand and cement in the ratio 2 : 5. If the total mass of the mixture is **35 kg**, find the mass of the sand used.",
              ["10 kg", "5 kg", "14 kg", "25 kg"]))
ITEMS.append(("A farmer feeds his **8 goats** with **200 kg** of feed in a week. How many goats can he feed with **500 kg** of feed?",
              ["20 goats", "16 goats", "25 goats", "32 goats"]))
assert len(ITEMS) == 40, len(ITEMS)

# ---- two-column newspaper body for the objective run
sec_body = doc.add_section(WD_SECTION.CONTINUOUS)
set_cols(sec_body, 2)
for sec in doc.sections:
    sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
    sec.top_margin, sec.bottom_margin = Cm(1.8), Cm(1.8)
    sec.left_margin, sec.right_margin = Cm(2.0), Cm(2.0)

LINK_PHRASE_DONE = False
for i, (stem, opts) in enumerate(ITEMS, start=1):
    n = i
    if n == 24:
        objective(n, stem, opts, image_name="diagram_05_angle_bisector_construction.png")
    elif n == 25:
        objective(n, stem, opts, image_name="diagram_mockset1_transversal_cointerior140.png", ndts=True)
    elif n == 27:
        objective(n, stem, opts, image_name="diagram_16_isosceles_exterior_angle.png", ndts=True)
    elif n == 28:
        objective(n, stem, opts, image_name="diagram_mockset1_straight_line_3x5_2x15.png", ndts=True)
    elif n == 33:
        if not LINK_PHRASE_DONE:
            line(doc, "*Use the information below to answer questions **33** and **34**.*",
                 italic=True, space_before=8, space_after=2)
            line(doc, "In the diagram, MNO is a right-angled triangle, right-angled at N, with "
                      "|MN| = 9 cm and |NO| = 12 cm.", space_after=2)
            picture(doc, FIQ / "diagram_mockset1_pythagoras_9_12_x.png", 7.3, space_before=2, space_after=2)
            line(doc, "Diagram **not** drawn to scale.", italic=True, size=10,
                 align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
            LINK_PHRASE_DONE = True
        objective(n, stem, opts, image_name=None)
    elif n == 37:
        objective(n, stem, opts, image_name="diagram_mockset1_number_line_texle2.png")
    else:
        objective(n, stem, opts)

# back to single column for the closing banner
sec_end = doc.add_section(WD_SECTION.CONTINUOUS)
set_cols(sec_end, 1)
centered(doc, "END OF PAPER", space_before=16)

# ------------------------------------------------------------------ header / footer codes
page_number_header(doc.sections[0])
footer_code(doc.sections[0])

# ------------------------------------------------------------------ MARKING SCHEME
page_break(doc)
centered(doc, "MARKING SCHEME — FOR TEACHERS / INVIGILATORS ONLY", space_after=2)
centered(doc, "STARALEX BECE MATHEMATICS MOCK — OCTOBER 2026", space_after=10)
line(doc, "(Method = **M1**, Accuracy = **A1**, Independent result = **B1**; −1 ou/wu or 2 dp, "
          "once only, per paper. Every question = 15 marks; candidates earn four questions × 15 "
          "= 60 marks on Paper 2.)", italic=True, space_after=8)

centered(doc, "PAPER 1 — OBJECTIVE TEST (one mark each = 40 marks)", space_after=6)
for chunk_start in range(0, len(p1_key), 8):
    chunk = p1_key[chunk_start:chunk_start + 8]
    line(doc, "        ".join(f"{n_}. {k_}" for n_, k_ in chunk), space_after=2)

line(doc, "", space_after=8)
centered(doc, "PAPER 2 — ESSAY (any four of the eight questions × 15 marks = 60 marks)", space_after=6)
scheme = [
    ("Question 1 (15 marks)", [
        "1(a) (2y + 1)(y − 4) = 2y² − 8y + y − 4 = **2y² − 7y − 4** — expand both brackets, then collect like terms",
        "1(b) 3x(y − 2z) − 4(y − 2z) = **(y − 2z)(3x − 4)** — group, then take out the common bracket",
        "1(c)(i) **h = V/(4x²)**   1(c)(ii) h = 108 ÷ (4 × 9) = 108 ÷ 36 = **3**",
    ]),
    ("Question 2 (15 marks)", [
        "2(a) 2(2x + 5) = 3(x + 7) → 4x + 10 = 3x + 21 → **x = 11**",
        "2(b) 5x − 2x > 9 + 3 → 3x > 12 → **x > 4**; number line: open circle at 4, arrow to the right",
        "2(c) Esi = e, Kofi = 3e; 3e + 8 = 2(e + 8) → 3e + 8 = 2e + 16 → e = **8**. Esi = **8 years**, Kofi = **24 years**",
    ]),
    ("Question 3 (15 marks)", [
        "3(a) y = 4x − 1: m = 4(2) − 1 = **7**; n = 4(5) − 1 = **19** (full row: 3, 7, 11, 15, 19)",
        "3(b) square numbers 1², 2², 3², 4²: 5th = **25**; 10th = **100**; rule = **n² (square of the term position)**",
        "3(c) 9 increases: 15 + 4 × 9 = **51 pages** (T₁₀ = a + (n − 1)d with a = 15, d = 4)",
    ]),
    ("Question 4 (15 marks)", [
        "4(a) angles on a straight line: (2x + 10) + (3x − 5) = 180 → 5x + 5 = 180 → **x = 35**; "
        "larger angle = 3(35) − 5 = **100°** (the smaller is 80°)",
        "4(b) exterior = sum of interior opposite: (x + 30) + (2x − 10) = 4x → x = **20**; exterior = 4 × 20 = **80°** "
        "(check: 50° + 30° = 80°)",
        "4(c) 2(3y − 6) + 30 = 180 → 6y + 18 = 180 → **y = 27**; each base angle = 3(27) − 6 = **75°** (75 + 75 + 30 = 180)",
    ]),
    ("Question 5 (15 marks)", [
        "5(a) 60° constructed with equal-radius arcs (equilateral-triangle method); bisector through the "
        "second pair of arc crossings; each part = **30°**",
        "5(b)(i) right-angled triangle: wall 12 m, ground 5 m, right angle marked, ladder as hypotenuse",
        "5(b)(ii) x² = 5² + 12² = 25 + 144 = 169 → ladder = **13 m** (5 : 12 : 13 triple)",
        "5(c) perimeter = 5 + 12 + 13 = **30 m**",
    ]),
    ("Question 6 (15 marks)", [
        "6(a)(i) helper parallel through T: 40° alternate at the top arm and 180° − 140° = 40° at "
        "the bottom arm → y = 360° − (40° + 40°) = **280°** (reflex); 6(a)(ii) alternate angles "
        "equal (or co-interior supplementary / angles at a point = 360°)",
        "6(b) angles on a straight line DF: 140 + (3x − 5) = 180 → 3x = 45 → **x = 15** "
        "(or 3x − 5 = 40 by alternate angles at B with the helper at T); angle FET = 3(15) − 5 = **40°**",
        "6(c) angles at a point: BTE = 360° − 280° = **80°** (or 40 + 40 by alternate angles at each arm) "
        "→ 5u − 20 = 80 → **u = 20**; angle BTE = **80°**",
    ]),
    ("Question 7 (15 marks)", [
        "7(a)(i) right-angled triangle: mast 26 m vertical, peg 10 m from the foot on the ground, "
        "right angle marked, wire as hypotenuse",
        "7(a)(ii) x² = 26² − 10² = 676 − 100 = 576 → wire = **24 m** (10 : 24 : 26 = 5 : 12 : 13 "
        "doubled)",
        "7(b) d² = 12² + 9² = 144 + 81 = 225 → distance = **15 km** (3 : 4 : 5 triple)",
        "7(c) squares: 7² = 49, 24² = 576, 25² = 625; 49 + 576 = 25² → the **converse** holds, so "
        "the triangle is right-angled (right angle opposite the 25 cm side)",
    ]),
    ("Question 8 (15 marks)", [
        "8(a) new wage = 110/100 × 25.00 = GH₵ 27.50; total = 27.50 × 30 = **GH₵ 825.00**",
        "8(b) parts = 4 + 5 = 9; Kojo = 4/9 × 8,100.00 = **GH₵ 3,600.00**; Yaw = 5/9 × 8,100.00 = **GH₵ 4,500.00**; "
        "Yaw − Kojo = **GH₵ 900.00**",
        "8(c) profit = 3,250.00 − 2,500.00 = GH₵ 750.00; 750/2,500 × 100 = **30%**",
    ]),
]
for header, points in scheme:
    line(doc, header, bold=True, space_before=8, space_after=2)
    for pt_ in points:
        p = line(doc, "", indent=0.8, space_after=1)
        add_runs(p, "• " + pt_)

line(doc, "", space_after=8)
centered(doc, "PAPER 1 — WORKING NOTES (selected items)", space_after=6)
notes = [
    "1. Cost = selling price ÷ 1.2 = 48.00 ÷ 1.2 = **GH₵ 40.00** (C). GH₵ 57.60 is the opposite direction (buying at 48, selling 20% up).",
    "4. Common difference is 4: m = −5 + 4 = **−1** (A).",
    "7. k = 2.4 ÷ 0.03 = **80** (C); 0.072 multiplies instead of divides.",
    "12. x − 5(3 − 2x) − 12x + 7 = x − 15 + 10x − 12x + 7 = **−x − 8** (C). A dropped the sign on 5(3 − 2x); B dropped it on −12x; D dropped it on both.",
    "13. 2pq + 6p − 6q − 18 = 2p(q + 3) − 6(q + 3) = **2(q + 3)(p − 3)** (D).",
    "16. x = (2¼) ÷ ¾ = **3** (D). 27/16 multiplies ¾ × 2¼ instead of dividing.",
    "20. Each step of x adds −2 to y: **y = −2x + 6** (D).",
    "25. u and 140° are co-interior angles between the parallels: u = 180° − 140° = **40°** (A).",
    "27. Interior base angle = 180° − 108° = 72°, so y = 180° − 2 × 72° = **36°** (A).",
    "28. (3x − 5)° + (2x + 15)° = 180° → 5x + 10 = 180 → x = **34** (B).",
    "33. |MO|² = 9² + 12² = 81 + 144 = 225 → |MO| = **15 cm** (B). 13 cm is the classic 5 : 12 : 13 slip; 21 cm = 9 + 12 added.",
    "34. Perimeter = 9 + 12 + 15 = **36 cm** (C).",
    "35. Shortest distance = hypotenuse: √(12² + 5²) = √169 = **13 km** (B). 17 km = walking path; 30 km = walking path plus hypotenuse.",
    "36. 7 − 2x > 15 − 4x → 7 + 2x > 15 → 2x > 8 → **x > 4** (A).",
    "37. Solid dot at 2 with the ray pointing left (smaller values included): **x ≤ 2** (B).",
    "39. Sand = 2/7 of 35 kg = **10 kg** (A). 14 kg = the error of taking 2/5 of 35.",
    "40. 200 kg feeds 8 goats → 25 kg per goat → 500 ÷ 25 = **20 goats** (A). 25 is the kg-per-goat value mistaken as the answer.",
]
for pt_ in notes:
    p = line(doc, "", indent=0.8, space_after=1)
    add_runs(p, "• " + pt_)

# ------------------------------------------------------------------ save + self-check
doc.save(OUT)
print("saved:", OUT)
counts = Counter(k for _, k in p1_key)
print("Paper 1 key:", " ".join(f"{n}{k}" for n, k in p1_key))
print("key counts:", dict(counts))
assert dict(counts) == {"A": 7, "B": 11, "C": 12, "D": 10}, "key must match the .md paper: A7 B11 C12 D10"

# picture census: 2 essay diagrams + 6 objective diagrams + 1 cover logo == 9 embedded images
inline_shapes = 0
for r in doc.part.rels.values():
    if "image" in r.reltype:
        inline_shapes += 1
print("embedded images:", inline_shapes)
assert inline_shapes == 9, "expected 9 embedded images (2 essay + 6 objective diagrams + logo)"
print("build checks passed")
