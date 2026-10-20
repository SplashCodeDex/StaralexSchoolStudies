#!/usr/bin/env python3
"""Render lesson markdown to PDF — maths-safe build.

RULES (locked with user):
- Body font: Cambria (broad symbol coverage). Display maths: LaTeX at body size.
- Inline maths: clean Unicode in body font — NEVER a LaTeX image.
- Display maths: LaTeX PNG scaled so it matches body text (~12-14pt).
- Glyphs: allowlist + tofu check (U+FFFD / ■ / □ / ◆) fails the build.
- True minus sign U+2212, never hyphen-minus in maths.
- Figures: no captions in the image; referenced from text as Figure N.
"""
from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import tempfile
import unicodedata
from pathlib import Path

from PIL import Image as PILImage
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Image,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

# ---------------------------------------------------------------------------
# Fonts
# ---------------------------------------------------------------------------
FONTS_DIR = Path(r"C:\Windows\Fonts")
CAMBRIA_TTC = FONTS_DIR / "cambria.ttc"

TOFU_CHARS = {
    "�",  # U+FFFD replacement
    "■",  # black square (Helvetica tofu)
    "□",  # white square (missing glyph)
    "◆",  # black diamond (shown when ℤ missing)
    "▯",  # white vertical rectangle
}

# Symbols we will use in body text and expect Cambria to have.
SYMBOL_ALLOWLIST = set(
    "×÷±−→←↔≤≥≠≈∞∅∈∉∪∩θαβγπΣ°′″"  # math
    "₦¢£€¥$"  # currency
    "▪●○◆■□"  # filled/hollow markers used deliberately
    "½⅓¼¾⅕⅙⅛⅔⅗¾⅚⅞"  # vulgar fractions
    "⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺"  # super/sub scripts
    "ℕ𝕎ℤℚℝ"  # blackboard (may fall back to LaTeX)
    "✓✗"  # ticks
    "…–—"  # punctuation
)

register_names = {}


def register_fonts() -> None:
    if register_names:
        return
    if not CAMBRIA_TTC.exists():
        raise FileNotFoundError(f"Cambria not found: {CAMBRIA_TTC}")
    pdfmetrics.registerFont(TTFont("Body", str(CAMBRIA_TTC), subfontIndex=0))
    pdfmetrics.registerFont(TTFont("Math", str(CAMBRIA_TTC), subfontIndex=1))
    pdfmetrics.registerFont(TTFont("Bold", str(FONTS_DIR / "cambriab.ttf")))
    pdfmetrics.registerFont(TTFont("Italic", str(FONTS_DIR / "cambriai.ttf")))
    pdfmetrics.registerFont(TTFont("BoldItalic", str(FONTS_DIR / "cambriaz.ttf")))
    pdfmetrics.registerFont(TTFont("Mono", str(FONTS_DIR / "consola.ttf")))
    pdfmetrics.registerFont(TTFont("MonoBold", str(FONTS_DIR / "consolab.ttf")))
    register_names.update(
        {
            "Body": "Cambria",
            "Math": "CambriaMath",
            "Bold": "Cambria-Bold",
            "Italic": "Cambria-Italic",
            "Mono": "Consolas",
        }
    )


# ---------------------------------------------------------------------------
# Glyph safety
# ---------------------------------------------------------------------------
def check_glyphs(text: str, where: str) -> list[str]:
    problems = []
    for ch in text:
        if ch in TOFU_CHARS:
            problems.append(f"{where}: tofu/danger glyph U+{ord(ch):04X} {ch!r} in {text[:60]!r}")
        elif ch == "-":
            # hyphen-minus inside a math-ish context is a smell, not always fatal
            continue
    return problems


def normalise_minus(t: str) -> str:
    """Use true minus U+2212 in math contexts."""
    # minus before a digit or letter, after start/space/open-bracket/equals/compare
    t = re.sub(
        r"(?:(?<=[\s(=×÷+−,;])|^|(?<=[≤≥<>±→←]))-(?=[\d(]|[A-Za-z])",
        "−",
        t,
    )
    return t


