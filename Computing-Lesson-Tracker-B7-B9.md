# Computing — Master Curriculum Roadmap & Lesson Tracker (Grades 7–9)

*Based on the NaCCA Computing Common Core Programme (CCP) Curriculum for JHS1 (B7) – JHS3 (B9).*

- **Source of Truth:** [`Computing-Lesson-Plan-B7-B9.md`](Computing-Lesson-Plan-B7-B9.md) (`125` canonical NaCCA indicators across `43` Content Standards, `4` Main Strands, and `14` Sub-strands).
- **Existing Grade Trackers Reconciled:** [`Grade7-Computing/Curriculum_Tracker.md`](Grade7-Computing/Curriculum_Tracker.md) (`3/20` delivered) and [`Grade9-Computing/Curriculum_Tracker.md`](Grade9-Computing/Curriculum_Tracker.md) (`5/21` delivered).
- **BECE Exam Weighting Source:** `BECE_MOCK_PAPERS` (`1,276` total Computing/ICT items in `catalog.db`, `100%` embedded with `google/embeddinggemma-2` and tagged to primary NaCCA indicators — `973` Paper 1 Objective MCQs, `173` Paper 2 Theory/Essay items [`145` Theory + `28` Essay], and `130` Marking Scheme entries; `1,255` items at high confidence `>= 0.70`).
- **Standard:** International British English conventions (*organise*, *colour*, *programme*, *centre*); strict adherence to [`RULES-BECE-PATTERN.md`](RULES-BECE-PATTERN.md), NaCCA CCP indicators, and BECE examinable standards.
- **Pedagogical Model & Time Allocation:** `3–4 periods × 50 minutes/week` (`1–2` periods theory/concepts + `2` periods hands-on computer lab practicals). Every lesson combines structured **Theory Questions and Answers** (`Q1. …? Ans. …`), acronym/shortcut/formula tables, step-by-step GUI/lab procedures, contextual diagrams, worked exam exemplars, and an `8×5` or `5×5` exercise battery with complete marking schemes.

---

## High-Level Delivery Summary

| Grade | Level | Indicators | Total Lessons | Delivered | Pending | Completion |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Grade 7** | Basic 7 / JHS 1 | 50 | 20 | 3 | 17 | 15.0% |
| **Grade 8** | Basic 8 / JHS 2 | 38 | 19 | 0 | 19 | 0.0% |
| **Grade 9** | Basic 9 / JHS 3 | 37 | 21 | 5 | 16 | 23.8% |
| **Total** | **JHS 1–3 Cycle** | **125** | **60** | **8** | **52** | **13.3%** |

### Rollup by Main Strand & BECE Bank Weighting

