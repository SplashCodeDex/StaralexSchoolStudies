# Grade 9 Computing: Master Curriculum Roadmap and Progress Tracker

## Syllabus Overview
- **Curriculum**: Ministry of Education / NaCCA Computing Curriculum (Basic 9 / Grade 9)
- **Standard**: International British English conventions (spelling, grammar, terminology)
- **Duration**: 2 Months (8 Weeks, 40 Study Days)
- **Pacing**: 1 to 2 Sub-strands per 2 to 3 Days, split into digestible parts with deep conceptual explanations
- **Assessment Policy**: 7 to 10 distinct exercises per sub-strand (5 questions each), including 10% to 20% cumulative review questions from prior strands
- **Visuals**: Clean text-based structural diagrams and high-resolution generated illustration figures embedded in each study module and compiled PDF lesson

---

## Workspace Directory Architecture

The repository will be structured as follows:

```text
Grade9-Computing/
├── Rules.md
├── Curriculum_Tracker.md
├── Grade9-Computing.pdf
├── Strand_1_Introduction_to_Computing/
│   ├── Substrand_1_Components_of_Computers/
│   │   ├── Lessons/
│   │   ├── Diagrams/
│   │   ├── Exercises/
│   │   └── PDFs/
│   ├── Substrand_2_Technology_in_the_Community/
│   │   ├── Lessons/
│   │   ├── Projects/
│   │   └── PDFs/
│   └── Substrand_3_Health_and_Safety/
│       ├── Lessons/
│       ├── Exercises/
│       └── PDFs/
├── Strand_2_Productivity_Software/
│   ├── Substrand_1_Word_Processing/
│   ├── Substrand_2_Presentation/
│   ├── Substrand_3_Desktop_Publishing/
│   └── Substrand_4_Electronic_Spreadsheet/
├── Strand_3_Communication_Networks/
│   ├── Substrand_1_Computer_Networks/
│   ├── Substrand_2_Internet_and_Social_Media/
│   ├── Substrand_3_Information_Security/
│   └── Substrand_4_Web_Technologies/
└── Strand_4_Computational_Thinking/
    ├── Substrand_1_Introduction_to_Programming/
    ├── Substrand_2_Algorithm/
    ├── Substrand_3_Robotics/
    └── Substrand_4_Artificial_Intelligence/
```

---

## 2-Month Master Schedule (8 Weeks / 40 Days)

### Month 1: Hardware Foundations, Productivity, and Initial Networks

#### Week 1: Introduction to Computing (Strand 1 - Part 1)
- **Day 1**: Strand 1, Sub-strand 1 (Part 1) - Next-Generation Computing & Supercomputing
  - Indicator: B9.1.1.1.1
  - Key Topics: Trends in next-generation hardware, Google Quantum Sycamore (54/53 qubits), comparison with classical supercomputers.
  - Deliverables:
    - Notes: `Lesson_01_Next_Generation_Computers_and_Supercomputing.md`
    - PDF: `Lesson_01_Next_Generation_Computers_and_Supercomputing.pdf`
    - Playground: `next_gen_computers_playground.py`
    - Diagrams: `classical_vs_quantum_bit.jpg`, `quantum_supremacy_comparison.jpg`
  - Status: [x] Completed
- **Day 2**: Strand 1, Sub-strand 1 (Part 2) - Storage, Direct Data Entry, Printers and File Management
  - Indicators: B9.1.1.1.4 (network/cloud storage, smart cards), B9.1.1.2.2 (file management techniques) + recap of B7.1.1.2.2, B8.1.1.1.2, B8.1.1.1.3, B8.1.1.1.4, B8.1.1.2.2
  - Key Topics: Magnetic/optical/flash storage, capacity units (MB/GB/TB), drives and partitions, barcode/OMR/RFID direct data entry, impact vs non-impact printers, file, folder and drive management.
  - Deliverables:
    - Notes: `Lesson_02_Storage_Direct_Data_Entry_Printers_And_File_Management.md`
    - PDF: `Lesson_02_Storage_Direct_Data_Entry_Printers_And_File_Management.pdf`
    - Exercises: 5 sections × 5 questions + marking scheme (embedded in lesson).
  - Status: [x] Completed
  - Note: originally planned Perceptual Computing (B9.1.1.1.2) and Novel Output Devices (B9.1.1.1.3) rescheduled to a later consolidation lesson (see Day 3).
