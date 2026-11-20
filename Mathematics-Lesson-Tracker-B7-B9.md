# Mathematics — Master Curriculum Roadmap & Lesson Tracker (Grades 7–9)

*Based on the NaCCA Mathematics Common Core Programme (CCP) Curriculum for JHS1 (B7) – JHS3 (B9).*

- **Source of Truth:** [`Mathematics-Lesson-Plan-B7-B9.md`](Mathematics-Lesson-Plan-B7-B9.md) (`181` canonical NaCCA indicators across `51` Content Standards, `4` Main Strands, and `12` Sub-strands).
- **Existing Grade Trackers Reconciled:** [`Grade7-Maths/LESSON_TRACKER.md`](Grade7-Maths/LESSON_TRACKER.md) (`4/16` delivered) and [`Grade9-Maths/LESSON_TRACKER.md`](Grade9-Maths/LESSON_TRACKER.md) (`24/30` delivered).
- **BECE Exam Weighting Source:** `BECE_MOCK_PAPERS` (`3,480` total Mathematics items in `catalog.db`, `100%` embedded with `google/embeddinggemma-2` and tagged to primary NaCCA indicators — `1,814` Paper 1 Objective, `451` Paper 2 Essay/Theory [`229` Essay + `222` Theory], and `1,215` Marking Scheme entries).
- **Standard:** International British English conventions (*factorise*, *organise*, *centre*, *trapezium*, *cuboid*, *BODMAS*); strict adherence to NaCCA CCP indicators and BECE marking standards.
- **Pedagogical Model:** Plain-English preambles and unpacked technical terms before symbolic working; textbook-grade LaTeX display equations; contextual 300 DPI PNG figures built from TikZ sources via `tools/math-diagrams/`; and BECE-shaped exercise batteries (standard `8×5 = 40` questions or override `5×5 = 25` questions with `10–20%` spiral review) plus full marking-scheme solutions.

---

## High-Level Delivery Summary

| Grade | Level | Indicators | Planned Lessons | Delivered | Pending | Completion |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Grade 7** | Basic 7 / JHS 1 | 71 | 16 | 4 | 12 | 25.0% |
| **Grade 8** | Basic 8 / JHS 2 | 58 | 20 | 0 | 20 | 0.0% |
| **Grade 9** | Basic 9 / JHS 3 | 52 (+bridges) | 30 | 24 | 6 | 80.0% |
| **Total** | **JHS 1–3 Cycle** | **181** | **66** | **28** | **38** | **42.4%** |

*Note:* Grade 9 counts include 24 core B9 lesson modules plus 6 prerequisite/mock bridge packages delivered inside `Grade9-Maths/` (covering essential B7/B8 foundations in Triangles, Constructions, Perimeter/Area, Polygon Area, and Circle Measures).

### Rollup by Main Strand & BECE Bank Weighting

| Main Strand | B7 | B8 | B9 | Total | Delivered | BECE Tagged | Share | Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Strand 1: Number** | 4 | 7 | 9 | 20 | 12 | 1,809 | 52.0% | 60.0% (B7 100%; B9 Surds complete; SSNIT pending) |
| **Strand 2: Algebra** | 3 | 4 | 5 | 12 | 3 | 564 | 16.2% | 25.0% (Simultaneous graphs & Formula/Factorisation pending) |
| **Strand 3: Geometry & Measurement** | 6 | 6 | 13 | 25 | 11 | 733 | 21.1% | 44.0% (3D Nets/Vectors II & Enlargement pending) |
| **Strand 4: Handling Data** | 3 | 3 | 3 | 9 | 2 | 374 | 10.7% | 22.2% (Histograms/Bias/Outliers pending) |
| **Curriculum Total** | **16** | **20** | **30** | **66** | **28** | **3,480** | **100.0%** | **42.4%** |

### Sub-strand BECE Exam Weighting Breakdown (`BECE_MOCK_PAPERS`)

