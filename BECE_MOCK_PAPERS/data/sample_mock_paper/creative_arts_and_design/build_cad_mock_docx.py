# -*- coding: utf-8 -*-
"""
Build the Staralex BECE Creative Arts & Design Mock (Paper 1 & Paper 2) as .docx.

Visual formatting mirrors the approved Computing mock
(data/sample_mock_paper/computing/Staralex_Computing_Mock_2027_Paper1_and_2.docx):
  - Cover with logo box (Oct 2026 Mock) + school letterhead, dotted candidate fields,
    shaded 'Basic Education Certificate Mock Examination' bar, PAPER 2 on page 1.
  - Essay body: bold-number questions, bold scenario keywords, (a)(b) lettered groups,
    (i)(ii)(iii) sub-parts, dotted answer lines, right-aligned '[n marks]' group tags.
  - Drawing boxes for Q1 as bordered empty tables, like real WAEC CAD papers.
  - Paper 1: WAEC rubric + worked example, 40 x 1-mark items, two-column newspaper
    body, options A-D, balanced answer key (10 of each letter, shuffled).
  - Marking scheme: model answers per sub-question; Paper 1 key in rows of 8.
  - Header: centered page number. Footer: 26/1001026/2&1/stx/oct/bece stamp.

CAD Paper 2 structure (true to BECE 2024-2026):
  Section A - VISUAL ART [30] : Q1 compulsory draw-and-render + any one of Q2/Q3.
  Section B - DANCE [15]      : Q4 or Q5.
  Section C - DANCE AND DRAMA [15]: Q6 or Q7.
Content: only the topics taught - dance, creativity, innovation, drama, drawing,
idea development, modelling, principles of design, elements of design.
Style mix: 75% command-verb stems (define/what is/explain/highlight/list/state/state),
25% scenario-based stems (Paper 1: 10 items; Paper 2: Question 2, 15/60 marks).
"""
from __future__ import annotations

import random
import re
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt

OUT = Path(__file__).with_name("CDT_CAD_Staralex_Mock_Oct2026_Paper1and2.docx")
LOGO = Path(__file__).with_name("assets") / "logo_staralex.png"

# ----------------------------------------------------------------------------- helpers
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
WML = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

VERBS = {'what', 'draw', 'draws', 'render', 'shade', 'shades', 'sketch', 'list', 'lists',
         'state', 'states', 'give', 'gives', 'identify', 'identifies', 'explain', 'explains',
         'enumerate', 'enumerates', 'describe', 'describes', 'define', 'defines', 'highlight',
         'highlights', 'name', 'names', 'suggest', 'suggests', 'group', 'notate', 'construct'}
QTY = {'one', 'two', 'three', 'four', 'five', 'six'}


def add_runs(par, text: str, italic=False):
    """Bold only explicit **...** markers - like the approved Computing builder."""
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
    if shaded:  # grey bar behind the heading, like the real mock cover
        pPr = p._p.get_or_add_pPr()
        shd = OxmlElement("w:shd")
        shd.set(qn("w:val"), "clear")
        shd.set(qn("w:fill"), "D9D9D9")
        pPr.append(shd)
    return p


def dotted_line(doc, indent=1.4):
    return line(doc, "." * 124, space_before=4, space_after=0, indent=indent, size=10.5)


def right_marks(doc, text: str):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run(text)
    r.bold = True
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


def page_number_header(section):
    p = section.header.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    b = OxmlElement("w:fldChar"); b.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText"); instr.set(qn("xml:space"), "preserve"); instr.text = " PAGE "
    e = OxmlElement("w:fldChar"); e.set(qn("w:fldCharType"), "end")
    run._r.append(b); run._r.append(instr); run._r.append(e)


def footer_code(section, code="26/1001026/2&1/stx/oct/bece"):
    p = section.footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r = p.add_run(code)
    r.font.size = Pt(9)


def page_break(doc):
    p = doc.add_paragraph()
    p.add_run().add_break(WD_BREAK.PAGE)


