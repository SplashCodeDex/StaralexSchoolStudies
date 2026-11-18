# BECE Mathematics — Framing Study of REAL Papers 1 & 2 (2023–2026)

*Compiled 29 Oct 2026. Primary evidence = authentic WAEC scans read page-by-page (`storage/study_maths/BECE2022_paper/`, `BECE2021_paper/`, `BECE2026_real/`, `BECE2026_scheme/`) + full objective sets for 2024 and 2025 (re-typeset from ghlearner.com, saved as harvests). Complements `question_style_and_format_2021_2026.md` (§1–§2 unchanged); this study drills into **exactly how items are framed** — structure, stem grammar, distractor engineering, and mark-scheme behaviour.*

---

## 0. Evidence inventory (what was actually read)

| Year | Paper | Evidence | Quality |
|---|---|---|---|
| 2021 (June) | P2 essay (6 Q) | scan `BECE2021_paper/p02,p03.png` | authentic |
| 2022 (June) | P2 essay (6 Q) + P1 items + answer-sheet page | scan `BECE2022_paper/p01–p12` | authentic, full |
| 2023 | — | **NOT in repo** (ghlearner "still typing up") | gap |
| 2024 | P1 (40 items) | `data/harvested/Mathematics/txt/…2024…a106b41d.txt` | site re-type; some symbols mangled (see §6) |
| 2024 | P2 | passco.com.gh landing-page stub only ("2 pages… four questions… equal marks") | gap |
| 2025 | P1 (40 items) | `data/harvested/Mathematics/txt/…2025…cef4451c.txt` (newly saved 29 Oct 2026) | site re-type; a few LaTeX-only stems dropped symbols (Q7 empty stem in the saved copy) |
| 2025 | P2 | — | gap |
| 2026 (June) | **Full 2&1 booklet** | scan `BECE2026_real/p01–p11.png` | authentic, complete, ground truth for rubric |
| 2026 (June) | WAEC **FINAL MARKING SCHEME** for Maths 2 | scan `BECE2026_scheme/p01,p02.png` | authentic; M1/A1/B1 methodology visible |

> Rule: whenever a re-type disagrees with an authentic scan, the scan wins. The 2026 scan is the single best ground truth in the repo.

---

## 1. The booklet shell (verified verbatim from 2022 + 2026 scans)

Cover page, identical in both years (2026 shown; bold printed exactly as in the scan):

> (stamp box: `03001/2&1` **BECE** / **June 2026** / **MATHEMATICS 2&1** / **Essay & Objective** / **2 hours**) — Name: … Index Number: …
>
> **THE WEST AFRICAN EXAMINATIONS COUNCIL — GHANA**
> (grey band) **Basic Education Certificate Examination**
> June 2026 · MATHEMATICS 2&1 · ESSAY AND OBJECTIVE · 2 hours

> *Do **not** open this booklet until you are told to do so. While you are waiting, read and observe the following instructions carefully. Write your **name** and **index number in ink** in the spaces provided above.*
> *This booklet consists of **two** papers. Answer Paper **2**, which comes first, in your answer booklet and Paper **1** on your Objective Test answer sheet. Paper **2** will last **1 hour** after which the answer booklet will be collected. Do **not** start Paper **1** until you are told to do so. Paper **1** will last for **1 hour**.*
> *The use of calculators is **not** allowed.* (line is on its own, below the block)

2022 wording differs by two words only ("read and observe the following instructions" — no "carefully"; "in the spaces" — no "in ink").

**Interleaved guard page** between the papers (2022 scan p05, printed page 5):
> **DO NOT TURN OVER THIS PAGE UNTIL YOU ARE TOLD TO DO SO.**
> **YOU WILL BE PENALIZED SEVERELY IF YOU ARE FOUND LOOKING AT THE NEXT PAGE BEFORE YOU ARE TOLD TO DO SO.**
> PAPER 1 — OBJECTIVE TEST — 1 hour · *Answer all the questions on your Objective Test answer sheet.*
> 1. Use **2B** pencil throughout. 2. On the pre-printed answer sheet, check that the following details are **correctly** printed: Your **surname** followed by your **other names**, the *Subject Name*, your *Index Number*, *Centre Number* and the *Paper Code*. 3. In the boxes marked *Candidate Number, Centre Number* and *Paper Code*, **reshade** each of the shaded spaces. 4. An example is given below…. **Dora Afi SULE**, index number **772384188**, Centre Number **77234**… Paper Code **0301**.

