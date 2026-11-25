# -*- coding: utf-8 -*-
"""
Build the Staralex BECE Computing Mock (Paper 1 & Paper 2) as .docx.

Visual formatting verified against WAEC BECE June 2026 Computing 2&1 scan and the
2024/2025 Super BECE Mock scans:
  - A4 pages, dedicated cover: bordered code box (top-left) + candidate fields (right),
    italic instruction paragraphs, examiner's use grid.
  - Paper 2 (Essay) FIRST: Section A [24 marks] (Q1 compulsory) + Section B [36 marks]
    (three of four, 12 marks each); sub-parts (a)(i)(ii)(iii) alpha ladder;
    printed dotted answer lines; right-aligned '[n marks]' tags.
  - Paper 1 (Objective) LAST: WAEC rubric block + worked example, 40 items x 1 mark,
    two-column newspaper body, A-D options.
  - Header page number, footer exam-code stamp.

Topics: computer generations, quantum computing, file explorer, parts of computer,
hardware & software, use of ICT tools in various fields, keyboard, mouse,
files & folders, file names, word processing.
"""
from __future__ import annotations

import random
import sys
from collections import Counter
from pathlib import Path

from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Pt

TOOLS_DIR = Path(__file__).resolve().parents[4] / "tools"
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

from waec_mock_docx import (  # noqa: E402
    add_paper1_rubric,
    add_runs,
    centered,
    dotted_line,
    dotted_rows as _dotted_rows,
    footer_code,
    line,
    new_waec_doc,
    nil_borders,
    page_break,
    page_number_header,
    render_balanced_objectives,
    render_marking_scheme_p1_key,
    render_marking_scheme_sections,
    right_marks,
    set_cols,
)

OUT = Path(__file__).with_name("Staralex_Computing_Mock_2027_Paper1_and_2.docx")


