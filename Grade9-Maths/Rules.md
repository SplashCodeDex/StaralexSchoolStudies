Keep lessons simple, PLAIN SIMPLE ENGLIGHS FOR EASY UNDERSTANDING, well explained in the most easiest way possible. diagrams are greatly needed for easier learning. All mathematics figures are produced as real PNG images from **LaTeX/TikZ sources** using the `math-diagrams` skill (`/.agents/skills/math-diagrams/SKILL.md` + `tools/math-diagrams/`) and must be inserted in the pdf lessons that will be created. Structure and map the learning curve on a 2 months period. 1 or 2 Sub-strand each Day/2 Days depending. after every covered and well learnt Sub strand, make sure you give about 7-10 different exercise(about 5 questions each) to try whiles also providing the answers as well. if there is a previously covered strand, include 10%-20% of that previously covered questions in the new questions.

---

## Mathematics notation, diagrams, and BECE-shaped drills (mandatory)

These rules override any older habit. They fix the broken symbols and missing figures that were shipping in maths PDFs.

### M1. Notation must be true math typesetting

- Display equations and any symbol-heavy working are typeset with **LaTeX** (MiKTeX/pdflatex), not plain Unicode guesses and not raw `\Rightarrow` leaking into the page.
- Inline maths may use clean Unicode (`× ÷ ≤ ≥ π ² √ −`), but **fractions, indices, and multi-line working** go through LaTeX.
- The PDF must contain **zero** raw LaTeX command names (`\times`, `\frac`, `\Rightarrow`, `\mathbf`, `\;`, `\ge`, `\le`, …). If you see one, the build is wrong.
- Common forms that must look like a textbook:
  - fractions: 13/21 stacked (not `(13)/(21)`)
  - mixed numbers: 1 1/3 stacked (not `1(1)/(3)`)
  - inequalities: x ≥ −4/3 stacked
  - indices: 2^(2m), 4^14
  - vectors: column vectors
  - sets: {5, 10, 15}

### M2. Contextual diagrams only — but the ones that are needed are compulsory

Do **not** decorate. Do **add** a figure whenever the concept is visual or the exam question is visual.

Topics that MUST carry a figure (at least one per concept, not one per lesson):

| Topic | Required figure |
| :--- | :--- |
| Number lines / inequalities | a real number line with open/closed dots and arrow |
| Place value / standard form | place-value chart or number line |
| Angles, polygons, triangles | labelled geometry figure |
| Circles, semicircles | labelled circle with radius/diameter |
| Vectors | axes with the vector drawn |
| Graphs / gradient | Cartesian axes with the line |
| Venn diagrams | the two- or three-set diagram |
| Stem-and-leaf, pie charts, histograms | the actual chart |
| Nets / surface area | the net |
| Locus | the locus figure |
| Scale drawings | the diagram with the scale marked |

Every figure: caption (`Figure 1: …`), referenced from the question text (`see Figure 1`), drawn as a real PNG from a TikZ source in `tools/math-diagrams/` and stored in `diagrams/`. Strictly NO `.svg` and NO `.pdf` diagram assets may be created, stored, or committed (300 DPI PNG is the sole asset target). ASCII/text art is only for the smallest one-line ideas and must render with zero black blocks.

**Authoring is mandatory through the `math-diagrams` skill** — shared styles in `tools/math-diagrams/styles/mathdiagrams.sty`, templates + `catalog.json`, build with `python tools/math-diagrams/build.py`. Never generate maths figures with an image model.

### M3. Exercises are BECE-shaped

Same philosophy as `RULES-BECE-PATTERN.md`, in maths voice:

- **Paper 1 Objective drill:** MCQ with options A–D and answer = letter + one-line reason.
- **Paper 2 Essay drill:** structured questions with **mark allocations** `(2 marks) (3 marks)` and **marking points** in the answers.
- **All authentic BECE/mock/exam questions** for that strand/substrand go into the drills. If there are more authentic questions than the quota, expand the quota — never drop an authentic one.
- Generated questions fill the rest, 10–20% spiral review from earlier sub-strands.
- Default quota stays 7–10 sections × 5 questions.

### M4. Lesson body is taught in plain English first, then worked examples

Keep the existing structure (preamble → concept → worked examples → exercises → solutions), but every worked example must use the typeset notation from M1 and the figures from M2.

---

[IMPORTANT]

EXPLANATIONS AND STUDY MUST NOT BE RUSHED AND BARE. IT IS NOT POSSIBLE TO TEACH A WHOLE STRAND AND SOME LONG SUBSTRAND IN A DAY AND THOSE MUST BE CONTINUED THE NEXT DAY.  MAKING IT EASIER TO UNDERSTAND AND ADDING MORE EASIER WELL EXPLAINATION EVEN IF THE SOURCE DIDN'T INCLUDE IS THE CORE MANDATE. IT'S OKAY TO BREAK SUBSTRANDS INTO PARTS IF CONTEXT WINDOW CAN'T FIT EVERYTHING SO THAT A SIMPLE 'CONTINUE/PROCEED' APPROVAL CAN MAKE YOU CONTINUE TILL EVERYTHING IS COVERED.  EVERYTHING STUDY, TEACHINGS AND LEARNING IS INTER ATIONAL BRITISH RULES(NO AMERICAN STANDARD). MAKE SURE ALL STANDS AND SUBSTRANDS PDFS, AND OTHER RELEVANT FILES, ILLUSTRATIONS, LEARNING MATERIALS if image should be included in the pdf lesson. ALL WELL ORGANIZED, STRUCTURED AND SAVED IN THEIR PRESPECTIVE STUDYSPACE. REMEMBER THE PLAIN SIMPLE ENGLIGHS FOR THE LESSONS. AND DON'T ASSUME I ALREADY KNOW SOME STUFFS AND BLINDLY FOLLOWS THE SOURCE WITHOUT GIVEN ME SOME PREAMBLES AND PRE-LESSONS OF BASICS AS LONG AS STUDYING IS CONCERNED



before we start lesson, create the comprehensive and detailed map/tableofcontent/tracker for the entire  lessons.

