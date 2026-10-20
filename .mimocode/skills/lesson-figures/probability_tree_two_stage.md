# probability_tree_two_stage — Two-stage tree (without replacement)

**Status:** PERFECT (2026-10-20)  
**Source:** `tools/math-diagrams/templates/probability_tree_two_stage.tex`  
**Output:** `Grade9-Maths/.../Lesson-01-Probability/diagrams/probability_tree_two_stage.png`

## Build
```powershell
& $env:MIMO_PYTHON tools/math-diagrams/build.py --only probability_tree_two_stage
```

## Data (Mock 2026 P2 Q5a — 5 red, 3 blue, 2 green pens, two drawn without replacement)

Branch probabilities must satisfy the sum-to-1 check at every node:

| Node | Branches | Check |
| :--- | :--- | :--- |
| Start | $G = 2/10$, $R = 8/10$ | $2/10 + 8/10 = 1$ |
| after G | $G = 1/9$, $R = 8/9$ | $1/9 + 8/9 = 1$ |
| after R | $G = 2/9$, $R = 7/9$ | $2/9 + 7/9 = 1$ |

Outcomes: $GG = 2/90$, $GR = 16/90$, $RG = 16/90$, $RR = 56/90$.
**Check:** $2+16+16+56 = 90$ → sums to 1. Never ship a tree that fails this.

## Geometry (labels OFFSET off strokes and off each other)

| Point | Position |
| :--- | :---: |
| Start | $(0,0)$ |
| G node | $(2.7,\ -1.0)$ |
| R node | $(2.7,\ -3.4)$ |
| Stage-2 ends (G) | $(5.7,\ -0.35)$ and $(5.7,\ -1.75)$ |
| Stage-2 ends (R) | $(5.7,\ -2.7)$ and $(5.7,\ -4.1)$ |

Labels sit **above** the upper branch of each pair and **below** the lower branch,
with ≥ 0.3 units of clearance computed from the branch's height at the label's x.

## Pitfalls (do not repeat)
1. **Labels on the strokes.** `midway` puts text on the line. Compute the
   branch's y at the label's x and offset vertically.
2. **Label–label collision.** The two sub-trees were only 1.6 units apart in y,
   so `R, 8/9` and `G, 2/9` overprinted. Spread the trees to 2.4 units apart
   (nodes at $y=-1.0$ and $y=-3.4$).
3. **White sticker boxes** (`md label`) on every node — plain `font=\sffamily` text.
4. **Unchecked probabilities.** Always verify each node sums to 1 and the four
   outcomes sum to 1 before declaring the figure done.

## Contract
- [x] No white boxes
- [x] No label collisions (branch or label)
- [x] Probabilities sum to 1 at every node and across outcomes
- [x] Stacked fractions via `\tfrac{}{}` (not `1/2` slashes)