# ----------------------------------------------------------------------------- essay data
# Uniform structure: a question = (intro_text_or_None, intro_is_part_a, groups)
#   group  = (letter, letter_text_or_None, subs_or_None, leaf_mark_or_None)
#     - subs  = [(tag, marks, text), ...] mapped as (i)(ii)(iii) under the group letter
#     - subs None -> leaf part carrying `leaf_mark` by itself (text in `letter_text`)
ESSAY = [
    # Q1 — compulsory [24]: standalone intro, then lettered groups
    ("Your school's computing laboratory has been furnished with **ten new computers**. The headteacher "
     "has directed the **computing club** to organise the machines and prepare a computerised notice for "
     "the school's Open Day.", False, [
        ("a", "The club has decided to keep all its documents in folders labelled **Executives**, "
              "**Projects** and **Attendance**.",
         [("i", 3, "State the difference between a file and a folder."),
          ("ii", 3, "State two advantages of storing files in folders.")], None),
        ("b", "One of the members saved the notice as **Opn/Day*.docx**.",
         [("i", 2, "State the two characters in the file name that make it invalid under Windows."),
          ("ii", 2, "Suggest a suitable descriptive file name for the notice."),
          ("iii", 2, "State one benefit of giving files descriptive names on a computer.")], None),
        ("c", "The club has finished typing the notice in Microsoft Word.",
         [("i", 2, "Name the alignment that would place the heading exactly in the middle of the page."),
          ("ii", 2, "The club wants to keep a copy of the notice on a removable medium. Name the device "
                    "the members would use."),
          ("iii", 4, "State two ways of taking proper care of the new computers in the laboratory.")], None),
        ("d", None,
         [("i", 2, "Name the Windows tool the members would use to locate the saved notice."),
          ("ii", 2, "State the key combination on the keyboard that opens this tool.")], None),
    ]),
    # Q2 — generations + quantum [12]: intro doubles as part (a)
    ("During the school's **science and technology fair**, Mr Nyarko, an information scientist, set up an "
     "exhibition showing pictures of computers from the time of vacuum tubes to the time of artificial "
     "intelligence. He then gave a short presentation on an emerging technology that solves problems too "
     "difficult for ordinary computers. State the technology found in **each** of the following "
     "generations of computers.", True, [
        ("a", None,
         [("i", 2, "First generation:"),
          ("ii", 2, "Second generation:"),
          ("iii", 2, "Third generation:")], None),
        ("b", "In your own words, explain the term **quantum computing**.", None, 3),
        ("c", "State **two** areas of national life in which quantum computing could be useful.", None, 3),
    ]),
    # Q3 — files & folders [12]
    ("Abena has been saving all her school documents straight on the desktop since B7. Scattered "
     "pictures, music and worksheet files now make it difficult for her to find her work. Describe "
     "**two** problems Abena is likely to face as a result of saving all her documents on the desktop.",
     True, [
        ("a", None,
         [("i", 3, "Problem 1:"),
          ("ii", 3, "Problem 2:")], None),
        ("b", "Abena now wants to arrange her documents by subject.",
         [("i", 2, "Name the container she would create to hold the documents of each subject."),
          ("ii", 2, "State the command she would use to change an already-saved name such as **hw** "
                    "into a more meaningful one."),
          ("iii", 2, "Give a suitable descriptive name for an assignment saved on 5th March, 2026.")], None),
    ]),
    # Q4 — keyboard & mouse + health [12]
    ("During a practical lesson in the laboratory, Miss Dede taught the class how to type without looking "
     "at the keyboard and how to use the mouse correctly.", True, [
        ("a", None,
         [("i", 2, "Name the row of keys on which the fingers rest when touch typing."),
          ("ii", 4, "State the function of each of the following keys: **Enter**; **Backspace**.")], None),
        ("b", "Miss Dede also demonstrated correct use of the mouse and computer health.",
         [("i", 2, "Name the mouse action that displays a menu containing options such as **Copy**, "
                   "**Rename** and **Delete**."),
          ("ii", 4, "State two health practices a pupil should observe when working on the computer "
                    "for a long time.")], None),
    ]),
    # Q5 — ICT tools in fields [12]
    ("The District Education Office held a **career day** during which four professionals spoke to the "
     "pupils about how ICT tools support their work. The professionals were a **nurse**, a **banker**, "
     "a **farmer** and a **broadcaster**. For each of the professionals, state **one** way an ICT tool "
     "is used in his/her work.", True, [
        ("a", None,
         [("i", 2, "Nurse:"),
          ("ii", 2, "Banker:"),
          ("iii", 2, "Farmer:"),
          ("iv", 2, "Broadcaster:")], None),
        ("b", "State **two** features of the computer that make it useful in all the fields above.",
         None, 4),
    ]),
]


def dotted_rows(n, indent=1.5):
    _dotted_rows(doc, n, indent=indent)


SUB_ROWS = {1: 2, 2: 2, 3: 3, 4: 3}


def render_question(num, intro, intro_is_a, groups):
    """Render one essay question: bold number, scenario, lettered groups, dotted
    answer lines, right-aligned group-total mark tags."""
    first_p = line(doc, "", space_before=14, space_after=2)
    r = first_p.add_run(f"{num}.  ")
    r.bold = True
    if intro:
        add_runs(first_p, intro)
    for letter, text, subs, leaf_mark in groups:
        covers = intro_is_a and letter == "a"
        if subs:
            if not covers:
                p = line(doc, "", indent=0.6, space_before=12, space_after=0)
                if text:
                    add_runs(p, f"({letter}) {text}")
                else:
                    p.add_run(f"({letter})")
            for tag, marks, stext in subs:
                p = line(doc, "", indent=1.6, space_before=5, space_after=0)
                add_runs(p, f"({tag}) {stext}")
                dotted_rows(SUB_ROWS.get(marks, 2))
            right_marks(doc, f"[{sum(m for _, m, _ in subs)} marks]")
        else:
            p = line(doc, "", indent=0.6, space_before=12, space_after=0)
            add_runs(p, f"({letter}) {text}")
            dotted_rows(max(2, leaf_mark or 2))
            right_marks(doc, f"[{leaf_mark} marks]" if leaf_mark != 1 else "[1 mark]")

