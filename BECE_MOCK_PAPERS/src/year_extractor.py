"""Content-year extraction from the paper heading itself (ground truth).

Priority ladder (highest first):
  1. heading_explicit  — year tied to exam semantics in the heading zone
                          ("BECE 2021", "OCTOBER 2022 MOCK", "2026 PAPER 1")
  2. heading_range_max — a year range in the heading ("2010-2017" -> 2017)
  3. heading_generic   — bare plausible year anywhere in the heading zone (max)
  4. filename_fallback — year token from filename/context (weak, flagged)
  5. none              — nothing found

OCR tolerance: 2O21 / 2O2T / 2O2I / 2Ol9-style tokens are normalized *only*
inside strict 4-char year-shaped tokens, with at most 2 substituted chars.
"""

from __future__ import annotations

import io
import re
from dataclasses import dataclass
from typing import Optional

YEAR_MIN_PLAUSIBLE, YEAR_MAX_PLAUSIBLE = 1990, 2029

# Char -> digit substitutions permitted inside year-shaped tokens
OCR_MAP = {"O": "0", "o": "0", "Q": "0", "I": "1", "l": "1", "1": "1",
           "S": "5", "T": "1", "B": "8", "Z": "2", "g": "9"}

# 4-char tokens plausibly a mangled year
_CAND_YEAR = re.compile(r"[0-9OoQIl1STSBZg]{4}")

# "2010-2017", "2010/2017", "2010 TO 2017", "2010 - 2017"
_RANGE = re.compile(
    r"\b(19[9]\d|20[0-2]\d)\s*(?:-|--|–|—|/|TO|to|To)\s*(19[9]\d|20[0-2]\d)\b"
)

# year semi-explicitly tied to an exam word within the heading zone
_EXAM_CTX = re.compile(
    r"(?:BECE|WASSCE|JHS|MOCK|PAPER|EXAM|OCTOBER|NOVEMBER|SEPTEMBER|MAY|APRIL|MARCH|FEBRUARY|JANUARY|PASSCO|SUPER|PRIVATE|CANDIDATES|GAGA|CORRECTED|SPECIAL)"
    r"[^.\n]{0,40}?"
    r"\b(19[9]\d|20[0-2]\d)\b",
    re.I,
)
_EXAM_CTX_AFTER = re.compile(
    r"\b(19[9]\d|20[0-2]\d)\b[^.\n]{0,40}?"
    r"(?:BECE|WASSCE|JHS|MOCK|PAPER|EXAM|PASSCO|SUPER|PRIVATE|CANDIDATES|GAGA|CORRECTED|SPECIAL)",
    re.I,
)


@dataclass
class YearResult:
    year: Optional[int] = None
    source: str = "none"
    evidence: str = ""
    all_candidates: list = None  # type: ignore

    def __post_init__(self):
        if self.all_candidates is None:
            self.all_candidates = []


def _ocr_decode(token: str) -> Optional[str]:
    """Decode a year-shaped OCR-mangled token to a plausible year string."""
    decoded, subs = [], 0
    for ch in token:
        if ch.isdigit():
            decoded.append(ch)
        elif ch in OCR_MAP:
            decoded.append(OCR_MAP[ch])
            subs += 1
        else:
            return None
    if subs > 2 or subs == 0:
        # no substitution needed -> regex already matched it as plain year;
        # reject only pure-digit overloads? keep as normal match
        if subs == 0:
            return "".join(decoded)
        return None
    year = "".join(decoded)
    if year.isdigit() and YEAR_MIN_PLAUSIBLE <= int(year) <= YEAR_MAX_PLAUSIBLE:
        return year
    return None


def _year_candidates(text: str) -> list[tuple[str, int]]:
    """All years in text, including OCR-mangled forms. Returns (evidence_token, year)."""
    found: dict[int, str] = {}

    # Plain years first (regex directly)
    for m in re.finditer(r"\b(19[9]\d|20[0-2]\d)\b", text):
        y = int(m.group(1))
        if found.get(y) is None or len(m.group(0)) < len(found[y]):
            found[y] = m.group(1)

    # OCR-mangled candidates (skip tokens that are already plain years)
    for m in _CAND_YEAR.finditer(text):
        token = m.group(0)
        if re.fullmatch(r"\d{4}", token):
            continue
        y = _ocr_decode(token)
        if y and int(y) not in found:
            found[int(y)] = token

    return [(tok, yr) for yr, tok in found.items()]


def extract_heading_text(content: bytes, extension: str, max_chars: int = 1600) -> str:
    """Extract the heading zone (page 1 equivalent) from document bytes."""
    ext = extension.lower()
    text = ""
    try:
        if ext in (".pdf",):
            import pymupdf  # type: ignore
            doc = pymupdf.open(stream=content, filetype="pdf")
            for p in range(min(len(doc), 2)):
                text += "\n" + doc[p].get_text()
            doc.close()
        elif ext in (".docx",):
            from docx import Document  # type: ignore
            doc = Document(io.BytesIO(content))
            text += "\n".join(p.text for p in doc.paragraphs[:30])
        elif ext == ".txt":
            raw = content[:8000].decode("utf-8", errors="ignore")
            # for pipeline txt articles, skip SOURCE URL/TITLE/SUBJECT header
            sep = re.search(r"\n={5,}\n", raw)
            text = raw[sep.end():] if sep else raw
        elif ext == ".doc":
            # legacy binary format: best effort — pull printable runs
            raw = content[: 12000]
            runs = re.findall(rb"[ -~]{6,}", raw)
            text = "\n".join(r.decode("latin-1") for r in runs[:40])
    except Exception:
        text = ""
    return text[:max_chars]


def extract_content_year(
    content: bytes,
    extension: str,
    text_context: str = "",
    heading_text: Optional[str] = None,
) -> YearResult:
    """Ground-truth year from the paper itself, falling back to the filename."""
    heading = heading_text if heading_text is not None else extract_heading_text(content, extension)
    cands = _year_candidates(heading)
    result = YearResult(all_candidates=cands)

    # 1. explicit exam-context year (min of the exam-context matches = exam season year;
    #    a paper is written for one sitting — take the first/most frequent context year)
    ctx_years: list[int] = []
    for m in _EXAM_CTX.finditer(heading):
        ctx_years.append(int(m.group(1)))
    for m in _EXAM_CTX_AFTER.finditer(heading):
        ctx_years.append(int(m.group(1)))
    if ctx_years:
        result.year, result.source = _argmax_common(ctx_years), "heading_explicit"
        # evidence = the tightest match (shortest surrounding text)
        best = min(_EXAM_CTX.finditer(heading), key=lambda m: len(m.group(0)), default=None)
        result.evidence = (best.group(0) if best else str(result.year))[:60]
        return result

    # 2. year range -> compilation's latest paper
    rm = _RANGE.search(heading)
    if rm:
        result.year, result.source = int(max(int(rm.group(1)), int(rm.group(2)))), "heading_range_max"
        result.evidence = rm.group(0)
        return result

    # 3. generic years in the heading zone (max = most recent referenced)
    if cands:
        years = [int(yr) for _, yr in cands]
        result.year, result.source = max(years), "heading_generic"
        result.evidence = str(max(cands, key=lambda t: t[1])[0])
        return result

    # 4. filename/context fallback
    fm = re.search(r"\b(19[9]\d|20[0-2]\d)\b", text_context)
    if fm:
        result.year, result.source = int(fm.group(1)), "filename_fallback"
        result.evidence = fm.group(0)
    return result


def _common_count(value: int, values: list) -> int:
    return values.count(value)


def _argmax_common(values: list) -> int:
    return max(set(values), key=values.count)