def shaded_heading(doc, text, space_before=6, space_after=6):
    return centered(doc, text, size=13, shaded=True, space_before=space_before, space_after=space_after)


def drawing_box(doc, label, width_cm=8.0, height_cm=6.0):
    """Bordered empty drawing box with a label row, like real CAD papers."""
    t = doc.add_table(rows=1, cols=1)
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = t.rows[0].cells[0]
    cell.width = Cm(width_cm)
    trPr = t.rows[0]._tr.get_or_add_trPr()
    trHeight = OxmlElement("w:trHeight")
    trHeight.set(qn("w:val"), str(int(height_cm * 567)))
    trHeight.set(qn("w:hRule"), "atLeast")
    trPr.append(trHeight)
    lab = cell.paragraphs[0].add_run(label)
    lab.bold = True
    lab.font.size = Pt(10)


# ----------------------------------------------------------------------------- essay data
# question = (intro, intro_is_a, groups)
#   group = (letter, letter_text_or_None, subs_or_None, leaf_mark_or_None)
ESSAY = [
    # Q1 - compulsory drawing practical [15]
    (None, False, [
        ("a", "In the space provided, **draw** a **football boot** and **render** it solid (**three tones**) "
              "using the **hatching** technique.", "BOX", 5),
        ("b", "In the spaces provided, **draw** any **two** different objects that are **cylindrical** in "
              "shape. Use the **stippling** technique to **shade** the drawn object in **Box A** and the "
              "**mass shading** technique to **shade** the other in **Box B**.", "BOXES", 10),
    ]),
    # Q2 - THE scenario question (creativity + idea development + design) [15]
    ("Your school has been selected to represent the district in a **creativity and innovation "
     "exhibition**. As a member of the school team, you are required to develop a new product from "
     "**discarded plastic bottles** for the exhibition.\n"
     "As a **Creative Arts and Design learner**:", False, [
        ("a", None, [("i", 4, "In an orderly manner, **list** the first four steps in **idea development**.")], None),
        ("b", None, [("i", 2, "**State** **two** reasons for developing ideas before the production of the product.")], None),
        ("c", None, [("i", 4, "**Identify** **four** elements of design you would apply in the production of the product.")], None),
        ("d", None, [("i", 3, "**Explain** the principle of design you would use to make your product the most noticeable work in the exhibition.")], None),
        ("e", None, [("i", 2, "**Highlight** **two** ways in which the product you have designed shows innovation.")], None),
    ]),
    # Q3 - modelling (command stems) [15]
    (None, False, [
        ("a", None,
         [("i", 3, "**List** **three** materials or tools you would use for the modelling task."),
          ("ii", 3, "**Describe**, in **three** ordered steps, how you would prepare the clay for the task."),
          ("iii", 1, "**Identify** one technique you would use to decorate the finished statue"),
          ("iv", 2, "**State** **two** precautions you would observe during the clay work.")], None),
        ("b", None,
         [("i", 3, "**Explain** the term **modelling** as used in Creative Arts and Design."),
          ("ii", 3, "**Enumerate** **three** techniques used in modelling.")], None),
    ]),
    # Q4 - dance (Section B) [15]
    (None, False, [
        ("a", None, [("i", 2, "**What is** dance?")], None),
        ("b", None, [("i", 3, "**State** **three** purposes for which dances are performed in Ghanaian communities.")], None),
        ("c", "Ghanaian traditional dances belong to different ethnic groups. In the table provided in "
              "your answer booklet, **group** the listed traditional dances under the appropriate headings.\n"
              "DANCES: **Adowa, Bamaaya, Agbadza, Apatampa, Nagla, Kete**.", "TABLE", 6),
        ("d", None, [("i", 4, "**Explain** **two** dance movements a performer would use to show respect and humility before a chief.")], None),
    ]),
    # Q5 - dance elements [15]
    (None, False, [
        ("a", None, [("i", 5, "**List** the **five** elements of dance.")], None),
        ("b", None, [("i", 6, "**Explain** any **three** of the elements listed in 5(a), using appropriate dance examples.")], None),
        ("c", None, [("i", 4, "**State** **two** importance of dance to the health of the Ghanaian youth.")], None),
    ]),
    # Q6 - dance & drama (Section C) [15]
    (None, False, [
        ("a", None, [("i", 2, "**What is** drama?")], None),
        ("b", None,
         [("i", 3, "**State** **three** elements of drama the troupe would use in the performance."),
          ("ii", 2, "**List** **two** roles you would assign to learners in preparing the performance."),
          ("iii", 3, "**State** **three** roles of **dance** in the Ghanaian society."),
          ("iv", 2, "In **not more than four words**, **suggest** a suitable title for the performance."),
          ("v", 2, "**Highlight** **two** ways the performance would educate the audience.")], None),
    ]),
    # Q7 - drama terms + qualities [15]
    (None, False, [
        ("a", None,
         [("i", 6, "**Describe** the following terms as used in drama: costume; audience; mime.")], None),
        ("b", None, [("i", 9, "**Explain** **three** qualities every good dancer or actor should possess.")], None),
    ]),
]

