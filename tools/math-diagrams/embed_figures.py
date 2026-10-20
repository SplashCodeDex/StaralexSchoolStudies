"""Insert TikZ figure embeds into lesson markdowns at the right concept anchors."""
from pathlib import Path

ROOT = Path(r"W:\StaralexSchoolStudies")
G9 = ROOT / "Grade9-Maths"

# (lesson_path_relative_to_G9, anchor_line_contains, image_md)
INSERTS = [
    (
        "Strand-1-Number/Substrand-1-Numeration-Systems/Lesson-01-Place-Value-And-Standard-Form/Lesson_01_Place_Value_and_Standard_Form.md",
        "### 3.1 The place-value chart",
        "\n![Figure 1: Place-value chart for a large number](diagrams/place_value_chart.png)\n",
    ),
    (
        "Strand-1-Number/Substrand-1-Numeration-Systems/Lesson-02-Number-Systems-And-Venn-Diagrams/Lesson_02_Number_Systems_and_Venn_Diagrams.md",
        "### 5.2 Two-set Venn diagram layout",
        "\n![Figure 1: Two-set Venn diagram in a universal set U](diagrams/venn_2set.png)\n",
    ),
    (
        "Strand-1-Number/Substrand-1-Numeration-Systems/Lesson-02-Number-Systems-And-Venn-Diagrams/Lesson_02_Number_Systems_and_Venn_Diagrams.md",
        "If we add a third set C",
        "\n![Figure 2: Three-set Venn diagram — fill from the centre outwards](diagrams/venn_3set.png)\n",
    ),
    (
        "Strand-1-Number/Substrand-1-Numeration-Systems/Lesson-02-Number-Systems-And-Venn-Diagrams/Lesson_02_Number_Systems_and_Venn_Diagrams.md",
        "### 5.1 What a Venn diagram does",
        "\n![Figure 0: Real number system hierarchy](diagrams/number_system_hierarchy.png)\n",
    ),
    (
        "Strand-2-Algebra/Substrand-1-Patterns-And-Relations/Lesson-01-Linear-Relations-And-Gradient/Lesson_01_Linear_Relations_and_Gradient.md",
        "gradient",
        "\n![Figure 1: Gradient as rise over run on Cartesian axes](diagrams/linear_graph_gradient.png)\n",
    ),
    (
        "Strand-2-Algebra/Substrand-2-Algebraic-Expressions/Lesson-01-Algebraic-Expressions-And-Modelling/Lesson_01_Algebraic_Expressions_and_Modelling.md",
        "### Example 8 — Length from diagram (Mock P1 Q17)",
        "\n![Figure 1: Rectangle length from a diagram (Mock P1 Q17)](diagrams/algebra_length_from_diagram.png)\n",
    ),
    (
        "Strand-2-Algebra/Substrand-3-Variables-And-Equations/Lesson-01-Equations-And-Inequalities/Lesson_01_Equations_and_Inequalities.md",
        "$1 < x \\le 5$ on a number line",
        "\n![Figure 3: Solution of 1 < x ≤ 5 on a number line](diagrams/number_line_double_inequality_1_5.png)\n",
    ),
    (
        "Strand-3-Geometry-And-Measurement/Substrand-1-Shapes-And-Space/Lesson-03-Angles-Parallel-Lines-And-Trigonometry/Lesson_03_Angles_Parallel_Lines_and_Trigonometry.md",
        "### 3.5 Isosceles triangle (Mock P1 Q27)",
        "\n![Figure 1: Isosceles △XYZ with XY = YZ and vertex angle 42°](diagrams/isosceles_triangle_xyz_42.png)\n",
    ),
    (
        "Strand-3-Geometry-And-Measurement/Substrand-1-Shapes-And-Space/Lesson-03-Angles-Parallel-Lines-And-Trigonometry/Lesson_03_Angles_Parallel_Lines_and_Trigonometry.md",
        "**Mock P1 Q30:**",
        "\n![Figure 2: Alternate angles in the Z-configuration (Mock P1 Q30)](diagrams/parallel_lines_alternate_mon_pmo.png)\n",
    ),
    (
        "Strand-3-Geometry-And-Measurement/Substrand-1-Shapes-And-Space/Lesson-03-Angles-Parallel-Lines-And-Trigonometry/Lesson_03_Angles_Parallel_Lines_and_Trigonometry.md",
        "**Mock P1 Q31:**",
        "\n![Figure 3: Find ∠MON from the given 57° and 105° (Mock P1 Q31)](diagrams/parallel_lines_find_mon_57_105.png)\n",
    ),
    (
        "Strand-3-Geometry-And-Measurement/Substrand-1-Shapes-And-Space/Lesson-03-Angles-Parallel-Lines-And-Trigonometry/Lesson_03_Angles_Parallel_Lines_and_Trigonometry.md",
        "**Mock P2 Q3(b):**",
        "\n![Figure 4: Right triangle QPR, QR = 6 cm, PR = 8 cm (Mock P2 Q3b)](diagrams/right_triangle_qpr_6_8.png)\n",
    ),
    (
        "Strand-3-Geometry-And-Measurement/Substrand-2-Measurement-And-Vectors/Lesson-01-Measurement-Circles-And-Scale/Lesson_01_Measurement_Circles_and_Scale.md",
        "### Example 4 — Circumference from radius",
        "\n![Figure 1: Circle with centre O, radius r and diameter d](diagrams/circle_radius_diameter.png)\n",
    ),
    (
        "Strand-3-Geometry-And-Measurement/Substrand-2-Measurement-And-Vectors/Lesson-01-Measurement-Circles-And-Scale/Lesson_01_Measurement_Circles_and_Scale.md",
        "**Mock P2 Q3(d):**",
        "\n![Figure 2: Semicircle with radius 7 cm](diagrams/semicircle_r7.png)\n",
    ),
    (
        "Strand-3-Geometry-And-Measurement/Substrand-2-Measurement-And-Vectors/Lesson-01-Measurement-Circles-And-Scale/Lesson_01_Measurement_Circles_and_Scale.md",
        "1. **[Mock 2026 P1 Q24]**",
        "\n![Figure 3: Scale drawing — a 20 m hall drawn as 10 cm](diagrams/scale_drawing_20m_10cm.png)\n",
    ),
    (
        "Strand-3-Geometry-And-Measurement/Substrand-2-Measurement-And-Vectors/Lesson-02-Vectors/Lesson_02_Vectors.md",
        "### Example 5 — Position vector",
        "\n![Figure 1: Position vector of P(4, 3)](diagrams/vector_position_op.png)\n",
    ),
    (
        "Strand-3-Geometry-And-Measurement/Substrand-2-Measurement-And-Vectors/Lesson-02-Vectors/Lesson_02_Vectors.md",
        "### Example 6 — Add vectors",
        "\n![Figure 2: Triangle law of vector addition](diagrams/vector_triangle_law.png)\n",
    ),
    (
        "Strand-4-Handling-Data/Substrand-1-Data-And-Statistics/Lesson-01-Data-Statistics-And-Representations/Lesson_01_Data_Statistics_and_Representations.md",
        "Split each number into a **stem**",
        "\n![Figure 1: Stem-and-leaf plot of examination marks](diagrams/stem_and_leaf_marks.png)\n",
    ),
    (
        "Strand-4-Handling-Data/Substrand-1-Data-And-Statistics/Lesson-01-Data-Statistics-And-Representations/Lesson_01_Data_Statistics_and_Representations.md",
        "(i) Draw a pie chart for the data.",
        "\n![Figure 2: Pie chart of monthly salary spending](diagrams/pie_chart_salary.png)\n",
    ),
    (
        "Strand-4-Handling-Data/Substrand-2-Chance-And-Probability/Lesson-01-Probability/Lesson_01_Probability.md",
        "tree",
        "\n![Figure 1: Two-stage probability tree (without replacement)](diagrams/probability_tree_two_stage.png)\n",
    ),
]


def main() -> None:
    for rel, anchor, img in INSERTS:
        path = G9 / rel
        if not path.exists():
            print(f"MISSING lesson: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        if img.strip() in text:
            print(f"already: {path.name} :: {img.split('/')[-1][:40]}")
            continue
        idx = text.find(anchor)
        if idx < 0:
            print(f"ANCHOR NOT FOUND: {path.name} :: {anchor[:50]}")
            continue
        # insert after the anchor line
        line_end = text.find("\n", idx)
        if line_end < 0:
            line_end = len(text)
        new = text[: line_end + 1] + img + text[line_end + 1 :]
        path.write_text(new, encoding="utf-8")
        print(f"inserted into {path.name} after {anchor[:40]!r}")


if __name__ == "__main__":
    main()