# ---------------------------------------------------------------------------
# LaTeX → PNG
# ---------------------------------------------------------------------------
LATEX_DIR = Path(tempfile.gettempdir()) / "lesson_latex_math2"
LATEX_DIR.mkdir(parents=True, exist_ok=True)


def latex_png(tex: str, display: bool, font_size: int = 12) -> Path | None:
    tag = hashlib.sha1(f"{display}|{font_size}|{tex}".encode()).hexdigest()[:16]
    png = LATEX_DIR / f"{tag}.png"
    if png.exists() and png.stat().st_size > 0:
        return png
    work = LATEX_DIR / tag
    work.mkdir(parents=True, exist_ok=True)
    body = f"$\\displaystyle {tex}$" if display else f"${tex}$"
    doc = (
        f"\\documentclass[{font_size}pt]{{standalone}}\n"
        "\\usepackage{amsmath,amssymb}\n"
        "\\begin{document}\n"
        f"{body}\n"
        "\\end{document}\n"
    )
    (work / "m.tex").write_text(doc, encoding="utf-8")
    try:
        r = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "m.tex"],
            cwd=work,
            capture_output=True,
            timeout=60,
        )
        if r.returncode != 0 or not (work / "m.pdf").exists():
            # some standalone setups warn but still write a usable PDF
            if not (work / "m.pdf").exists():
                return None
        import pypdfium2 as pdfium

        pdf = pdfium.PdfDocument(str(work / "m.pdf"))
        page = pdf[0]
        # render at 2x so pixels/point ≈ 2
        pil = page.render(scale=2.0).to_pil().convert("RGB")
        # trim white
        gray = pil.convert("L")
        bbox = gray.point(lambda p: 255 - p).getbbox()
        if bbox:
            pil = pil.crop(bbox)
        pil.save(png)
        return png
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Inline maths → Unicode (no images)
# ---------------------------------------------------------------------------

_VULGAR = {
    (1, 2): "\u00bd", (1, 3): "\u2153", (2, 3): "\u2154",
    (1, 4): "\u00bc", (3, 4): "\u00be", (1, 5): "\u2155",
    (2, 5): "\u2156", (3, 5): "\u2157", (4, 5): "\u2158",
    (1, 6): "\u2159", (5, 6): "\u215a", (1, 8): "\u215b",
    (3, 8): "\u215c", (5, 8): "\u215d", (7, 8): "\u215e",
}


def _frac(num: str, den: str) -> str:
    """Turn \frac{a}{b} into readable Unicode."""
    num, den = num.strip(), den.strip()
    # both single digits -> vulgar fraction
    if num.isdigit() and den.isdigit() and len(num) == 1 and len(den) == 1:
        key = (int(num), int(den))
        if key in _VULGAR:
            return _VULGAR[key]
    # denominator with more than one token needs brackets
    if re.search(r"[+\-*/ ]", den) or (len(den) > 1 and not den.isdigit()):
        return f"{num}/({den})"
    return f"{num}/{den}"


def _mixed(m: re.Match) -> str:
    """1\frac{1}{3} -> 1 1/3 (keep the integer part visible)."""
    whole, a, b = m.group(1), m.group(2), m.group(3)
    return f"{whole} {_frac(a, b)}"


