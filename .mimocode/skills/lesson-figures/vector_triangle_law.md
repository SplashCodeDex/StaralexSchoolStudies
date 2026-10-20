# vector_triangle_law — AB + BC = AC

**Status:** PERFECT (2026-10-20)  
**Source:** `tools/math-diagrams/templates/vector_triangle_law.tex`  
**Output:** `Grade9-Maths/.../Lesson-02-Vectors/diagrams/vector_triangle_law.png`

## Build
```powershell
& $env:MIMO_PYTHON tools/math-diagrams/build.py --only vector_triangle_law
```

## Layout
- `A = (0,0)`, `B = (3.2,0.3)`, `C = (4.6,2.8)`.
- Vectors (all `md accent, thick, ->` except the sum):
  - $\vec{AB} = \mathbf{a}$ — accent
  - $\vec{BC} = \mathbf{b}$ — accent
  - $\vec{AC} = \mathbf{a}+\mathbf{b}$ — highlight (red)
- Label positions (computed off the strokes, **not** `midway`):

| Label | Position | Why |
| :--- | :---: | :--- |
| `a` | $(1.6,\ -0.45)$ | well below the near-horizontal A→B |
| `b` | $(4.35,\ 1.55)$ | right of B→C, clear of the segment |
| `a+b` | $(1.75,\ 1.85)$ | A→C has slope $0.61$; $y_{\text{line}}(1.75)=1.07$, so 0.8 units above |
| formula | $(2.3,\ -1.05)$ | below everything |

## Pitfalls (do not repeat)
1. **`midway, left=3pt` on A→C put `a+b` on the stroke.** Midpoint of A→C is
   $(2.3, 1.4)$ — and `left=3pt` still left the text touching the line. Compute
   the line's height at the label's x and pick empty space.
2. **Prose prefix `triangle law:`** before the formula is a caption. Keep the
   formula `$\vec{AB}+\vec{BC}=\vec{AC}$` alone; the lesson prose names the law.
3. **White sticker boxes** on `A`, `B`, `C` — plain `font=\sffamily` nodes.

## Contract
- [x] No white boxes
- [x] No prose captions
- [x] Every vector name clear of its stroke
- [x] Formula is data, placed below the figure
