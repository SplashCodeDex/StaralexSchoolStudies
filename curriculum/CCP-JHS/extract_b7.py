#!/usr/bin/env python3
"""Extract B7 (JHS 1 / Grade 7) Strand 1 sections from NaCCA CCP PDFs."""
from pathlib import Path

from pypdf import PdfReader

BASE = Path(r"W:\StaralexSchoolStudies\curriculum\CCP-JHS")
OUT = Path(r"W:\StaralexSchoolStudies\curriculum\CCP-JHS\extracted")
OUT.mkdir(exist_ok=True)

FILES = {
    "maths": BASE / "CCP_Mathematics_JHS.pdf",
    "computing": BASE / "CCP_Computing_JHS.pdf",
    "cad": BASE / "CCP_Creative_Arts_and_Design_JHS.pdf",
}

# Pull every page's text and also dump a marker index for B7/Strand 1.
for key, path in FILES.items():
    reader = PdfReader(str(path))
    pages = []
    for i, page in enumerate(reader.pages):
        try:
            t = page.extract_text() or ""
        except Exception as e:
            t = f"[extract error: {e}]"
        pages.append(t)
    full = "\n\n".join(f"<<<PAGE {i+1}>>>\n{t}" for i, t in enumerate(pages))
    out_path = OUT / f"{key}_full.txt"
    out_path.write_text(full, encoding="utf-8", errors="replace")

    # Find pages mentioning Strand 1 / B7 / JHS 1 near "Strand"
    hits = []
    for i, t in enumerate(pages):
        low = t.lower()
        if ("b7." in low or "jhs 1" in low or "grade 7" in low or "basic 7" in low) and (
            "strand" in low or "substrand" in low or "sub-strand" in low
        ):
            hits.append(i + 1)
    print(f"{key}: pages={len(pages)} b7/strand-hits={hits[:40]} size={out_path.stat().st_size}")
