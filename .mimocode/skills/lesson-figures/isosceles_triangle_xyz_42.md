# isosceles_triangle_xyz_42 — XY = YZ, vertex 42°, base angles x

**Status:** PERFECT (2026-10-20)  
**Source:** `tools/math-diagrams/templates/isosceles_triangle_xyz_42.tex`  
**Output:** `Grade9-Maths/.../Lesson-03-Angles-Parallel-Lines-And-Trigonometry/diagrams/isosceles_triangle_xyz_42.png`

## Build
```powershell
& $env:MIMO_PYTHON tools/math-diagrams/build.py --only isosceles_triangle_xyz_42
```

## Geometry
- `Y(0, 2.6)` vertex, `X(-2.2, 0)` and `Z(2.2, 0)` base.
- Equal-side ticks on XY and YZ (single slash each).
- Angle values: $42°$ at Y, $x$ at X, $x$ at Z — placed **inside** each angle.

## Math
$2x + 42° = 180° \Rightarrow 2x = 138° \Rightarrow x = 69°$ (matches Mock 2026 P1 Q27 option D).

## THE critical pitfall — TikZ angle direction

`angle=A--B--C` sweeps **counterclockwise** from the ray $B \to A$ to the ray $B \to C$.

At X the interior angle sits between $X \to Z$ (0°) and $X \to Y$ (≈50°). Writing
`angle=Y--X--Z` sweeps 50° → 0° the **long way round (310°)** and draws a huge
reflex arc. Use **`angle=Z--X--Y`** so it sweeps the small interior angle.

| Vertex | Correct | Wrong |
| :---: | :--- | :--- |
| Y | `angle=X--Y--Z` | — |
| X | `angle=Z--X--Y` | `angle=Y--X--Z` (reflex) |
| Z | `angle=Y--Z--X` | — |

## Other pitfalls
1. **Prose in the formula** `XY = YZ ⇒ base angles equal; …` — keep only
   `$XY = YZ \qquad 2x + 42^\circ = 180^\circ$`.
2. **White sticker boxes** (`md label bold`, `md label muted`) — plain
   `font=\sffamily` nodes.
3. Angle values go **inside** the angle; if the arc is reflex the label gets
   pushed outside — a sure sign the ray order is wrong.

## Contract
- [x] No white boxes
- [x] No prose captions
- [x] All arcs are small interior angles
- [x] Angle values inside their angle
