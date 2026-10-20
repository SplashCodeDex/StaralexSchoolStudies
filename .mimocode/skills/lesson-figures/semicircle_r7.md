# semicircle_r7 — Semicircle with radius 7 cm

**Status:** PERFECT (2026-10-20)  
**Source:** `tools/math-diagrams/templates/semicircle_r7.tex`  
**Output:** `Grade9-Maths/.../Lesson-01-Measurement-Circles-And-Scale/diagrams/semicircle_r7.png`

## Build
```powershell
& $env:MIMO_PYTHON tools/math-diagrams/build.py --only semicircle_r7
```

## Layout
- Arc only: `(-2.2,0) arc[start angle=180, end angle=0, radius=2.2]` — **no `-- cycle`**.
- Diameter base: one `md accent, thick, dashed` line from `(-2.2,0)` to `(2.2,0)`.
- Radius: `md accent, thick` from `O` to `(2.2,0)`.
- `O` at `(0.22, -0.3)` (below-right of the centre dot).
- `r = 7 cm` at `(1.15, 0.28)` (above the radius).
- Formulas at `(0, -0.85)`: `$\text{Area} = \tfrac{1}{2}\pi r^{2} \qquad \text{perimeter} = \pi r + 2r$`.

## Pitfalls (do not repeat)
1. **Doubled base line.** `arc … -- cycle` closes the path and strokes the flat base
   in ink; drawing the dashed diameter on top gave a thick blue-over-black slab.
   Draw the **arc alone**, then the diameter as one line.
2. **White sticker boxes** on `O` and the formula node — plain `font=\sffamily` nodes.
3. Formulas are **data** (like `d = 2r`), not captions — but keep them below the
   shape and out of the stroke.

## Contract
- [x] Exactly one base line
- [x] No white boxes
- [x] Formulas kept, placed clear of the shape
- [x] No label collisions