| Strand & Sub-strand | Paper 1 (Obj) | Paper 2 (Essay/Theory) | Marking Scheme | Total Tagged | Share | Priority Tier |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **S1.1** Number & Numeration Systems | 179 | 59 | 50 | 288 | 8.3% | High |
| **S1.2** Number Operations | 568 | 81 | 415 | 1,064 | 30.6% | **Critical (#1)** |
| **S1.3** Fractions, Decimals & Percentages | 51 | 20 | 93 | 164 | 4.7% | Moderate |
| **S1.4** Number: Ratios & Proportion | 195 | 32 | 66 | 293 | 8.4% | High |
| **S2.1** Patterns & Relations | 55 | 33 | 53 | 141 | 4.1% | High (Paper 2 heavy) |
| **S2.2** Algebraic Expressions | 123 | 41 | 101 | 265 | 7.6% | High |
| **S2.3** Variables & Equations | 57 | 31 | 70 | 158 | 4.5% | Moderate-High |
| **S3.1** Shape & Space | 154 | 42 | 92 | 288 | 8.3% | High |
| **S3.2** Measurement | 167 | 47 | 131 | 345 | 9.9% | **Critical (#2)** |
| **S3.3** Position & Transformation | 57 | 11 | 32 | 100 | 2.9% | Standard (Obj heavy) |
| **S4.1** Data | 111 | 30 | 87 | 228 | 6.6% | High |
| **S4.2** Chance or Probability | 97 | 24 | 25 | 146 | 4.2% | Standard |
| **Total Tagged Mathematics Bank** | **1,814** | **451** | **1,215** | **3,480** | **100.0%** | **42.4% Lessons Built** |

---

## Academic Term Schedule Matrix (Terms 1–3 across B7–B9)

Paced at **4 periods × 50 minutes/week** (~12 instructional weeks per term = 48 periods/term) in strict prerequisite order so algebraic and geometric tools are never taught before their underlying number operations:

| Term | Grade 7 (JHS 1) | Grade 8 (JHS 2) | Grade 9 (JHS 3) |
| :--- | :--- | :--- | :--- |
| **Term 1** *(Foundations & Number)* | **Strand 1 Complete (L01–L04):** Numeration beyond billions, Mental math & 4-digit ops, Prime factors/index form, FDP conversions & ops, Ratios & unit rates. | **Strand 1 Complete (L01–L07):** Standard form & factor sets, Multi-digit ops & Laws of Indices, FDP with BODMAS, Unit conversions, Travel graphs & Constant of proportionality. | **Strand 1 Complete (L01–L09):** Place value/Standard form, Real number sets/Venns, Operational laws, Decimals, **Surds**, FDP, Commercial math, **Taxes/Depreciation/SSNIT**. |
| **Term 2** *(Algebra & Shape/Space)* | **Strand 2 Complete + Strand 3 SS1 (L05–L09):** Patterns/mappings, Algebraic expressions, Linear equations (1 var), Angle classification/pairs, Perpendicular & angle bisectors. | **Strand 2 Complete + Strand 3 SS1 (L08–L13):** Gradient & $y=mx+c$, Binomial expansion & algebraic fractions, Factorisation, Inequalities & domains, Parallel transversals, Standard constructions & loci. | **Strand 2 Complete + Strand 3 SS1 (L10–L20):** Linear relations & **Simultaneous graphs**, Modelling, **Change of subject & Quadratic factorisation**, Inequalities, Polygons, Similarity, Trig bridge & Constructions I–II. |
| **Term 3** *(Measurement, Vectors, Transformations & Data)* | **Strand 3 SS2–3 + Strand 4 Complete (L10–L16):** Compound perimeter, Circumference, Triangle/quad areas, Bearings & column vectors, Reflection & translation, Surveys, Bar charts, Mean/median, Single-event probability. | **Strand 3 SS2–3 + Strand 4 Complete (L14–L20):** Circle area & Pythagoras, Basic trig ($\sin/\cos/\tan$), Vector arithmetic, Rotation, Grouped/ungrouped charts (stem-leaf/box/pie), Central tendency choice, Compound independent probability. | **Strand 3 SS2–3 + Strand 4 Complete + Mock Prep (L21–L30):** Circle/scale, Perimeter/area bridges, **3D nets/surface area & Parallel/perpendicular vectors**, **Enlargement**, Statistics, **Histograms/bias/outliers**, Dependent probability + Synoptic BECE Mocks. |

---

<!-- pagebreak -->

# GRADE 7 MATHEMATICS — LESSON DELIVERY SCHEDULE

## Strand 1: Number *(Term 1 — 52.0% BECE Bank Weight)*

| # | Term | Lesson Title & Sub-strand | Indicators | BECE Weight | Folder & Status |
| :---: | :---: | :--- | :--- | :---: | :--- |
| **01** | T1 | **Numeration and Big Numbers (Beyond Billions, Rounding & Significant Figures)** — *SS1 Number & Numeration Systems* | B7.1.1.1.1–5 *(incl. B7.1.1.2)* | 288 (8.3%) | `Grade7-Maths/.../Substrand-1-Numeration/Lesson-01-Numeration-and-Big-Numbers/` — **[x] Delivered** (PDF + 8×5 exercises + solutions) |
| **02** | T1 | **Number Operations, Decimals, Prime Factors & Index Notation** — *SS2 Number Operations* | B7.1.2.1.1–3, B7.1.2.2.1–3, B7.1.2.3.1–5 | 1,064 (30.6%) | `Grade7-Maths/.../Substrand-2-Operations/Lesson-01-Number-Operations-and-Indices/` — **[x] Delivered** (PDF + 8×5 exercises + solutions) |
| **03** | T1 | **Fractions, Decimals and Percentages (Conversions & Operations)** — *SS3 Fractions, Decimals & Percentages* | B7.1.3.1.1–2, B7.1.3.2.1–2, B7.1.3.3.1–4 | 164 (4.7%) | `Grade7-Maths/.../Substrand-3-FDP/Lesson-01-Fractions-Decimals-Percentages/` — **[x] Delivered** (PDF + 8×5 exercises + solutions) |
| **04** | T1 | **Ratio, Unit Rates, Equivalent Tables & Percentage Rates** — *SS4 Ratios & Proportion* | B7.1.4.1.1–5 | 293 (8.4%) | `Grade7-Maths/.../Substrand-4-Ratio/Lesson-01-Ratio-and-Proportion/` — **[x] Delivered** (PDF + 8×5 exercises + solutions) |

## Strand 2: Algebra *(Term 2 — 16.2% BECE Bank Weight)*

| # | Term | Lesson Title & Sub-strand | Indicators | BECE Weight | Target Folder & Status |
| :---: | :---: | :--- | :--- | :---: | :--- |
| **05** | T2 | **Patterns, Verbal Rules, Mappings & Tables of Values** — *SS1 Patterns & Relations* | B7.2.1.1.1–4 | 141 (4.1%) | `Grade7-Maths/.../Substrand-1-Patterns-And-Relations/Lesson-01-Patterns-Mappings-and-Graphs/` — **[ ] Pending** |
| **06** | T2 | **Algebraic Expressions — Translation, Like Terms & Substitution** — *SS2 Algebraic Expressions* | B7.2.2.1.1–5 | 265 (7.6%) | `Grade7-Maths/.../Substrand-2-Algebraic-Expressions/Lesson-01-Algebraic-Expressions-and-Substitution/` — **[ ] Pending** |
| **07** | T2 | **Linear Equations in One Variable — Balance Models & Algebra Tiles** — *SS3 Variables & Equations* | B7.2.3.1.1–4 | 158 (4.5%) | `Grade7-Maths/.../Substrand-3-Variables-And-Equations/Lesson-01-Linear-Equations-One-Variable/` — **[ ] Pending** |

## Strand 3: Geometry and Measurement *(Terms 2–3 — 21.1% BECE Bank Weight)*

| # | Term | Lesson Title & Sub-strand | Indicators | BECE Weight | Target Folder & Status |
| :---: | :---: | :--- | :--- | :---: | :--- |
| **08** | T2 | **Angle Classification & Angle Pair Theorems (Complementary, Supplementary, Vertically Opposite)** — *SS1 Shape & Space* | B7.3.1.1.1–3 | 288 (8.3%) | `Grade7-Maths/.../Substrand-1-Shapes-And-Space/Lesson-01-Angle-Classification-and-Pairs/` — **[ ] Pending** |
| **09** | T2 | **Fundamental Geometric Constructions — Perpendiculars, Line Bisectors & Angle Bisectors** — *SS1 Shape & Space* | B7.3.1.2.1–3, B7.3.1.2.7 | 288 (8.3%) | `Grade7-Maths/.../Substrand-1-Shapes-And-Space/Lesson-02-Perpendiculars-and-Bisectors/` — **[ ] Pending** |
| **10** | T3 | **Compound-Unit Perimeter, Circle Circumference (π) & Grid Areas** — *SS2 Measurement* | B7.3.2.1.1–3 | 345 (9.9%) | `Grade7-Maths/.../Substrand-2-Measurement/Lesson-01-Perimeter-Circumference-and-Grid-Areas/` — **[ ] Pending** |
| **11** | T3 | **Area of Triangles, Parallelograms & Trapeziums** — *SS2 Measurement* | B7.3.2.2.1–2 | 345 (9.9%) | `Grade7-Maths/.../Substrand-2-Measurement/Lesson-02-Area-of-Triangles-and-Quadrilaterals/` — **[ ] Pending** |
| **12** | T3 | **Three-Digit Bearings, Back Bearings & 2D Column Vectors** — *SS2 Measurement* | B7.3.2.3.1–5 | 345 (9.9%) | `Grade7-Maths/.../Substrand-2-Measurement/Lesson-03-Bearings-and-2D-Column-Vectors/` — **[ ] Pending** |
| **13** | T3 | **Reflectional Symmetry, Coordinate Reflection & Vector Translation** — *SS3 Position & Transformation* | B7.3.3.1.1–4 | 100 (2.9%) | `Grade7-Maths/.../Substrand-3-Position-And-Transformation/Lesson-01-Reflection-and-Translation/` — **[ ] Pending** |

## Strand 4: Handling Data *(Term 3 — 10.7% BECE Bank Weight)*

| # | Term | Lesson Title & Sub-strand | Indicators | BECE Weight | Target Folder & Status |
| :---: | :---: | :--- | :--- | :---: | :--- |
| **14** | T3 | **Qualitative vs Quantitative Data, Questionnaires, Tally Tables & Bar Charts** — *SS1 Data* | B7.4.1.1.1–3 | 228 (6.6%) | `Grade7-Maths/.../Substrand-1-Data/Lesson-01-Data-Collection-and-Charts/` — **[ ] Pending** |
| **15** | T3 | **Measures of Central Tendency — Mean and Median of Ungrouped Data** — *SS1 Data* | B7.4.1.2.1–2 | 228 (6.6%) | `Grade7-Maths/.../Substrand-1-Data/Lesson-02-Mean-and-Median-Ungrouped/` — **[ ] Pending** |
| **16** | T3 | **Chance & Single-Event Probability (Likelihood Scale, Sample Space & Forms)** — *SS2 Chance or Probability* | B7.4.2.1.1–3 | 146 (4.2%) | `Grade7-Maths/.../Substrand-2-Chance-And-Probability/Lesson-01-Single-Event-Probability/` — **[ ] Pending** |

---

<!-- pagebreak -->

# GRADE 8 MATHEMATICS — LESSON DELIVERY SCHEDULE

## Strand 1: Number *(Term 1 — 52.0% BECE Bank Weight)*

| # | Term | Lesson Title & Sub-strand | Indicators | BECE Weight | Target Folder & Status |
| :---: | :---: | :--- | :--- | :---: | :--- |
| **01** | T1 | **Large Numbers, Skip Counting, Standard Form ($A \times 10^n$) & Significant Rounding** — *SS1 Number & Numeration Systems* | B8.1.1.1.1–6 | 288 (8.3%) | `Grade8-Maths/.../Substrand-1-Numeration/Lesson-01-Standard-Form-and-Place-Value/` — **[ ] Pending** |
| **02** | T1 | **Sets of Factors, Perfect Squares, Square Roots & Set Operations ($\cup, \cap$)** — *SS1 Number & Numeration Systems* | B8.1.1.2.1–2 | 288 (8.3%) | `Grade8-Maths/.../Substrand-1-Numeration/Lesson-02-Factor-Sets-and-Square-Roots/` — **[ ] Pending** |
| **03** | T1 | **Mental Mathematics & Multi-Digit Four Operations (Whole Numbers & Decimals)** — *SS2 Number Operations* | B8.1.2.1.1–3, B8.1.2.2.1–3 | 1,064 (30.6%) | `Grade8-Maths/.../Substrand-2-Operations/Lesson-01-Mental-Math-and-Multi-Digit-Ops/` — **[ ] Pending** |
| **04** | T1 | **Laws of Indices, Order of Operations (BODMAS/PEMDAS) & Exponential Equations** — *SS2 Number Operations* | B8.1.2.3.1–4 | 1,064 (30.6%) | `Grade8-Maths/.../Substrand-2-Operations/Lesson-02-Laws-of-Indices-and-Exponential-Equations/` — **[ ] Pending** |
| **05** | T1 | **Mixed & Negative Fractions with BODMAS/PEMDAS & Financial Word Problems** — *SS3 Fractions, Decimals & Percentages* | B8.1.3.1.1–3 | 164 (4.7%) | `Grade8-Maths/.../Substrand-3-FDP/Lesson-01-Fraction-Operations-and-BODMAS/` — **[ ] Pending** |
| **06** | T1 | **Unit Conversions, Unit Rates, Speed & Distance-Time Travel Graphs** — *SS4 Ratios & Proportion* | B8.1.4.1.1–3 | 293 (8.4%) | `Grade8-Maths/.../Substrand-4-Ratio/Lesson-01-Unit-Rates-Speed-and-Travel-Graphs/` — **[ ] Pending** |
| **07** | T1 | **Direct Proportion Verification & Constant of Proportionality ($y = kx$)** — *SS4 Ratios & Proportion* | B8.1.4.1.4–5 | 293 (8.4%) | `Grade8-Maths/.../Substrand-4-Ratio/Lesson-02-Proportional-Relationships/` — **[ ] Pending** |

## Strand 2: Algebra *(Term 2 — 16.2% BECE Bank Weight)*

| # | Term | Lesson Title & Sub-strand | Indicators | BECE Weight | Target Folder & Status |
| :---: | :---: | :--- | :--- | :---: | :--- |
| **08** | T2 | **Linear Relations — Gradient ($m$) & Straight-Line Equations ($y = mx + c$)** — *SS1 Patterns & Relations* | B8.2.1.1.1–3 | 141 (4.1%) | `Grade8-Maths/.../Substrand-1-Patterns-And-Relations/Lesson-01-Gradient-and-Linear-Equations/` — **[ ] Pending** |
| **09** | T2 | **Expanding Binomials $(ax+b)(cx+d)$ & Operations on Algebraic Fractions** — *SS2 Algebraic Expressions* | B8.2.2.1.1–2 | 265 (7.6%) | `Grade8-Maths/.../Substrand-2-Algebraic-Expressions/Lesson-01-Binomial-Expansion-and-Algebraic-Fractions/` — **[ ] Pending** |
| **10** | T2 | **Substitution with Fractions/Negatives & Factorisation (Common Factors & Grouping)** — *SS2 Algebraic Expressions* | B8.2.2.1.3–4 | 265 (7.6%) | `Grade8-Maths/.../Substrand-2-Algebraic-Expressions/Lesson-02-Substitution-and-Factorisation/` — **[ ] Pending** |
| **11** | T2 | **Linear Inequalities in One Variable & Solution Sets over Domains** — *SS3 Variables & Equations* | B8.2.3.1.1–3 | 158 (4.5%) | `Grade8-Maths/.../Substrand-3-Variables-And-Equations/Lesson-01-Linear-Inequalities-and-Domains/` — **[ ] Pending** |

## Strand 3: Geometry and Measurement *(Terms 2–3 — 21.1% BECE Bank Weight)*

| # | Term | Lesson Title & Sub-strand | Indicators | BECE Weight | Target Folder & Status |
| :---: | :---: | :--- | :--- | :---: | :--- |
| **12** | T2 | **Parallel Lines Cut by a Transversal & Interior/Exterior Angles of Triangles** — *SS1 Shape & Space* | B8.3.1.1.1–2 | 288 (8.3%) | `Grade8-Maths/.../Substrand-1-Shapes-And-Space/Lesson-01-Parallel-Lines-and-Triangle-Angles/` — **[ ] Pending** |
| **13** | T2 | **Construction of Standard Angles (60°–150°), Triangles & Classic Loci** — *SS1 Shape & Space* | B8.3.1.2.1–3 | 288 (8.3%) | `Grade8-Maths/.../Substrand-1-Shapes-And-Space/Lesson-02-Constructions-Triangles-and-Loci/` — **[ ] Pending** |
| **14** | T3 | **Area of a Circle ($A = \pi r^2$), Pythagoras' Theorem & Triangle Heights** — *SS2 Measurement* | B8.3.2.1.1–4 | 345 (9.9%) | `Grade8-Maths/.../Substrand-2-Measurement/Lesson-01-Circle-Area-and-Pythagoras-Theorem/` — **[ ] Pending** |
| **15** | T3 | **Basic Right-Triangle Trigonometric Ratios ($\sin\theta, \cos\theta, \tan\theta$)** — *SS2 Measurement* | B8.3.2.1.5 | 345 (9.9%) | `Grade8-Maths/.../Substrand-2-Measurement/Lesson-02-Basic-Trigonometric-Ratios/` — **[ ] Pending** |
| **16** | T3 | **2D Vector Arithmetic — Addition, Subtraction, Scalar Multiplication & Equality** — *SS2 Measurement* | B8.3.2.2.1–2 | 345 (9.9%) | `Grade8-Maths/.../Substrand-2-Measurement/Lesson-03-Vector-Arithmetic-and-Equality/` — **[ ] Pending** |
| **17** | T3 | **Geometric Rotation in the Coordinate Plane & Rotational Congruence** — *SS3 Position & Transformation* | B8.3.3.1.1–3 | 100 (2.9%) | `Grade8-Maths/.../Substrand-3-Position-And-Transformation/Lesson-01-Rotation-and-Congruence/` — **[ ] Pending** |

## Strand 4: Handling Data *(Term 3 — 10.7% BECE Bank Weight)*

| # | Term | Lesson Title & Sub-strand | Indicators | BECE Weight | Target Folder & Status |
| :---: | :---: | :--- | :--- | :---: | :--- |
| **18** | T3 | **Data Types & Statistical Charts (Pie, Line, Stem-and-Leaf, Waffle & Box Plots)** — *SS1 Data* | B8.4.1.1.1–3 | 228 (6.6%) | `Grade8-Maths/.../Substrand-1-Data/Lesson-01-Data-Types-and-Visual-Representations/` — **[ ] Pending** |
| **19** | T3 | **Mean, Median & Mode of Ungrouped Data — Comparison & Context Justification** — *SS1 Data* | B8.4.1.2.1–2 | 228 (6.6%) | `Grade8-Maths/.../Substrand-1-Data/Lesson-02-Central-Tendency-Comparison/` — **[ ] Pending** |
| **20** | T3 | **Compound Independent Probability (With Replacement, Outcome Grids & Tree Diagrams)** — *SS2 Chance or Probability* | B8.4.2.1.1–2 | 146 (4.2%) | `Grade8-Maths/.../Substrand-2-Chance-And-Probability/Lesson-01-Compound-Independent-Probability/` — **[ ] Pending** |

---

<!-- pagebreak -->

# GRADE 9 MATHEMATICS — LESSON DELIVERY SCHEDULE

*Tracks all B9 syllabus modules plus the cross-grade Geometry Foundation Bridges (`[Bridge]`) housed inside `Grade9-Maths/`. See [`Grade9-Maths/LESSON_TRACKER.md`](Grade9-Maths/LESSON_TRACKER.md) for the day-by-day 60-day schedule.*

## Strand 1: Number *(Term 1 — 52.0% BECE Bank Weight)*

| # | Term | Lesson Title & Sub-strand | Indicators | BECE Weight | Folder & Status |
| :---: | :---: | :--- | :--- | :---: | :--- |
| **01** | T1 | **Place Value, Large Numbers, Rounding & Standard Form** — *SS1 Numeration Systems* | B9.1.1.1.1–2 | 288 (8.3%) | `Grade9-Maths/.../Substrand-1-Numeration-Systems/Lesson-01-Place-Value-And-Standard-Form/` — **[x] Delivered** (PDF + 20 worked + 8×5 + 1 PNG) |
| **02** | T1 | **Real Number System Hierarchy ($\mathbb{N}\subset\mathbb{W}\subset\mathbb{Z}\subset\mathbb{Q}$) & Venn Diagrams** — *SS1 Numeration Systems* | B9.1.1.2.1–2 | 288 (8.3%) | `Grade9-Maths/.../Substrand-1-Numeration-Systems/Lesson-02-Number-Systems-And-Venn-Diagrams/` — **[x] Delivered** (PDF + 20 worked + 8×5 + 3 PNGs) |
| **03** | T1 | **Indices, Powers of 10 & Multi-Step Operations** — *SS2 Number Operations* | B9.1.2.1.1, B9.1.2.1.4, B9.1.2.2.1–2 | 1,064 (30.6%) | `Grade9-Maths/.../Substrand-2-Number-Operations/Lesson-01-Indices-Decimals-And-Number-Operations/` — **[x] Delivered** (PDF + 20 worked + 8×5) |
| **04** | T1 | **Number Properties & Operational Laws (Commutative, Associative, Distributive)** — *SS2 Number Operations* | B9.1.2.1.2–4 | 1,064 (30.6%) | `Grade9-Maths/.../Substrand-2-Number-Operations/Lesson-02-Number-Properties-And-Operational-Laws/` — **[x] Delivered** (PDF + 15 worked + 5×5 + 1 PNG) |
| **05** | T1 | **Decimal Operations & Multi-Step Word Problems** — *SS2 Number Operations* | B9.1.2.2.1–2 | 1,064 (30.6%) | `Grade9-Maths/.../Substrand-2-Number-Operations/Lesson-03-Decimal-Operations-And-Word-Problems/` — **[x] Delivered** (PDF + 15 worked + 5×5) |
| **06** | T1 | **Surds (Simple/Compound, Identities, Simplification, Rationalisation & Non-Perfect Roots)** — *SS2 Number Operations* | B9.1.2.4.1–4 *(incl. B9.1.2.3.4)* | 1,064 (30.6%) | `Grade9-Maths/.../Substrand-2-Number-Operations/Lesson-04-Surds-And-Irrational-Roots/` — **[x] Delivered** (PDF + 15 worked + 8×5 + 3 PNGs) |
| **07** | T1 | **Fraction Arithmetic, Order of Operations (BODMAS/PEMDAS) & Percentages** — *SS3 FDP* | B9.1.3.1.1–3 | 164 (4.7%) | `Grade9-Maths/.../Substrand-3-Fractions-Decimals-Percentages/Lesson-01-Fractions-Decimals-And-Percentages/` — **[x] Delivered** (PDF + 20 worked + 8×5) |
| **08** | T1 | **Ratio, Proportion, Rates, Wages & Commercial Financial Maths** — *SS4 Ratios & Proportions* | B9.1.4.1.1–2 *(partial)* | 293 (8.4%) | `Grade9-Maths/.../Substrand-4-Ratios-And-Proportions/Lesson-01-Ratios-Proportion-And-Financial-Maths/` — **[x] Delivered** (PDF + 20 worked + 8×5) |
| **09** | T1 | **Taxes (VAT/NHIL), Asset Depreciation, Insurance & SSNIT Contributions/Benefits (Act 766 & PNDCL 247)** — *SS4 Ratios & Proportions* | B9.1.4.1.2–3 | 293 (8.4%) | `Grade9-Maths/.../Substrand-4-Ratios-And-Proportions/Lesson-02-Taxes-Depreciation-And-SSNIT/` — **[ ] Pending (Gap: NHIL, Depreciation & SSNIT)** |

## Strand 2: Algebra *(Term 2 — 16.2% BECE Bank Weight)*

| # | Term | Lesson Title & Sub-strand | Indicators | BECE Weight | Folder & Status |
| :---: | :---: | :--- | :--- | :---: | :--- |
| **10** | T2 | **Linear Relations, Gradient & Unit Rate as Slope** — *SS1 Patterns & Relations* | B9.1.4.1.4, B9.2.1.1.1 | 141 (4.1%) | `Grade9-Maths/.../Substrand-1-Patterns-And-Relations/Lesson-01-Linear-Relations-And-Gradient/` — **[x] Delivered** (PDF + 20 worked + 8×5 + 1 PNG) |
| **11** | T2 | **Simultaneous Linear Relations & Graphical Solution by Intersection** — *SS1 Patterns & Relations* | B9.2.1.1.2–3 | 141 (4.1%) | `Grade9-Maths/.../Substrand-1-Patterns-And-Relations/Lesson-02-Simultaneous-Linear-Graphs/` — **[ ] Pending (Gap: Simultaneous Graphs)** |
| **12** | T2 | **Substitution, Simplification & Real-Life Algebraic Modelling** — *SS2 Algebraic Expressions* | B9.2.2.1.2, B9.2.2.1.4 | 265 (7.6%) | `Grade9-Maths/.../Substrand-2-Algebraic-Expressions/Lesson-01-Algebraic-Expressions-And-Modelling/` — **[x] Delivered** (PDF + 20 worked + 8×5 + 2 PNGs) |
| **13** | T2 | **Change of Subject of Formulae & Quadratic Factorisation (Difference of Squares & Trinomials)** — *SS2 Algebraic Expressions* | B9.2.2.1.1, B9.2.2.1.3 | 265 (7.6%) | `Grade9-Maths/.../Substrand-2-Algebraic-Expressions/Lesson-02-Change-Of-Subject-And-Factorisation/` — **[ ] Pending (Gap: Change of Subject & Quadratics)** |
| **14** | T2 | **Linear Equations, Rational-Coefficient Inequalities & Number-Line Solutions** — *SS3 Variables & Equations* | B9.2.3.1.1–3 | 158 (4.5%) | `Grade9-Maths/.../Substrand-3-Variables-And-Equations/Lesson-01-Equations-And-Inequalities/` — **[x] Delivered** (PDF + 21 worked + 8×5 + 4 PNGs) |

## Strand 3: Geometry and Measurement *(Terms 2–3 — 21.1% BECE Bank Weight)*

| # | Term | Lesson Title & Sub-strand | Indicators | BECE Weight | Folder & Status |
| :---: | :---: | :--- | :--- | :---: | :--- |
| **15** | T2 | **Polygons & Angle Sum Formulas ($S = (n-2)\times 180°$)** — *SS1 Shapes & Space* | B9.3.1.1.1 | 288 (8.3%) | `Grade9-Maths/.../Substrand-1-Shapes-And-Space/Lesson-01-Polygons-And-Angle-Properties/` — **[x] Delivered** (PDF + 8×5 + 4 PNGs + Python playground) |
| **16** | T2 | **Congruence and Similarity in Triangles** — *SS1 Shapes & Space* | B9.3.1.1.2 | 288 (8.3%) | `Grade9-Maths/.../Substrand-1-Shapes-And-Space/Lesson-02-Congruence-And-Similarity/` — **[x] Delivered** (PDF + 8×5 + 5 PNGs + Python playground) |
| **17** | T2 | **Angles, Parallel Lines & Basic Trigonometry** *(Mock Bridge)* — *SS1 Shapes & Space* | B9.3.1.1.1–2, B8.3.1.1, B8.3.2.1.5 | 288 (8.3%) | `Grade9-Maths/.../Substrand-1-Shapes-And-Space/Lesson-03-Angles-Parallel-Lines-And-Trigonometry/` — **[x] Delivered** (PDF + 20 worked + 8×5 + 4 PNGs) |
| **18** | T2 | **[Bridge B] Triangle Types, Angle Properties & Pythagoras' Theorem** — *SS1 Shapes & Space* | B8.3.1.1.2, B8.3.2.1.2–4 | 288 (8.3%) | `Grade9-Maths/.../Substrand-1-Shapes-And-Space/Lesson-04-Triangle-Types-And-Angles/` — **[x] Delivered** (PDF + 15 worked + 5×5 + 5 PNGs) |
| **19** | T2 | **[Bridge E] Geometric Constructions I — Perpendiculars, Bisectors, 60°–105° & Loci** — *SS1 Shapes & Space* | B7.3.1.2.1–2, B8.3.1.2.1, B8.3.1.2.3 | 288 (8.3%) | `Grade9-Maths/.../Substrand-1-Shapes-And-Space/Lesson-05-Geometric-Constructions-I/` — **[x] Delivered** (PDF + 15 worked + 5×5 + 8 PNGs) |
| **20** | T2 | **Geometric Constructions II — Triangles (SSS/SAS/ASA), Quadrilaterals, Incircles & Circumcircles** — *SS1 Shapes & Space* | B8.3.1.2.2, B9.3.1.2.1–2 | 288 (8.3%) | `Grade9-Maths/.../Substrand-1-Shapes-And-Space/Lesson-06-Geometric-Constructions-II/` — **[x] Delivered** (PDF + 15 worked + 5×5 + 5 PNGs) |
| **21** | T3 | **Circles, Semicircles, Scale Drawings & Measurement** — *SS2 Measurement & Vectors* | B9.3.2.1.1 *(intro)* + mock | 345 (9.9%) | `Grade9-Maths/.../Substrand-2-Measurement-And-Vectors/Lesson-01-Measurement-Circles-And-Scale/` — **[x] Delivered** (PDF + 20 worked + 8×5 + 3 PNGs) |
| **22** | T3 | **Position Vectors, Triangle Law & Component Arithmetic** — *SS2 Measurement & Vectors* | B9.3.2.1.4, B9.3.2.2.2 *(previews B9.3.2.2.1)* | 345 (9.9%) | `Grade9-Maths/.../Substrand-2-Measurement-And-Vectors/Lesson-02-Vectors/` — **[x] Delivered** (PDF + 20 worked + 8×5 + 3 PNGs) |
| **23** | T3 | **[Bridge A] Perimeter & Area Basics — Squares, Rectangles & Rectilinear Shapes** — *SS2 Measurement & Vectors* | B7.3.2.1.1, B7.3.2.1.3 | 345 (9.9%) | `Grade9-Maths/.../Substrand-2-Measurement-And-Vectors/Lesson-03-Perimeter-And-Area-Basics/` — **[x] Delivered** (PDF + 15 worked + 5×5 + 3 PNGs) |
| **24** | T3 | **[Bridge C] Area of Polygons — Parallelogram, Triangle, Trapezium, Rhombus & Kite** — *SS2 Measurement & Vectors* | B7.3.2.2.1–2, B8.3.2.1.4 | 345 (9.9%) | `Grade9-Maths/.../Substrand-2-Measurement-And-Vectors/Lesson-04-Area-Of-Polygons/` — **[x] Delivered** (PDF + 15 worked + 5×5 + 3 PNGs) |
| **25** | T3 | **[Bridge D] Circle Parts, Circumference & Area Measures** — *SS2 Measurement & Vectors* | B7.3.2.1.2, B8.3.2.1.1 | 345 (9.9%) | `Grade9-Maths/.../Substrand-2-Measurement-And-Vectors/Lesson-05-Circle-Parts-And-Measures/` — **[x] Delivered** (PDF + 15 worked + 5×5 + 6 PNGs) |
| **26** | T3 | **3D Nets & Surface Area (Cuboids & Triangular Prisms), Parallel/Perpendicular Vectors & Parallelogram Law** — *SS2 Measurement & Vectors* | B9.3.2.1.1–3, B9.3.2.2.1–2 | 345 (9.9%) | `Grade9-Maths/.../Substrand-2-Measurement-And-Vectors/Lesson-06-3D-Nets-Surface-Area-And-Vectors/` — **[ ] Pending (Gap: 3D Nets/Surface Area & Orthogonal Vectors)** |
| **27** | T3 | **Geometric Enlargement, Scale Factors ($k > 0, 0 < k < 1, k < 0$), Area Scale ($k^2$) & Similarity** — *SS3 Position & Transformation* | B9.3.3.1.1–3 | 100 (2.9%) | `Grade9-Maths/.../Substrand-3-Position-And-Transformation/Lesson-01-Enlargement-And-Similarity/` — **[ ] Pending (Gap: Entire B9 Enlargement unit)** |

## Strand 4: Handling Data *(Term 3 — 10.7% BECE Bank Weight)*

| # | Term | Lesson Title & Sub-strand | Indicators | BECE Weight | Folder & Status |
| :---: | :---: | :--- | :--- | :---: | :--- |
| **28** | T3 | **Data Types, Frequency Tables, Stem-and-Leaf & Descriptive Statistics** — *SS1 Data & Statistics* | B9.4.1.1.1–2, B9.4.1.2.2 | 228 (6.6%) | `Grade9-Maths/.../Substrand-1-Data-And-Statistics/Lesson-01-Data-Statistics-And-Representations/` — **[x] Delivered** (PDF + 20 worked + 8×5 + 2 PNGs) |
| **29** | T3 | **Survey Bias & Ethics, Continuous Grouped Histograms, Modal Estimation & Outlier Effects** — *SS1 Data & Statistics* | B9.4.1.1.3, B9.4.1.2.1, B9.4.1.2.3 | 228 (6.6%) | `Grade9-Maths/.../Substrand-1-Data-And-Statistics/Lesson-02-Histograms-Survey-Bias-And-Outliers/` — **[ ] Pending (Gap: Histograms, Survey Ethics & Outliers)** |
| **30** | T3 | **Probability, Sample Spaces & Dependent Two-Stage Events** — *SS2 Chance & Probability* | B9.4.2.1.1–2 | 146 (4.2%) | `Grade9-Maths/.../Substrand-2-Chance-And-Probability/Lesson-01-Probability/` — **[x] Delivered** (PDF + 20 worked + 8×5 + 1 PNG) |

---

<!-- pagebreak -->

# Execution Playbook & Delivery Protocol

1. **Standard Mathematics Lesson Package Architecture:**
   Every lesson package lives in `Grade<7|8|9>-Maths/Strand-<n>-<Name>/Substrand-<m>-<Name>/Lesson-<nn>-<Topic>/` and ships with:
   - `Lesson_<nn>_<Topic>.md` — Plain British English preamble, unpacked technical vocabulary, step-by-step concept proofs, worked exam examples (`12–20`, authentic BECE/mock items marked with year), and exercises + full worked solutions.
   - `Lesson_<nn>_<Topic>.pdf` — Compiled with `tools/build_lesson_pdf.py` (Cambria body font, MiKTeX display maths, zero raw LaTeX leaks, zero tofu glyphs).
   - `diagrams/` — `.tex` TikZ master sources + `300 DPI` `.png` renders only (per `.agents/skills/math-diagrams/SKILL.md` and `tools/math-diagrams/`). Zero `.svg` or `.jpg` figure assets.
   - Exercise Battery — Default `8 sections × 5 questions = 40` (or `5×5 = 25` when under explicit user quota override) combining Paper 1 Objective MCQs and Paper 2 Theory/Structured questions with `[marks]`, including `10–20%` spiral review from prior sub-strands.

2. **BECE Paper 2 Section-Rotation Delivery Rule (Round-Robin Across Strands 1–4 — Never Sequential):**
   - **Why Section Rotation:** BECE Mathematics Paper 2 (`60 marks`, `1 hour`, calculators not allowed) sets **`6` equal `15-mark` structured `(a)(b)(c)` / `(i)(ii)` / `(α)(β)` questions** (candidates answer `4`) spanning all four strands: **Strand 1: Number** (Sets/Venn, Fractions/Surds/Indices, Commercial `GH₵` 2 d.p. word problems), **Strand 2: Algebra** (Factorisation, Change of Subject, Linear Equations/Inequalities on number lines, Straight-line graphs), **Strand 3: Geometry & Measurement** (Angles/Polygons, Mensuration/L-shapes/Circles `[Take π = 22/7]`, Trig `[Take tan 60° = 1.732]`, Vectors/Transformations, Compass Constructions), and **Strand 4: Handling Data** (Frequency table construction, Mean/Median/Mode, Probability).
   - Every delivery round rotates **one lesson per strand (`Strand 1 → Strand 2 → Strand 3 → Strand 4`)** so all four BECE Paper 2 domains advance together:

| Rotation Round | Focus Tier | Strand 1: Number | Strand 2: Algebra | Strand 3: Geometry & Measurement | Strand 4: Handling Data |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **Round 1** | **B9 Closure I** | **G9 L09:** Taxes (VAT/NHIL), Depreciation & SSNIT (`B9.1.4.1.2–3`) | **G9 L13:** Change of Subject & Quadratic Factorisation (`B9.2.2.1.1/3`) | **G9 L26:** 3D Nets/Surface Area & Orthogonal Vectors (`B9.3.2.1–2`) | **G9 L29:** Histograms, Survey Bias & Outliers (`B9.4.1.1–2`) |
| **Round 2** | **B9 Closure II + B7 I** | *(G9 & G7 S1 100% Built)* | **G9 L11:** Simultaneous Linear Graphs (`B9.2.1.1.2–3`) | **G9 L27:** Geometric Enlargement & Similarity (`B9.3.3.1.1–3`) | **G7 L14:** Questionnaires, Tally Tables & Bar Charts (`B7.4.1.1.1–3`) |
| **Round 3** | **B7 Rotation I** | *(G7 S1 100% Built)* | **G7 L05:** Patterns, Mappings & Tables (`B7.2.1.1.1–4`) | **G7 L08 & L10:** Angle Theorems & Circle Circumference (`B7.3.1.1`, `B7.3.2.1`) | **G7 L15:** Mean & Median of Ungrouped Data (`B7.4.1.2.1–2`) |
| **Round 4** | **B7 Rotation II** | *(G7 S1 100% Built)* | **G7 L06–L07:** Algebraic Expressions & Linear Equations (`B7.2.2–3`) | **G7 L09, L11–L13:** Bisectors, Triangle/Quad Areas, Bearings/Vectors & Reflection (`B7.3.1–3`) | **G7 L16:** Single-Event Probability (`B7.4.2.1.1–3`) |
| **Round 5** | **B8 Rotation I** | **G8 L01–L02:** Standard Form & Factor Sets/Venn (`B8.1.1.1–2`) | **G8 L08:** Gradient ($m$) & $y = mx + c$ (`B8.2.1.1.1–3`) | **G8 L12 & L14:** Parallel Transversals, Circle Area & Pythagoras (`B8.3.1.1`, `B8.3.2.1`) | **G8 L18:** Pie, Stem-Leaf, Waffle & Box Plots (`B8.4.1.1.1–3`) |
| **Round 6** | **B8 Rotation II** | **G8 L03–L05:** Multi-Digit Ops, Laws of Indices & BODMAS Fractions (`B8.1.2–3`) | **G8 L09–L10:** Binomial Expansion, Algebraic Fractions & Factorisation (`B8.2.2.1.1–4`) | **G8 L13 & L15:** Standard Constructions/Loci & Basic Trig ($\sin/\cos/\tan$) (`B8.3.1.2`, `B8.3.2.1.5`) | **G8 L19:** Central Tendency Comparison (`B8.4.1.2.1–2`) |
| **Round 7** | **B8 Closure** | **G8 L06–L07:** Travel Graphs & Direct Proportion $y = kx$ (`B8.1.4.1.1–5`) | **G8 L11:** Linear Inequalities & Solution Domains (`B8.2.3.1.1–3`) | **G8 L16–L17:** 2D Vector Arithmetic & Coordinate Rotation (`B8.3.2.2`, `B8.3.3.1`) | **G8 L20:** Compound Independent Probability (`B8.4.2.1.1–2`) |

3. **Bank Query Workflow:**
   Before authoring any pending lesson, pull all authentic bank questions tagged to its indicator(s):
   ```powershell
   .\.venv\Scripts\python.exe BECE_MOCK_PAPERS/src/bece_cli.py query --indicator <code> --subject Mathematics --limit 50 --format markdown
   ```
