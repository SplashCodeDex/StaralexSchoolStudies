# BECE Question Style & Format Analysis (2021–2026)

*Compiled 27 Oct 2026 from `data/harvested/` papers + `data/extracted_questions/questions_bank.jsonl`.*
*Purpose: guide how questions should be set for Staralex BECE mock papers and lessons.*

---

## 1. The common WAEC BECE "shell" (all subjects)

| Feature | Convention |
|---|---|
| Booklet | Combined "2&1" booklet — **Paper 2 (Essay) answered FIRST**, collected, then Paper 1 (Objective) |
| Total time | Maths: 2 h (2 × 1 h) · Computing 2026: 2 h (1 h 15 essay / 45 min objective) · Career Tech 2026: 2 h 10 (1 h 20 essay / 50 min objective) |
| Paper 1 | **40 objective items × 1 mark, options A–D**, "Answer all the questions"; 2022 and earlier CDT had **30 items** |
| Paper 2 | Maths: **6 questions, answer FOUR, all equal marks (15 each ≈ 60)** · Computing 2026: ~72 marks, one **compulsory 24-mark scenario Q1** + 12-mark questions · 2022 CDT: core skills [20] + elective [50] |
| Calculators | **"The use of calculators is not allowed"** (maths) |
| Header block | "THE WEST AFRICAN EXAMINATIONS COUNCIL, GHANA" → grey bar "Basic Education Certificate Examination" → subject / date / papers / time |
| Cover instructions | "*Do not* open this booklet until you are told to do so… Write your **name** and **index number** in **ink**…" |
| Objective rubric | "Each question is followed by **four** options lettered **A to D**… **shade in pencil** on your answer sheet… Give only **one answer**… **erase your first answer completely**… **Do all rough work in this paper**." Includes a **worked example** (3n + 2 = 8 → answer D shaded). |
| Footers | Print codes like `26/03/2021 2&1/as/feb/b/bece`; "Turn over"; "END OF ESSAY TEST" / "END OF PAPER"; "© 2026 The West African Examinations Council" |

---

## 2. Mathematics — phrasing conventions (2021–2026, constant)

**Signature stems (recycled every year):**
- "Find the **image of** P(10, −3) when **translated by the vector r**… Find r."
- "Find the image of p(−3, 5) when **rotated through 360° about the origin**."
- "Make h **the subject of the relation** V = πr²h"
- "Express 7352.4658 **correct to three significant figures**" / "in **standard form**" / "(0.725) as a fraction in its **lowest term(s)**"
- "**Factorize completely:** xy − xm − my + m²"
- "find the **gradient of the line joining** P to Q"
- "find **n(A∩B)**"; "If … and P = Q, find the value of k" (odd element in set)
- Bearings (2024+): three-figure answers (155°, 065°)

**Number/accuracy conventions:**
- Bracketed constants inline: **[Take π = 22/7]**, **[Take tan 60° = 1.732, cos 60° = ½]**
- "correct to one decimal place / nearest whole number"; "leave the answer in the form **a + b√c**, where a, b and c are integers"
- Money as **GH₵ with 2 dp**: "GH₵ 3,000", "GH¢ 1,800.00"; ratio-sharing (Kofi/Ama), profit %, simple interest, typist wage "GH₵ 68.00 first 8 sheets, GH₵ 11.00 each additional"
- **Ghanaian contexts**: yam/mangoes/cashew, District Assembly clinic, cocoa stem-and-leaf, farmers-to-children ratio 13:11, names Kofi, Ama, Kobby, Araba, Mr Mensah, Antwi
- Bold emphasis inside stems: **not**, **each**, **one-third**, **correct**

**Data questions:** one table/plot → **2–3 consecutive items** ("Use the information to answer question(s) below"); 2026 Paper 2 asks to **construct** a frequency distribution table, not just read one.

**Diagram stamps:** "**NOT DRAWN TO SCALE**", congruence ticks, angle labels 2y / 56°.

**Marks:** Paper 2 prints **NO per-part mark tags** — only "All questions carry equal marks" + "All working must be clearly shown. Marks will **not** be awarded for correct answers without working."
Sub-part ladder: (a) (b) (c) → (i) (ii) (iii) → (α) (β).

**Topic load (2026 objective census):** algebra ~28% · GH₵ commercial word problems ~23% · sets/statistics/probability ~18% · number/theory ~10% · geometry/mensuration ~10% · proportion/rate ~7% · vectors/transformations ~6%.

**2021→2026 evolution:** 2021–2023 short computational → 2024 adds bearings + "learners" lexis → 2026 nested (α)(β), constructed tables, surds to a + b√c, L-shape composite area in essays.

---

## 3. Computing/ICT — phrasing conventions

