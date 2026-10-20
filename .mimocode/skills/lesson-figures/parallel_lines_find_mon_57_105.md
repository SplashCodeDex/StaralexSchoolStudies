# parallel_lines_find_mon_57_105 — Given 57° and 105°, find ∠MON

**Status:** PERFECT (2026-10-20)  
**Source:** `tools/math-diagrams/templates/parallel_lines_find_mon_57_105.tex`  
**Output:** `Grade9-Maths/.../Lesson-03-Angles-Parallel-Lines-And-Trigonometry/diagrams/parallel_lines_find_mon_57_105.png`

## Build
```powershell
& $env:MIMO_PYTHON tools/math-diagrams/build.py --only parallel_lines_find_mon_57_105
```

## Geometry
- Parallel lines `p` at $y = 2.8$, `q` at $y = 0$, both $x \in [-2.8, 5.0]$.
- Points: `P(-2.4,2.8) M(0.2,2.8) O(1.5,0) N(4.4,0)`.
- Transversal `M–O` in accent.
- Arcs: $\angle PMO$ (blue, radius 0.55) and the marked angle at O
  (highlight red, radius 0.70).

## Label placement

| Label | Position | Why |
| :--- | :---: | :--- |
| $57°$ | $(M)+(-1.05,\ -0.50)$ | **inside** the $\angle PMO$ wedge (below $p$, left of the transversal) |
| $105°$ | $(O)+(1.35,\ -1.05)$ | below-right of O, clear of the red arc |
| $\angle MON = ?$ | $(2.15,\ 0.75)$ | inside the upper wedge, clear of the transversal |

## Pitfalls (do not repeat)
1. **`57°` placed above line $p$.** The angle $\angle PMO$ opens **below** $p$
   (between the leftward ray $M\to P$ and the transversal $M\to O$). Placing the
   value above the line puts it outside the angle it names.
2. **`∠MON = ?` on the transversal.** The `∠` glyph is wide; at $x = 1.85$ it
   still touched the $M\to O$ stroke. Push the node to $x = 2.15$.
3. **White sticker boxes** (`md label`, `md label bold`, `md label accent`) —
   plain `font=\sffamily` nodes.

## Contract
- [x] No white boxes
- [x] Each angle value inside the angle it names
- [x] Unknown label clear of the transversal
- [x] Parallel marks present on both lines