- **Day 3**: Strand 1, Sub-strand 1 (Part 3) - Perceptual Computing, E-Paper Readers and Personalisation
  - Indicators: B9.1.1.1.2 (perceptual computing), B9.1.1.1.3 (novel output devices: wearable displays, E-Paper, e-readers), B9.1.1.2.1 (desktop personalisation), B9.1.1.2.2 (device drivers and plug-and-play — completes sub-strand 1)
  - Key Topics: Perceptual computing (facial recognition, gesture control, voice processing) and its privacy risk; E-Paper reflective displays vs LCD; e-readers (Kindle); wearable displays (Google Glass); device drivers (printer, sound, graphics); plug-and-play; desktop personalisation — wallpaper, icons, shortcuts, mouse pointers; taskbar and context menu.
  - Deliverables:
    - Notes: `Lesson_04_Perceptual_Computing_Novel_Output_Devices_And_Personalisation.md`
    - PDF: `Lesson_04_Perceptual_Computing_Novel_Output_Devices_And_Personalisation.pdf` (7 pages, glyph-checked)
    - Diagrams: `diagrams/figure_01_ereader_parts.png`, `diagrams/figure_02_desktop_personalise.png` (TikZ + PNG masters kept)
    - Exercises: 5 sections × 5 questions + full marking scheme (embedded in lesson), with [Review] spiral items from Lessons 01-03.
  - Status: [x] Completed — **sub-strand 1 is now fully covered** (B9.1.1.1.1-4, B9.1.1.2.1-2)
- **Day 4**: Strand 1, Sub-strand 2 - Technology in the Community (Assistive, Adaptive and Portable Technology + Environment)
  - Indicators: B8.1.2.1.1 (assistive/adaptive technologies), B8.1.2.1.2 (portable computing devices) + recap of B7.1.2.1.4 (environmental impact), B7.1.2.1.5 (responsible practices)
  - Key Topics: Assistive vs adaptive technology for learners with disabilities (memory hook: Assistive = Adds, Adaptive = Adjusted), portable devices and battery trade-offs, e-waste, product life cycle, environmentally responsible use of computers.
  - Deliverables:
    - Notes: `Lesson_03_Assistive_And_Adaptive_Technology_Portable_Devices_And_The_Environment.md`
    - PDF: `Lesson_03_Assistive_And_Adaptive_Technology_Portable_Devices_And_The_Environment.pdf`
    - Exercises: 5 sections × 5 questions + marking scheme (embedded in lesson).
  - Status: [x] Completed
  - Note: B9-level community problem-solving indicators (B9.1.2.1.1–3: community problem evaluation, solution proposals, project design and presentation) still to deliver as a project/case-study lesson.
- **Day 5**: Strand 1, Sub-strand 3 - Health and Safety at Workstations
  - Indicators: B9.1.3.1.1, B9.1.3.1.2
  - Key Topics: Ergonomic setups (keyboards, document holders, monitor positioning), lighting considerations, thermal dissipation and heat reduction.
  - Deliverable: Sub-strand 3 Exercise Battery + Strand 1 Cumulative Review (incorporating 15% Sub-strand 1 questions).
  - Status: [ ] Not Started

---

#### Week 2: Productivity Software - Word Processing and Presentation (Strand 2 - Part 1)
- **Day 6**: Strand 2, Sub-strand 1 (Part 1) - Advanced Word Processing & Graphical Integration
  - Indicator: B9.2.1.1.1
  - Key Topics: Screenshot insertion, screen clipping, Print Screen mechanics, image formatting and placement.
  - Status: [ ] Not Started
- **Day 7**: Strand 2, Sub-strand 1 (Part 2) - SmartArt, Charts, Hyperlinks, and Multimedia in Word
  - Indicators: B9.2.1.1.2, B9.2.1.1.3
  - Key Topics: SmartArt hierarchy/processes, embedding charts, hyperlinks, embedded media.
  - Deliverable: Sub-strand 1 Exercise Battery + Strand 1 Cumulative Review.
  - Status: [ ] Not Started