# ----------------------------------------------------------------------------- objectives
# (stem, [correct option, d1, d2, d3]) — correct stored FIRST; balanced shuffle below.
OBJECTIVES = [
    # computer generations (4)
    ("During a computer history lesson, the class was told that the **first** generation computers used "
     "large glass electronic devices to control the flow of electricity. These devices are referred to as",
     ["vacuum tubes", "transistors", "integrated circuits", "microprocessors"]),
    ("Which of the following technologies made the **second** generation of computers smaller and "
     "faster than the first generation?",
     ["transistors", "vacuum tubes", "punched cards", "artificial intelligence"]),
    ("The **third** generation of computers were made with",
     ["integrated circuits", "transistors", "vacuum tubes", "punched cards"]),
    ("One feature of **fifth**-generation computers is their ability to",
     ["understand human language and learn from data", "punch holes into paper cards",
      "use vacuum tubes to process data", "store only numbers"]),
    # quantum computing (3)
    ("In quantum computing, the basic unit of information, which can represent two states at the same "
     "time, is the",
     ["qubit", "byte", "pixel", "nibble"]),
    ("In a technology talk, a guest speaker said that a quantum bit can hold 0 and 1 together at the "
     "same time, whiles an ordinary bit is either 0 or 1. This ability of the quantum bit is referred to as",
     ["superposition", "substitution", "simulation", "synchronisation"]),
    ("Which of the following tasks is a quantum computer most likely to handle better than an "
     "ordinary computer?",
     ["solving extremely difficult scientific problems", "typing a school report",
      "printing class notes", "adding two small numbers"]),
    # file explorer (3)
    ("A pupil wanted to locate, view and manage files and folders on the computer. The correct Windows "
     "tool for the task is",
     ["File Explorer", "Recycle Bin", "Calculator", "Microsoft Store"]),
    ("In a class discussion, the teacher gave the statement: whiles a web browser is used to visit "
     "websites, File Explorer is used to",
     ["manage files and folders", "browse the internet", "play sound tracks", "charge the mouse"]),
    ("In File Explorer, the bar that shows the location (path) of the folder you are currently "
     "working in is the",
     ["address bar", "scroll bar", "status bar", "keyboard layout"]),
    # parts of computer (4)
    ("The part of the computer often described as the **brain** because it carries out all the "
     "processing is the",
     ["central processing unit", "monitor", "keyboard", "speaker"]),
    ("Which of the following is **not** an output device?",
     ["mouse", "monitor", "printer", "speaker"]),
    ("A teacher needed a device for taking the pictures of pupils during an online video lesson. "
     "The appropriate device is the",
     ["webcam", "photocopier", "fax machine", "calculator"]),
    ("Computer devices such as the mouse, trackpad and joystick are referred to as",
     ["pointing devices", "processing devices", "storage devices", "network devices"]),
    # hardware & software (4)
    ("The physical parts of a computer system that can be seen and touched are referred to as",
     ["hardware", "software", "firmware", "liveware"]),
    ("Windows 11, an operating system that controls the computer hardware, is an example of",
     ["system software", "application software", "utility software", "entertainment software"]),
    ("Which of the following items of the computer laboratory is **not** software?",
     ["keyboard", "antivirus", "spreadsheet", "word processor"]),
    ("PowerPoint, a program members of the computing club use to prepare slides, is an example of",
     ["application software", "system software", "hardware", "firmware"]),
    # ICT tools in various fields (4)
    ("Officers at a health centre used computers to keep and retrieve the records of their patients. "
     "This application of ICT in the field of health is referred to as",
     ["e-health", "e-learning", "e-commerce", "e-voting"]),
    ("A customer withdrew money from an ATM machine without meeting the cashier. The application of "
     "ICT shown here is in the field of",
     ["finance", "agriculture", "education", "entertainment"]),
    ("Farmers in a community received messages about the weather on their mobile phones to help them "
     "plan when to plant. The ICT tool used here is the",
     ["mobile phone", "typewriter", "abacus", "television"]),
    ("Which of the following activities shows the use of ICT in the field of education?",
     ["learners watching an interactive science lesson on a projector",
      "bankers reconciling accounts at the counter",
      "farmers weighing sacks of cocoa at the market",
      "drivers checking the oil of a vehicle"]),
    # computer keyboard (4)
    ("The keys F1, F2, F3 up to F12 that are programmed to perform special tasks in applications are "
     "referred to as",
     ["function keys", "arrow keys", "control keys", "navigation keys"]),
    ("A pupil quickly pressed a combination of keys to save the document he was typing in Microsoft "
     "Word. The key combination pressed is",
     ["Ctrl + S", "Ctrl + P", "Ctrl + V", "Ctrl + X"]),
    ("To type the asterisk (*) above the number key 8, the key pressed together with the number key is",
     ["Shift", "Ctrl", "Alt", "Tab"]),
    ("In touch typing, the row of letter keys on which the fingers rest before typing is called the",
     ["home row", "top row", "space row", "number row"]),
    # computer mouse (3)
    ("A user rolled a part of the mouse to move through the pages of a long document without clicking. "
     "The part rolled is the",
     ["scroll wheel", "left button", "right button", "mouse pad"]),
    ("A pupil wanted a menu with options such as **Copy**, **Rename** and **Delete** to appear for a "
     "file on the desktop. The mouse action that would display this menu is the",
     ["right-click", "left-click", "double-click", "drag and drop"]),
    ("The small flat surface on which a computer mouse is moved is called the",
     ["mouse pad", "mouse trap", "track surface", "drive bay"]),
    # files and folders (3)
    ("The container used to group and keep related files together on a computer is the",
     ["folder", "ribbon", "tray", "panel"]),
    ("After saving a project, Abena decided to change the file name from Project1 to MyProject. The "
     "command used to carry out this action is",
     ["Rename", "Delete", "Copy", "Restore"]),
    ("Which of the following statements about a computer folder is **not** true?",
     ["it can be typed into", "it can hold files", "it can hold other folders", "it can be renamed"]),
    # file names (3)
    ("The part of a file name written **after the full stop**, such as docx, which identifies the type "
     "of file, is the",
     ["extension", "caption", "prefix", "label"]),
    ("Which of the following file names gives the best description of the content of the file?",
     ["Computing_Assignment_Term3.docx", "Doc1.docx", "New file.docx", "sdf jkl.docx"]),
    ("A file saved as report.xlsx was most likely created in",
     ["Microsoft Excel", "Microsoft Word", "Microsoft PowerPoint", "Microsoft Paint"]),
    # word processing (5)
    ("While typing the notice of a class monitor, the feature that automatically corrects tehe to the "
     "is",
     ["AutoCorrect", "AutoSum", "AutoFill", "Track Changes"]),
    ("A form master wanted the lines of a notice to line up exactly at both the left and right "
     "margins. The alignment recommended is",
     ["justify", "left", "centre", "right"]),
    ("In Microsoft Word, changing the letters of a document from Times New Roman to Arial changes the",
     ["font face", "font size", "line spacing", "page margin"]),
    ("The command that saves the current document under a different name whiles the original document "
     "remains untouched is",
     ["Save As", "Save", "Print", "Exit"]),
    ("In Microsoft Word, the automatic moving of a word to the next line once the current line is full "
     "is referred to as",
     ["word wrap", "word count", "word art", "word spacing"]),
]