Objective-answer-sheet facsimile follows (WAEC logo block, candidate grid, "If only four alternative answers are given for each question, ignore the letter E"). Print codes appear as small-run footers `bec/ea/03008/2&1/22/sc/spd` (2022) and `26/03001/2&1/aefeb/bece` (2026).

---

## 2. PAPER 2 (Essay) — framing anatomy

### 2.1 Constant header of the paper (every year, 2022+2026 verbatim)

> PAPER 2 *(2022 prints "PAPER 2 Essay"; 2026 prints just "PAPER 2")* — 1 hour
> **Answer four questions only.**
> **All questions carry equal marks.**
> **All** working must be clearly shown. Marks will **not** be awarded for **correct** answers without corresponding working.

Six questions are set; four answered ⇒ 4 × 15 = 60 marks. The 2026 marking scheme confirms: each question block ends with **[15 marks]** and no per-part mark tags appear on the question paper.

### 2.2 The 6-question skeleton — and its Q-slot logic

Every essay question is a compact 2–3 part mini-paper `(a) (b) (c)` (2021 uses three INDEPENDENT (a)(b)(c) items; 2022/2026 mix nested sub-parts under one theme). Observed slot logic:

| Slot | 2021 | 2022 | 2026 |
|---|---|---|---|
| **Q1** | Venn 8x+4/6/2x+7 → n(M)=n(N) | Sets P/Q factors of 36/54 → (α)(β)(γ) ∩, n(∩), HCF → (b) sequence next two 1,4,9 → (c) median with 4m−3 slot | Sets {1..11} (i) list primes (ii) P(not prime) → factorize (x+y)(2m−n)−m(x+y) → typist GH¢ wage ladder |
| **Q2** | factorise 4-term → solve 6/(4p−1) | fraction ÷ mixed ( 1/3+1/12 )÷(2/3−5/8) → product (2x−3)(2x+3) → (c) equilateral diagram (3x+2), 11, (2y+3) | translate by vector r → Joyce & Richard profit: manager one-third + ratio rest |
| **Q3** | vectors r−m → sum/twice number → tiles 9 m × 4 m by 20×30 cm | relation L = 2(m²−n²)/4(m+n) → solve 4/(3x) = 7−3/x → salesman commission 5½% of mixed sales | Asana cashew wage +10% → L-shape floor metre (i) perimeter (ii) area (iii) carpet cost |
| **Q4** | Antiwaa 25 mangoes % ripe → mapping arrows m,n → bus speed/time | Fred age algebra 3-ways → perimeter of cocoa farm 497 km, length 2½ width | monthly GH¢ of 3 workers ×12 → ladder 60° (i) illustrate (ii)(α) ladder length (β) window–base distance [Take tan 60° = 1.732, cos 60° = ½] |
| **Q5** | expand (4x+2)(x−2)−3x² → circle centre angles 40,60,100,3x°,5x° → cost C(x)=25+0.6x two-way | factorise (x−y)(3m+n)−(x−y)(m−2n) → vectors p−q=(6,8) → inequality: truth set x−1/2 ≤ ½ + x, then **number line** | surds √72/(√18−√12) → a+b√c → inequality ½(2x+1) ≥ ⅓x + 1 9/10 → athlete 4 laps r = 70 m [Take π = 22/7] |
| **Q6** | statistics: copy-and-complete fx table (one gap in f, one hidden) → how many / mean nearest whole | **full graph paper question**: copy/complete y = 5−2x table → scale 2 cm:1 unit axes → plot + line → read (i) y at −2.6 (ii) x at −2.8 (iii) gradient | statistics: raw list of 30 shoe sizes → **(a) construct** frequency table → (b)(i–iv) which size most/least + "give reason for the answer in (b)(i)/(b)(iii)" → (c) mean nearest whole |