- **Day 8**: Strand 2, Sub-strand 2 (Part 1) - Presentation Design and Animation Mechanics
  - Indicators: B9.2.2.1.1, B9.2.2.1.2
  - Key Topics: Slide composition, screenshot clipping, transition timing, object animation sequences.
  - Status: [ ] Not Started
- **Day 9**: Strand 2, Sub-strand 2 (Part 2) - Presentation Multimedia, Tables, and Slide Project
  - Indicator: B9.2.2.1.3
  - Key Topics: Embedded audio/video, linked tables and charts, complete seven-slide animated presentation project.
  - Deliverable: Sub-strand 2 Exercise Battery + Solutions.
  - Status: [ ] Not Started
- **Day 10**: Strand 2, Sub-strand 3 - Desktop Publishing and Document Critique
  - Indicators: B9.2.3.1.1, B9.2.3.1.2, B9.2.3.1.3
  - Key Topics: Multi-page document publishing (flyers, brochures, business cards), overflow handling, design evaluation criteria (typography, colour, mechanics, layout).
  - Deliverable: Sub-strand 3 Evaluation Matrix & Exercise Battery.
  - Status: [ ] Not Started

---

#### Week 3: Productivity Software - Electronic Spreadsheets (Strand 2 - Part 2)
- **Day 11**: Strand 2, Sub-strand 4 (Part 1) - Structured Data Architecture in Spreadsheets
  - Indicator: B9.2.4.1.1 (Foundations)
  - Key Topics: Structured vs unstructured data, fields (columns), records (rows), data list conversions.
  - Status: [ ] Not Started
- **Day 12**: Strand 2, Sub-strand 4 (Part 2) - Validation Rules, Filtering, and Multi-Level Sorting
  - Indicator: B9.2.4.1.1 (Operations)
  - Key Topics: Data validation lists, dropdown constraints, multi-column ascending/descending sorts, auto-filters and custom filters.
  - Status: [ ] Not Started
- **Day 13**: Strand 2, Sub-strand 4 (Part 3) - Styles, Themes, Predefined Templates, and Macros
  - Indicator: B9.2.4.1.2
  - Key Topics: Template architecture vs macros, applying unified themes/styles, recording and running automated macros.
  - Status: [ ] Not Started
- **Day 14**: Strand 2, Sub-strand 4 (Part 4) - Pivot Tables, Pivot Charts, and Dynamic Summaries
  - Indicator: B9.2.4.1.3
  - Key Topics: Data aggregation, pivot table generation, field dragging, pivot charts, dynamic filtering.
  - Deliverable: Complete Spreadsheet Exercise Battery (8 Exercises + Solutions).
  - Status: [ ] Not Started
- **Day 15**: Strand 2 Consolidation & Cross-Strand Review
  - Comprehensive assessment spanning Word Processing, PowerPoint, Desktop Publishing, and Spreadsheets with 20% Strand 1 review questions.
  - Status: [ ] Not Started

---

#### Week 4: Communication Networks - E-Commerce and Collaboration (Strand 3 - Part 1)
- **Day 16**: Strand 3, Sub-strand 1 (Part 1) - E-Commerce and the Cashless Society
  - Indicator: B9.3.1.1.1
  - Key Topics: Online business models, payment gateways, card transactions (MasterCard, Visa), mobile money architecture, Bitcoin and digital currencies, QR code payment mechanisms.
  - Status: [ ] Not Started
- **Day 17**: Strand 3, Sub-strand 1 (Part 2) - E-Learning Infrastructure and Collaborative Platforms
  - Indicator: B9.3.1.1.2
  - Key Topics: E-learning frameworks, pedagogical benefits and constraints, offline/local platforms (iBox network), ad-hoc resource sharing, collaborative cloud platforms (Wikis, Google Docs).
  - Deliverable: Sub-strand 1 Exercise Battery + Solutions.
  - Status: [ ] Not Started
- **Day 18**: Strand 3, Sub-strand 2 - Internet Communication, Social Media, and Electronic Mail
  - Indicator: B9.3.2.1.1
  - Key Topics: Social media dynamics, professional and educational utility, privacy and operational risks, email protocol features (Reply, Reply All, Forward, Forward All, CC, BCC).
  - Deliverable: Sub-strand 2 Exercise Battery + Solutions.
  - Status: [ ] Not Started
