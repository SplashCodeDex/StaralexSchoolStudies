---
name: lesson-figures
description: Draw textbook figures (number lines, geometry, graphs, Venn, vectors) for lesson PDFs. Use whenever a lesson needs a diagram — or when a figure is wrong, mangled, has baked-in captions, wrong dot positions, or missing labels. Covers the TikZ toolkit in tools/math-diagrams, the Pillow number-line tool, and the locked visual contract.
---

# Lesson Figures & Number Lines

## When to use

A lesson PDF needs a figure whenever the concept is visual **or** the exam question is visual
(geometry, number lines, graphs, vectors, Venn, nets, hardware labels, design elements).
Do **not** decorate. `RULES-BECE-PATTERN.md` §4 lists the topics that require one.

## Canonical toolchain

| Figure type | Tool | Notes |
| :--- | :--- | :--- |
| Number lines, geometry, graphs, Venn, vectors | **`tools/math-diagrams/`** (TikZ → PNG) | preferred; shared style file |
| Quick number lines only | `tools/draw_number_line.py` (Pillow) | fallback if TikZ is down |
| Display maths (equations) | `tools/build_lesson_pdf.py` (LaTeX) | not figures — maths |

Build:
```powershell
$env:PYTHON  tools/math-diagrams/build.py --only <template-id>
$env:PYTHON  tools/math-diagrams/lint_templates.py     # MUST pass before shipping
```

## The locked visual contract

1. **No captions in the image.** No `Figure 1: …`, no `solid dot at …, arrow to the right`,
   no `1 < x ≤ 5` written inside the drawing. The prose says `See Figure 1.` and nothing else.
2. **Measurement labels are fine.** `6 cm`, `57°`, `A`, `B`, `x`, tick numbers — these are data,
   not captions.
3. **Number line: the solution sits ABOVE the axis.** Axis (ticks + numbers) is the base at
   `\\y`; the solution ray/dots live at `\\yr > \\y`.
4. **Numbers are exact.** $-4/3$ draws at `-1.333333`, never at `-1`.
   Open circle for `<` / `>`; filled for `≤` / `≥`.
5. **One shape language.** Ink `#1A1A1A` axis, accent `#1F4E79` solution, no gradients/glows.
6. **No risky glyphs.** `✓ ✗ ℤ 𝕎 ■ □ ◆` have all printed as tofu in Cambria. Use words or shapes.
7. **Delete stale siblings.** A leftover `.svg` from an older renderer is how Figure 3 shipped
   mangled. Regenerate PNG; do not leave two sources of truth in `diagrams/`.
8. **Rasterise the PDF page and look at it** before declaring done.

## Template rules (enforced by `lint_templates.py`)

```
FORBIDDEN in a .tex template
  ✓ caption sentences / inequality statements in \\node bodies
  ✓ "solid dot at… / arrow to…" prose
  ✓ "Figure N:" text
  ✓ number-line solution drawn at \\y (on the axis) instead of \\yr (above)
  ✓ duplicate bold point labels when tick numbers already exist
ALLOWED
  ✓ tick numbers, measurement labels (6 cm, 57°, A, B)
  ✓ geometric marks: dots, arcs, arrows, shaded regions
```

`lint_templates.py` exits 2 on any violation. **Always run it before building.**

## Number-line recipe (TikZ)

```tex
\\def\\y{0}      % axis height
\\def\\yr{0.55}  % solution height, above the axis
\\draw[md axis] (-1,\\y) -- (7,\\y);
\\foreach \\x in {-1,...,7}{
  \\draw[md tick] (\\x,\\y-0.12) -- (\\x,\\y+0.12) node[md label naked, below=2.5pt] {\\x};
}
\\draw[md accent, thick] (1,\\yr) -- (5,\\yr);
\\node[md open point] at (1,\\yr) {};      % excluded endpoint
\\node[md accent point] at (5,\\yr) {};    % included endpoint
```

Compound `1 < x ≤ 5`:
```powershell
python tools/math-diagrams/build.py --only number_line_double_inequality_1_5
```

## Known failures (do not repeat)

| Failure | Cause | Fix |
| :--- | :--- | :--- |
| `●━━━▶` ASCII number lines | text diagram in markdown | always PNG via TikZ/Pillow |
| Dot at −1, prose said −1⅓ | eyeballed pixel offset | compute from the value |
| Baked `1 < x ≤ 5` caption + duplicate `1`/`5` labels | old template used `md label accent` nodes | caption lives in markdown; tick numbers only |
| Skeletal / hollow ticks (`fill-opacity=0`) | dvisvgm SVG used as the shipped PNG | ship the pdflatex→PNG output, not the dvisvgm SVG |
| Stale PNG from an older renderer | two generators writing `diagrams/` | one canonical builder; delete sibling `.svg` if unused |
| `✓` printing as `.` in the PDF body | Cambria has no U+2713 | write `(correct)` or draw a tick |
| `ℤ` printing as `◆` | font fallback | words (`integers`) or LaTeX |

## Integration

- Skill copy: `.mimocode/skills/lesson-figures/SKILL.md` (this file).
- PDF builder: `tools/build_lesson_pdf.py --strict` fails on tofu glyphs.
- Lesson rules: `RULES-BECE-PATTERN.md` §4, `Grade9-Maths/Rules.md` M2.