Patterns this pins down (house rules for generated essays):
1. **Always exactly 6 numbered questions, header demands 4, equal marks, no per-part tags.**
2. Every question number is a **(a)(b)(c) sandwich**; one slot typically nested two levels deeper: `(i)/(ii)` and, when trig/scalar sub-answers exist, `(α)/(β)`.
3. **Q1 reliably opens on sets** (list members / ∩ / probability) — 2022, 2026; 2021 used a Venn diagram with algebraic regions (`8x+4`, `2x+7`) in the same slot.
4. **Q6 is always the "big-output" question**: 2021/2026 statistics (copy-and-complete/construct table + most-common-value by eye + mean correct-to-nearest), 2022 coordinate-graph construction. In 2026 WAEC swapped graph-drawing for table-construction, and introduced the self-referential sub-answer "give reason for the answer in (b)(i)" — that phrasing is authentic.
5. **Word problems carry real Ghanaian money**: typist GH¢ 68.00/8 sheets + GH¢ 11.00 additional; Asana GH¢ 25.00/day +10%; Joyce GH¢ 10,000.00 & Richard GH¢ 5,000.00, profit 9,000.00, manager one-third; Kofi/Ama; workers GH¢ 5,000.00 / 6,500.00 / 4,200.00 monthly. Money always 2 dp, prefix GH¢ (reject GHS/GHc).
6. **Percent increases in wages/food/farm** phrasing: "was paid a wage of… If the daily wage increased by 10% and she worked 30 days, how much will she be paid?"
7. **One trig-style item appears when present as the only (α)(β) nested sub-question**, always with bracketed constants at the END of the stem: `[Take tan 60° = 1.732, and cos 60° = ½]` and "illustrate the information in a diagram" as a scored sub-step.
8. Rough accuracy instructions are embedded inside stems: "correct to **one** decimal place", "correct to the **nearest** whole number", "leave the answer in the form **a + b√c**, where a, b and c are integers" (the 𝑎+b√c form is 2026-new on P2).
9. Diagram stamp **NOT DRAWN TO SCALE** — own line, centred, right under the diagram. 2026 L-shape: outer 8 m × 5 m with 5 m notch (perimeter/area/carpeting cost).
10. Observed typos in the real 2026 paper: "**circular truck**" (= track), spacing breaks ("Answe", " Answe ") — real papers do carry small typos; they are not evidence of inauthenticity, and mocks needn't reproduce them.

### 2.3 Essay stem grammar (verb → object ordering)

- "Given that …: list / find / Factorize completely:" — colon chains a stem into scored sub-steps on the same line.
- "Find the:" + run-on list of nouns with semicolons (`perimeter; area; cost of carpeting…`) — WAEC's most-listed pattern.
- "Calculate the / the amount earned if…" for money.
- "Solve: ½(2x+1) ≥ ⅓x + 1 9/10." — inequality essay item keeps mixed-number inside one line.
- "illustrate the information in a diagram" / "Illustrate the answer in (i) on the number line" (2022) — direct drawing instructions.
- "Copy and complete the table for the relation y = 5−2x for −3 ≤ x ≤ 4." — full table with 2 blanks + scale instruction "Using a scale of 2 cm to 1 unit on *x*-axis and 2 cm to 2 units on the *y*-axis, draw on a graph sheet two perpendicular axes ox and oy for −5 ≤ x ≤ 5 and −12 ≤ y ≤ 12."
  (axis pair labelled **ox and oy**, bold.)

---

## 3. PAPER 1 (Objective) — framing anatomy

### 3.1 Rubric (2026, verbatim; 2022's identical except minor word placement)

> *Answer **all** the questions.*
> *Each question is followed by **four** options lettered **A to D**. Find the **correct** option for **each** question and shade **in pencil** on your answer sheet, the space which bears the same letter as the option you have chosen. Give only **one** answer to **each** question. An example is given below.*
>
> If 3n + 2 = 8, find the value of n.
> A. 10  B. 6  C. 3  D. 2
> *The correct answer is 2, which is lettered **D** and therefore answer space **D** would be shaded. ⌐A⌐ ⌐B⌐ ⌐C⌐ ■D⌐ ⌐E⌐*
> *Think carefully before you shade the answer spaces, erase your first answer completely and shade the appropriate space for the new answer.*
> *Do all rough work in this paper.*
> *Now answer the following questions.*

(Note the shading sample includes an **E** position though no item ever uses it.)

