# polygon_exterior_angle_concept — Interior + exterior at vertex B

**Status:** PERFECT (2026-10-20)  
**Source:** `tools/math-diagrams/templates/polygon_exterior_angle_concept.tex`  
**Output:** `Grade9-Maths/.../Lesson-01-Polygons-And-Angle-Properties/diagrams/polygon_exterior_angle_concept.png`

## Build
```powershell
& $env:MIMO_PYTHON tools/math-diagrams/build.py --only polygon_exterior_angle_concept
```

## Geometry
- Hexagon `A(0,0) B(3.4,0) C(5.1,2.1) D(3.6,4.1) E(0.9,4.1) F(-0.7,2.1)`.
- AB extended past B with `md dashed` to `Dext = ($(A)!1.65!(B)$)`, then
  `md ray, thick` B → Dext (the exterior arm).
- Interior arc: `pic[md angle arc, angle radius=0.55cm] {angle=C--B--A}`.
- Exterior arc: `pic[md highlight, angle radius=0.85cm] {angle=Dext--B--C}`.

## Label placement (inside each wedge, off the arms)

| Label | Position | Why |
| :--- | :---: | :--- |
| `interior` | $(2.55,\ 1.15)$ | inside the B→A / B→C wedge |
| `exterior` | $(4.55,\ 0.55)$ | inside the B→D / B→C wedge; B→C has slope $1.235$, at $x = 4.55$ the edge is at $y = 1.41$, so 0.86 below |
| formula | $(1.7,\ -1.35)$ | below the figure |

## Pitfalls (do not repeat)
1. **`exterior` crossed the B→C edge.** At $(4.85, 1.15)$ the word spanned
   $x \in [4.25, 5.45]$ and the left half sat on the line. Keep the label in the
   **wedge**, computed off the arm's height.
2. **White sticker boxes** (`md label`) on the vertices, angle names, and formula
   — plain `font=\sffamily` nodes.
3. Angle names `interior` / `exterior` are legitimate labels (like `run` / `rise`),
   but the formula line must not carry a prose prefix.

## Contract
- [x] No white boxes
- [x] Angle labels inside their own wedge, clear of the arms
- [x] Formula is data (`interior + exterior = 180°`)
- [x] Dashed extension + arrowhead mark the exterior arm clearly