SUB_ROWS = {1: 1, 2: 2, 3: 2, 4: 5, 5: 2, 6: 3, 9: 5}

SECTION_HEADERS = {2: ("SECTION B  [15 MARKS]", "Answer **one** question only from this section."),
                   4: None, 5: ("SECTION C  [15 MARKS]", "Answer **one** question only from this section.")}


def render_question(doc, num, intro, groups):
    first_p = line(doc, "", space_before=14, space_after=2)
    r = first_p.add_run(f"{num}.  ")
    r.bold = True
    if intro:
        for chunk in intro.split("\n"):
            if first_p is None:
                first_p = line(doc, "")
            add_runs(first_p, chunk)
            first_p = None
    for letter, text, special, leaf_mark in groups:
        p = line(doc, "", indent=0.6, space_before=10, space_after=0)
        if text:
            add_runs(p, f"({letter}) {text}")
        else:
            p.add_run(f"({letter})").bold = True
        if special == "BOX":
            line(doc, "", space_after=2)
            drawing_box(doc, "DRAWING SPACE", width_cm=10.0, height_cm=6.5)
            right_marks(doc, f"[{leaf_mark} marks]")
        elif special == "BOXES":
            line(doc, "", space_after=2)
            t = doc.add_table(rows=1, cols=2)
            t.style = "Table Grid"
            t.alignment = WD_TABLE_ALIGNMENT.CENTER
            for cell, lab in zip(t.rows[0].cells, ["BOX A  (stippling)", "BOX B  (mass shading)"]):
                cell.width = Cm(7.6)
                r_ = cell.paragraphs[0].add_run(lab)
                r_.bold = True
                r_.font.size = Pt(10)
            trPr = t.rows[0]._tr.get_or_add_trPr()
            trHeight = OxmlElement("w:trHeight")
            trHeight.set(qn("w:val"), str(int(7.0 * 567)))
            trHeight.set(qn("w:hRule"), "atLeast")
            trPr.append(trHeight)
            right_marks(doc, f"[{leaf_mark} marks]")
        elif special == "TABLE":
            line(doc, "", space_after=2)
            t = doc.add_table(rows=2, cols=3)
            t.style = "Table Grid"
            t.alignment = WD_TABLE_ALIGNMENT.CENTER
            for j, h in enumerate(["AKAN", "EWE", "MOLE-DAGBANI"]):
                r_ = t.rows[0].cells[j].paragraphs[0].add_run(h)
                r_.bold = True
            trPr = t.rows[1]._tr.get_or_add_trPr()
            trHeight = OxmlElement("w:trHeight")
            trHeight.set(qn("w:val"), str(int(4.0 * 567)))
            trHeight.set(qn("w:hRule"), "atLeast")
            trPr.append(trHeight)
            right_marks(doc, f"[{leaf_mark} marks]")
        elif isinstance(special, list):
            for tag, marks, stext in special:
                sp = line(doc, "", indent=1.6, space_before=5, space_after=0)
                add_runs(sp, f"({tag}) {stext}")
                dotted_line(doc, indent=1.8)
                dotted_line(doc, indent=1.8)
                if marks >= 3:
                    dotted_line(doc, indent=1.8)
            right_marks(doc, f"[{sum(m for _, m, _ in special)} marks]")
        else:
            dotted_line(doc, indent=1.8)
            dotted_line(doc, indent=1.8)
            right_marks(doc, f"[{leaf_mark} marks]" if leaf_mark != 1 else "[1 mark]")


