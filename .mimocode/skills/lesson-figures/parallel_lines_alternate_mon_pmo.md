# parallel_lines_alternate_mon_pmo — Z-configuration alternate angles

**Status:** PERFECT (2026-10-20)  
**Source:** `tools/math-diagrams/templates/parallel_lines_alternate_mon_pmo.tex`  
**Output:** `Grade9-Maths/.../Lesson-03-Angles-Parallel-Lines-And-Trigonometry/diagrams/parallel_lines_alternate_mon_pmo.png`

## Build
```powershell
& $env:MIMO_PYTHON tools/math-diagrams/build.py --only parallel_lines_alternate_mon_pmo
```

## Geometry
- Parallel lines `p` at $y = 2.2$ and `q` at $y = 0$, both $x \in [-2.2, 3.6]$.
- Parallel marks: short dashes at $(-1.6, 2.32)$ and $(-1.6, 0.12)$.
- Points: `P(-1.8,2.2) M(0.2,2.2) O(-0.8,0) N(1.4,0)`.
- Transversal `M–O` in accent; the **Z** `P–M–O–N` in highlight red.

## Angle labels (inside their wedge, off the arms)

| Label | Position | Why |
| :--- | :---: | :--- |
| $\angle PMO$ | $(-1.00,\ 1.52)$ | wedge opens down-left from M (bisector ≈ 209°) |
| $\angle MON$ | $(0.35,\ 0.85)$ | wedge opens up-right from O; right of O–M, above O–N |
| formula | $(0.8,\ -1.15)$ | `$\angle PMO = \angle MON$` |

## Pitfalls (do not repeat)
1. **`∠MON` sat on the O vertex and its arc.** TikZ `angle eccentricity=1.45`
   pushed the label to the **reflex** side of the angle. Place angle names with
   an explicit coordinate inside the intended wedge instead.
2. **`∠PMO` grazed the red Z-line** for the same reason — explicit coordinates
   beat `angle eccentricity` when the arms are dense.
3. **Prose caption `Z-configuration ⇒ alternate angles`.** Keep only the
   equality `$\angle PMO = \angle MON$`; the lesson prose names the Z-rule.
4. **White sticker boxes** (`md label`) on every label — plain `font=\sffamily` nodes.

## Contract
- [x] No white boxes
- [x] No prose captions
- [x] Angle names inside their wedge, clear of the arms and the vertex
- [x] Formula states the equality
