# -*- coding: utf-8 -*-
"""Shared WAEC BECE Mock Examination .docx layout & typography helpers.

Centralises A4 page setup, **bold** inline run parsing, OOXML cell/section
primitives, Staralex letterhead covers, Paper 1 WAEC rubrics, two-column
objective layouts, and marking-scheme renderers used by the subject mock
builders under BECE_MOCK_PAPERS/data/sample_mock_paper/.
"""
from __future__ import annotations

import random
import re
from pathlib import Path
from typing import Iterable, Sequence

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt

BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
WML = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

DEFAULT_CANDIDATE_LABELS = (
    "Full Name:",
    "Index Number:",
    "Signature:",
    "Date of Examination:",
)


def configure_a4_sections(doc: Document) -> None:
    """Apply standard WAEC A4 page dimensions and margins to all sections."""
    for section in doc.sections:
        section.page_width, section.page_height = Cm(21.0), Cm(29.7)
        section.top_margin, section.bottom_margin = Cm(1.8), Cm(1.8)
        section.left_margin, section.right_margin = Cm(2.0), Cm(2.0)


def new_waec_doc(font_name: str = "Times New Roman", font_size_pt: float = 11.5) -> Document:
    """Create a fresh A4 WAEC-formatted Document with base Normal style."""
    doc = Document()
    normal = doc.styles["Normal"]
    normal.font.name = font_name
    normal.font.size = Pt(font_size_pt)
    configure_a4_sections(doc)
    return doc


def add_runs(par, text: str, italic: bool = False) -> None:
    """Render text with **bold** markers as alternating runs."""
    pos = 0
    for m in BOLD_RE.finditer(text):
        if m.start() > pos:
            r = par.add_run(text[pos : m.start()])
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


def line(
    doc: Document,
    text: str = "",
    bold: bool = False,
    italic: bool = False,
    align=None,
    indent: float | None = None,
    space_before: float = 0,
    space_after: float = 2,
    size: float | None = None,
):
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


def centered(
    doc: Document,
    text: str,
    bold: bool = True,
    italic: bool = False,
    space_before: float = 6,
    space_after: float = 6,
    size: float | None = None,
    shaded: bool = False,
):
    p = line(
        doc,
        text,
        bold=bold,
        italic=italic,
        align=WD_ALIGN_PARAGRAPH.CENTER,
        space_before=space_before,
        space_after=space_after,
        size=size,
    )
    if shaded:
        pPr = p._p.get_or_add_pPr()
        shd = OxmlElement("w:shd")
        shd.set(qn("w:val"), "clear")
        shd.set(qn("w:fill"), "D9D9D9")
        pPr.append(shd)
    return p


def shaded_heading(doc: Document, text: str, space_before: float = 6, space_after: float = 6):
    return centered(doc, text, size=13, shaded=True, space_before=space_before, space_after=space_after)


def dotted_line(doc: Document, indent: float = 1.4):
    """A printed dotted answer line, as on real WAEC essay pages."""
    return line(doc, "." * 124, space_before=4, space_after=0, indent=indent, size=10.5)


def dotted_rows(doc: Document, n: int, indent: float = 1.5) -> None:
    for _ in range(n):
        dotted_line(doc, indent=indent)


def right_marks(doc: Document, text: str):
    """Right-aligned bold '[n marks]' tag, like real WAEC essay pages."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run(text)
    r.bold = True
    return p


def set_cols(section, num: int, space: str = "480") -> None:
    sectPr = section._sectPr
    cols = sectPr.find(qn("w:cols"))
    if cols is None:
        cols = OxmlElement("w:cols")
        sectPr.append(cols)
    cols.set(qn("w:num"), str(num))
    cols.set(qn("w:space"), space)


def nil_borders(cell) -> None:
    tcPr = cell._tc.get_or_add_tcPr()
    borders = OxmlElement("w:tcBorders")
    for edge in ("top", "left", "bottom", "right"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "nil")
        borders.append(el)
    tcPr.append(borders)


def box_borders(cell, size: str = "6") -> None:
    tcPr = cell._tc.get_or_add_tcPr()
    borders = OxmlElement("w:tcBorders")
    for edge in ("top", "left", "bottom", "right"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), size)
        borders.append(el)
    tcPr.append(borders)


def shade_cell(cell, gray: str = "3F3F3F") -> None:
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), gray)
    tcPr.append(shd)


def page_number_header(section) -> None:
    """Centered real PAGE field in the page header (later sections inherit)."""
    p = section.header.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    b = OxmlElement("w:fldChar")
    b.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = " PAGE "
    e = OxmlElement("w:fldChar")
    e.set(qn("w:fldCharType"), "end")
    run._r.append(b)
    run._r.append(instr)
    run._r.append(e)


def footer_code(section, code: str = "26/1001026/2&1/stx/oct/bece") -> None:
    p = section.footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r = p.add_run(code)
    r.font.size = Pt(9)


def page_break(doc: Document) -> None:
    p = doc.add_paragraph()
    p.add_run().add_break(WD_BREAK.PAGE)


def picture(doc: Document, path: Path | str, width_cm: float, space_before: float = 4, space_after: float = 6):
    """Centered image in its own paragraph, sized for the current column."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pf = p.paragraph_format
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    p.add_run().add_picture(str(path), width=Cm(width_cm))
    return p


def drawing_box(doc: Document, label: str, width_cm: float = 8.0, height_cm: float = 6.0) -> None:
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