| Main Strand | B7 | B8 | B9 | Total | Delivered | BECE Tagged | Share | Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Strand 1: Introduction to Computing** | 3 | 4 | 5 | 12 | 8 | 465 | 36.4% | 66.7% Active (G7 & G9 100% Complete) |
| **Strand 2: Productivity Software** | 7 | 7 | 6 | 20 | 0 | 365 | 28.6% | 0.0% Pending (Word & Excel #2–#3 in Bank) |
| **Strand 3: Communication Networks** | 5 | 4 | 5 | 14 | 0 | 279 | 21.9% | 0.0% Pending |
| **Strand 4: Computational Thinking** | 5 | 4 | 5 | 14 | 0 | 167 | 13.1% | 0.0% Pending |
| **Curriculum Total** | **20** | **19** | **21** | **60** | **8** | **1,276** | **100.0%** | **13.3% Complete** |

### Sub-strand BECE Exam Weighting Breakdown (`BECE_MOCK_PAPERS`)

| Strand & Sub-strand | Paper 1 (Obj) | Paper 2 (Theory/Essay) | Marking Scheme | Total Tagged | Share of Bank | Priority Tier |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **S1.1 Components of Computers & Computer Systems** | 300 | 55 | 18 | 373 | 29.2% | **Critical (#1 — G7 & G9 Built)** |
| **S1.2 Technology in the Community** | 8 | 3 | 2 | 13 | 1.0% | Standard (G7 & G9 Built) |
| **S1.3 Health & Safety in the Use of ICT Tools** | 52 | 10 | 17 | 79 | 6.2% | **High (G7 & G9 Built)** |
| **S2.1 Introduction to Word Processing** | 98 | 27 | 4 | 129 | 10.1% | **Critical (#3 — Pending)** |
| **S2.2 Introduction to Presentation Software** | 38 | 2 | 9 | 49 | 3.8% | Moderate (Pending) |
| **S2.3 Introduction to Desktop Publishing** *(B8–B9)* | 35 | 10 | 4 | 49 | 3.8% | Moderate (Pending) |
| **S2.4 Introduction to Electronic Spreadsheet** | 111 | 17 | 10 | 138 | 10.8% | **Critical (#2 — Pending)** |
| **S3.1 Computer Networks** | 58 | 8 | 11 | 77 | 6.0% | **High (Pending)** |
| **S3.2 Internet and Social Media** | 47 | 9 | 11 | 67 | 5.3% | Moderate-High (Pending) |
| **S3.3 Information Security** | 43 | 11 | 11 | 65 | 5.1% | Moderate-High (Pending) |
| **S3.4 Web Technologies** | 49 | 4 | 17 | 70 | 5.5% | Moderate-High (Pending) |
| **S4.1 Introduction to Programming** | 46 | 7 | 6 | 59 | 4.6% | Moderate (Pending) |
| **S4.2 Algorithm** | 51 | 6 | 5 | 62 | 4.9% | Moderate (Pending) |
| **S4.3 Robotics** | 15 | 1 | 1 | 17 | 1.3% | Standard (Pending) |
| **S4.4 Artificial Intelligence** | 22 | 3 | 4 | 29 | 2.3% | Standard (Pending) |
| **Total Tagged Computing Bank** | **973** | **173** | **130** | **1,276** | **100.0%** | **36.4% Strand 1 Active** |

---

## Academic Term Schedule Matrix (Terms 1–3 across B7–B9)

Paced at **3–4 periods × 50 minutes/week** (~12 instructional weeks/term) from hardware & OS foundations in Term 1 through office productivity in Term 2 and networks/CS in Term 3:

| Term | Grade 7 (JHS 1) | Grade 8 (JHS 2) | Grade 9 (JHS 3) |
| :--- | :--- | :--- | :--- |
| **Term 1** *(Hardware, OS, Community Tech, Safety & Word/Presentation I)* | **Strand 1 Complete + Strand 2 Part A (L01–L07):** 4th-gen computers, I/O/storage, Windows GUI & file management; Ergonomics & electrical safety; Community tech & green upcycling; MS Word editing/proofing & typography/tabs; PowerPoint interface & Slide Master. | **Strand 1 Complete + Strand 2 Part A (L01–L08):** 5th-gen computers & Direct Data Entry (OCR/OMR/MICR/RFID/QR); Braille/3D printers & Flash/SSD storage; Windows Charms & drive partitioning; Assistive tech & workstation risks; MS Word tables/hyperlinks; PowerPoint layering; MS Publisher DTP I–II. | **Strand 1 Complete + Strand 2 Part A (L01–L08):** Next-gen & quantum supercomputing; Cloud/hybrid storage, DDE, printers & file systems; Assistive tech & e-waste lifecycle; Perceptual computing, AR/VR & desktop personalisation; Workstation auditing; MS Word SmartArt/multimedia; PowerPoint animations; Multi-panel DTP brochures. |
| **Term 2** *(Electronic Spreadsheets & Communication Networks)* | **Strand 2 Part B + Strand 3 Complete (L08–L15):** Excel interface, cell formatting, page setup, Autofill & basic arithmetic formulas; Network architectures & topologies (LAN/WAN, Star/Bus/Ring); Networking entrepreneurship; Social media & email protocols (CC/BCC); Information security (CIA triad, copyright); Educational portals, OERs & CRAAP evaluation. | **Strand 2 Part B + Strand 3 Complete (L09–L15):** Excel statistical functions (`SUM`, `AVERAGE`, `COUNT`, `MAX`, `MIN`), complex nested BODMAS formulas, relative/absolute (`$`) referencing & error codes; Data communication models & OSI/TCP-IP; Guided/unguided media, ISPs & DNS; Collaborative clouds, digital footprints & 4 data threats; Boolean search operators. | **Strand 2 Part B + Strand 3 Complete (L09–L16):** Excel multi-level sorting, auto-filtering, data validation, conditional formatting, analytical charts & Pivot Tables; E-commerce, Mobile Money (MoMo) & cashless society; E-learning & LMS architectures; Social media privacy & cyber-safety; Cyberbullying & 10 hacking techniques; School/club blog publishing. |
| **Term 3** *(Computational Thinking: Programming, Algorithms, Robotics & AI)* | **Strand 4 Complete (L16–L20):** Block programming environments (Scratch/Blockly) & primitive data types (`Integer`, `Float`, `Char`, `String`, `Boolean`); Variables, constants & assignment; Algorithm control structures (sequence, selection, iteration) & linear search; Robotics principles & Asimov's laws; AI vs human intelligence & everyday AI. | **Strand 4 Complete (L16–L19):** Arithmetic, relational & logical operators (`AND`, `OR`, `NOT`) and precedence; Variable state tracing, complex branching & dry-run tables; Robotics Sense-Think-Act cycle, sensors (ultrasonic, IR, LDR) & actuators (servos, steppers); Machine Learning & Artificial Neural Networks (input/hidden/output layers). | **Strand 4 Complete + BECE Mock Prep (L17–L21):** Binary data representation (Base 10 ↔ Base 2) & ASCII/Unicode; IDEs & text-based Python/JS/HTML coding; Flowchart symbols, structured pseudocode & bidirectional translation; Physical robot fabrication & microcontroller coding; Expert Systems (Knowledge Base, Inference Engine, UI) & AI ethics. |

---

<!-- pagebreak -->

# GRADE 7 COMPUTING — LESSON DELIVERY SCHEDULE

## Strand 1: Introduction to Computing

| # | Lesson Title | Sub-strand | Indicators | Package Path | Status |
|---|--------------|------------|------------|--------------|--------|
| **01** | Components of Computers and Computer Systems | Components of Computers and Computer Systems | B7.1.1.1.1–4<br>B7.1.1.2.1–2 | `Grade7-Computing/Strand-1-Introduction-To-Computing/Lesson-01-Components-and-File-Management/` | [x] Delivered — PDF + 8×5 exercises + solutions |
| **02** | Health and Safety in the Use of ICT Tools | Health and Safety in the Use of ICT Tools | B7.1.3.1.1–4 | `Grade7-Computing/Strand-1-Introduction-To-Computing/Lesson-02-Health-and-Safety/` | [x] Delivered — PDF + 8×5 exercises + solutions |
| **03** | Technology in the Community & Green Upcycling | Technology in the Community | B7.1.2.1.1–6 | `Grade7-Computing/Strand-1-Introduction-To-Computing/Lesson-03-Technology-in-the-Community/` | [x] Delivered — PDF + 8×5 exercises + solutions |

## Strand 2: Productivity Software

| # | Lesson Title | Sub-strand | Indicators | Target Package Path | Status |
|---|--------------|------------|------------|---------------------|--------|
| **04** | Word Processing I — Editing, Search, Replace & Proofing | Introduction to Word Processing | B7.2.1.1.1–4 | `Grade7-Computing/Strand-2-Productivity-Software/Lesson-04-Word-Processing-Editing-Proofing/` | [ ] Pending |
| **05** | Word Processing II — Typography, Paragraph Layout & Custom Tabs | Introduction to Word Processing | B7.2.1.1.5–7 | `Grade7-Computing/Strand-2-Productivity-Software/Lesson-05-Word-Processing-Typography-Layout/` | [ ] Pending |
| **06** | Presentation I — Workspace Navigation, Text Boxes & Special Characters | Introduction to Presentation Software | B7.2.2.1.1–3 | `Grade7-Computing/Strand-2-Productivity-Software/Lesson-06-Presentation-Interface-Text/` | [ ] Pending |
| **07** | Presentation II — Slide Master, Design Templates & Alignment Controls | Introduction to Presentation Software | B7.2.2.2.1–3 | `Grade7-Computing/Strand-2-Productivity-Software/Lesson-07-Presentation-Slide-Master-Themes/` | [ ] Pending |
| **08** | Electronic Spreadsheet I — Interface, Cell Data Types & Formatting | Introduction to Electronic Spreadsheet | B7.2.3.1.1–4 | `Grade7-Computing/Strand-2-Productivity-Software/Lesson-08-Spreadsheet-Interface-Formatting/` | [ ] Pending |
| **09** | Electronic Spreadsheet II — Page Setup, Headers, Footers & Autofill Sequences | Introduction to Electronic Spreadsheet | B7.2.3.2.1–3 | `Grade7-Computing/Strand-2-Productivity-Software/Lesson-09-Spreadsheet-PageSetup-Autofill/` | [ ] Pending |
| **10** | Electronic Spreadsheet III — Formula Syntax & Basic Arithmetic Computations | Introduction to Electronic Spreadsheet | B7.2.3.3.1 | `Grade7-Computing/Strand-2-Productivity-Software/Lesson-10-Spreadsheet-Formulas-Arithmetic/` | [ ] Pending |

## Strand 3: Communication Networks

| # | Lesson Title | Sub-strand | Indicators | Target Package Path | Status |
|---|--------------|------------|------------|---------------------|--------|
| **11** | Computer Networks — Components, Architectures & Topologies | Computer Networks | B7.3.1.1.1–2 | `Grade7-Computing/Strand-3-Communication-Networks/Lesson-11-Network-Topologies/` | [ ] Pending |
| **12** | Entrepreneurial Opportunities in Networking | Computer Networks | B7.3.1.1.3 | `Grade7-Computing/Strand-3-Communication-Networks/Lesson-12-Networking-Entrepreneurship/` | [ ] Pending |
| **13** | Internet & Social Media — Platform Classifications & Email Protocols | Internet and Social Media | B7.3.2.1.1–2 | `Grade7-Computing/Strand-3-Communication-Networks/Lesson-13-Social-Media-Email-Netiquette/` | [ ] Pending |
| **14** | Information Security — The CIA Triad, Intellectual Property & Forensics | Information Security | B7.3.3.1.1–3 | `Grade7-Computing/Strand-3-Communication-Networks/Lesson-14-Information-Security-CIA-Triad/` | [ ] Pending |
| **15** | Web Technologies — Educational Portals, OERs & CRAAP Web Evaluation | Web Technologies | B7.3.4.1.1–3 | `Grade7-Computing/Strand-3-Communication-Networks/Lesson-15-Educational-Web-CRAAP-Evaluation/` | [ ] Pending |

## Strand 4: Computational Thinking

| # | Lesson Title | Sub-strand | Indicators | Target Package Path | Status |
|---|--------------|------------|------------|---------------------|--------|
| **16** | Programming Fundamentals — Block Environments & Primitive Data Types | Introduction to Programming | B7.4.1.1.1–2 | `Grade7-Computing/Strand-4-Computational-Thinking/Lesson-16-Block-Programming-Data-Types/` | [ ] Pending |
| **17** | Variables, Constants & Assignment Operations | Introduction to Programming | B7.4.1.1.3 | `Grade7-Computing/Strand-4-Computational-Thinking/Lesson-17-Variables-Constants-Assignments/` | [ ] Pending |
| **18** | Algorithms — Control Structures (Sequence, Selection, Iteration) & Linear Search | Algorithm | B7.4.2.1.1–2 | `Grade7-Computing/Strand-4-Computational-Thinking/Lesson-18-Algorithm-Control-Structures/` | [ ] Pending |
| **19** | Robotics — Principles, Laws of Robotics & Societal Applications | Robotics | B7.4.3.1.1 | `Grade7-Computing/Strand-4-Computational-Thinking/Lesson-19-Robotics-Applications/` | [ ] Pending |
| **20** | Artificial Intelligence — Human vs Machine Intelligence & Everyday Systems | Artificial Intelligence | B7.4.4.1.1 | `Grade7-Computing/Strand-4-Computational-Thinking/Lesson-20-Artificial-Intelligence-Everyday-Systems/` | [ ] Pending |

---

<!-- pagebreak -->

# GRADE 8 COMPUTING — LESSON DELIVERY SCHEDULE

## Strand 1: Introduction to Computing

| # | Lesson Title | Sub-strand | Indicators | Target Package Path | Status |
|---|--------------|------------|------------|---------------------|--------|
| **01** | Fifth-Generation Computers & Direct Data Entry (DDE) Technologies | Components of Computers and Computer Systems | B8.1.1.1.1–2 | `Grade8-Computing/Strand-1-Introduction-To-Computing/Lesson-01-Fifth-Gen-Computers-DDE/` | [ ] Pending |
| **02** | Specialist Output Devices, Flash Storage & Solid-State Drives (SSDs) | Components of Computers and Computer Systems | B8.1.1.1.3–4 | `Grade8-Computing/Strand-1-Introduction-To-Computing/Lesson-02-Specialist-Output-Flash-SSDs/` | [ ] Pending |
| **03** | Windows Charms Bar & Drive Management (Partitioning & Maintenance) | Components of Computers and Computer Systems | B8.1.1.2.1–2 | `Grade8-Computing/Strand-1-Introduction-To-Computing/Lesson-03-Charms-Drive-Management/` | [ ] Pending |
| **04** | Assistive Tech, Portable Computing Devices & Workstation Health Risks | Technology in the Community<br>Health and Safety in ICT | B8.1.2.1.1–3<br>B8.1.3.1.1–2 | `Grade8-Computing/Strand-1-Introduction-To-Computing/Lesson-04-Assistive-Tech-Workstation-Health/` | [ ] Pending |

## Strand 2: Productivity Software

| # | Lesson Title | Sub-strand | Indicators | Target Package Path | Status |
|---|--------------|------------|------------|---------------------|--------|
| **05** | Word Processing — Advanced Tables, Calculations, Hyperlinks & Layout | Introduction to Word Processing | B8.2.1.1.1–3 | `Grade8-Computing/Strand-2-Productivity-Software/Lesson-05-Word-Processing-Tables-Hyperlinks/` | [ ] Pending |
| **06** | Presentation — Images, Screenshots, Shapes & Object Layering | Introduction to Presentation | B8.2.2.1.1–3 | `Grade8-Computing/Strand-2-Productivity-Software/Lesson-06-Presentation-Graphics-Object-Layering/` | [ ] Pending |
| **07** | Desktop Publishing I — MS Publisher Interface, Templates & Page Setup | Introduction to Desktop Publishing | B8.2.3.1.1–4 | `Grade8-Computing/Strand-2-Productivity-Software/Lesson-07-Desktop-Publishing-Interface-Setup/` | [ ] Pending |
| **08** | Desktop Publishing II — Text Overflow Frames, Pictures & Flyer/Card Design | Introduction to Desktop Publishing | B8.2.3.1.5–7 | `Grade8-Computing/Strand-2-Productivity-Software/Lesson-08-Desktop-Publishing-Flyers-Cards/` | [ ] Pending |
| **09** | Electronic Spreadsheet I — Built-in Statistical Functions (`SUM`, `AVERAGE`, `COUNT`, `MAX`, `MIN`) | Introduction to Electronic Spreadsheet | B8.2.4.1.1 | `Grade8-Computing/Strand-2-Productivity-Software/Lesson-09-Spreadsheet-Statistical-Functions/` | [ ] Pending |
| **10** | Electronic Spreadsheet II — Complex Formulas, Nesting & BODMAS Precedence | Introduction to Electronic Spreadsheet | B8.2.4.1.2 | `Grade8-Computing/Strand-2-Productivity-Software/Lesson-10-Spreadsheet-Complex-Formulas/` | [ ] Pending |
| **11** | Electronic Spreadsheet III — Cell Referencing (Relative/Absolute `$`) & Error Debugging | Introduction to Electronic Spreadsheet | B8.2.4.1.3 | `Grade8-Computing/Strand-2-Productivity-Software/Lesson-11-Spreadsheet-Cell-Referencing-Errors/` | [ ] Pending |

## Strand 3: Communication Networks

| # | Lesson Title | Sub-strand | Indicators | Target Package Path | Status |
|---|--------------|------------|------------|---------------------|--------|
| **12** | Data Communication Models, Protocols & Transmission Modes | Computer Networks | B8.3.1.1.1 | `Grade8-Computing/Strand-3-Communication-Networks/Lesson-12-Data-Communication-Models/` | [ ] Pending |
| **13** | Transmission Media & Internet Architecture (Guided/Unguided, ISPs & DNS) | Computer Networks | B8.3.1.1.2 | `Grade8-Computing/Strand-3-Communication-Networks/Lesson-13-Transmission-Media-Internet-DNS/` | [ ] Pending |
| **14** | Collaborative Social Media, Digital Footprints & 4 Major Data Threats | Internet and Social Media<br>Information Security | B8.3.2.1.1<br>B8.3.3.1.1–2 | `Grade8-Computing/Strand-3-Communication-Networks/Lesson-14-Social-Media-Data-Threats/` | [ ] Pending |
| **15** | Web Technologies — Boolean Search Operators & Search Engine Indexing | Web Technologies | B8.3.4.1.1–2 | `Grade8-Computing/Strand-3-Communication-Networks/Lesson-15-Advanced-Search-Boolean-Operators/` | [ ] Pending |

## Strand 4: Computational Thinking

| # | Lesson Title | Sub-strand | Indicators | Target Package Path | Status |
|---|--------------|------------|------------|---------------------|--------|
| **16** | Programming Constructs — Arithmetic, Relational & Logical Operators | Introduction to Programming | B8.4.1.1.1 | `Grade8-Computing/Strand-4-Computational-Thinking/Lesson-16-Operators-and-Expressions/` | [ ] Pending |
| **17** | Algorithmic Thinking — Variable States, Complex Branching & Iteration | Algorithm | B8.4.2.1.1–2 | `Grade8-Computing/Strand-4-Computational-Thinking/Lesson-17-Algorithms-Variables-Iteration/` | [ ] Pending |
| **18** | Robotics Anatomy — The Sense-Think-Act Cycle, Sensors & Actuators | Robotics | B8.4.3.1.1 | `Grade8-Computing/Strand-4-Computational-Thinking/Lesson-18-Robotics-Sense-Think-Act/` | [ ] Pending |
| **19** | Artificial Intelligence — Machine Learning & Artificial Neural Networks (ANN) | Artificial Intelligence | B8.4.4.1.1 | `Grade8-Computing/Strand-4-Computational-Thinking/Lesson-19-Machine-Learning-Neural-Networks/` | [ ] Pending |

---

<!-- pagebreak -->

# GRADE 9 COMPUTING — LESSON DELIVERY SCHEDULE

## Strand 1: Introduction to Computing

| # | Lesson Title | Sub-strand | Indicators | Package Path | Status |
|---|--------------|------------|------------|--------------|--------|
| **01** | Next-Generation Computing & Quantum Supercomputers | Components of Computers and Computer Systems | B9.1.1.1.1 | `Grade9-Computing/Strand-1-Introduction-To-Computing/Lesson-01-Next-Generation-Computers-And-Supercomputing/` | [x] Delivered — PDF + Notes + Playground + Figures |
| **02** | Storage Systems, Direct Data Entry, Printers & File Management | Components of Computers and Computer Systems | B9.1.1.1.4<br>B9.1.1.2.2 | `Grade9-Computing/Strand-1-Introduction-To-Computing/Lesson-02-Storage-Direct-Data-Entry-Printers-And-File-Management/` | [x] Delivered — PDF + 5×5 exercises + solutions |
| **03** | Assistive & Adaptive Tech, Portable Devices & E-Waste Lifecycle | Technology in the Community | B8.1.2.1.1–2<br>B7.1.2.1.4–5 | `Grade9-Computing/Strand-1-Introduction-To-Computing/Lesson-03-Assistive-And-Adaptive-Technology-Portable-Devices-And-The-Environment/` | [x] Delivered — PDF + 5×5 exercises + solutions |
| **04** | Perceptual Computing, Novel Output Devices & Desktop Personalisation | Components of Computers and Computer Systems | B9.1.1.1.2–3<br>B9.1.1.2.1–2 | `Grade9-Computing/Strand-1-Introduction-To-Computing/Lesson-04-Perceptual-Computing-Novel-Output-Devices-And-Personalisation/` | [x] Delivered — PDF + TikZ figures + exercises + solutions |
| **05** | Community Problem Solving & Workstation Health Compliance Auditing | Technology in the Community<br>Health and Safety in ICT | B9.1.2.1.1–3<br>B9.1.3.1.1–2 | `Grade9-Computing/Strand-1-Introduction-To-Computing/Lesson-05-Community-Problem-Solving-Workstation-Auditing/` | [x] Delivered — PDF + TikZ figures + exercises + solutions |

## Strand 2: Productivity Software

| # | Lesson Title | Sub-strand | Indicators | Target Package Path | Status |
|---|--------------|------------|------------|---------------------|--------|
| **06** | Word Processing — SmartArt Diagrams, Multimedia & Comprehensive Project Reports | Introduction to Word Processing | B9.2.1.1.1–3 | `Grade9-Computing/Strand-2-Productivity-Software/Lesson-06-Word-Processing-SmartArt-Multimedia/` | [ ] Pending |
| **07** | Presentation — Slide Animations, Transition Choreography & Delivery Techniques | Introduction to Presentation | B9.2.2.1.1–3 | `Grade9-Computing/Strand-2-Productivity-Software/Lesson-07-Presentation-Animations-Delivery/` | [ ] Pending |
| **08** | Desktop Publishing — Multi-Panel Brochures, Newsletters & Commercial Critique | Introduction to Desktop Publishing | B9.2.3.1.1–3 | `Grade9-Computing/Strand-2-Productivity-Software/Lesson-08-Desktop-Publishing-Brochures-Critique/` | [ ] Pending |
| **09** | Electronic Spreadsheet I — Multi-Level Sorting, Auto-Filtering & Data Validation | Introduction to Electronic Spreadsheet | B9.2.4.1.1 | `Grade9-Computing/Strand-2-Productivity-Software/Lesson-09-Spreadsheet-Sorting-Filtering-Validation/` | [ ] Pending |
| **10** | Electronic Spreadsheet II — Cell Styles, Templates & Conditional Formatting Rules | Introduction to Electronic Spreadsheet | B9.2.4.1.2 | `Grade9-Computing/Strand-2-Productivity-Software/Lesson-10-Spreadsheet-Conditional-Formatting/` | [ ] Pending |
| **11** | Electronic Spreadsheet III — Analytical Charts & Pivot Table Data Summaries | Introduction to Electronic Spreadsheet | B9.2.4.1.3 | `Grade9-Computing/Strand-2-Productivity-Software/Lesson-11-Spreadsheet-Charts-Pivot-Tables/` | [ ] Pending |

## Strand 3: Communication Networks

| # | Lesson Title | Sub-strand | Indicators | Target Package Path | Status |
|---|--------------|------------|------------|---------------------|--------|
| **12** | E-Commerce, Mobile Money (MoMo) & Cashless Society Foundations | Computer Networks | B9.3.1.1.1 | `Grade9-Computing/Strand-3-Communication-Networks/Lesson-12-E-Commerce-Cashless-Society/` | [ ] Pending |
| **13** | E-Learning Systems, LMS Infrastructures & Distance Learning Potentials | Computer Networks | B9.3.1.1.2 | `Grade9-Computing/Strand-3-Communication-Networks/Lesson-13-E-Learning-LMS-Systems/` | [ ] Pending |
| **14** | Social Media Hazards, Privacy Management & Youth Cyber-Safety | Internet and Social Media | B9.3.2.1.1 | `Grade9-Computing/Strand-3-Communication-Networks/Lesson-14-Social-Media-Hazards-Cyber-Safety/` | [ ] Pending |
| **15** | Interpersonal Cyber Harms & Ten Information Hacking Techniques | Information Security | B9.3.3.1.1–2 | `Grade9-Computing/Strand-3-Communication-Networks/Lesson-15-Cyberbullying-Ten-Hacking-Techniques/` | [ ] Pending |
| **16** | Web Technologies — School/Club Blog Development & Publishing Workflows | Web Technologies | B9.3.4.1.1–3 | `Grade9-Computing/Strand-3-Communication-Networks/Lesson-16-Blog-Development-Publishing/` | [ ] Pending |

## Strand 4: Computational Thinking

| # | Lesson Title | Sub-strand | Indicators | Target Package Path | Status |
|---|--------------|------------|------------|---------------------|--------|
| **17** | Number Systems — Binary Data Representation (Base 10 $\leftrightarrow$ Base 2) & Character Codes | Introduction to Programming | B9.4.1.1.1 | `Grade9-Computing/Strand-4-Computational-Thinking/Lesson-17-Binary-Data-Representation/` | [ ] Pending |
| **18** | Integrated Development Environments (IDEs) & Text-Based Coding Environments | Introduction to Programming | B9.4.1.1.2 | `Grade9-Computing/Strand-4-Computational-Thinking/Lesson-18-IDEs-Text-Based-Programming/` | [ ] Pending |
| **19** | Algorithms — Flowchart Modeling, Structured Pseudocode & Bidirectional Translation | Algorithm | B9.4.2.1.1–2 | `Grade9-Computing/Strand-4-Computational-Thinking/Lesson-19-Flowcharts-Pseudocode-Translation/` | [ ] Pending |
| **20** | Robotics — Physical Model Fabrication & Embedded Sensor-Actuator Programming | Robotics | B9.4.3.1.1 | `Grade9-Computing/Strand-4-Computational-Thinking/Lesson-20-Robot-Fabrication-Programming/` | [ ] Pending |
| **21** | Artificial Intelligence — Expert Systems Architecture & AI Societal/Ethical Impacts | Artificial Intelligence | B9.4.4.1.1 | `Grade9-Computing/Strand-4-Computational-Thinking/Lesson-21-Expert-Systems-AI-Ethics/` | [ ] Pending |

---

<!-- pagebreak -->

# Execution Playbook & Delivery Protocol

1. **Standard Lesson Package Architecture:**
   Each lesson package must be self-contained in its designated folder containing:
   - `Lesson_XX_[Topic].md` (Markdown notes, step-by-step guidance, technical vocabulary unpacked, worked examples).
   - `Lesson_XX_[Topic].pdf` (Compiled PDF via `tools/build_lesson_pdf.py` with zero tofu glyphs).
   - `diagrams/` (TikZ source scripts + high-resolution PNGs for architectural layouts, topologies, flowcharts).
   - Exercise Battery (7–10 distinct exercise sections or 5×5 / 8×5 question blocks, including 15–20% cumulative review questions from prior strands + complete marking scheme).

2. **Priority Closure Sequence (Highest BECE Weight First):**
   - **Priority 1 — Strand 2 Productivity Software (`365` items, `28.6%` bank share; `20` pending lessons):** Electronic Spreadsheets (`138` items, `10.8%` — Critical #2) and Word Processing (`129` items, `10.1%` — Critical #3) are the highest-weighted unbuilt topics in the Computing bank. Deliver Grade 9 Strand 2 (`L06–L11`) and Grade 7 Strand 2 (`L04–L10`) first, followed by Grade 8 Strand 2 (`L05–L11`, including MS Publisher DTP).
   - **Priority 2 — Grade 8 Strand 1 Hardware & OS (`L01–L04`):** Complete the remaining `4` lessons of Strand 1 (`465` items, `36.4%` bank share; G7 and G9 are already `100%` complete) so all `12/12` Strand 1 lessons across B7–B9 are closed.
   - **Priority 3 — Strand 3 Communication Networks (`279` items, `21.9%` bank share; `14` pending lessons):** Deliver Computer Networks (`77` items, `6.0%`), Web Technologies (`70` items, `5.5%`), Internet & Social Media (`67` items, `5.3%`), and Information Security (`65` items, `5.1%`) across G9 (`L12–L16`), G7 (`L11–L15`), and G8 (`L12–L15`).
   - **Priority 4 — Strand 4 Computational Thinking (`167` items, `13.1%` bank share; `14` pending lessons):** Deliver Algorithms (`62` items, `4.9%`), Programming (`59` items, `4.6%`), Artificial Intelligence (`29` items, `2.3%`), and Robotics (`17` items, `1.3%`) across G9 (`L17–L21`), G7 (`L16–L20`), and G8 (`L16–L19`).

3. **Bank Query & PDF Build Workflow:**
   - Before authoring any pending Computing lesson, pull all authentic bank questions tagged to its indicator(s):
     ```powershell
     .\.venv\Scripts\python.exe BECE_MOCK_PAPERS/src/bece_cli.py query --indicator <code> --subject Computing_ICT --limit 50 --format markdown
     ```
   - Compile any updated tracker or lesson markdown to PDF with strict glyph verification:
     ```powershell
     .\.venv\Scripts\python.exe tools/build_lesson_pdf.py Computing-Lesson-Tracker-B7-B9.md --title "Computing — Lesson Tracker (B7–B9)" --footer "Staralex · Computing Lesson Tracker · B7–B9" --strict
     ```
