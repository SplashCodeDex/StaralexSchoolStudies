# polygon_triangulation_proof — Hexagon triangulated from vertex A

**Status:** PERFECT (2026-10-20)  
**Source:** `tools/math-diagrams/templates/polygon_triangulation_proof.tex`  
**Output:** `Grade9-Maths/.../Lesson-01-Polygons-And-Angle-Properties/diagrams/polygon_triangulation_proof.png`

## Build
```powershell
& $env:MIMO_PYTHON tools/math-diagrams/build.py --only polygon_triangulation_proof
```

## Geometry
- Hexagon `A(0,0) B(3.4,0.15) C(5.0,1.9) D(4.0,4.0) E(1.5,4.4) F(-0.8,2.4)`.
- Three **dashed accent diagonals** from A to the non-adjacent vertices C, D, E.
- That yields $n - 3 = 3$ diagonals and $n - 2 = 4$ triangles — matches the
  formula at the bottom.

| Triangle | Vertices | Label position |
| :--- | :--- | :---: |
| $T_1$ | A-B-C | $(1.6,\ 1.10)$ |
| $T_2$ | A-C-D | $(3.0,\ 1.85)$ |
| $T_3$ | A-D-E | $(2.55,\ 3.35)$ |
| $T_4$ | A-E-F | $(0.75,\ 2.95)$ |

## Pitfalls (do not repeat)
1. **`T₁` on the A→C diagonal.** A→C has slope $1.9/5.0 = 0.38$; at $x = 1.7$
   the line is at $y = 0.65$, and the first label sat at $y = 0.70$ — on the
   stroke. Compute the diagonal's height and keep ≥ 0.4 clearance.
2. **Prose caption `from one vertex: (n−3) diagonals ⇒ (n−2) triangles`.** Keep
   only the formula `$d = n-3 \quad t = n-2$`; the lesson prose states the rule.
3. **White sticker boxes** on every vertex and triangle label — plain
   `font=\sffamily` nodes.
4. Each triangle label must sit in **its own** triangle (bounded by the two
   diagonals from A and one edge), not in a neighbour's.

## Contract
- [x] No white boxes
- [x] No prose captions
- [x] Triangle labels inside their own triangle, clear of the diagonals
- [x] Formula only at the bottom