### 3.2 Item grammar — the fixed shapes

40 items × 1 mark, four options, no per-question marks printed. 2026 measured topic flow:

| Block | Items | Content family |
|---|---|---|
| Q1–8 | commercial %/ratio, sequences, reverse-share word, ordering | number + money openers |
| Q9–16 | standard form, circle-from-area, probability, surds simplify, vector columns, factorize | algebra/mensuration cluster |
| Q17–24 | factorize common factor, fractions-of-money, % as fraction, evaluate-substituting, inverse rate, commission, diagram (parallel + isosceles 2y/56°), product-of-three | mixed, ends in geometry diagram |
| Q25–32 | mapping x→3x, simplify brackets, set-difference listing, **table→ linked median/probability pair (Q28+29)**, ratio equation, simple interest, linear inequality | data pair block |
| Q33–40 | word H A P P Y probability, time lapse 9:45→4:15, equivalent sets recall, square↔equilateral perimeter, indices 2^m, fractional equation, modal mark of 11 raw marks, transformation (x,y)→(x, y−2) | misc 8 |

Item anatomy rules:
1. **One line per stem**, never two clauses unless drag-in data; stems average 8–14 words.
2. **Interrogative endings dominate**: "…find the …", "What is the …", "…is the …". Declarative completions ("A quadrilateral with one pair of opposite sides parallel is called ______") also occur with options as the answer halves.
3. **Bold guards inside stems**: **not**, **each**, **greater than 3**, **base radius**, **largest**, **third**. WAEC bolds the word that flips easiest distractors.
4. **Units travel INTO options, consistently**: every option of a mensuration item carries the unit (`cm²`, `m³`, `km`); every money option carries GH¢ to 2 dp with thousands separators as digits (`GH¢ 1,250.00`, `GH¢ 10 000.00` style also exists); times in `minutes`/`hours` spelled out.
5. **Fractions are set vertically** (stacked 2/5), never slash; surds keep radix long ticks (205-style: `√75 − √18 − √3 + √2`).
6. Column-vectors set as tall brackets \binom pairs; transformations either "translated by the vector …", "reflected in the *y*-axis", or as the 2026 Q40 **rule-matrix** (x y) with a column arrow inside brackets.
7. **Linked data stems**: single table + `Use this information to answer questions **28** and **29**.` (italic line between them), frequently a Mark/Frequency pair or a stem-leaf plot producing **2 items, occasionally 3** (2024 Q11–13 stem-leaf gave modal/count/median in a row).
8. Diagram items always say "**In the diagram, …**" then ask a value; diagrams carry algebra labels (2y/56°, (3x+2) cm) with **NOT DRAWN TO SCALE** below. 2024 re-types "Diagram will be provided." is a site artefact, not WAEC wording.
9. Recall-definition items still appear — one-line orthodoxy checks: 2026 "not a composite number?" (Q16) and "Two sets which have the same number of members are … sets" (Q35); 2024 "even prime number" and "a quadrilateral with one pair of opposite sides parallel is called …"; 2022 "The **longest** chord of a circle is the …".

### 3.3 Distractor engineering (the craft)

Real options are **systematic error classes of the correct path** — this is the strongest "authenticity" fingerprint:

1. **Sign/position-flip for reflections/vectors**: reflect (−2, 3) in x-axis → options include (−3,2), (−2,3), (−3,−2) around correct (−2,−3); vector MN → (−3,−2) offered against (3,2).
2. **Order swap** in ordering tasks: "Arrange ¾, 0.8, ⅝, 0.65 in **descending** order" — each permutation offered exactly once across 4 options.
3. **Linear scale-factor lapsing** on enlargement: area 15 cm², k = 3 → 45 (=15k) as distractor, 135 (=15k²) correct; always includes 90 (=15k·2) and 75.
4. **Operation inversion** on topic pairs: subject formula p = (r−4y)/3 → correct y = ¼(r+3p), wrongs distribute the arithmetic (r−3p, 3p−r, r+p).
5. **π-carryover**: circumference of area 100π cm² → 10π correct; wrongs are 5π, 15π, 20π (pure multiples — no numeric fake of 31.4-style).
6. **Percent-of vs percent-left pair with each other across the paper** (2024 Q5 "what percentage of the maize was **left**" → 70 %; 2025 Q6 "What percentage did he **save**" → 20 %) — WAEC bolds the word (**left**, **each**, **not**) that anchors the required operation, and distractors include the complementary percent (40 % ≠ 100−70… i.e. wrong subtraction direction).
7. **Reciprocal / numerator-shuffle answer options** on fraction tasks: partial sums settle on 5/12 vs 7/12 vs 1/6 (books/pens remainder).
8. **Sequences**: missing middle term options from off-by-one common difference (−2, −3, −1, 1 for AP step 4 between −9 and −5).
9. **Time-lapse** wrong by the carry hour (5 h 30 vs 6 h 30 vs 8 h vs 7 h).
10. **Rounding-place confusions** on s.f. items: 2025 Q31 "56 782 to three significant figures" — distractors 56 700 (truncate instead of round), 567 and 568 (shift of place value) around correct 56 800.

