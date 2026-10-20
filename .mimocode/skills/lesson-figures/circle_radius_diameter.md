# circle_radius_diameter — Circle with centre O, radius r, diameter d = 2r

**Status:** PERFECT (2026-10-20)  
**Source:** `tools/math-diagrams/templates/circle_radius_diameter.tex`  
**Output:** `Grade9-Maths/.../Lesson-01-Measurement-Circles-And-Scale/diagrams/circle_radius_diameter.png`

## Build
```powershell
& $env:MIMO_PYTHON tools/math-diagrams/build.py --only circle_radius_diameter
```

## Layout
- Circle centre `(0,0)`, radius 2.1.
- `A = (-2.1, 0)`, `B = (2.1, 0)` — diameter endpoints.
- Diameter: `md accent, dashed` from A to B. Radius: `md accent, thick` from O to B.
- Labels (plain `font=\sffamily\small`, **no boxes**):
  - `O` at `(-0.38, 0.28)` — **above-left** of the centre dot
  - `A` at `(-2.45, 0)`, `B` at `(2.45, 0)` — outside the circle
  - `r` at `(1.15, 0.28)` — above the radius segment
  - `d = 2r` at `(0, -0.62)` — below the diameter line

## Pitfalls (do not repeat)
1. **`d = 2r` was placed at `midway, below=3pt` of A–B.** The midpoint of the diameter
   **is** the centre O, so the formula landed on top of the `O` label. Never use
   `midway` of a diameter for a label that must avoid the centre — give it an
   explicit offset coordinate.
2. **`O` label below-left of the dot** (`(-0.25,-0.22)`) sat in the same band as the
   formula. Put `O` **above** the dot instead.
3. **White sticker boxes** (`md label`) — plain text nodes.

## Contract
- [x] No caption sentences (formula `d = 2r` is data)
- [x] No white boxes
- [x] Zero label collisions (verify by reading the PNG)
- [x] Radius solid, diameter dashed — visually distinct
