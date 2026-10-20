# algebra_length_from_diagram — Mock P1 Q17 (2.1 + x + 3.4 = 9.7)

**Status:** PERFECT (2026-10-20)  
**Source:** `tools/math-diagrams/templates/algebra_length_from_diagram.tex`  
**Output:** `Grade9-Maths/.../Lesson-01-Algebraic-Expressions-And-Modelling/diagrams/algebra_length_from_diagram.png`

## Build
```powershell
& $env:MIMO_PYTHON tools/math-diagrams/build.py --only algebra_length_from_diagram
```

## Geometry
- Rectangle $(0,0)$ to $(6.4, 1.6)$.
- Dashed dividers at $x = 1.5$ and $x = 4.2$ — three segments of widths
  1.5, 2.7, 2.2 (proportional to 2.1, x, 3.4 once solved).
- Labels centred under each segment: `2.1` at $(0.75,\ -0.30)$, `x` at
  $(2.85,\ -0.30)$ (accent), `3.4` at $(5.3,\ -0.30)$.
- Total `9.7 cm` centred above at $(3.2,\ 1.88)$.
- Equation at $(3.2,\ -0.95)$: `$2.1 + x + 3.4 = 9.7$`.

## Math check
$2.1 + 3.4 = 5.5$; $x = 9.7 - 5.5 = 4.2$ (matches Mock 2026 P1 Q17).

## Pitfalls (do not repeat)
1. **White sticker boxes** (`md label`, `md label accent`, `md label muted`) —
   plain `font=\sffamily` nodes.
2. Segment labels must sit **under their own segment** (use the segment's
   midpoint x), not under the whole rectangle.

## Contract
- [x] No white boxes
- [x] No prose captions (equation is data)
- [x] Labels centred under their segment
- [x] Unknown `x` distinguished in accent colour