### 3.4 Money/commercial micro-template (heavily reused, re-skinned yearly)

Cost or wage (GH¢ x.00, realistic cedi multiples: 5.00 · 12.00 · 30.00 · 60.00 · 126.00 · 350.00 · 550.00 · 700.00 · 25,000.00) → operation (profit %, commission %, simple interest, ratio split, "wage increased by 10%", "# percent left/save") → "Find cost price / how much sales / what percentage…" — the **same three verbs** every year.

---

## 4. The 2026 WAEC Final Marking Scheme (authentic) — how marks are *framed*

Page 2 of `BECE2026_scheme` (Q1 of Maths 2), verbatim methodology:
- Table columns: QUESTION NO. | SOLUTION | MARKS
- Codes: **M1 for any three correct** / **A1 for all correct** / **B1 for listing non-primes or 11−5=6 or listing of K** / **B1 for 11** / **M1 A1** for the 6/11 probability-line; factorize shows **M1 for factorising (x+y) out**, **M1 for simplifying (at least one term correct)**, **A1 for (x+y)(m−n)**; typist wage shows per-step M1/A1 pairs: **M1 for subtracting** (35−8), **A1 for 27**, **M1 for multiplying by 11**, **A1 for GH¢297.00**, **M1 for adding**, **A1 for GH¢365.00**.
- Handwritten examiner directives on the displayed version: "**any three for all correct**", "**insist on 35− 8  to get M1**", "**at least one term correct**".
- Final note after earned total: **−1ou/wu or 2dp once only** ("ou/wu" = omitted/wrong units, deducted once only per paper), and question badge **[15 marks]**.

Marking-scheme framing rules for this repo:
- Every sub-answer is (M)ethod/ (A)nswer or (B)oth-paths pair; alternatives allowed with "or".
- "insist on"-style notes mark steps that must not be skipped (e.g. 35 − 8 must appear).
- Units/2-dp errors are capped: "‑1 once only", correct answers alone earn nothing (mirrors the essay header).

---

## 5. 2021 → 2026 evolution (framing deltas)

| Dimension | 2021 | 2022 | 2026 (2023–25 partially visible) |
|---|---|---|---|
| Sub-part architecture | loose (a)(b)(c) independent | nested theme per question (α)(β appear) | same; (α)(β) now also inside trig & surds |
| Lexis | "students" "marbles" | "learners" begins; cocoa farm | "learners", "shade", ghlearner re-types use "learners" |
| Q6 type | statistics copy-and-complete | **graph sheets** plotting y=5−2x (scale, axes ox/oy, readings, gradient) | statistics — **construct** table from raw list + give-reason sub-answers |
| Trig essays | none | none | ladder θ=60° with [Take …] + (α)(β) sub-answers |
| Surds | √ targeted in objectives only | objectives 2-term | P2 rationalise to a+b√c, plus 4-term objective simplify |
| Bearings | — | — | from 2024: "What is the actual bearing of S25°E?" (three-figure 115°) |
| Money | GHC 21,00.00 (dot-misprint), "ration" | salesman textbooks+calculators+biro boxes | typist, Asana, Joyce/Richard, 3-worker monthly incomes |