def add_staralex_letterhead(
    doc: Document,
    logo_path: Path | None,
    badge_text: str = "OCTOBER 2026  ·  MOCK",
    school_name: str = "STARALEX SCHOOL COMPLEX",
    motto: str = "MOTTO: Education is Power. Slogan: Happy Parents Our Pride.",
    contact: str = "For more info. About the school, please call: 026-2535-502/054-8028-300",
) -> None:
    """Render the standard Staralex logo + letterhead header block."""
    if logo_path and Path(logo_path).exists():
        head = doc.add_table(rows=1, cols=2)
        head.alignment = WD_TABLE_ALIGNMENT.CENTER
        c_logo, c_school = head.rows[0].cells
        c_logo.width, c_school.width = Cm(6.2), Cm(10.8)
        nil_borders(c_school)
        box_borders(c_logo)
        pl = c_logo.paragraphs[0]
        pl.alignment = WD_ALIGN_PARAGRAPH.CENTER
        pl.add_run().add_picture(str(logo_path), width=Cm(4.6))
        pb = c_logo.add_paragraph()
        pb.alignment = WD_ALIGN_PARAGRAPH.CENTER
        rb = pb.add_run(badge_text)
        rb.bold = True
        rb.font.size = Pt(10)
        t1 = c_school.paragraphs[0]
        r1 = t1.add_run(school_name)
        r1.bold = True
        r1.font.size = Pt(20)
        r1.font.name = "Old English Text MT"
        for text in (motto, contact):
            p_ = c_school.add_paragraph()
            rr = p_.add_run(text)
            rr.font.size = Pt(10.5)
    else:
        centered(doc, school_name, size=20)


def add_candidate_fields(
    doc: Document,
    labels: Sequence[str] = DEFAULT_CANDIDATE_LABELS,
    line_width: int = 84,
) -> None:
    line(doc, "", space_after=4)
    for label in labels:
        line(doc, label + "  " + "." * (line_width - len(label)), space_after=2)


def add_paper1_rubric(
    doc: Document,
    duration_label: str,
    sample_stem: str,
    sample_options: str,
    sample_explanation: str,
    sample_shading: str | None = None,
    marks_label: str = "40 MARKS",
    find_phrase: str = "Find out the **correct option**",
) -> None:
    """Render the authentic WAEC Paper 1 Objective Test header and rubric."""
    page_break(doc)
    centered(doc, "PAPER 1", space_after=0, size=13)
    centered(doc, f"OBJECTIVE TEST  ·  [{marks_label}]  ·  {duration_label}", space_after=10)
    line(doc, "**Answer all the questions.**", space_after=4)
    line(
        doc,
        f"Each question is followed by **four** options lettered **A to D**. {find_phrase} "
        "for **each** question and **shade in pencil** on your answer sheet the answer space "
        "which bears the same letter as the option you have chosen. Give only **one** answer to "
        "**each** question. An example is given below.",
        space_after=6,
    )
    line(doc, sample_stem, space_after=2)
    line(doc, sample_options, indent=1.0, space_after=2)
    line(doc, sample_explanation, space_after=2 if sample_shading else 6)
    if sample_shading:
        line(doc, sample_shading, indent=1.0, space_after=6)
    line(
        doc,
        "**Think carefully before you shade** the answer spaces. **Erase your first answer "
        "completely** and shade the appropriate space for the new answer. **Do all rough work in "
        "this paper.** **Now answer the following questions.**",
        space_after=12,
    )


def render_balanced_objectives(
    doc: Document,
    objectives: Sequence[tuple[str, Sequence[str]]],
    rng: random.Random,
    p1_key: list[tuple[int, str]],
) -> None:
    """Render 40 MCQs in 2 columns with a balanced 10×(A,B,C,D) shuffled key."""
    letters = "ABCD"
    letter_pool = list(letters) * (len(objectives) // 4)
    rng.shuffle(letter_pool)
    sec_body = doc.add_section(WD_SECTION.CONTINUOUS)
    set_cols(sec_body, 2)
    configure_a4_sections(doc)

    for i, (stem, opts) in enumerate(objectives, start=1):
        correct, others = opts[0], list(opts[1:])
        full = [correct] + others
        rng.shuffle(full)
        t = letters.index(letter_pool[i - 1])
        j = full.index(correct)
        k = (j - t) % 4
        full = full[k:] + full[:k]
        p1_key.append((i, letters[full.index(correct)]))

        stem_p = line(doc, "", space_before=8, space_after=2)
        num_run = stem_p.add_run(f"{i}.")
        num_run.bold = True
        add_runs(stem_p, f"  {stem}")
        for j2, opt in enumerate(full):
            line(doc, f"{letters[j2]}. {opt}", indent=0.5, space_after=1, size=11)

    sec_end = doc.add_section(WD_SECTION.CONTINUOUS)
    set_cols(sec_end, 1)
    centered(doc, "END OF PAPER", space_before=16)


def render_marking_scheme_p1_key(doc: Document, p1_key: Sequence[tuple[int, str]], per_row: int = 8) -> None:
    centered(doc, "PAPER 1 — OBJECTIVE TEST (one mark each = 40 marks)", space_after=6)
    for chunk_start in range(0, len(p1_key), per_row):
        chunk = p1_key[chunk_start : chunk_start + per_row]
        line(doc, "        ".join(f"{n}. {k}" for n, k in chunk), space_after=2)


def render_marking_scheme_sections(
    doc: Document,
    scheme: Iterable[tuple[str, Sequence[str]]],
) -> None:
    for header, points in scheme:
        line(doc, header, bold=True, space_before=8, space_after=2)
        for pt_ in points:
            p = line(doc, "", indent=0.8, space_after=1)
            add_runs(p, "• " + pt_)
