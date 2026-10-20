# venn_2set — Two-set Venn diagram

**Skill id:** `venn_2set`  
**Status:** PERFECT (verified by PNG observation, 2026-10-20)  
**Output:** `Grade9-Maths/Strand-1-Number/Substrand-1-Numeration-Systems/Lesson-02-Number-Systems-And-Venn-Diagrams/diagrams/venn_2set.png`  
**Source:** `tools/math-diagrams/templates/venn_2set.tex`

## What this figure shows

Two overlapping sets $A$ (blue) and $B$ (red) inside a universal set rectangle $U$.
Regions labelled `A only`, `A ∩ B`, `B only`; complement of the union is marked
`$(A \cup B)'$`. Used to teach set relationships and the counting rule
$n(A \cup B) = n(A) + n(B) - n(A \cap B)$.

## Build

```powershell
$env:Path = "C:\Program Files\MiKTeX\miktex\bin\x64;" + $env:Path
& $env:MIMO_PYTHON tools/math-diagrams/build.py --only venn_2set
& $env:MIMO_PYTHON tools/math-diagrams/lint_templates.py
```

## Exact geometry (do not eyeball)

| Element | Value | Why |
| :--- | :--- | :--- |
| Circle centres | $(-0.85,\,0.15)$ and $(0.85,\,0.15)$ | distance 1.70 |
| Radius | 1.35 | overlap width $= 2r - d = 1.00$ |
| Lens width | ≈ 1.00 | fits the label `A ∩ B` without touching the strokes |
| Rectangle | $(-3.0,-1.85)$ to $(3.2,\,2.35)$ | clears circles + outside labels |
| Set names | $(\pm1.75,\,1.85)$ | **outside / above** the circles, never inside |
| Region labels | $y = 0.15$ | vertical centre of the circles |
| Complement | $(0,\,-1.5)$ | below the circles, inside the rectangle |

**Critical check:** $d < 2r$. If the circles do not overlap, the intersection label
floats in empty space and the figure is mathematically wrong. First version of this
diagram had centres at $\pm1.5$ with $r=1.35$ ($d=3.0 > 2.70$) — **the circles did not
touch**. Always verify the overlap numerically before building.

## Styles used

| Style | Role |
| :--- | :--- |
| `md thin, draw=mdInk` | universal rectangle |
| `mdAccentSoft, opacity=0.9` | fill of $A$ |
| `mdRed, opacity=0.15` | fill of $B$ (lens blends to purple) |
| `md, draw=mdAccent/Red, line width=1pt` | circle strokes |
| `md label naked` / plain `font=\sffamily` | labels — **no white sticker boxes** |

## Visual contract (from tools/README-figures.md)

- [x] No caption sentences inside the figure
- [x] No `Figure N:` text
- [x] No white boxes behind labels
- [x] Region labels are data (`A only`, `A ∩ B`), not prose
- [x] Complement written as maths `$(A \cup B)'$`, not the word "outside"
- [x] No risky glyphs (`✓ ℤ ■` …)
- [x] Set names outside the shapes

## Pitfalls observed (do not repeat)

1. **Non-overlapping circles** — wrong geometry makes the diagram a lie. Check $d < 2r$.
2. **White sticker boxes** (`md label` with `fill=white, fill opacity=0.85`) look like
   sticky notes. Use plain `font=\sffamily` text nodes instead.
3. **Prose captions** (`outside: A ∪ B`) — replace with the mathematical symbol.
4. **Label wider than its region** — `A ∩ B` at `\small` touched the circle strokes in a
   0.70-wide lens; drop to `\footnotesize` or widen the overlap.
5. **Set names inside the circles** — they read as region labels. Put them outside, above.

## How to replicate

1. Copy `templates/venn_2set.tex` and adjust the two set letters and colours if needed.
2. Keep the geometry table values unless the label text is much longer.
3. Build, **read the PNG**, check every box above.
4. Run `lint_templates.py` — it must pass.
5. Reference from the lesson prose as `![Figure N](diagrams/venn_2set.png)` with **no
   caption text** in the markdown link.
