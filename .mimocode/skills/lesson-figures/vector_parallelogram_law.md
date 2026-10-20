# vector_parallelogram_law — a + b via the parallelogram

**Status:** PERFECT (2026-10-20)  
**Source:** `tools/math-diagrams/templates/vector_parallelogram_law.tex`  
**Output:** `Grade9-Maths/.../Lesson-02-Vectors/diagrams/vector_parallelogram_law.png`

## Build
```powershell
& $env:MIMO_PYTHON tools/math-diagrams/build.py --only vector_parallelogram_law
```

## Layout
- `O = (0,0)`, `B = (3.0, 0.2)`, `D = (0.8, 2.3)`, `C = B + D = (3.8, 2.5)`.
- Outline `O -- B -- C -- D -- cycle`.
- Vectors: $\mathbf{a} = \vec{OB}$, $\mathbf{b} = \vec{OD}$ (accent), $\mathbf{a}+\mathbf{b} = \vec{OC}$ (highlight red).
- All **four** vertices labelled (O, B, C, D) — plain `font=\sffamily` nodes.

## Label positions (computed off the strokes)

| Label | Position | Why |
| :--- | :---: | :--- |
| `a` | $(1.55,\ -0.45)$ | below the near-horizontal $\vec{OB}$ |
| `b` | $(0.28,\ 1.35)$ | left of $\vec{OD}$ |
| `a+b` | $(2.35,\ 0.75)$ | $\vec{OC}$ slope $\approx 0.658$; $y_{\text{line}}(2.35)=1.55$ — 0.8 below |
| formula | $(2.0,\ -1.15)$ | below the figure |

## Pitfalls (do not repeat)
1. **`a + b` floating in the interior** as a region-looking label. Put it beside
   the diagonal it names, computed off the line's height.
2. **Prose caption `parallelogram law`.** The lesson prose names the law; the
   figure carries only the formula `$\vec{OB}+\vec{OD}=\vec{OC}$`.
3. **Only O and C named.** A parallelogram has four vertices — if the vectors
   start at O and end at B and D, those corners must be labelled too or the
   formula cannot be read from the figure.
4. **White sticker boxes** (`md label`) — plain text nodes.

## Contract
- [x] No white boxes
- [x] No prose captions
- [x] All four vertices named
- [x] Vector names clear of their strokes