- **Day 19**: Mid-Course Progress Review & Hands-on Practical Lab
  - Structured practical checkpoint covering Strands 1, 2, and 3.1-3.2.
  - Status: [ ] Not Started
- **Day 20**: Buffer / Revision Day
  - Remediation and deep exploration of student queries or complex topics.
  - Status: [ ] Not Started

---

### Month 2: Cybersecurity, Web Technologies, and Computational Thinking

#### Week 5: Cybersecurity and Web Technologies (Strand 3 - Part 2)
- **Day 21**: Strand 3, Sub-strand 3 (Part 1) - Cyberspace Dynamics and Digital Identity
  - Indicator: B9.3.3.1.1
  - Key Topics: Cyberbullying, cyberstalking, psychological impact, digital footprint (active) vs digital shadow (passive), online reputation hygiene.
  - Status: [ ] Not Started
- **Day 22**: Strand 3, Sub-strand 3 (Part 2) - Ten Critical Information Hacking Techniques
  - Indicator: B9.3.3.1.2
  - Key Topics: Phishing, keyloggers, Denial of Service (DoS/DDoS), eavesdropping/packet sniffing, man-in-the-middle, spoofing, brute-force attacks, spyware, SQL injection, social engineering.
  - Status: [ ] Not Started
- **Day 23**: Strand 3, Sub-strand 3 (Part 3) - Countermeasures and Defensive Protocols
  - Synthesis of B9.3.3.1
  - Key Topics: Multi-factor authentication, cryptographic basics, firewall policies, intrusion detection.
  - Deliverable: Sub-strand 3 Cybersecurity Exercise Battery (8 Exercises) with 15% Strand 2 review questions.
  - Status: [ ] Not Started
- **Day 24**: Strand 3, Sub-strand 4 (Part 1) - Web Technologies and Blog Architecture
  - Indicators: B9.3.4.1.1, B9.3.4.1.2
  - Key Topics: The role of blogs in community and institutional communication, content structure, editorial workflow.
  - Status: [ ] Not Started
- **Day 25**: Strand 3, Sub-strand 4 (Part 2) - Blog Publishing, Moderation, and Interaction
  - Indicator: B9.3.4.1.3
  - Key Topics: Publishing steps, comment moderation, hyperlinking, embedding multimedia, security considerations.
  - Deliverable: Sub-strand 4 Exercise Battery + Strand 3 Cumulative Review.
  - Status: [ ] Not Started

---

#### Week 6: Computational Thinking - Data Representation & Environments (Strand 4 - Part 1)
- **Day 26**: Strand 4, Sub-strand 1 (Part 1) - Number Bases and Radix Conversions
  - Indicator: B9.4.1.1.1
  - Key Topics: Decimal (Base 10) to Binary (Base 2), Binary to Decimal, Hexadecimal (Base 16) representation, nibbles and bytes.
  - Status: [ ] Not Started
- **Day 27**: Strand 4, Sub-strand 1 (Part 2) - Binary Arithmetic and Logic
  - Indicator: B9.4.1.1.1 (Arithmetic)
  - Key Topics: Binary addition, binary subtraction, overflow concepts, representation of signed numbers.
  - Status: [ ] Not Started
- **Day 28**: Strand 4, Sub-strand 1 (Part 3) - Integrated Development Environments (IDEs)
  - Indicator: B9.4.1.1.2
  - Key Topics: IDE anatomy (code editor, interpreter/compiler, console, debugger), block-based environments (Snap, Scratch) vs high-level textual environments (Python).
  - Status: [ ] Not Started
- **Day 29**: Strand 4, Sub-strand 1 (Part 4) - Core Programming Constructs & Web Intro
  - Indicator: B9.4.1.1.2 (Implementation)
  - Key Topics: Variables, data types, operators, events, control structures, introductory HTML/CSS structure for simple web pages.
  - Deliverable: Sub-strand 1 Exercise Battery (8 Exercises) with 15% Strand 3 review questions.
  - Status: [ ] Not Started
- **Day 30**: Practice Lab: Number Conversions & IDE Playground
  - Step-by-step calculation drills and coding environment setup verification.
  - Status: [ ] Not Started

---