# ----------------------------------------------------------------------------- objectives
# (stem, [correct, d1, d2, d3]) - correct stored FIRST; balanced shuffle at build time.
OBJECTIVES = [
    ("The ability to produce **new** and useful ideas, things or solutions from existing materials or situations is called",
     ["creativity", "imitation", "copying", "repetition"]),
    ("Ama collected discarded bottles and bottle caps and turned them into a beautiful flower vase for the classroom. Ama has demonstrated",
     ["innovation", "imitation", "sketching", "observing"]),
    ("Which of the following is the basic unit of design that begins where a pencil touches paper?",
     ["line", "shape", "texture", "colour"]),
    ("A learner drew a watering can, a bucket and a cloth which had been arranged on a table in the art room. This type of drawing is",
     ["still life drawing", "imaginative drawing", "figure drawing", "landscape drawing"]),
    ("The element of design that refers to the surface **feel** of an object is",
     ["texture", "form", "tone", "space"]),
    ("Shading an artwork using series of small dots and speckles is called",
     ["stippling", "hatching", "cross-hatching", "blending"]),
    ("Which of the following shading techniques produces a smooth, even tone **without** any visible pencil strokes?",
     ["mass shading", "stippling", "hatching", "cross-hatching"]),
    ("The space actually occupied by the objects in a composition is described as",
     ["positive space", "negative space", "background", "foreground"]),
    ("A type of balance in which identical objects are placed at equal distances on both sides of a central line is",
     ["formal balance", "radial balance", "informal balance", "asymmetrical balance"]),
    ("Adjoa wants the school emblem to be the first thing people notice in her poster. The principle of design she should apply is",
     ["emphasis", "rhythm", "variety", "movement"]),
    ("The regular repetition of elements of design to create a feeling of movement is",
     ["rhythm", "unity", "proportion", "emphasis"]),
    ("The principle of design that binds **all** parts of an artwork together into one whole is",
     ["harmony", "contrast", "movement", "rhythm"]),
    ("The relationship in **size** between the objects that make up an artwork is",
     ["proportion", "balance", "space", "pattern"]),
    ("The striking difference between light and dark in a work of art is",
     ["contrast", "rhythm", "pattern", "unity"]),
    ("A teacher asked learners to mention as many uses of the calabash as possible within one minute. The creative thinking skill the learners were demonstrating is",
     ["fluency", "flexibility", "originality", "elaboration"]),
    ("Which of the following traits **best** describes a creative person?",
     ["curiosity", "fear of change", "copying everything", "laziness"]),
    ("Before beginning her project, Sena wrote a clear statement of the problem and what she intended to design. The document Sena wrote is a",
     ["design brief", "pencil sketch", "working drawing", "master copy"]),
    ("In idea development, the stage of gathering and studying of **facts** about a problem is",
     ["investigating", "abstracting", "detailing", "presenting"]),
    ("In the idea development process, trying out the design to find out whether it solves the problem identified is",
     ["testing the design", "making the final sketch", "presenting the work", "measuring the material"]),
    ("After modelling a clay pot, Naa put it in a kiln to make it permanent. The process Naa carried out is",
     ["firing", "pinching", "wedging", "slaking"]),
    ("The stage in clay preparation in which clay is kneaded like dough to push out trapped air bubbles is",
     ["wedging", "firing", "glazing", "casting"]),
    ("A modelling method of rolling clay into long ropes and winding them up to build a pot is",
     ["coiling", "pinching", "slabbing", "moulding"]),
    ("The technique whereby a ball of clay is opened by pressing with the thumb and shaped with the fingers is",
     ["pinching", "coiling", "slabbing", "throwing"]),
    ("A flat piece of **even-thickness** clay used for building pottery forms is called a",
     ["slab", "slip", "coil", "kiln"]),
    ("Which of the following is **not** a material for modelling?",
     ["poster colour", "clay", "plasticine", "wax"]),
    ("The course along which a dancer moves across the performance space is",
     ["pathway", "tempo", "dynamic", "gesture"]),
    ("During a traditional performance, a dancer kneels and bows in front of the chief. The movement communicates",
     ["respect and submission", "victory", "anger", "invitation"]),
    ("In African traditional dance, the circular formation mostly represents",
     ["community and togetherness", "war", "power", "loneliness"]),
    ("The organized sequence of events in a drama script is",
     ["plot", "setting", "cast", "prompt"]),
    ("In the school play, an actor put on the beads and cloth of a king. The actor has taken up a",
     ["character", "plot", "setting", "prompt"]),
    ("The spoken words passed between characters in a play are referred to as",
     ["dialogue", "narration", "monologue", "dirge"]),
    ("The message or main idea of a drama is",
     ["theme", "plot", "cast", "scene"]),
    ("The time and place in which the action of a play happens is",
     ["setting", "plot", "theme", "act"]),
    ("A drama performance that relies on body movement and facial expression without spoken words uses",
     ["mime", "chorus", "recitation", "voice over"]),
    ("The set of people watching and listening to a performance is",
     ["audience", "crew", "troupe", "casting"]),
    ("Which of the following is a traditional Ghanaian form of storytelling drama?",
     ["folktale", "telenovela", "opera", "circus"]),
    ("The clothing and accessories worn by actors to fit the roles they take in a play is",
     ["costume", "prop", "make-up", "set"]),
    ("At night, an old man narrated Ananse stories which carried moral messages to village children. The performance described is",
     ["folktale", "concert party", "puppet show", "televangelism"]),
    ("Which of the following **best** describes dance?",
     ["the rhythmic movement of the body usually to music", "the shaping of clay into useful forms",
      "the arranging of colours on a palette", "the writing of drama scripts"]),
    ("An art form that communicates a story through speech, song, movement, costume and gesture before a live audience is",
     ["drama", "painting", "sculpture", "weaving"]),
]