# ----------------------------------------------------------------------------- build
rng = random.Random(20271027)
p1_key: list[tuple[int, str]] = []
doc = new_waec_doc()

# ------------------------------------------------------------------ cover
box = doc.add_table(rows=1, cols=2)
box.alignment = WD_TABLE_ALIGNMENT.CENTER
box.style = "Table Grid"
c_code, c_fields = box.rows[0].cells
c_code.width, c_fields.width = Cm(8.4), Cm(10.6)
nil_borders(c_fields)

code_lines = [
    ("1001026 / 2&1  ·  BECE", False),
    ("OCTOBER 2026  ·  STARALEX MOCK", True),
    ("COMPUTING  2&1", True),
    ("Essay and Objective", False),
    ("2 hours", False),
]
for t, bold in code_lines:
    p = c_code.paragraphs[0] if t == code_lines[0][0] else c_code.add_paragraph()
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run(t)
    r.bold = bold

for i, label in enumerate(["Full Name:", "Index Number:", "Signature:", "Date of Examination:"]):
    p = c_fields.paragraphs[0] if i == 0 else c_fields.add_paragraph()
    p.paragraph_format.space_after = Pt(8)
    r = p.add_run(label + "  " + "." * (34 - len(label)))
    r.font.size = Pt(11)

line(doc, "", space_after=6)
centered(doc, "STARALEX SCHOOL STUDIES", space_after=2)
centered(doc, "Basic Education Certificate Mock Examination", space_after=10)

