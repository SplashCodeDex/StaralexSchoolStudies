# hexagon_angles_diagram — Irregular hexagon with algebraic interior angles

**Status:** PERFECT (2026-10-20)  
**Source:** `tools/math-diagrams/templates/hexagon_angles_diagram.tex`  
**Output:** `Grade9-Maths/.../Lesson-01-Polygons-And-Angle-Properties/diagrams/hexagon_angles_diagram.png`

## Build
```powershell
& $env:MIMO_PYTHON tools/math-diagrams/build.py --only hexagon_angles_diagram
```

## Geometry
- Irregular hexagon `A(0,0) B(3.0,0.2) C(4.5,1.9) D(3.7,3.9) E(1.2,4.2) F(-0.85,2.3)`.
- Six interior arcs (`md angle arc`, radius 0.38, eccentricity 1.15).

## Angle values (must sum to 720°)

| Vertex | Label | At x = 20 |
| :---: | :---: | :---: |
| A | $120°$ | 120° |
| B | $(5x-6)°$ | 94° |
| C | $(4x+14)°$ | 94° |
| D | $7x°$ | 140° |
| E | $(8x-8)°$ | 152° |
| F | $6x°$ | 120° |

**Check:** $120 + (5x-6) + (4x+14) + 7x + (8x-8) + 6x = 120 + 30x = 720 \Rightarrow x = 20$.
$120+94+94+140+152+120 = 720$ ✓. Never ship the figure without this check.

## Label positions (outside the vertex, clear of the edges)
`A(−0.55,−0.75)  B(3.15,−0.85)  C(5.85,1.85)  D(3.95,5.15)  E(1.15,5.45)  F(−2.15,2.35)`

## Pitfalls (do not repeat)
1. **White sticker boxes** (`md label big`, `md label muted`) — plain
   `font=\sffamily\large` / `\small` nodes.
2. **Unchecked angle sum.** The algebraic labels must satisfy the interior-sum
   formula before the figure is built.
3. Angle labels belong **outside** the vertex, not inside the hexagon where they
   would collide with the arcs.

## Contract
- [x] No white boxes
- [x] No prose captions (formula `interior sum = (n−2) × 180° = 720°` is data)
- [x] All six angles labelled, values sum to 720°
- [x] Labels clear of edges and arcs
