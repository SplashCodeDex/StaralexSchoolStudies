---
name: math-diagrams
description: >
  Produce textbook-quality mathematics diagrams for Staralex school lessons
  (Grade7/Grade9/Basic maths) as real PNG figures using LaTeX/TikZ. Use whenever
  a maths lesson needs a number line, Venn diagram, angle/polygon/triangle figure,
  circle, vector, graph, pie chart, stem-and-leaf, probability tree, place-value
  chart, scale drawing, net, or locus — or when replacing imperfect AI/JPG figures.
  Trigger on: maths diagram, TikZ figure, geometry figure, Venn, number line,
  plot a graph for the lesson, "draw the figure", diagrams/ folder for maths.
---

# Maths Diagrams (LaTeX / TikZ)

## Mission

Every maths figure in this workspace is a **precise, labelled, textbook-style
PNG**, compiled from a **TikZ source**. Never ship ASCII art for complex shapes,
never bake labels into an AI-generated image, never leave a mock question that
says "in the diagram" without a figure.

## Non-negotiables

1. **TikZ is the only authoring path** for maths figures. Source lives in
   `tools/math-diagrams/templates/<id>.tex`. Output is a trimmed PNG in the
   lesson's `diagrams/` folder.
2. **Shared style package** `tools/math-diagrams/styles/mathdiagrams.sty` —
   always `\usepackage{mathdiagrams}`. Do not invent new colours or fonts.
3. **Caption + reference.** Markdown embeds
   `![Figure N: <caption>](diagrams/<file>.png)` and the question text must say
   `see Figure N` (or `the figure below`).
4. **Contextual only.** Add a figure when the concept or the exam question is
   visual (see table below). Never decorate.
5. **Mock fidelity.** If the bank says "use the diagram with 57° and 105°",
   the figure must show those exact givens and support the published answer.
6. **British English**, SI units, `GH₵` for money where relevant.

## Pipeline

```
tools/math-diagrams/
  styles/mathdiagrams.sty     shared TikZ styles & macros
  templates/<id>.tex          one standalone figure per id
  catalog.json                id → output PNG path + caption
  build.py                    compile catalog → PNG (200 dpi, white, trimmed)
```

### Build

```powershell
# everything
$env:MIMO_PYTHON tools/math-diagrams/build.py

# one figure
$env:MIMO_PYTHON tools/math-diagrams/build.py --only venn_2set

# single ad-hoc source
$env:MIMO_PYTHON tools/math-diagrams/build.py --tex path\fig.tex --out path\fig.png

# staleness check
$env:MIMO_PYTHON tools/math-diagrams/build.py --check
```

Requirements already on this machine: MiKTeX (`pdflatex`), Python with
`pypdfium2` and `Pillow` (use `$env:MIMO_PYTHON`).

### Add a new figure

1. Write `templates/<id>.tex` — standalone, `mathdiagrams`, stable coordinates.
2. Append a catalog entry:
   ```json
   {
     "id": "<id>",
     "tex": "templates/<id>.tex",
     "out": "Grade9-Maths/.../Lesson-.../diagrams/<id>.png",
     "caption": "Figure description used in the lesson",
     "lesson": "path without /diagrams"
   }
   ```
3. `build.py --only <id>`, open the PNG, fix labels/overflow.
4. Embed in the lesson markdown with caption and in-text reference.
5. Keep the `.tex` source forever — it is the editable master.

## Figure types → template catalog

| Need | Template id (copy & adapt) |
| --- | --- |
| Number line, open/closed dot, interval | `number_line_x_gt_4`, `number_line_x_ge_minus_4_3`, `number_line_double_inequality_1_5` |
| Place-value chart | `place_value_chart` |
| Number system hierarchy | `number_system_hierarchy` |
| Venn 2-set / 3-set | `venn_2set`, `venn_3set` |
| Polygon triangulation | `polygon_triangulation_proof` |
| Exterior angle of polygon | `polygon_exterior_angle_concept` |
| Triangle exterior angle | `triangle_exterior_angle_diagram` |
| Labelled irregular polygon angles | `hexagon_angles_diagram` |
| Congruent / similar triangles | `congruent_triangles_schema`, `similar_triangles_schema` |
| Similar compound shapes | `similarity_compound_shape_diagram` |
| Parallel lines, alternate angles | `parallel_lines_alternate_mon_pmo` |
| Parallel lines, find an angle | `parallel_lines_find_mon_57_105` |
| Isosceles triangle | `isosceles_triangle_xyz_42` |
| Right triangle (Pythagoras / tan) | `right_triangle_qpr_6_8` |
| Circle r/d | `circle_radius_diameter` |
| Semicircle | `semicircle_r7` |
| Scale drawing | `scale_drawing_20m_10cm` |
| Position vector | `vector_position_op` |
| Vector triangle / parallelogram law | `vector_triangle_law`, `vector_parallelogram_law` |
| Straight-line gradient | `linear_graph_gradient` |
| Algebraic length / shaded region | `algebra_length_from_diagram`, `algebra_shaded_region` |
| Pie chart | `pie_chart_salary` |
| Stem-and-leaf | `stem_and_leaf_marks` |
| Probability tree (2-stage) | `probability_tree_two_stage` |

Still worth adding when a lesson needs them (same style kit):
nets of solids, locus (circle / perpendicular bisector / angle bisector),
histogram, bar chart, distance–time graph, fraction wall, bar model for ratio,
convex vs concave, regular vs irregular, hour-glass similarity, midpoints.