#### Week 7: Algorithms and Robotics (Strand 4 - Part 2)
- **Day 31**: Strand 4, Sub-strand 2 (Part 1) - Algorithm Fundamentals: Sequence, Selection, Iteration
  - Indicator: B9.4.2.1.1
  - Key Topics: Problem decomposition, algorithmic thinking, sequencing instructions, conditional branching (IF-THEN-ELSE), loops/iteration (WHILE, FOR).
  - Status: [ ] Not Started
- **Day 32**: Strand 4, Sub-strand 2 (Part 2) - Real-World Problem Modeling
  - Indicator: B9.4.2.1.1 (Exemplars)
  - Key Topics: Correct procedural algorithms (e.g. multi-step hygienic hand-washing protocol, conditional beverage preparation), algorithmic efficiency and execution speed.
  - Status: [ ] Not Started
- **Day 33**: Strand 4, Sub-strand 2 (Part 3) - Flowcharts and Pseudocode Inter-Translation
  - Indicator: B9.4.2.1.2
  - Key Topics: Standard flowchart symbols (terminator, process, decision, input/output, connector), pseudocode conventions, bidirectional translation (Flowchart <-> Pseudocode).
  - Deliverable: Sub-strand 2 Exercise Battery (8 Exercises) with cumulative review.
  - Status: [ ] Not Started
- **Day 34**: Strand 4, Sub-strand 3 (Part 1) - Foundations of Robotics & Asimov's Laws
  - Indicator: B9.4.3.1.1 (Theory)
  - Key Topics: Robotic systems definition, hardware architecture (actuators, microcontrollers, sensors, power), Isaac Asimov's Three Laws of Robotics and their ethical implications.
  - Status: [ ] Not Started
- **Day 35**: Strand 4, Sub-strand 3 (Part 2) - Robotic Assembly, Simulation, and Programming
  - Indicator: B9.4.3.1.1 (Practical/Simulation)
  - Key Topics: Robot assembly walkthrough, simulator environments (Scratch, Webots, mBlock/mBot, EV3, Lightbot), sensor-driven logic.
  - Deliverable: Sub-strand 3 Exercise Battery + Solutions.
  - Status: [ ] Not Started

---

#### Week 8: Artificial Intelligence & Final Synthesis (Strand 4 - Part 3)
- **Day 36**: Strand 4, Sub-strand 4 (Part 1) - Classical AI and Knowledge-Based Expert Systems
  - Indicator: B9.4.4.1.1 (Expert Systems)
  - Key Topics: Rule-based inference engines, IF-THEN production rules, knowledge bases, query interfaces, domain applications (Telemedicine diagnostic systems).
  - Status: [ ] Not Started
- **Day 37**: Strand 4, Sub-strand 4 (Part 2) - Machine Learning and Sensory Intelligence
  - Indicator: B9.4.4.1.1 (Machine Learning)
  - Key Topics: Supervised learning fundamentals, data collection, training models, Google Teachable Machine practical exploration (image, sound, pose recognition), societal impact and data privacy.
  - Deliverable: Sub-strand 4 Exercise Battery + Solutions.
  - Status: [ ] Not Started
- **Day 38**: Computational Thinking Holistic Review (Strand 4 Consolidation)
  - Algorithmic translation challenges, binary arithmetic speed runs, AI/Robotics conceptual synthesis.
  - Status: [ ] Not Started
- **Day 39**: Comprehensive Mock BECE / Examination Simulation (All Strands 1-4)
  - Part A: 40 Objective Test Questions (balanced across Strands 1-4).
  - Part B: 4 Structured Theory & Problem-Solving Scenarios.
  - Status: [ ] Not Started
- **Day 40**: Final Review, Scoring Analysis, and Remediation Blueprint
  - Complete curriculum mastery audit and final assessment feedback.
  - Status: [ ] Not Started

---

## Detailed Curriculum Mapping & Competencies Reference

