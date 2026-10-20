# triangle_exterior_angle_diagram — Triangle ABC with exterior angle at C

**Status:** PERFECT (2026-10-20)  
**Source:** `tools/math-diagrams/templates/triangle_exterior_angle_diagram.tex`  
**Output:** `Grade9-Maths/.../Lesson-01-Polygons-And-Angle-Properties/diagrams/triangle_exterior_angle_diagram.png`

## Build
```powershell
& $env:MIMO_PYTHON tools/math-diagrams/build.py --only triangle_exterior_angle_diagram
```

## Geometry
- Triangle `A(0,0) B(4.6,0) C(1.55,2.35)`.
- Extend **BC beyond C** to D: `D = ($(B)!1.55!(C)$)` ≈ `(-0.13, 3.64)`.
  Draw the extension as `md dashed` (B→D) and `md ray` (C→D).
- Interior arcs (accent, radius 0.65):
  - at A: `angle=B--A--C`, label `25°`
  - at B: `angle=C--B--A`, label `(x+15)°`
- Exterior arc (highlight red, radius 0.75) at C: `angle=D--C--A`, label `(3x−10)°`
- Small muted interior arc at C: `angle=A--C--B` (radius 0.40).

## The geometric fact being shown
The exterior angle at C equals the sum of the two opposite interior angles:
$(3x - 10) = 25 + (x + 15)$, so $2x = 0 \Rightarrow x = 0$ — the lesson prose solves it;
the figure only shows the configuration.

## Pitfalls (do not repeat)
1. **Wrong side for the exterior angle.** The exterior at C is between **CA and
   CD** where D lies on BC **extended past C**. Extending AC instead, or putting
   D on AB, gives a different angle. Keep `D = ($(B)!1.55!(C)$)`.
2. **White sticker boxes** (`md label`) on A, B, C, D and the angle values —
   plain `font=\sffamily` nodes.
3. Angle labels ride outside their arc via `angle eccentricity` (1.3–1.4);
   do not drop them to 1.0 or they land on the arc.

## Contract
- [x] No white boxes
- [x] No prose captions
- [x] Exterior angle on the correct arm
- [x] Angle values are data (kept), placed outside their arcs
