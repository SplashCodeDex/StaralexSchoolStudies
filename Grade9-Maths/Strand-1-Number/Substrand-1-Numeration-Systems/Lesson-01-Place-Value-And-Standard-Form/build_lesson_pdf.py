#!/usr/bin/env python3
"""Render Lesson_01 markdown to PDF via reportlab Platypus."""
from __future__ import annotations

import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

BASE = Path(
    r"W:\StaralexSchoolStudies\Grade9-Maths\Strand-1-Number"
    r"\Substrand-1-Numeration-Systems\Lesson-01-Place-Value-And-Standard-Form"
)
MD = BASE / "Lesson_01_Place_Value_and_Standard_Form.md"
PDF = BASE / "Lesson_01_Place_Value_and_Standard_Form.pdf"

INK = colors.HexColor("#1A1A1A")
ACCENT = colors.HexColor("#1F4E79")
RULE = colors.HexColor("#C5CDD8")
BG_SOFT = colors.HexColor("#F4F7FB")

styles = getSampleStyleSheet()
S = {
    "h1": ParagraphStyle(
        "h1", parent=styles["Heading1"], fontName="Helvetica-Bold",
        fontSize=16, leading=20, textColor=ACCENT, spaceBefore=8, spaceAfter=8,
    ),
    "h2": ParagraphStyle(
        "h2", parent=styles["Heading2"], fontName="Helvetica-Bold",
        fontSize=13, leading=17, textColor=ACCENT, spaceBefore=12, spaceAfter=6,
    ),
    "h3": ParagraphStyle(
        "h3", parent=styles["Heading3"], fontName="Helvetica-Bold",
        fontSize=11, leading=15, textColor=INK, spaceBefore=9, spaceAfter=4,
    ),
    "h4": ParagraphStyle(
        "h4", parent=styles["Heading4"], fontName="Helvetica-Bold",
        fontSize=10, leading=14, textColor=INK, spaceBefore=7, spaceAfter=3,
    ),
    "body": ParagraphStyle(
        "body", parent=styles["BodyText"], fontName="Helvetica",
        fontSize=9.5, leading=13.5, textColor=INK, spaceBefore=2, spaceAfter=4,
        alignment=TA_LEFT,
    ),
    "bullet": ParagraphStyle(
        "bullet", parent=styles["BodyText"], fontName="Helvetica",
        fontSize=9.5, leading=13, textColor=INK, leftIndent=12, spaceBefore=1, spaceAfter=1,
    ),
    "num": ParagraphStyle(
        "num", parent=styles["BodyText"], fontName="Helvetica",
        fontSize=9.5, leading=13, textColor=INK, leftIndent=14, spaceBefore=1, spaceAfter=1,
    ),
    "code": ParagraphStyle(
        "code", parent=styles["Code"], fontName="Courier", fontSize=8, leading=11,
        textColor=INK, backColor=BG_SOFT, leftIndent=8, rightIndent=8,
        spaceBefore=4, spaceAfter=6, borderPadding=6,
    ),
    "meta": ParagraphStyle(
        "meta", parent=styles["BodyText"], fontName="Helvetica-Oblique",
        fontSize=8.5, leading=11.5, textColor=colors.HexColor("#555555"), spaceAfter=6,
    ),
    "th": ParagraphStyle(
        "th", parent=styles["BodyText"], fontName="Helvetica-Bold",
        fontSize=8.5, leading=11, textColor=colors.white,
    ),
    "td": ParagraphStyle(
        "td", parent=styles["BodyText"], fontName="Helvetica",
        fontSize=8.5, leading=11, textColor=INK,
    ),
}


_LATEX_MAP = [
    (r"\\mathbf\{([^{}]*)\}", r"\1"),
    (r"\\mathrm\{([^{}]*)\}", r"\1"),
    (r"\\text\{([^{}]*)\}", r"\1"),
    (r"\\operatorname\{([^{}]*)\}", r"\1"),
    (r"\\times", "×"),
    (r"\\div", "÷"),
    (r"\\pm", "±"),
    (r"\\le(?!q)", "≤"),
    (r"\\ge(?!q)", "≥"),
    (r"\\ne(?!q)", "≠"),
    (r"\\approx", "≈"),
    (r"\\equiv", "≡"),
    (r"\\implies", "⇒"),
    (r"\\iff", "⇔"),
    (r"\\to", "→"),
    (r"\\infty", "∞"),
    (r"\\pi", "π"),
    (r"\\theta", "θ"),
    (r"\\alpha", "α"),
    (r"\\beta", "β"),
    (r"\\gamma", "γ"),
    (r"\\cdot", "·"),
    (r"\\;", " "),
    (r"\\,", " "),
    (r"\\quad", "  "),
    (r"\\qquad", "    "),
    (r"\\left", ""),
    (r"\\right", ""),
    (r"\\sum", "Σ"),
    (r"\\sqrt\{([^{}]*)\}", r"√(\1)"),
    (r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"(\1)/(\2)"),
    (r"\^\{([^{}]*)\}", r"^(\1)"),
    (r"_\{([^{}]*)\}", r"_(\1)"),
    (r"\\%", "%"),
    (r"\\\$", "$"),
]