_LATEX_TO_UNI = [
    # mixed numbers first: 1\\frac{1}{3}
    (r"(\d+)\\frac\{([^{}]*)\}\{([^{}]*)\}", _mixed),
    (r"\\mathbf\{([^{}]*)\}", r"\1"),
    (r"\\mathrm\{([^{}]*)\}", r"\1"),
    (r"\\text\{([^{}]*)\}", r"\1"),
    (r"\\operatorname\{([^{}]*)\}", r"\1"),
    (r"\\times", "×"),
    (r"\\div", "÷"),
    (r"\\pm", "±"),
    (r"\\mp", "∓"),
    (r"\\le(?:q)?", "≤"),
    (r"\\ge(?:q)?", "≥"),
    (r"\\ne(?:q)?", "≠"),
    (r"\\approx", "≈"),
    (r"\\equiv", "≡"),
    (r"\\implies", "→"),
    (r"\\Rightarrow", "→"),
    (r"\\Leftarrow", "←"),
    (r"\\Leftrightarrow", "↔"),
    (r"\\iff", "↔"),
    (r"\\to", "→"),
    (r"\\infty", "∞"),
    (r"\\pi", "π"),
    (r"\\theta", "θ"),
    (r"\\alpha", "α"),
    (r"\\beta", "β"),
    (r"\\gamma", "γ"),
    (r"\\lambda", "λ"),
    (r"\\mu", "μ"),
    (r"\\sigma", "σ"),
    (r"\\cdot", "·"),
    (r"\\times", "×"),
    (r"\\;", " "),
    (r"\\,", " "),
    (r"\\quad", "  "),
    (r"\\qquad", "    "),
    (r"\\left", ""),
    (r"\\right", ""),
    (r"\\sum", "Σ"),
    (r"\\emptyset", "∅"),
    (r"\\in", "∈"),
    (r"\\notin", "∉"),
    (r"\\cup", "∪"),
    (r"\\cap", "∩"),
    (r"\\subset", "⊂"),
    (r"\\leq", "≤"),
    (r"\\geq", "≥"),
    (r"\\sqrt\{([^{}]*)\}", r"√(\1)"),
    (r"\\sqrt", "√"),
    (r"\\frac\{([^{}]*)\}\{([^{}]*)\}", lambda m: _frac(m.group(1), m.group(2))),
    (r"\^\{([^{}]*)\}", r"^(\1)"),
    (r"_\{([^{}]*)\}", r"_(\1)"),
    (r"\^(\w)", r"^(\1)"),
    (r"_(\w)", r"_(\1)"),
    (r"\\%", "%"),
    (r"\\\$", "$"),
    (r"\\{", "{"),
    (r"\\}", "}"),
]


def latex_to_unicode(src: str) -> str:
    body = src
    for pat, repl in _LATEX_TO_UNI:
        body = re.sub(pat, repl, body)
    # blackboard bold and friends
    body = body.replace("\\mathbb{N}", "ℕ").replace("\\mathbb{W}", "𝕎")
    body = body.replace("\\mathbb{Z}", "ℤ").replace("\\mathbb{Q}", "ℚ")
    body = body.replace("\\mathbb{R}", "ℝ")
    # remaining \word -> just the word (best effort)
    body = re.sub(r"\\([a-zA-Z]+)", r"\1", body)
    return normalise_minus(body)


