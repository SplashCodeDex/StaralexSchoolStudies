# number_system_hierarchy — Nested number-system circles

**Status:** PERFECT (2026-10-20)  
**Source:** `tools/math-diagrams/templates/number_system_hierarchy.tex`  
**Output:** `Grade9-Maths/.../Lesson-02-Number-Systems-And-Venn-Diagrams/diagrams/number_system_hierarchy.png`

## Build
```powershell
& $env:MIMO_PYTHON tools/math-diagrams/build.py --only number_system_hierarchy
```

## Layout
- **Concentric** circles (same centre `(0,0)`), radii `1.2, 1.95, 2.7, 3.45, 4.2`.
- Innermost `ℕ` gets `mdAccentSoft` fill + accent stroke; the rest alternate
  `mdFill` / `mdWhite` so each ring band is readable.
- Set labels sit at the **midpoint of their ring band** on the 45° diagonal
  (radius × `cos45 ≈ 0.707`):

| Label | Band mid-radius | Position |
| :--- | :---: | :---: |
| `ℕ` | 0 | (0, 0) |
| `𝕎` | 1.575 | (1.11, 1.11) |
| `ℤ` | 2.325 | (1.64, 1.64) |
| `ℚ` | 3.075 | (2.17, 2.17) |
| `ℝ` | 3.825 | (2.70, 2.70) |

## Pitfalls (do not repeat)
1. **Off-centre nesting** (`(0.15i, 0)` centres) made the rings lopsided — thick on one
   side, thin on the other. Use one shared centre.
2. **`ℝ` placed outside the outermost circle** (at radius ≈ 4.6) — it read as a detached
   label. Keep every label inside its own band.
3. **White sticker boxes** (`md label bold`) — plain `font=\sffamily\bfseries` nodes.
4. **Prose caption** `Natural ⊂ Whole ⊂ Integers ⊂ Rationals ⊂ Reals` at the bottom —
   the nesting already shows containment. The lesson prose states the chain.

## Contract
- [x] No caption sentences
- [x] No white boxes
- [x] Every label inside its ring band
- [x] Concentric geometry
- [x] Blackboard glyphs `ℕ 𝕎 ℤ ℚ ℝ` render (verified — no tofu)