centered(doc, "INSTRUCTIONS TO CANDIDATES", space_before=18, space_after=4)
line(doc, "**Do not** open this booklet until you are told to do so. While you are waiting, read and "
          "observe the following instructions carefully.", italic=True, space_after=6)
line(doc, "Write your **name**, **index number** and **date of examination** in **ink** in the spaces "
          "provided above.", italic=True, space_after=6)
line(doc, "This booklet consists of **two papers**. Answer **Paper 2, which comes first**, in "
          "**this booklet** in the spaces provided and **Paper 1** on your Objective Test answer "
          "sheet. **Paper 2** will last **1 hour 15 minutes** after which it will be collected. "
          "**Do not start Paper 1** until you are told to do so. **Paper 1** will last **45 minutes**.",
     italic=True, space_after=6)
line(doc, "Any candidate who tears off **any** part of this question paper will be severely penalized.",
     italic=True, space_after=6)
line(doc, "Whether you answer all the questions in this paper or not, hand in the **entire** question "
          "paper to the invigilator.", italic=True, space_after=6)

# examiner grid (For Examiner's Use Only)
ex = doc.add_table(rows=3, cols=2)
ex.alignment = WD_TABLE_ALIGNMENT.CENTER
ex.style = "Table Grid"
hdr = ex.rows[0].cells
hdr[0].merge(hdr[1]).paragraphs[0].add_run("For Examiner's Use Only").bold = True
ex.rows[1].cells[0].paragraphs[0].add_run("Question Number").bold = True
ex.rows[1].cells[1].paragraphs[0].add_run("Mark").bold = True
ex.rows[2].cells[0].paragraphs[0].add_run("TOTAL").bold = True
ex.rows[1].height = Cm(4.5)   # empty writing space, like the real grid
for row in ex.rows:
    for cell in row.cells:
        cell.width = Cm(6.0)
        for p in cell.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER

# ------------------------------------------------------------------ PAPER 2
centered(doc, "PAPER 2", space_before=20, space_after=0, size=13)
centered(doc, "ESSAY  ·  [60 MARKS]  ·  1 HOUR 15 MINUTES", space_after=8)
line(doc, "**SECTION A  [24 MARKS]**", space_after=2)
line(doc, "Answer **Question 1** [Compulsory].", italic=True, space_after=8)


for q_idx, (intro, intro_is_a, groups) in enumerate(ESSAY, start=1):
    if q_idx == 2:
        centered(doc, "SECTION B  [36 MARKS]", space_before=18, space_after=0)
        line(doc, "Answer **three** questions only from this section.", italic=True, space_after=4)
    render_question(q_idx, intro, intro_is_a, groups)

centered(doc, "END OF SECTION B", bold=True, space_before=16)

# ------------------------------------------------------------------ PAPER 1
add_paper1_rubric(
    doc,
    duration_label="45 MINUTES",
    sample_stem="Which of the following is an example of an input device?",
    sample_options="A. Monitor       B. Printer       C. Keyboard       D. Speaker",
    sample_explanation="The correct answer is **Keyboard**, which is lettered **C**, and therefore answer space **C** would be shaded.",
)
render_balanced_objectives(doc, OBJECTIVES, rng, p1_key)

# ------------------------------------------------------------------ header / footer codes
# Written ONCE on the first section — all later sections inherit (linked), so no
# duplicate header/footer parts are created.
page_number_header(doc.sections[0])
footer_code(doc.sections[0])

# ------------------------------------------------------------------ MARKING SCHEME
page_break(doc)
sect_ms = doc.add_section(WD_SECTION.CONTINUOUS)
set_cols(sect_ms, 1)

