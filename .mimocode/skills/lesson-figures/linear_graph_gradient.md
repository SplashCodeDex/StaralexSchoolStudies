# linear_graph_gradient — Gradient as rise/run

**Status:** PERFECT (2026-10-20)  
**Source:** `tools/math-diagrams/templates/linear_graph_gradient.tex`  
**Output:** `Grade9-Maths/.../Lesson-01-Linear-Relations-And-Gradient/diagrams/linear_graph_gradient.png`

## Build
```powershell
& $env:MIMO_PYTHON tools/math-diagrams/build.py --only linear_graph_gradient
```

## Layout
- Axes via `\mdAxes{-1}{6}{-1}{5}{1}{1}` (x −1…6, y −1…5, step 1).
- Line through `(-0.5, 0.5)` and `(5.5, 4.5)`.
- Two marked points `P1 = (1, 1.5)`, `P2 = (3, 3)` — slope $m = \frac{3-1.5}{3-1} = \frac{1}{2}$.
- Rise/run triangle (highlight red): horizontal leg `run = 2` from P1 to `(3, 1.5)`,
  vertical leg `rise = 1` up to P2.
- Formula `$m = \frac{\text{rise}}{\text{run}}$` in accent, placed **below the x-axis**
  at `(3.6, -0.55)` — empty space the line never enters.

## Pitfalls (do not repeat)
1. **Formula placed ON the line.** At `(4.6, 4.0)` the line passes through
   $y = \frac{2}{3}(x+0.5)+0.5 \approx 3.9$ — the label sat on the stroke. Always
   compute the line's height at the label's x and choose an empty region.
2. **White sticker box** behind the formula (`md label accent`) — use a plain
   `font=\sffamily` node.
3. Rise/run labels must not overlap the legs; use `below=3pt` / `right=3pt`.

## Contract
- [x] Formula is data (allowed), placed in empty space
- [x] No white boxes
- [x] No caption sentences
- [x] Rise/run legs and labels unambiguous
