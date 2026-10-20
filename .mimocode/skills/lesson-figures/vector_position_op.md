# vector_position_op — Position vector OP for P(4,3)

**Status:** PERFECT (2026-10-20)  
**Source:** `tools/math-diagrams/templates/vector_position_op.tex`  
**Output:** `Grade9-Maths/.../Lesson-02-Vectors/diagrams/vector_position_op.png`

## Build
```powershell
& $env:MIMO_PYTHON tools/math-diagrams/build.py --only vector_position_op
```

## Layout
- Axes `\mdAxes{-1}{6}{-1}{5}{1}{1}`.
- `O = (0,0)`, `P = (4,3)`. Vector `md accent, thick, ->` from O to P.
- `P(4,3)` above-right of P; `O` below-left of O.
- Formula `$\vec{OP} = \begin{pmatrix} 4 \\ 3 \end{pmatrix}$` at **(3.35, 1.05)**.

## The collision rule (this is the whole lesson)

The vector line has slope $3/4$, so its equation is $y = \tfrac{3}{4}x$.
Any label at $(x, \tfrac{3}{4}x)$ sits **on the stroke**. The first version put the
formula at $(2.4, 1.8)$ — and $1.8 = \tfrac{3}{4}\times 2.4$ exactly.

**Before placing a label near a line, compute the line's height at that x and
choose a region clearly off it.** Here `(3.35, 1.05)` works because
$y_{\text{line}}(3.35) = 2.51$ — the label is 1.5 units below the line.

## Pitfalls
1. **Label on the vector line** — see the collision rule above.
2. **White sticker boxes** (`md label accent`, `md label bold`) — plain
   `font=\sffamily` nodes.
3. Column vector must use `\begin{pmatrix} … \end{pmatrix}` so it stacks properly.

## Contract
- [x] No white boxes
- [x] Formula is data, placed in empty space off the line
- [x] Point and origin labelled
- [x] Arrowhead visible on the vector