centered(doc, "MARKING SCHEME — FOR TEACHERS / INVIGILATORS ONLY", space_after=2)
centered(doc, "STARALEX BECE COMPUTING MOCK, OCTOBER 2026", space_after=10)

render_marking_scheme_p1_key(doc, p1_key)

line(doc, "", space_after=8)
centered(doc, "PAPER 2 — ESSAY (Question 1 + any three of Questions 2–5 = 60 marks)", space_after=6)
scheme = [
    ("Question 1 (24 marks)", [
        "1(a)(i) A file is a single saved document/data item, while a folder is a container that holds related files — 3 marks",
        "1(a)(ii) Any two @ 2 or 1 marks each: keeps related files together; makes files easy to find; prevents accidental loss or misplacement of files — 3 marks",
        "1(b)(i) The slash ( / ) and the asterisk ( * ) — 1 mark each",
        "1(b)(ii) e.g. Open_Day_Notice_2026.docx (must not contain / or *) — 2 marks",
        "1(b)(iii) Any one @ 2 marks: easy identification; quick searching; shows the content of the file at a glance",
        "1(c)(i) Centre alignment — 2 marks",
        "1(c)(ii) USB flash drive (pen drive) / external storage device — 2 marks",
        "1(c)(iii) Any two @ 2 marks each: cover the computers from dust; keep food and drinks away from the lab; use a surge protector/UPS; shut down the computers properly after use",
        "1(d)(i) File Explorer — 2 marks",
        "1(d)(ii) Windows logo key + E — 2 marks",
    ]),
    ("Question 2 (12 marks)", [
        "2(a)(i) Vacuum tubes — 2 marks",
        "2(a)(ii) Transistors — 2 marks",
        "2(a)(iii) Integrated circuits — 2 marks",
        "2(b) Quantum computing is a type of computing that uses quantum bits (qubits), which can represent 0 and 1 at the same time (superposition), to solve very complex problems extremely fast — 3 marks",
        "2(c) Any two @ 1 or 2 marks: drug discovery and medicine; secure communication and data encryption; weather and climate modelling; financial modelling; advanced scientific research — 3 marks",
    ]),
    ("Question 3 (12 marks)", [
        "3(a) Any two @ 3 marks: files pile up and it becomes difficult to find a particular file; the system slows down; risk of accidentally deleting needed files; files get mixed up without order",
        "3(b)(i) A folder — 2 marks",
        "3(b)(ii) Rename (right-click and choose Rename, or press F2) — 2 marks",
        "3(b)(iii) e.g. Computing_Assignment_05_03_2026 — 2 marks (descriptive name with subject/topic and/or date)",
    ]),
    ("Question 4 (12 marks)", [
        "4(a)(i) The home row — 2 marks",
        "4(a)(ii) Enter: confirms an entry, sends a command or starts a new line — 2 marks; Backspace: deletes the character before the cursor — 2 marks",
        "4(b)(i) Right-click — 2 marks",
        "4(b)(ii) Any two @ 2 marks each: take short breaks from the screen; do simple eye exercises/look away from the screen; maintain proper sitting posture; adjust screen brightness to a comfortable level",
    ]),
    ("Question 5 (12 marks)", [
        "5(a)(i) Nurse — any one @ 2 marks: uses computers to store patient records; telemedicine; monitors vital signs",
        "5(a)(ii) Banker — any one @ 2 marks: ATM and online banking; keeps and processes customer accounts",
        "5(a)(iii) Farmer — any one @ 2 marks: receives weather and market price information on mobile phones; uses drones to monitor crops",
        "5(a)(iv) Broadcaster — any one @ 2 marks: edits audio and video on computers; streams programmes online",
        "5(b) Any two @ 2 marks each: speed; accuracy; large storage capacity; reliability; can work for long hours without getting tired",
    ]),
]
render_marking_scheme_sections(doc, scheme)

doc.save(OUT)
print("saved:", OUT)
print("Paper 1 key:", " ".join(f"{n}{k}" for n, k in p1_key))
print("key counts:", Counter(k for _, k in p1_key))