Steady-state constants (never changed across 2021–2026): 40 objective items on Paper 1; six essay questions on Paper 2, answer four, equal 15 marks each; "The use of calculators is **not** allowed."; combined 2-hour "2&1" booklet with Paper 2 answered first; "END OF ESSAY TEST" closes Paper 2, "END OF PAPER" closes Paper 1; "Turn over" on facing pages.


---

## 6. 2023–2025 coverage notes & artefact warning

- 2023: no authentic paper or re-types accessible in repo or on ghlearner (page states "We're still typing up this paper."). Treat any 2023 Mathematics item that enters the bank by another route as unverified.
- 2025 Paper 2 & 2024 Paper 2: passco.com.gh landing-page stubs only — descriptions confirm "1 hour, four questions to answer, all carrying equal marks. 2 pages" (wording consistent with 2022/2026, but no item bank to mine).
- Site re-types introduce their own corruption: 2024 Q9 ratio answers rendered "2:03" for 2:3; 2024 Q10 inequality rendered "3(x − 2) − x³ + 6 > 0" where the original was evidently `3(x − 2) − x + 6 > 0` ⇒ x > 0 (the site's LaTeX stripped a plain "x" into "x³"); 2025 cedi signs became "GH?" (lossy non-ASCII); several stems lost ∠/≤/≥ symbols entirely. **Use the re-types for style enumeration only; bank items must be re-derivable or scan-verified.**
- The 2025 P1 re-type (saved by this study) is usable for style enumeration but must not be quoted as WAEC ground truth text.

---

## 7. Checklist for generating authentic-framed maths items

When generating BECE-style Maths items for Staralex, enforce:

**Paper 2 essay**
1. 6 questions; instructions "Answer four questions only. All questions carry equal marks. All working must be clearly shown. Marks will not be awarded for correct answers without corresponding working." — no per-part marks.
2. (a)(b)(c) with nesting `(i)(ii)(iii)`; (α)(β) allowed once under a (ii).
3. Slot game: Q1 sets/news; Q2 factor/geometry; Q3 vectors→geometry; Q4 commercial/light-algebra; Q5 inequality or surds; Q6 statistics table (construct) or graph.
4. One ladder-money item, one percent-increase wage, one GH¢ ratio-share. Two-dp money, GH¢ (never GHS).
5. Bracketed constants *after* the stem: [Take π = 22/7], [Take tan 60° = 1.732, cos 60° = ½].
6. "correct to the nearest whole number/one decimal place" inside the stem; NOT DRAWN TO SCALE centred under diagrams; answer-referential parts ("give reason for the answer in (b)(i)").

**Paper 1 objectives**
7. 40 items; A–D; waec rubric block verbatim with worked 3n+2 = 8 example; rough-work line.
8. → Topic spread policy observed ≈ money/percent 23 % · algebra/mapping 22 % · stats/prob/sets 18 % · number/indices 15 % · mensuration/geometry 11 % · vectors/transformations 6 % · rate/time 5 %.
9. Bold the trap word (**not**, **each**, **third**, **greater than**); units inside every option; fractions stacked; distributed-difference distractors per §3.3.
10. One linked block: shared table/plot marked "Use this information to answer questions **m** and **n**."
11. ≤ 5 pure-recall items and ≥ 3 diagram items per 40.

**Marking scheme**
12. M1 method / A1 accuracy / B1 independent; alternatives "or"; per-step one-liner "for" descriptors; cap accuracy exits: "-1ou/wu or 2dp once only"; quote ends with [15 marks] per essay question.

---

## 8. Files produced by this study

- `storage/study_maths/BECE2026_real/p01–p11.png` — authentic June 2026 booklet, page images.
- `storage/study_maths/BECE2026_scheme/p01–p08.png` — authentic WAEC final marking scheme scan.
- `storage/study_maths/BECE2022_paper/p01–p12.png`, `BECE2021_paper/p01–p06.png` — June 2022 / 2021 scans.
- `data/harvested/Mathematics/txt/Mathematics_GhLearner_Download_2025_BECE_Mathematics_Questions_cef4451c.txt` — new cleaned 2025 P1 harvest (40 items, A–D).
- Helper scripts: `storage/_extract.py`, `storage/_render.py`, `storage/_render2.py`, `storage/_fetch2025.py`, `storage/_clean2025.py` (deletable).
