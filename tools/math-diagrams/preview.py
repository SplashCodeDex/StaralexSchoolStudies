#!/usr/bin/env python3
"""MANDATORY visual QA for maths diagrams.

After every build, run:
  python preview.py --id <catalog_id>
  python preview.py            # all catalog outputs

Prints an ASCII ink map (so the agent can see layout) and flags:
  - missing/very-faint label ink
  - extreme whitespace (label likely outside the crop)
  - PNG/SVG pair mismatch
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parent
CATALOG = ROOT / "catalog.json"
WS = ROOT.parents[1]


def ascii_map(im: Image.Image, cols: int = 72, rows: int = 30) -> str:
    g = im.convert("L")
    g.thumbnail((cols, rows))
    a = np.array(g)
    chars = " .:-=+*#%@"
    lines = []
    for row in a:
        lines.append("".join(chars[min(9, (255 - int(v)) * 10 // 256)] for v in row))
    return "\n".join(lines)


def inspect(png: Path) -> list[str]:
    issues: list[str] = []
    if not png.exists():
        return [f"MISSING PNG: {png}"]
    im = Image.open(png).convert("L")
    a = np.array(im)
    dark = a < 100
    density = dark.mean()
    if density < 0.004:
        issues.append(f"almost no ink (dark%={density*100:.2f}) — labels may be missing")
    if im.width > 1400 or im.height > 1200:
        issues.append(f"huge canvas {im.size} — labels will look tiny; tighten geometry")
    if im.width < 80 or im.height < 40:
        issues.append(f"tiny canvas {im.size} — may be clipped")
    # whitespace ratio
    bbox = Image.eval(im, lambda p: 255 - p).getbbox()
    if bbox:
        ink_w, ink_h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        fill = (ink_w * ink_h) / (im.width * im.height)
        if fill < 0.15:
            issues.append(
                f"ink bbox only {fill*100:.0f}% of canvas — labels may sit outside trim"
            )
    svg = png.with_suffix(".svg")
    if not svg.exists():
        issues.append("missing sibling SVG")
    return issues


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--id", help="catalog id")
    ap.add_argument("--show", action="store_true", help="print ASCII maps")
    args = ap.parse_args()

    entries = json.loads(CATALOG.read_text(encoding="utf-8"))["diagrams"]
    if args.id:
        entries = [e for e in entries if e["id"] == args.id]
    bad = 0
    for e in entries:
        out = Path(e["out"])
        if not out.is_absolute():
            out = (WS / out).resolve()
        issues = inspect(out)
        status = "OK " if not issues else "BAD"
        print(f"[{status}] {e['id']}")
        for msg in issues:
            print(f"       - {msg}")
            bad += 1
        if args.show and out.exists():
            print(ascii_map(Image.open(out)))
            print()
    print(f"\n{len(entries)} figures checked, {bad} issues.")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