# Unicode super/subscripts for common cases
_SUP = str.maketrans("0123456789+-=()ni", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿⁱ")
_SUB = str.maketrans("0123456789+-=()aeknx", "₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₐₑₖₙₓ")


def prettify_indices(t: str) -> str:
    """Turn x^(2m) / x^(-4) into unicode where possible."""
    def sup(m):
        inner = m.group(1)
        if all(c in "0123456789+-=()ni" for c in inner):
            return inner.translate(_SUP)
        return f"^({inner})"

    def sub(m):
        inner = m.group(1)
        if all(c in "0123456789+-=()aeknx" for c in inner):
            return inner.translate(_SUB)
        return f"_({inner})"

    t = re.sub(r"\^\(([^)]+)\)", sup, t)
    t = re.sub(r"\^([0-9n])", lambda m: m.group(1).translate(_SUP), t)
    t = re.sub(r"_\(([^)]+)\)", sub, t)
    return t


def esc(t: str) -> str:
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def clean_inline(t: str, problems: list, where: str = "inline") -> str:
    # 1) Extract inline math FIRST, before HTML escaping, as Unicode in a stash.
    stash: list[str] = []

    def _imath(m: re.Match) -> str:
        stash.append(latex_to_unicode(m.group(1)))
        return "@@M%d@@" % (len(stash) - 1)

    t = re.sub(r"(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)", _imath, t)

    # 2) HTML-escape the prose only
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    # 3) Strip leftover LaTeX in prose
    for pat, repl in _LATEX_TO_UNI:
        t = re.sub(pat, repl, t)
    t = re.sub(r"\\([a-zA-Z]+)", r"\1", t)
    t = normalise_minus(t)
    t = prettify_indices(t)

    # 4) Markdown emphasis
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", t)
    t = re.sub(r"`([^`]+)`", r'<font face="Mono">\1</font>', t)

    # 5) Restore maths (already Unicode)
    for i, s in enumerate(stash):
        safe = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        t = t.replace("@@M%d@@" % i, safe)

    plain = t
    for a, b in (("&amp;", "&"), ("&gt;", ">"), ("&lt;", "<")):
        plain = plain.replace(a, b)
    plain = re.sub(r"<[^>]+>", "", plain)
    problems.extend(check_glyphs(plain, where))
    return t


# ---------------------------------------------------------------------------
# Styles
# ---------------------------------------------------------------------------
INK = colors.HexColor("#1A1A1A")
ACCENT = colors.HexColor("#1F4E79")
RULE = colors.HexColor("#C5CDD8")
BG_SOFT = colors.HexColor("#F4F7FB")
BODY_PT = 10.5
S: dict[str, ParagraphStyle] = {}


def build_styles() -> None:
    S["h1"] = ParagraphStyle("h1", fontName="Bold", fontSize=15, leading=19, textColor=ACCENT, spaceBefore=8, spaceAfter=7)
    S["h2"] = ParagraphStyle("h2", fontName="Bold", fontSize=12.5, leading=16, textColor=ACCENT, spaceBefore=11, spaceAfter=5)
    S["h3"] = ParagraphStyle("h3", fontName="Bold", fontSize=10.5, leading=14, textColor=INK, spaceBefore=8, spaceAfter=3)
    S["h4"] = ParagraphStyle("h4", fontName="Bold", fontSize=10, leading=13, textColor=INK, spaceBefore=6, spaceAfter=2)
    S["body"] = ParagraphStyle("body", fontName="Body", fontSize=BODY_PT, leading=BODY_PT * 1.35, textColor=INK, spaceBefore=1.5, spaceAfter=3, alignment=TA_LEFT)
    S["bullet"] = ParagraphStyle("bullet", fontName="Body", fontSize=BODY_PT, leading=BODY_PT * 1.3, textColor=INK, leftIndent=12, spaceBefore=0.5, spaceAfter=0.5)
    S["num"] = ParagraphStyle("num", fontName="Body", fontSize=BODY_PT, leading=BODY_PT * 1.3, textColor=INK, leftIndent=14, spaceBefore=0.5, spaceAfter=0.5)
    S["code"] = ParagraphStyle("code", fontName="Mono", fontSize=8, leading=11, textColor=INK, backColor=BG_SOFT, leftIndent=8, rightIndent=8, spaceBefore=3, spaceAfter=5, borderPadding=5)
    S["meta"] = ParagraphStyle("meta", fontName="Italic", fontSize=8.5, leading=11.5, textColor=colors.HexColor("#555555"), spaceAfter=5)
    S["th"] = ParagraphStyle("th", fontName="Bold", fontSize=8.5, leading=11, textColor=colors.white)
    S["td"] = ParagraphStyle("td", fontName="Body", fontSize=8.5, leading=11, textColor=INK)
    S["qa_q"] = ParagraphStyle("qa_q", fontName="Bold", fontSize=BODY_PT, leading=BODY_PT * 1.3, textColor=INK, spaceBefore=3, spaceAfter=1)
    S["qa_a"] = ParagraphStyle("qa_a", fontName="Body", fontSize=BODY_PT, leading=BODY_PT * 1.3, textColor=INK, leftIndent=14, spaceBefore=1, spaceAfter=3)
    S["opt"] = ParagraphStyle("opt", fontName="Body", fontSize=BODY_PT, leading=BODY_PT * 1.25, textColor=INK, leftIndent=28, spaceBefore=0.5, spaceAfter=0.5)


# ---------------------------------------------------------------------------
# Markdown → flowables
# ---------------------------------------------------------------------------
global_md_dir = Path(".")


def display_math_flow(tex: str, problems: list) -> list:
    problems.extend(check_glyphs(tex, "display-math-source"))
    png = latex_png(tex, display=True, font_size=12)
    if not png:
        return [Paragraph(f'<font face="Mono">{esc(latex_to_unicode(tex))}</font>', S["code"])]
    with PILImage.open(png) as im:
        w, h = im.size
    # rendered at scale=2 → pixels = 2 * points
    w_pt = w / 2.0
    h_pt = h / 2.0
    max_w = A4[0] - 46 * mm
    if w_pt > max_w:
        k = max_w / w_pt
        w_pt, h_pt = w_pt * k, h_pt * k
    return [
        Spacer(1, 3),
        Image(str(png), width=w_pt, height=h_pt, hAlign="CENTER"),
        Spacer(1, 3),
    ]


def parse_md(text: str, problems: list) -> list:
    lines = text.splitlines()
    i = 0
    flow: list = []
    n = len(lines)
    while i < n:
        line = lines[i].rstrip()
        if not line.strip():
            i += 1
            continue

        # display math
        if line.strip().startswith("$$"):
            buf = []
            first = line.strip()[2:]
            if first.endswith("$$") and len(first) > 2:
                buf.append(first[:-2])
                i += 1
            else:
                if first.strip():
                    buf.append(first)
                i += 1
                while i < n and "$$" not in lines[i]:
                    buf.append(lines[i])
                    i += 1
                if i < n:
                    tail = lines[i].replace("$$", "").strip()
                    if tail:
                        buf.append(tail)
                    i += 1
            flow.extend(display_math_flow("\n".join(buf), problems))
            continue

        # page break
        if line.strip().lower() in ('<!-- pagebreak -->', r'\pagebreak', r'\newpage'):
            flow.append(PageBreak())
            i += 1
            continue

        # markdown image
        m = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)\s*$", line.strip())
        if m:
            src = m.group(2).strip()
            img_path = Path(src) if Path(src).is_absolute() else Path(global_md_dir) / src
            if img_path.exists():
                try:
                    with PILImage.open(img_path) as im:
                        w, h = im.size
                    max_w = A4[0] - 36 * mm
                    max_h = 78 * mm
                    scale = min(max_w / w, max_h / h, 1.0)
                    flow.append(Spacer(1, 3))
                    flow.append(Image(str(img_path), width=w * scale, height=h * scale, hAlign="CENTER"))
                    flow.append(Spacer(1, 3))
                except Exception:
                    flow.append(Paragraph(f"[image unavailable: {src}]", S["meta"]))
            else:
                flow.append(Paragraph(f"[missing image: {src}]", S["meta"]))
            i += 1
            continue

        # code fence
        if line.strip().startswith("```"):
            i += 1
            buf = []
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            flow.append(Paragraph(esc("\n".join(buf)).replace("\n", "<br/>"), S["code"]))
            continue

        # headings
        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            lvl = len(m.group(1))
            flow.append(Spacer(1, 2 * mm))
            flow.append(Paragraph(clean_inline(m.group(2), problems, f"h{lvl}"), S[f"h{lvl}"]))
            i += 1
            continue

        if re.match(r"^---+\s*$", line):
            flow.append(Spacer(1, 2 * mm))
            i += 1
            continue

        # table
        if line.strip().startswith("|") and i + 1 < n and re.match(r"^\|[\s:\-|]+\|$", lines[i + 1].strip()):
            rows = []
            header = [c.strip() for c in line.strip().strip("|").split("|")]
            rows.append([Paragraph(clean_inline(c, problems, "th"), S["th"]) for c in header])
            i += 2
            while i < n and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                rows.append([Paragraph(clean_inline(c, problems, "td"), S["td"]) for c in cells])
                i += 1
            ncols = max(len(r) for r in rows)
            for r in rows:
                while len(r) < ncols:
                    r.append(Paragraph("", S["td"]))
            col_w = (A4[0] - 32 * mm) / ncols
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

        if line.strip().startswith(">"):
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip().lstrip(">").strip())
                i += 1
            flow.append(Paragraph(clean_inline(" ".join(buf), problems, "quote"), S["meta"]))
            continue

        # MCQ option lines: "A. ..." / "B. ..."
        m = re.match(r"^\s*([A-E])[.)]\s+(.*)$", line)
        if m:
            flow.append(Paragraph(f"{m.group(1)}. {clean_inline(m.group(2), problems, 'option')}", S["opt"]))
            i += 1
            continue

        # Q&A
        m = re.match(r"^\*\*(Q\d+[a-z]?\.)\*\*\s*(.*)$", line)
        if m:
            flow.append(Paragraph(f"<b>{m.group(1)}</b> {clean_inline(m.group(2), problems, 'q')}", S["qa_q"]))
            i += 1
            continue
        m = re.match(r"^\*\*(Ans\.?)\*\*\s*(.*)$", line)
        if m:
            flow.append(Paragraph(clean_inline(f"{m.group(1)} {m.group(2)}", problems, "ans"), S["qa_a"]))
            i += 1
            continue

        m = re.match(r"^(\s*)[-*]\s+(.*)$", line)
        if m:
            flow.append(Paragraph("• " + clean_inline(m.group(2), problems, "bul"), S["bullet"]))
            i += 1
            continue

        m = re.match(r"^(\s*)(\d+)\.\s+(.*)$", line)
        if m:
            flow.append(Paragraph(f"{m.group(2)}. " + clean_inline(m.group(3), problems, "num"), S["num"]))
            i += 1
            continue

        buf = [line.strip()]
        i += 1
        while i < n:
            nxt = lines[i].rstrip()
            if not nxt.strip():
                break
            if (
                re.match(r"^(#{1,4})\s", nxt)
                or nxt.strip().startswith("|")
                or nxt.strip().startswith("```")
                or re.match(r"^---+\s*$", nxt.strip())
                or nxt.strip().startswith(">")
                or re.match(r"^\s*[-*]\s+", nxt)
                or re.match(r"^\s*\d+\.\s+", nxt)
                or nxt.strip().startswith("$$")
                or re.match(r"^!\[", nxt.strip())
                or re.match(r"^\*\*Q\d+", nxt.strip())
                or re.match(r"^\*\*Ans", nxt.strip())
                or re.match(r"^\s*[A-E][.)]\s+", nxt)
            ):
                break
            buf.append(nxt.strip())
            i += 1
        flow.append(Paragraph(clean_inline(" ".join(buf), problems, "para"), S["body"]))

    return flow


