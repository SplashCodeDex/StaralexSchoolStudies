# right_triangle_qpr_6_8 — Right triangle QPR (QR=6, PR=8, θ at Q)

**Status:** PERFECT (2026-10-20)  
**Source:** `tools/math-diagrams/templates/right_triangle_qpr_6_8.tex`  
**Output:** `Grade9-Maths/.../Lesson-03-Angles-Parallel-Lines-And-Trigonometry/diagrams/right_triangle_qpr_6_8.png`

## Build
```powershell
& $env:MIMO_PYTHON tools/math-diagrams/build.py --only right_triangle_qpr_6_8
```

## Layout
- Vertices: `R = (0,0)`, `Q = (3.0,0)`, `P = (0,4.0)` (right angle at R).
- Right-angle mark: **square corner** of legs 0.32 —
  `($(R)+(0.32,0)$) -- ($(R)+(0.32,0.32)$) -- ($(R)+(0,0.32)$)`.
- Measurements `6 cm`, `8 cm`; hypotenuse named `|PQ|`; angle `θ` at Q via `pic[angle=P--Q--R]`.

## Pitfalls (do not repeat)
1. **Malformed right-angle mark.** The calc idiom
   `($(R)!0.35!(Q)!0.35!90:(Q)$)` produced a pentagon-looking blob. Use the
   absolute square-corner path above — two equal legs from R along RQ and RP.
2. **Baked-in worked solution** (`$|PQ|=\sqrt{6^2+8^2}=10$; $\tan\theta=8/6=4/3$`)
   was a caption. The working belongs in the lesson prose, never in the figure.
3. **`md label` white boxes** on vertices and measurements — use plain nodes.

## Contract
- [x] No solution / caption text in the figure
- [x] Right-angle mark is a true square
- [x] Measurements and vertex names only
- [x] Angle arc + `θ` label at the correct vertex