## TikZ authoring rules

### Document skeleton

```tex
\documentclass[tikz,border=6pt]{standalone}
\usepackage{mathdiagrams}
\begin{document}
\begin{tikzpicture}[md]
  % geometry / labels
\end{tikzpicture}
\end{document}
```

### Style kit (already defined — use these names)

| Style | Use |
| --- | --- |
| `md` | base (ink, 0.8pt, sffamily small) |
| `md shape` / `md shape fill` | drawn polygons |
| `md accent` / `md accent fill` | highlighted lines / regions (accent blue) |
| `md highlight` | secondary emphasis (red) |
| `md label`, `md label bold`, `md label muted`, `md label accent` | text |
| `md point` / `md open point` | filled / open dots (number lines, vertices) |
| `md axis`, `md grid`, `md tick` | coordinate work |
| `md angle arc` | interior angle arcs |
| `md venn A/B/C`, `md venn U` | Venn sets |
| `md arrow`, `md ray`, `md dashed`, `md thin`, `md thick` | strokes |

Macros: `\mdOpenDot{x}{y}{label}`, `\mdClosedDot{x}{y}{label}`,
`\mdMarkAngle{A}{B}{C}{radius}{label}`, `\mdDim{p1}{p2}{offset}{text}`,
`\mdAxes{xmin}{xmax}{ymin}{ymax}{xstep}{ystep}`.

### Geometry hygiene

- **Coordinates are truth.** Place vertices first as `\coordinate`, then draw.
  Keep side lengths and angles **visually honest** (an isosceles triangle must
  look isosceles; 105° must look obtuse).
- **Labels outside the shape** when they would collide; prefer
  `above left`, `below right` over absolute positions.
- **Angle arcs** use `pic[md angle arc, angle radius=0.55cm, "$42^\circ$", angle eccentricity=1.3] {angle=A--B--C}`.
  Increase `angle eccentricity` when the label is long (`$(5x-6)^\circ$`).
- **Right angle**: draw a small square along the legs
  (`(B)!0.35!(A) -- ... !0.35!90:(A) -- (B)!0.35!(C)`), or
  `pic {right angle=A--B--C}`.
- **Parallel marks**: short matching ticks on both lines.
- **Equal sides**: matching tick pairs on the sides.
- **Arrow keys** must use `>={Stealth[...]}` (braces) — bare `>=Stealth[length=…]`
  breaks the parser.
- Canvas: typically 4–12 cm wide. `border=4pt` (number lines) or `border=6pt`
  (geometry). Never rely on the PDF page size.

### Charts & diagrams

- **Number lines**: integers get ticks and labels; solution ray in `md accent`;
  open circle for `<,>`; solid dot for `≤,≥`; label the solution set above.
- **Venn**: rectangle = `U`, circles drawn with `md venn *`; fill from the
  centre outwards; region labels stay short (`A∩B`).
- **Pie**: compute sector angles from percentages first
  (`40% → 144°`), draw sectors from the origin, label **inside** the sector.
- **Trees**: one row per stage, branch probability on the branch, outcome
  probability at the leaf.
- **Axes**: `\mdAxes` then plot; mark rise/run for gradient; label axes `x`,`y`
  and origin `O`.

## Quality gate (before calling a figure done)

**Mandatory visual check — never ship a figure you have not inspected:**

```powershell
$env:MIMO_PYTHON tools/math-diagrams/build.py --only <id>
$env:MIMO_PYTHON tools/math-diagrams/preview.py --id <id> --show
```

`preview.py --show` prints an ASCII ink map. You MUST read it and confirm:
geometry is closed, labels sit on empty canvas (not on strokes), nothing is
clipped. If the map shows a label as a faint smear on a line, move the
`\node` and rebuild. Do not trust a clean compile.

Also run `preview.py` (all ids) before a batch is considered finished.

Hard fails:
- ASCII map shows text overlapping a path
- `preview.py` reports BAD (missing ink, tiny/huge canvas, missing SVG)
- Label characters unreadable at the lesson PDF scale (~9–10 pt body)

Then:
- [ ] Every givens number in the question appears on the figure.
- [ ] Unknown marked `?` or with the letter used in the working.
- [ ] Shape proportions match the maths (right angles look right, parallels
      look parallel).
- [ ] Caption in markdown matches the catalog `caption`.
- [ ] Lesson text references the figure.
- [ ] File name is `snake_case`, no spaces, no `diagram_final_v2`.

## What not to do

- No ASCII / Unicode box-drawing art for spheres, Venn, nets, 3-D, graphs.
- No AI image models for figures with baked-in labels (text garbles; geometry
  drifts). Image gen is only for photographic-style references.
- No JPG masters (use PNG). No huge 1024×1024 empty padding — trim to the ink.
- No remote / `file:///w:/BECE_MOCK_PAPERS/...` links in lessons. Copy the
  figure into the lesson `diagrams/` or redraw it in TikZ.
- No raw LaTeX command names leaking into rendered lesson PDFs.

## Lesson layout reminder

```
<Lesson-Name>/
  Lesson_XX_Name.md
  Lesson_XX_Name.pdf
  diagrams/
    figure_01_<slug>.png   # or <semantic_id>.png matching catalog id
```

Update `catalog.json` so `build.py --check` keeps figures in sync with sources.

## Related rules

- `Grade9-Maths/Rules.md` — M1 notation (LaTeX maths), M2 contextual figures,
  M3 BECE-shaped drills.
- `RULES-BECE-PATTERN.md` — figure standards for all subjects.
