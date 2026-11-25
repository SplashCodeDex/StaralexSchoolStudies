"""Smoke tests for tools/waec_mock_docx.py shared WAEC mock DOCX helpers."""
from __future__ import annotations

import random
import sys
from collections import Counter
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOLS_DIR = REPO_ROOT / "tools"
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

import waec_mock_docx as wmd  # noqa: E402


def test_new_waec_doc_page_setup_and_style():
    doc = wmd.new_waec_doc()
    normal = doc.styles["Normal"]
    assert normal.font.name == "Times New Roman"
    assert round(normal.font.size.pt, 1) == 11.5
    sec = doc.sections[0]
    assert round(sec.page_width.cm, 1) == 21.0
    assert round(sec.page_height.cm, 1) == 29.7
    assert round(sec.top_margin.cm, 1) == 1.8
    assert round(sec.left_margin.cm, 1) == 2.0


def test_add_runs_parses_bold_and_italic():
    doc = wmd.new_waec_doc()
    p = wmd.line(doc, "Answer **four** questions **only**.", italic=True)
    runs = [(r.text, bool(r.bold), bool(r.italic)) for r in p.runs]
    assert runs == [
        ("Answer ", False, True),
        ("four", True, True),
        (" questions ", False, True),
        ("only", True, True),
        (".", False, True),
    ]


def test_add_paper1_rubric_renders_with_optional_shading():
    doc = wmd.new_waec_doc()
    wmd.add_paper1_rubric(
        doc,
        duration_label="1 HOUR",
        sample_stem="If 3n + 2 = 8, find n.",
        sample_options="A. 10  B. 6  C. 3  D. 2",
        sample_explanation="The correct answer is **D**.",
        sample_shading="A ☐  B ☐  C ☐  D ☑",
    )
    texts = [p.text for p in doc.paragraphs]
    assert any("PAPER 1" in t for t in texts)
    assert any("OBJECTIVE TEST  ·  [40 MARKS]  ·  1 HOUR" in t for t in texts)
    assert any("If 3n + 2 = 8, find n." in t for t in texts)
    assert any("D ☑" in t for t in texts)


def test_render_balanced_objectives_and_docx_roundtrip(tmp_path: Path):
    doc = wmd.new_waec_doc()
    wmd.add_staralex_letterhead(doc, logo_path=None)
    wmd.add_candidate_fields(doc)
    wmd.drawing_box(doc, "Box A", width_cm=7.0, height_cm=4.0)

    objectives = [(f"Question {i} stem?", [f"right_{i}", "d1", "d2", "d3"]) for i in range(1, 41)]
    p1_key: list[tuple[int, str]] = []
    wmd.render_balanced_objectives(doc, objectives, random.Random(2027), p1_key)

    assert len(p1_key) == 40
    assert Counter(k for _, k in p1_key) == {"A": 10, "B": 10, "C": 10, "D": 10}

    # Two-column objective body section followed by single-column closing section
    cols = [sec._sectPr.find(qn("w:cols")) for sec in doc.sections]
    assert any(c is not None and c.get(qn("w:num")) == "2" for c in cols)
    assert cols[-1] is not None and cols[-1].get(qn("w:num")) == "1"

    wmd.page_number_header(doc.sections[0])
    wmd.footer_code(doc.sections[0], code="26/TEST/bece")
    wmd.render_marking_scheme_p1_key(doc, p1_key)
    wmd.render_marking_scheme_sections(doc, [("Question 1 (15 marks)", ["1(a) **Correct** working"])])

    out = tmp_path / "smoke_mock.docx"
    doc.save(out)
    assert out.exists() and out.stat().st_size > 0

    reloaded = Document(out)
    full_text = "\n".join(p.text for p in reloaded.paragraphs)
    assert "END OF PAPER" in full_text
    assert "Question 40 stem?" in full_text
    assert "1(a) Correct working" in full_text
    assert reloaded.sections[0].footer.paragraphs[0].text == "26/TEST/bece"
