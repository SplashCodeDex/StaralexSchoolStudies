# pie_chart_salary — Pie chart with four labelled sectors

**Status:** PERFECT (2026-10-20)  
**Source:** `tools/math-diagrams/templates/pie_chart_salary.tex`  
**Output:** `Grade9-Maths/.../Lesson-01-Data-Statistics-And-Representations/diagrams/pie_chart_salary.png`

## Build
```powershell
& $env:MIMO_PYTHON tools/math-diagrams/build.py --only pie_chart_salary
```

## Data (must sum to 360°)

| Sector | Angle | Fill |
| :--- | :---: | :--- |
| Food | 144° | `mdAccentSoft` |
| Rent | 90° | `mdRed!18` |
| Transport | 72° | `mdGreen!18` |
| Savings | 54° | `mdAmber!22` |

Check before building: $144 + 90 + 72 + 54 = 360$.

## Layout
- Radius `\r = 2.0`; sectors drawn as `(\theta_1:\r) arc(\theta_1:\theta_2:\r)`.
- Divider radii at $0°, 144°, 234°, 306°$ plus the outer circle stroke.
- Labels **outside** the circle on the sector's mid-angle:
  Food `72:2.9`, Rent `189:2.9`, Transport `270:2.9`, Savings `333:3.15`
  (Savings needs a larger radius so it clears the stroke).
- Formula at `(0, -3.75)`: `$\theta = \dfrac{\text{percent}}{100} \times 360^\circ$`.

## Pitfalls (do not repeat)
1. **White sticker boxes** (`md label bold`) behind sector names — plain
   `font=\sffamily\bfseries` nodes.
2. **`Savings 54°` collided with the circle stroke** at radius 2.75. Push
   near-tangential labels out to ~3.15.
3. **`$frac{%}{100}$`** rendered as a cramped `%` over `100`. Write
   `$\frac{\text{percent}}{100}$` (or `$\frac{p}{100}$`) so the numerator reads.
4. **Formula stacked too close under `Transport 72°`** at `y = -3.35`. Move to
   `y = -3.75` for a clear gap.

## Contract
- [x] Labels outside the circle, clear of the stroke
- [x] No white boxes
- [x] Angles sum to 360°
- [x] Formula is data, rendered cleanly, clear of the shape
