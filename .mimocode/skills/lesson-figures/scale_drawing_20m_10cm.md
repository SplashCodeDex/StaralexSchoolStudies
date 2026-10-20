# scale_drawing_20m_10cm — Drawing 10 cm ↔ actual 20 m

**Status:** PERFECT (2026-10-20)  
**Source:** `tools/math-diagrams/templates/scale_drawing_20m_10cm.tex`  
**Output:** `Grade9-Maths/.../Lesson-01-Measurement-Circles-And-Scale/diagrams/scale_drawing_20m_10cm.png`

## Build
```powershell
& $env:MIMO_PYTHON tools/math-diagrams/build.py --only scale_drawing_20m_10cm
```

## Layout
- Two equal-length bars (both $x \in [0, 5]$) with end ticks — they represent the
  **same object** at two scales, so they are drawn the same length.
- Upper bar `md thick` (ink) labelled `$10$ cm`.
- Lower bar `md accent, thick` labelled `$20$ m`.
- Formula at $(2.5,\ -2.25)$: `scale $= 10 \text{ cm} : 20 \text{ m} = 1 : 200$`.

## Check
$10 \text{ cm} : 20 \text{ m} = 10 : 2000 = 1 : 200$ ✓ (matches Mock 2026 P1 Q24).

## Pitfalls (do not repeat)
1. **Prose qualifiers** `on diagram` / `in real life` are caption text. Keep the
   labels to pure measurements — the formula already names both quantities.
2. **White sticker boxes** (`md label`, `md label accent`) — plain
   `font=\sffamily` nodes.
3. Both bars must be the **same drawn length**; making the "real life" bar longer
   breaks the idea that the drawing represents the object at a reduced scale.

## Contract
- [x] No white boxes
- [x] No prose qualifiers
- [x] Pure measurement labels + formula
- [x] Scale arithmetic verified
