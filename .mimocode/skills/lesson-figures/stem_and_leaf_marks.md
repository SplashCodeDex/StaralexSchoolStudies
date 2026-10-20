# stem_and_leaf_marks — Stem-and-leaf plot (20 mock marks)

**Status:** PERFECT (2026-10-20)  
**Source:** `tools/math-diagrams/templates/stem_and_leaf_marks.tex`  
**Output:** `Grade9-Maths/.../Lesson-01-Data-Statistics-And-Representations/diagrams/stem_and_leaf_marks.png`

## Build
```powershell
& $env:MIMO_PYTHON tools/math-diagrams/build.py --only stem_and_leaf_marks
```

## Data (Mock 2026 P2 Q1d — 20 marks)

| Stem | Leaf |
| :---: | :--- |
| 3 | 8 |
| 4 | 0 2 5 8 |
| 5 | 4 4 6 7 7 7 8 8 |
| 6 | 1 3 3 4 6 |
| 7 | 2 3 |

Key: `5 | 4 = 54`. Mode 57, median 57.5 (stated in the lesson prose, not in the figure).

## Layout
- Header row `Stem` at `(0,0)`, `Leaf` anchored **west** at `(1.1,0)`.
- Vertical rule at `x = 0.95`, from `y = 0.28` down to `y = -4.0`.
- Stem digits at `x = 0` (centred on the stem column).
- Leaf rows **`anchor=west` at `(1.1, y)`** — never centred.
- Font: `\ttfamily\small` for all data digits (tabular, consistent).
- Key at `(2.15, -4.35)` in muted footnotesize (a legend, allowed).

## Pitfalls (do not repeat)
1. **Centred leaf nodes overflow left across the divider.** The 8-leaf row
   `4 4 6 7 7 7 8 8` at `x=1.9` centred pushed `4 4` to the left of the rule.
   Always `anchor=west` at a fixed x just right of the divider.
2. **Math-mode digits** (`$0\ 2\ 5\ 8$`) mixed figure styles between rows
   (lining vs old-style). Use `\ttfamily` **text** digits for data.
3. **White sticker boxes** (`md label`) — plain `font=\sffamily` / `\ttfamily` nodes.

## Contract
- [x] All leaves right of the divider
- [x] Consistent tabular digit font
- [x] Leaves in ascending order
- [x] Key legend present (allowed — it defines the notation)
- [x] No white boxes, no caption sentences