# ----------------------------------------------------------------------------- build
rng = random.Random(20271028)
p1_key: list[tuple[int, str]] = []

doc = Document()
normal = doc.styles["Normal"]
normal.font.name = "Times New Roman"
normal.font.size = Pt(11.5)
for section in doc.sections:
    section.page_width, section.page_height = Cm(21.0), Cm(29.7)
    section.top_margin, section.bottom_margin = Cm(1.8), Cm(1.8)
    section.left_margin, section.right_margin = Cm(2.0), Cm(2.0)

# ------------------------------------------------------------------ cover
if LOGO.exists():
    head = doc.add_table(rows=1, cols=2)
    head.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_logo, c_school = head.rows[0].cells
    c_logo.width, c_school.width = Cm(6.2), Cm(10.8)
    nil_borders(c_school)
    # bordered logo box, like the approved cover
    tcPr = c_logo._tc.get_or_add_tcPr()
    borders = OxmlElement("w:tcBorders")
    for edge in ("top", "left", "bottom", "right"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), "6")
        borders.append(el)
    tcPr.append(borders)
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

shaded_heading(doc, "Basic Education Certificate Mock Examination", space_before=10, space_after=2)
centered(doc, "CREATIVE ARTS AND DESIGN  2&1", space_after=2)
centered(doc, "Essay and Objective: 2 hours 15 minutes", bold=False, space_after=10)