- Same objectives shell: 40 × [1], A–D. 2026 timing: **Paper 2 = 1 h 15 (~72 marks), Paper 1 = 45 min**.
- 2026 Paper 2: **one compulsory 24-mark scenario mega-question** ("Your school is organizing a Technology Awareness Day… the club's role includes planning, communication, creating publicity materials…") + 12-mark scenario questions; per-part tags sum printed (3+3+3+3 / 5+4+3…); response scaffolds (i)(ii), (α)(β)(γ).
- Essay verbs: *Name, List, State, Suggest, Write the algorithm using pseudocode, Draw a flowchart, Explain, Describe, Outline the steps, Calculate, Write a formula/function, Identify.*
- **Curriculum pivot:** 2021–2023 = transitional old ICT (floppy disks 1.44 MB, toolbars, booting, typing fingers, Swedish desktop trivia, monitor radiation) → **2024–2026 = full new standards-based Computing**: AI/deep learning/bias, robotics (sensors, collaborative robots), pseudocode (FOR keyword), debugging, flowchart symbols, decimal→binary (20 → 10100), hex→binary (A2 → 10100010), Excel `=IF(logical_test, [value_if_true], [value_if_false])`, COUNT, cybersecurity (interception, cyberbullying, identity theft), green computing, blogs/AR.
- Objective stems = **narrative scenario anchors**: "A student in the computer laboratory wants to…", "A quiz master asked participants to…", "Cindy was trying to access information from the WAEC website…", "The most appropriate… is", "The process of X is **referred to as**…", "Which of the following…".
- Note: no B9-style curriculum codes are printed on real papers — codes are attached externally (repo tagging).

---

## 4. CDT/CAD (Career Technology & Creative Arts and Design)

**Career Technology June 2026 (code 04x/2&1), 100 marks, 2 h 10:**
- Paper 2 **Part A [30 marks] — 40 min**: "Answer **Question 1 [Compulsory]** and any other question." Answers on dotted lines in the booklet.
- Paper 2 **Part B [30 marks] — 40 min**: technical drawing on **A3 sheets**: "Answer **Question 4 [Compulsory]** and any other one." Q4 riveted sheet-metal joint (Figure 1); Q5 cone Ø40/h60 → "Draw to **full size in First Angle Projection** the: front view / plan" + "Copy and complete Table 1" (Trowel/Spirit level/Float — use + care); Q6 "Make a sketch of a G-clamp and identify the frame and the fixed jaw."
- Paper 1 objective 40 × A–D, 50 min, two-column.
- Cover lines: "All diagrams or drawings should be in pencil… **All dimensions are in millimetres.**"
- 2026 style = **scenarios/design briefs with named characters**: "A group of unemployed mothers in your community have approached you to demonstrate the making of sweet pancakes… Outline the recipe needed"; "Mrs Owusu… Explain the first three steps involved in setting up the business"; "State one design brief for the problem of eating late." Quantity words (two/three/four) **bolded**.

**Creative Arts and Design June 2026 (041/2&1):** Visual Arts [30] (2 questions; drawings in printed **box A**; mass shading/hatching) + Music [15] (notation to match 3/4 time; Kofi Antobam) + Dance & Drama [15] (one question; script excerpt with "In **not more than four words**, suggest a suitable title for this script. [2 marks]"; classify dances Bobɔbɔ/Asafo/Takai/Klama → Royal/Ritual/War/Recreational table).

**Legacy 2022 BDT (contrast):** "Paper 2 is in two sections: A and B. Answer three questions only: Question 1 in section A and two questions from section B." Section A [20] CORE SKILLS recall ("State two ways fresh tomatoes are preserved", "List two vegetable fibres", "Spiral / Diagonal / Vertical / Zig-Zag symbolic meanings"); Section B [50], 25-mark equal questions: "Make a **freehand pictorial sketch** of a claw hammer and **label any two parts**"; isometric Figure 2 → "Draw a full size of the front view in **First Angle Orthographic Projection** in the direction of arrow N." Home Econs variant examines essays **in the booklet** ("State three types of button holes. [3]", "Define seam.", [2] tags present) and adds the classic invigilator lines: "Any candidate who **tears off any part** of this question paper will be severely penalized… hand in the entire question paper to the invigilator."

**Evolution:** 2022 = 20+50+30 essay-on-A3 core-skills recall → 2026 = 40 objective × [1] + 60 essay, scenario/design-brief driven, "CORE SKILLS" wording dropped, objective guards ("DO NOT TURN OVER THIS PAGE UNTIL YOU ARE TOLD TO DO SO. YOU WILL BE PENALIZED SEVERELY…") with full candidate facsimile (Dora Afi SULE, index 772384188, centre 77234, code 0541).

**Marking-scheme format (WAEC style):** "2026 BASIC EDUCATION CERTIFICATE EXAMINATION … FINAL MARKING SCHEME"; bulleted acceptable-response lists; "Any two @ 2 marks each [4 marks]"; "The bar must be correct to earn all marks; no awarding of partial marks."

