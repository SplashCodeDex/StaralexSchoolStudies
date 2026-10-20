# place_value_chart — Place-value grid (2 500 000)

**Status:** PERFECT (2026-10-20)  
**Source:** `tools/math-diagrams/templates/place_value_chart.tex`  
**Output:** `Grade9-Maths/.../Lesson-01-Place-Value-And-Standard-Form/diagrams/place_value_chart.png`

## Build
```powershell
& $env:MIMO_PYTHON tools/math-diagrams/build.py --only place_value_chart
```

## Layout
- 7 columns × 2 rows: heading row `M HTh TTh Th H T U`, digit row `2 5 0 0 0 0 0`.
- Cell width 1.35, heights 0.55 (heading) + 0.95 (digit).
- One-line muted legend giving each abbreviation's value (a **key**, not a caption).
- The number `$2\,500\,000$` in accent, below the key.

## Pitfalls
1. **Two-line prose key** ("M millions · HTh hundred-thousands · …") read like a caption.
   Compress to one line of `HTh 100 000` pairs.
2. **`md label` / `md label bold` white sticker boxes** — use plain `font=\sffamily` nodes.

## Contract
- [x] No caption sentences (the key is a compact legend)
- [x] No white boxes
- [x] Digits and place abbreviations are data