centered(doc, "INSTRUCTIONS TO CANDIDATES", space_before=16, space_after=4)
line(doc, "**Do not** open this booklet until you are told to do so. While you are waiting, read and "
          "observe the following instructions carefully.", italic=True, space_after=6)
line(doc, "Write your **name**, **index number** and **date of examination** in **ink** in the spaces "
          "provided above.", italic=True, space_after=6)
line(doc, "This booklet consists of **two papers**. Answer **Paper 2, which comes first**, in **this "
          "booklet** in the spaces provided and **Paper 1** on your Objective Test answer sheet. "
          "**Paper 2** will last **1 hour 30 minutes** after which it will be collected. "
          "**Do not start Paper 1** until you are told to do so. **Paper 1** will last **45 minutes**.",
     italic=True, space_after=6)
line(doc, "Any candidate who tears off **any** part of this question paper will be severely penalized.",
     italic=True, space_after=6)
line(doc, "Whether you answer all the questions in this paper or not, hand in the **entire** question "
          "paper to the invigilator.", italic=True, space_after=6)

# ------------------------------------------------------------------ PAPER 2
centered(doc, "PAPER 2", space_before=20, space_after=0, size=13)
centered(doc, "ESSAY  ·  [75 MARKS]  ·  1 HOUR 30 MINUTES", space_after=8)
line(doc, "**Answer five questions only: Question 1 [Compulsory] and any other four questions "
          "from Sections A, B and C.**", space_after=2)
line(doc, "**SECTION A - VISUAL ART**", space_after=2)
line(doc, "Answer **Question 1** [Compulsory].", italic=True, space_after=8)

for q_idx, (intro, _is_a, groups) in enumerate(ESSAY, start=1):
    if q_idx == 4:
        centered(doc, "SECTION B - DANCE  [15 MARKS AVAILABLE]", space_before=18, space_after=0)
        line(doc, "Choose your **other** questions from this section and Sections A and C.", italic=True, space_after=4)
    if q_idx == 6:
        centered(doc, "SECTION C - DANCE AND DRAMA  [15 MARKS AVAILABLE]", space_before=18, space_after=0)
        line(doc, "Choose your **other** questions from this section and Sections A and B.", italic=True, space_after=4)
    render_question(doc, q_idx, intro, groups)

centered(doc, "END OF PAPER 2", bold=True, space_before=16)

# ------------------------------------------------------------------ PAPER 1
page_break(doc)
centered(doc, "PAPER 1", space_after=0, size=13)
centered(doc, "OBJECTIVE TEST  ·  [40 MARKS]  ·  45 MINUTES", space_after=10)
line(doc, "**Answer all the questions.**", space_after=4)
line(doc, "Each question is followed by **four** options lettered **A to D**. Find out the **correct "
          "option** for **each** question and **shade in pencil** on your answer sheet the answer "
          "space which bears the same letter as the option you have chosen. Give only **one** answer "
          "to **each** question. An example is given below.", space_after=6)
line(doc, "Which of the following is a technique of applying colour on a surface?", space_after=2)
line(doc, "A. Painting       B. Weaving       C. Carving       D. Moulding", indent=1.0, space_after=2)
line(doc, "The correct answer is **Painting**, which is lettered **A**, and therefore answer space "
          "**A** would be shaded.", space_after=6)
line(doc, "**Think carefully before you shade** the answer spaces. **Erase your first answer "
          "completely** and shade the appropriate space for the new answer. **Do all rough work in "
          "this paper.** **Now answer the following questions.**", space_after=12)

letters = "ABCD"
letter_pool = list(letters) * 10
rng.shuffle(letter_pool)
pattern = letter_pool
sec_body = doc.add_section(WD_SECTION.CONTINUOUS)
set_cols(sec_body, 2)
for sec in doc.sections:
    sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
    sec.top_margin, sec.bottom_margin = Cm(1.8), Cm(1.8)
    sec.left_margin, sec.right_margin = Cm(2.0), Cm(2.0)

