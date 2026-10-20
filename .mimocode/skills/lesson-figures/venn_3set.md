# venn_3set — Three-set Venn diagram

**Skill id:** `venn_3set`  
**Status:** PERFECT (verified by PNG observation, 2026-10-20)  
**Output:** `Grade9-Maths/Strand-1-Number/Substrand-1-Numeration-Systems/Lesson-02-Number-Systems-And-Venn-Diagrams/diagrams/venn_3set.png`  
**Source:** `tools/math-diagrams/templates/venn_3set.tex`

## What this figure shows

Three overlapping sets $M$ (Mathematics, blue), $E$ (English, red), $S$ (Science, green)
inside a universal rectangle $U$. All **seven** regions are labelled with set notation so
the learner can "fill from the centre outwards".

## Build

```powershell
$env:Path = "C:\Program Files\MiKTeX\miktex\bin\x64;" + $env:Path
& $env:MIMO_PYTHON tools/math-diagrams/build.py --only venn_3set
& $env:MIMO_PYTHON tools/math-diagrams/lint_templates.py
```

## Exact geometry

| Element | Value | Why |
| :--- | :--- | :--- |
| Circle centres | $(-0.9, 0.55)$, $(0.9, 0.55)$, $(0, -0.85)$ | symmetric triple overlap |
| Radius | 1.55 | all pair distances $< 2r = 3.10$ |
| $M$–$E$ distance | 1.80 | overlaps |
| $M$–$S$ distance | 1.66 | overlaps |
| Rectangle | $(-3.3,-2.95)$ to $(3.5,2.55)$ | clears circles + outside `S` name |

**Critical check:** every pair must overlap ($d < 2r$) **and** the triple region must exist
(centroid $(0, 0.083)$ lies inside all three circles). If the triple vanishes, the
`M ∩ E ∩ S` label floats in a pairwise lens and the diagram is wrong.

## Region label positions

| Region | Position | Size |
| :--- | :--- | :--- |
| `M only` | $(-1.95,\ 0.85)$ | footnotesize |
| `E only` | $(1.95,\ 0.85)$ | footnotesize |
| `S only` | $(0,\ -1.5)$ | footnotesize |
| `M ∩ E` | $(0,\ 1.15)$ | tiny |
| `M ∩ S` | $(-1.05,\ -0.55)$ | tiny |
| `E ∩ S` | $(1.05,\ -0.55)$ | tiny |
| `M ∩ E ∩ S` | $(0,\ 0.12)$ | tiny |

Tiny is mandatory for the intersection labels — footnotesize overflows the lenses.

## Set names

`M`, `E`, `S` sit **outside** their circles (above $M$/$E$, below $S$), colour-matched to
the circle stroke. Never place a set name inside a circle — it reads as a region label.

## Visual contract

- [x] No caption sentences / prose
- [x] No white sticker boxes (`md label` with white fill)
- [x] All seven regions labelled with maths notation
- [x] Set names outside the shapes
- [x] No risky glyphs

## Pitfalls observed (do not repeat)

1. **White sticker boxes** (`md label`, `md label bold`) — replace with plain
   `font=\sffamily` text nodes.
2. **`M ∩ E ∩ S` at `\small`** overflowed the triple region and spilled into the pairwise
   lenses. Use `\tiny`.
3. **Set name `S` inside the circle** collided with the `S only` region label. Circle $S$
   bottom is $y = -0.85 - 1.55 = -2.40$; the name must sit below that ($y \approx -2.7$),
   which also requires extending the rectangle to $y = -2.95$.
4. **Only the triple region labelled** — a teaching figure needs all seven regions or the
   "fill from the centre outwards" method cannot be read from the picture.

## How to replicate

1. Copy `templates/venn_3set.tex`; change set letters if the subject differs.
2. Keep the centre triangle and radius unless label text is much longer.
3. Build, **read the PNG**, verify: 7 labels, names outside, no boxes, triple present.
4. `lint_templates.py` must pass.
5. Reference from prose as `![Figure N](diagrams/venn_3set.png)` — no caption text.