def esc(t: str) -> str:
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    # lightweight markdown inline
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"\*(.+?)\*", r"<i>\1</i>", t)
    t = re.sub(r"`([^`]+)`", r'<font face="Courier">\1</font>', t)
    # capture math segments, clean LaTeX, then restore
    def _clean_math(m: re.Match) -> str:
        body = m.group(1)
        for pat, repl in _LATEX_MAP:
            body = re.sub(pat, repl, body)
        return f'<font face="Courier">{body}</font>'

    t = re.sub(r"\$\$?(.+?)\$?\$", _clean_math, t)
    # any leftover bare LaTeX commands in prose
    for pat, repl in _LATEX_MAP:
        t = re.sub(pat, repl, t)
    return t


def parse_md(text: str):
    lines = text.splitlines()
    i = 0
    flow = []
    n = len(lines)
    while i < n:
        raw = lines[i]
        line = raw.rstrip()
        if not line.strip():
            i += 1
            continue

        # fenced code
        if line.strip().startswith("```"):
            i += 1
            buf = []
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            code = "\n".join(buf)
            flow.append(Paragraph(esc(code).replace("\n", "<br/>"), S["code"]))
            continue

        # headings
        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            level = len(m.group(1))
            key = f"h{level}"
            flow.append(Spacer(1, 2 * mm))
            flow.append(Paragraph(esc(m.group(2)), S[key]))
            i += 1
            continue

        # horizontal rule
        if re.match(r"^---+\s*$", line):
            flow.append(Spacer(1, 2 * mm))
            i += 1
            continue

        # table
        if line.strip().startswith("|") and i + 1 < n and re.match(r"^\|[\s:\-|]+\|$", lines[i + 1].strip()):
            rows = []
            header = [c.strip() for c in line.strip().strip("|").split("|")]
            rows.append([Paragraph(esc(c), S["th"]) for c in header])
            i += 2
            while i < n and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                rows.append([Paragraph(esc(c), S["td"]) for c in cells])
                i += 1
            ncols = max(len(r) for r in rows)
            for r in rows:
                while len(r) < ncols:
                    r.append(Paragraph("", S["td"]))
            col_w = (A4[0] - 30 * mm) / ncols
            tbl = Table(rows, colWidths=[col_w] * ncols, hAlign="LEFT")
            tbl.setStyle(
                TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, 0), ACCENT),
                        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, BG_SOFT]),
                        ("GRID", (0, 0), (-1, -1), 0.3, RULE),
                        ("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("LEFTPADDING", (0, 0), (-1, -1), 4),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                        ("TOPPADDING", (0, 0), (-1, -1), 3),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                    ]
                )
            )
            flow.append(Spacer(1, 2 * mm))
            flow.append(tbl)
            flow.append(Spacer(1, 2 * mm))
            continue

        # blockquote
        if line.strip().startswith(">"):
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip().lstrip(">").strip())
                i += 1
            flow.append(Paragraph(esc(" ".join(buf)), S["meta"]))
            continue

        # unordered bullet
        m = re.match(r"^(\s*)[-*]\s+(.*)$", line)
        if m:
            flow.append(Paragraph("• " + esc(m.group(2)), S["bullet"]))
            i += 1
            continue

        # ordered list
        m = re.match(r"^(\s*)(\d+)\.\s+(.*)$", line)
        if m:
            flow.append(Paragraph(f"{m.group(2)}. " + esc(m.group(3)), S["num"]))
            i += 1
            continue

        # default paragraph (merge consecutive plain lines)
        buf = [line.strip()]
        i += 1
        while i < n:
            nxt = lines[i].rstrip()
            if not nxt.strip():
                break
            if re.match(r"^(#{1,4})\s", nxt) or nxt.strip().startswith("|") or nxt.strip().startswith("```") or re.match(r"^---+\s*$", nxt.strip()) or nxt.strip().startswith(">") or re.match(r"^\s*[-*]\s+", nxt) or re.match(r"^\s*\d+\.\s+", nxt):
                break
            buf.append(nxt.strip())
            i += 1
        flow.append(Paragraph(esc(" ".join(buf)), S["body"]))

    return flow


def chrome(canv, doc):
    canv.saveState()
    canv.setFont("Helvetica", 8)
    canv.setFillColor(colors.HexColor("#667085"))
    canv.drawString(18 * mm, 12 * mm, "Grade 9 Mathematics · Strand 1 · Lesson 1")
    canv.drawRightString(A4[0] - 18 * mm, 12 * mm, f"Page {doc.page}")
    canv.setStrokeColor(RULE)
    canv.line(18 * mm, 16 * mm, A4[0] - 18 * mm, 16 * mm)
    canv.restoreState()


def main():
    text = MD.read_text(encoding="utf-8")
    flow = parse_md(text)
    doc = SimpleDocTemplate(
        str(PDF),
        pagesize=A4,
        leftMargin=16 * mm,
        rightMargin=16 * mm,
        topMargin=14 * mm,
        bottomMargin=20 * mm,
        title="Lesson 1 — Place Value, Large Numbers, Rounding, and Standard Form",
        author="Staralex School Studies",
    )
    doc.build(flow, onFirstPage=chrome, onLaterPages=chrome)
    print("PDF written:", PDF, "size:", PDF.stat().st_size)


if __name__ == "__main__":
    main()