| Strand | Sub-strand | Indicator Code | Focus Area | British Standard Terminology & Exemplars |
| :--- | :--- | :--- | :--- | :--- |
| **1. Intro to Computing** | 1. Components | B9.1.1.1.1 | Next-Gen Computing | Quantum computing, Google Sycamore (54 qubits, 53 operational), supercomputers. |
| | | B9.1.1.1.2 | Perceptual Computing | Gesture control, facial recognition, voice processing, natural interaction. |
| | | B9.1.1.1.3 | Output Devices | Wearable displays (e.g. Google Glass), E-Paper displays, E-Readers (Kindle). |
| | | B9.1.1.1.4 | Storage Systems | Cloud storage (Google Drive, OneDrive), smart cards, holographic storage, media servers. |
| | | B9.1.1.2.1 | Personalisation | Desktop icon customization, mouse pointer schemes, visual accessibility. |
| | | B9.1.1.2.2 | File & Driver Management | Device drivers (graphics, sound), plug-and-play installation, driver updates. |
| | 2. Technology in Community | B9.1.2.1.1-3 | Problem Solving | Identifying local challenges, technological intervention design, presentation. |
| | 3. Health & Safety | B9.1.3.1.1-2 | Workstation Ergonomics | Ergonomic keyboards, copy holders, illumination guidelines, thermal mitigation. |
| **2. Productivity Software** | 1. Word Processing | B9.2.1.1.1-3 | Multimedia Documents | Screenshots, screen clippings, Print Screen, SmartArt diagrams, charts, hyperlinks. |
| | 2. Presentation | B9.2.2.1.1-3 | Dynamic Slide Shows | Transition mechanics, object animation order, video/audio embedding, 7-slide deck. |
| | 3. Desktop Publishing | B9.2.3.1.1-3 | Document Critique | Flyers, brochures, business cards, text overflow, peer evaluation rubric. |
| | 4. Spreadsheets | B9.2.4.1.1-3 | Advanced Operations | Fields, records, tables, validation lists, sorting/filtering, templates, macros, pivot tables. |
| **3. Communication Networks**| 1. Computer Networks | B9.3.1.1.1-2 | E-Commerce & E-Learning | Cashless society, mobile money, Bitcoin, QR payments, iBox networks, collaborative docs. |
| | 2. Internet & Social Media | B9.3.2.1.1 | Digital Communication | Social platform dynamics, operational risks, email anatomy (Reply/Forward/BCC). |
| | 3. Information Security | B9.3.3.1.1-2 | Cyber Threats & Defences| Cyberbullying, digital footprint/shadow, 10 hacking techniques (phishing, DoS, etc.). |
| | 4. Web Technologies | B9.3.4.1.1-3 | Web Publishing & Blogs | Blog architecture, purpose, content formulation, publishing and comment moderation. |
| **4. Computational Thinking**| 1. Programming | B9.4.1.1.1-2 | Number Bases & IDEs | Decimal <-> Binary <-> Hexadecimal, binary calculations, IDEs (Scratch, Snap, Python). |
| | 2. Algorithm | B9.4.2.1.1-2 | Algorithmic Design | Sequencing, selection, iteration, flowcharts, pseudocode, bidirectional conversion. |
| | 3. Robotics | B9.4.3.1.1 | Robotic Intelligence | Asimov's 3 Laws of Robotics, components (sensors, actuators), Webots/mBot simulations. |
| | 4. Artificial Intelligence | B9.4.4.1.1 | AI Systems & ML | Expert systems (IF-THEN inference, Telemedicine), Teachable Machine, neural basics. |

---

## Lesson Delivery Guidelines & Pedagogical Protocol

1. **Clarity and Plain English**: Break down technical jargon into accessible, visual analogies before introducing technical definitions.
2. **Strict British English**: Employ UK spelling and grammar across all notes, exercises, and rubrics (e.g. *programme*, *colour*, *visualise*, *organisation*, *modelling*).
3. **Diagrams First**: Every key concept must be paired with either:
   - A clean, monospace text-based diagram that renders reliably across markdown viewers, or
   - A dedicated generated high-fidelity diagram graphic embedded directly into lesson documents and compiled PDFs.
4. **Cumulative Exercise Battery**: Each completed sub-strand concludes with 7 to 10 distinct exercises of 5 questions each (35 to 50 questions total per sub-strand), structured into:
   - Level 1: Conceptual Recall and Terminology
   - Level 2: Real-World Scenarios and Practical Analysis
   - Level 3: Algorithmic / Calculation / Diagnostic Drills
   - Level 4: Cumulative Retention Review (10% to 20% drawn from earlier strands)
   - Comprehensive Answer Keys and Marking Guides provided for every exercise.
5. **PDF Production**: Each finished sub-strand will be compiled into a publication-quality standalone PDF lesson module with full typography, diagrams, and exercises stored in its dedicated strand workspace.