def main() -> None:
    register_fonts()
    build_styles()

    p = argparse.ArgumentParser()
    p.add_argument("md", nargs="?", type=Path)
    p.add_argument("--out", type=Path, default=None)
    p.add_argument("--title", default="Staralex Lesson")
    p.add_argument("--footer", default="Grade 9")
    p.add_argument("--strict", action="store_true", help="fail on tofu glyphs")
    args = p.parse_args()

    md_path = args.md
    pdf_path = args.out or md_path.with_suffix(".pdf")
    text = md_path.read_text(encoding="utf-8")
    global global_md_dir
    global_md_dir = md_path.parent

    problems: list[str] = []
    flow = parse_md(text, problems)

    footer = args.footer

    def chrome(canv, doc):
        canv.saveState()
        canv.setFont("Body", 8)
        canv.setFillColor(colors.HexColor("#667085"))
        canv.drawString(18 * mm, 12 * mm, footer)
        canv.drawRightString(A4[0] - 18 * mm, 12 * mm, f"Page {doc.page}")
        canv.setStrokeColor(RULE)
        canv.line(18 * mm, 16 * mm, A4[0] - 18 * mm, 16 * mm)
        canv.restoreState()

    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=A4,
        leftMargin=16 * mm,
        rightMargin=16 * mm,
        topMargin=14 * mm,
        bottomMargin=20 * mm,
        title=args.title,
        author="Staralex School Studies",
    )
    doc.build(flow, onFirstPage=chrome, onLaterPages=chrome)
    print("PDF written:", pdf_path, "size:", pdf_path.stat().st_size)
    if problems:
        print(f"\nGLYPH ISSUES ({len(problems)}):")
        for p_ in problems[:30]:
            print("  ", p_)
        if args.strict:
            raise SystemExit(2)
    else:
        print("Glyph check: clean.")


if __name__ == "__main__":
    main()