---

## 5. Mock papers — how mocks diverge from real BECE

**Sources:** Best Brain (Mar 2026, Sept 2026, Oct 2026), Stepping Stone (BECE 2027), KuulChat Mock 1 2025, Secret Mock 2024, Superb Mock / Palm & Cedar Super Mock (May 2025), plus repo Maths Mock August 2026 PDF.

**What mocks get right (copy of the shell):**
- Two-paper order (Paper 2 first), ~100 marks, 40 objectives A–D, "calculators are not allowed", and the **near-verbatim WAEC objective rubric** (best example in the repo: `Mathematics_BECE-MATHS-MOCK-AUGUST-2026-MOCK-Qs-Only_a756f9e1.pdf` with banners `PAPER 2 - ESSAY - [60 MARKS]` / `PAPER 1 - OBJECTIVE TEST - [40 MARKS]`).
- Mocks ship **with marking schemes**; mocks are dated **one year ahead** of the cohort ("Sept 2026 mock **for BECE 2027 candidates**").

**Where mocks break WAEC discipline:**
1. **Essay structure drifts** — Aug 2026 Maths mock sets 6 unequal-part essays vs the real "4 equal questions"; ghlearner-flattened mocks tag per-part marks [5]/[10]/[15]/[20] and split sub-parts into separate items. Computing mocks (Stepping Stone) inflate totals to 100 marks vs real 2026 ≈ 72 + 40.
2. **Provenance is mixed** — heavy **verbatim recycling** of real BECE classics (identical storekeeper GH¢10.00 question in two different mocks), **GCSE-style imports** ("There are p counters in a bag… estimate the value of p" — AQA sampling), **WASSCE-flavoured items** (cliff 105 m, angle of depression 35°, take tan 35° = 0.613), and easy invented drill items ("Add 424, 8071 and 29", "Jane arrived at work at 7:55 am…").
3. **New Common Core vocabulary pokes through** — "skip count 71012300 forward by 100000", straight-line equations from one point + slope, truth sets on a number line.
4. **Production quality** — numbering slips (two consecutive "a." parts, dangling "iii."), broken cross-references ("in 1(c)(i) above"), contradictory stems (|XY| = |YX| = 13 and 5 cm), typos ("how man are girls", "the his total monthly income"), inconsistent GH¢/GHS/GHO.
5. **Header branding** — Best Brain replaces the WAEC block with its own "Best Brain Examinations Konsortium"; extracted-platform mocks lose headers entirely to site chrome.

---

## 6. Implications for setting questions in this repo (per Rules.md)

- **Priority = authentic WAEC/BECE past questions**; never import GCSE/WASSCE patterns; question text should follow the 2026 scanned booklet as ground truth for rubric wording.
- **Essay paper:** keep the real discipline — Maths: six questions, answer four, equal marks, NO per-part marks; Computing: one compulsory 24-mark scenario Q1 + 12-mark scenarios with printed sub-totals; CAD: compulsory Q1/Q4 + A3 technical-drawing conventions ("full size", "First Angle Projection", "All dimensions are in millimetres").
- **Objectives:** 40 × 1 mark, A–D, standard WAEC rubric block verbatim, worked sample, "Turn over" footers.
- Adopt these house conventions (already in the bank): sub-parts (a)(i)(α), bracketed "Take π = 22/7", "correct to …", "NOT DRAWN TO SCALE", GH₵ 2-dp notation, 2–3 linked items per data stem, bolded quantity words ("two", "three"), Ghanaian names/contexts, scenario-anchored Computing items.
- Marking schemes: bulleted alternative lists, "Any two @ 2 marks each", "no partial marks" notes.

## 7. Data-quality caveats

- Only the **2026 Maths scan** (`Mathematics_BECE-2026-MATHEMATICS-QUESTIONS_6f2a94b5.pdf`) and the 2026 CAD scans are faithful WAEC layouts. Website scrapes of 2021/2022/2023/2024 lose cover pages and mangle fractions/vectors — don't treat them as rubric evidence.
- Several computing/math mocks exist only as passco.com.gh **landing-page stubs** (PalmCedar, SuperbMock, Best Brain Sept/Oct 2026, KuulChat) — underlying PDFs not OCR'd; re-harvest before modelling "mock voice".
- `questions_bank.jsonl` schema: `id, subject, year, paper_type ("Paper 1 - Objective" | "Paper 2 - Theory" | "Marking Scheme / Solutions"), question_text, option_a..d, correct_answer, has_diagram, diagram_path, indicator_code (B7/B8/B9.*), confidence, tag_method, dedup_hash, migrated_from, created_at`. Coverage: CDT_CAD 2010–2017 (667, no 2021+), Mathematics 1990–2012 & 2026, Computing_ICT 2024–2025.
- Bank conventions for answers: "(State any two of the following)" + "• bullet" alternatives + `[n marks]` tags.