for i, (stem, opts) in enumerate(OBJECTIVES, start=1):
    correct, others = opts[0], opts[1:]
    full = [correct] + others
    rng.shuffle(full)
    t = letters.index(pattern[i - 1])
    j = full.index(correct)
    k = (j - t) % 4
    full = full[k:] + full[:k]
    key = letters[full.index(correct)]
    p1_key.append((i, key))

    stem_p = line(doc, "", space_before=8, space_after=2)
    num_run = stem_p.add_run(f"{i}.")
    num_run.bold = True
    add_runs(stem_p, f"  {stem}")
    for j2, opt in enumerate(full):
        line(doc, f"{letters[j2]}. {opt}", indent=0.5, space_after=1, size=11)

sec_end = doc.add_section(WD_SECTION.CONTINUOUS)
set_cols(sec_end, 1)
centered(doc, "END OF PAPER", space_before=16)

# ------------------------------------------------------------------ header / footer
page_number_header(doc.sections[0])
footer_code(doc.sections[0])

# ------------------------------------------------------------------ marking scheme
page_break(doc)
centered(doc, "MARKING SCHEME — FOR TEACHERS / INVIGILATORS ONLY", space_after=2)
centered(doc, "STARALEX BECE CREATIVE ARTS AND DESIGN MOCK, OCTOBER 2026", space_after=10)

centered(doc, "PAPER 1 — OBJECTIVE TEST (one mark each = 40 marks)", space_after=6)
for chunk_start in range(0, len(p1_key), 8):
    chunk = p1_key[chunk_start:chunk_start + 8]
    line(doc, "        ".join(f"{n}. {k}" for n, k in chunk), space_after=2)

