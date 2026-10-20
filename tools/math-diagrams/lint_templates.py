#!/usr/bin/env python3
"""Lint TikZ figure templates against the locked drawing rules.

See tools/README-figures.md.  Run:
  python tools/math-diagrams/lint_templates.py
Exit code 2 if any template violates the rules.

Allowed in a figure:  tick numbers, measurement labels (6 cm, 57°, A, B, x),
                      geometric marks (dots, arcs, arrows).
Forbidden in a figure: caption sentences, inequality statements,
                      "solid dot at… / arrow to the right" prose,
                      the solution ray drawn ON a number-line axis.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TEMPLATES = ROOT / "templates"


def strip_comments(tex: str) -> str:
    return re.sub(r"(?<!\\)%.*", "", tex)


# A "caption sentence" in a node body: long, or reads like English prose / inequality.
_CAPTIONISH = re.compile(
    r"(<|\\le|\\ge|\\leq|\\geq)"          # inequality statement
    r"|(?:\b(?:solid dot|open circle|arrow to|Figure \d+|solution of)\b)"
    r"|(?:\b(?:the|which|that|shows|where|represents)\b.*\b(?:the|a|an)\b)"
)


def check(path: Path) -> list[str]:
    raw = path.read_text(encoding="utf-8")
    text = strip_comments(raw)
    issues: list[str] = []

    # literal caption strings
    for pat, why in [
        (re.compile(r"Figure\s+\d+\s*:"), "literal 'Figure N:' text baked into the drawing"),
        (re.compile(r"solid dot|open circle|arrow to the"), "verbal description of the drawing baked into the figure"),
    ]:
        if pat.search(text):
            issues.append(f"{path.name}: {why}")

    # caption-ish node bodies (label accent or otherwise)
    for m in re.finditer(r"\\node\[[^\]]*\]\s*(?:\([^)]*\)\s*)?\{([^}]*)\}", text):
        body = m.group(1).strip()
        if not body:
            continue
        if _CAPTIONISH.search(body):
            issues.append(
                f"{path.name}: caption-like node body {body!r} — move it to the markdown prose"
            )
        elif len(body.split()) > 6:
            issues.append(
                f"{path.name}: long node body {body!r} looks like a caption, not a measurement label"
            )

    # number-line specific
    if re.match(r"number_line_.*\.tex$", path.name):
        if re.search(r"\\draw\[[^\]]*accent[^\]]*\]\s*\([^,]+,\s*\\y\)", text):
            issues.append(
                f"{path.name}: solution ray drawn ON the axis (\\y) — it must sit ABOVE the axis (\\yr)"
            )
        if "md label bold" in text:
            issues.append(
                f"{path.name}: duplicate bold point labels — tick numbers are enough"
            )
    return issues


def main() -> int:
    all_issues: list[str] = []
    files = sorted(TEMPLATES.glob("*.tex"))
    for tex in files:
        all_issues.extend(check(tex))
    if all_issues:
        print(f"LINT FAILED ({len(all_issues)} issue(s) in {len(files)} templates):")
        for s in all_issues:
            print("  !", s)
        return 2
    print(f"LINT OK — {len(files)} templates follow the drawing rules.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