centered(doc, "PAPER 2 — ESSAY (Question 1 + any four of Questions 2–7 = 75 marks)", space_before=10, space_after=6)
scheme = [
    ("Question 1 (15 marks)", [
        "1(a) A football boot drawn with correct proportion and outline 1 mark; three tones 2 marks; correct hatching (parallel lines closer together in dark areas, wider in light areas) 2 marks — 5 marks",
        "1(b) Any two cylindrical objects, e.g. tin can, water bottle, drum, pencil holder, cup, pipe, pillar — 1 mark each = 2 marks",
        "Box A: dots closely clustered for dark areas and spread out for light areas (stippling) — 4 marks",
        "Box B: smooth, even tone with no visible pencil strokes; light source consistent (mass shading) — 4 marks",
    ]),
    ("Question 2 (15 marks) — scenario on creativity, idea development and design", [
        "2(a) Four steps in order, 1 mark each: (1) identify the problem or need; (2) investigate/gather information about the problem; (3) generate possible solutions/sketch initial ideas; (4) select and develop the best idea (5) make the product — 4 marks",
        "2(b) Any two @ 1 mark each: it saves time and materials; it avoids costly mistakes; it produces a better finished product; it guides the making process — 2 marks",
        "2(c) Any four @ 1 mark each: line; shape; colour; texture; space; form; tone/value — 4 marks",
        "2(d) Emphasis (focal point): the-most-noticeable feature is made to stand out through size, contrast, colour or placement; explain briefly — 3 marks",
        "2(e) Any two @ 1 mark each: turning discarded bottles into a new useful product; a new/novel design or function; an unusual combination of materials; a creative finishing technique — 2 marks",
    ]),
    ("Question 3 (15 marks) — modelling", [
        "3(a)(i) Any three @ 1 mark each: clay; water; modelling/pottery tools; knife; board or wheel; kiln; sponge — 3 marks",
        "3(a)(ii) Three ordered steps: wedge/knead the clay to remove air bubbles; add or remove water to reach workable consistency; shape and smooth the model — 3 marks",
        "3(a)(iii) Any one: incising; burnishing; glazing; painting; sprigging; sgraffito — 1 mark",
        "3(a)(iv) Any two @ 1 mark each: wash hands and cut nails before work; be careful with sharp modelling tools; keep clay and water away from polished surfaces; tie back long hair — 2 marks",
        "3(b)(i) Modelling is the technique of shaping a soft, pliable material such as clay or plasticine into a solid three-dimensional form by hand or with tools — 3 marks",
        "3(b)(ii) Any three @ 1 mark each: pinching; coiling; slab building; sculpting/carving into the mass; moulding with a press — 3 marks",
    ]),
    ("Question 4 (15 marks) — dance", [
        "4(a) Dance is the rhythmic movement of the body, usually to music, to express ideas, feelings or tell a story — 2 marks",
        "4(b) Any three @ 1 mark each: for ceremonies (festivals, funerals, weddings); for entertainment; for worship/rituals; for education and moral lessons; for physical fitness; to preserve culture — 3 marks",
        "4(c) AKAN: Adowa, Apatampa, Kete; EWE: Agbadza; MOLE-DAGBANI: Bamaaya, Nagla — 1 mark each placement = 6 marks",
        "4(d) Any two @ 2 marks each: kneeling or bowing to the chief (submission and respect); slow, dignified, controlled steps (humility); smiling and greeting gestures (reverence); soft/low body carriage — 4 marks",
    ]),
    ("Question 5 (15 marks) — elements of dance", [
        "5(a) Body, action, space, time, energy — 1 mark each = 5 marks",
        "5(b) Any three @ 2 marks each with an example: Body - parts of body used, e.g. stamping feet in kpanlogo; Action - locomotor and non-locomotor movements such as bending, jumping, stepping; Space - levels, directions and pathways the dancer travels; Time - rhythm/speed/beat of the movements; Energy - force/quality, sharp vs smooth — 6 marks",
        "5(c) Any two @ 2 marks each: keeps the body physically fit and healthy; relieves stress/refreshes the mind; builds confidence and social skills — 4 marks",
    ]),
    ("Question 6 (15 marks) — dance and drama", [
        "6(a) Drama is an art form in which actors perform a story through speech, action, song, movement, costume and gesture before an audience — 2 marks",
        "6(b)(i) Any three @ 1 mark each: plot; character; dialogue; setting; costume; mime; audience — 3 marks",
        "6(b)(ii) Any two @ 1 mark each: director; choreographer; scriptwriter/playwright; actors/dancers; drummers; costume designer — 2 marks",
        "6(b)(iii) Any three @ 1 mark each: preserves culture and history; entertains at festivals, funerals and weddings; promotes physical fitness and health; unites the community; accompanies ceremonies and rituals; educates through movement — 3 marks",
        "6(b)(iv) e.g. Stop Galamsey Now (any suitable title not more than four words) — 2 marks",
        "6(b)(v) Any two @ 1 point each: it shows the dangers/destruction caused by illegal mining; it teaches protection of water bodies and land; it inspires patriotism — 2 marks",
    ]),
    ("Question 7 (15 marks) — drama terms + qualities", [
        "7(a) 2 marks each: Costume - clothing and accessories worn by actors that fit the role taken; Audience - the set of people watching and listening to the performance; Mime - acting out a story with body movements and facial expressions without speaking — 6 marks",
        "7(b) Any three @ 3 marks each (state and explain): good memory/retention of lines and steps; discipline and punctuality; expressiveness/creativity; confidence; teamwork/cooperation; good body posture and coordination — 9 marks",
    ]),
]
for header, points in scheme:
    line(doc, header, bold=True, space_before=8, space_after=2)
    for pt_ in points:
        p = line(doc, "", indent=0.8, space_after=1)
        add_runs(p, "• " + pt_)

doc.save(OUT)
from collections import Counter
print("saved:", OUT)
print("Paper 1 key:", " ".join(f"{n}{k}" for n, k in p1_key))
print("key counts:", Counter(k for _, k in p1_key))
