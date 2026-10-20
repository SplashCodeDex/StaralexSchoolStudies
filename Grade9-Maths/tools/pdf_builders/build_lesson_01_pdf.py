import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_header_footer(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_header_footer(self, page_count):
        self.saveState()
        self.setFont('Helvetica', 8)
        self.setFillColor(colors.HexColor('#4B5563'))
        
        # Header (Pages 2+)
        if self._pageNumber > 1:
            self.drawString(36, 806, "Grade 9 Mathematics | Strand 3: Geometry & Measurement")
            self.drawRightString(559, 806, "Sub-strand 1: Shapes and Space (Lesson 1)")
            self.setStrokeColor(colors.HexColor('#D1D5DB'))
            self.setLineWidth(0.5)
            self.line(36, 800, 559, 800)
            
        # Footer (All pages)
        self.setStrokeColor(colors.HexColor('#D1D5DB'))
        self.setLineWidth(0.5)
        self.line(36, 42, 559, 42)
        self.drawString(36, 30, "Lesson 1: Polygons, Angle Properties and Angle Formulas")
        self.drawRightString(559, 30, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()

def build_pdf():
    base_dir = r"W:\StaralexSchoolStudies\Grade9-Maths\Strand-3-Geometry-And-Measurement\Substrand-1-Shapes-And-Space\Lesson-01-Polygons-And-Angle-Properties"
    pdf_path = os.path.join(base_dir, "Lesson_01_Polygons_and_Angle_Properties.pdf")
    
    # Page setup: A4 with 0.5 in (36pt) margins
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=46,
        bottomMargin=46
    )
    
    styles = getSampleStyleSheet()
    
    # Custom typographical hierarchy (clean, modern, no gradients/glow)
    primary_color = colors.HexColor('#1E3A8A')  # British educational deep navy
    dark_neutral = colors.HexColor('#111827')
    body_neutral = colors.HexColor('#374151')
    accent_box = colors.HexColor('#F3F4F6')
    border_color = colors.HexColor('#D1D5DB')
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=primary_color,
        spaceAfter=4
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#4B5563'),
        spaceAfter=10
    )
    
    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=primary_color,
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )
    
    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=dark_neutral,
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12.5,
        textColor=body_neutral,
        spaceAfter=5
    )
    
    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12.5,
        textColor=body_neutral,
        leftIndent=15,
        spaceAfter=3
    )
    
    math_callout_style = ParagraphStyle(
        'MathCallout',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13.5,
        textColor=primary_color
    )
    
    caption_style = ParagraphStyle(
        'CaptionStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8,
        leading=10,
        alignment=1, # Center
        textColor=colors.HexColor('#4B5563'),
        spaceAfter=8
    )

    story = []
    
    # Document Header Banner
    header_data = [
        [
            Paragraph("<b>MINISTRY OF EDUCATION & NACCA STANDARDS — GRADE 9 MATHEMATICS</b>", subtitle_style),
            Paragraph("<b>BRITISH CURRICULUM</b>", ParagraphStyle('RSub', parent=subtitle_style, alignment=2))
        ],
        [
            Paragraph("<b>Strand 3: Geometry and Measurement</b><br/><b>Sub-strand 1: Shapes and Space</b>", title_style),
            Paragraph("<b>Content Standard: B9.3.1.1</b><br/><b>Indicator: B9.3.1.1.1</b>", ParagraphStyle('RCur', parent=body_style, alignment=2))
        ]
    ]
    header_table = Table(header_data, colWidths=[360, 163])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(header_table)
    story.append(HRFlowable(width="100%", thickness=1.5, color=primary_color, spaceAfter=8, spaceBefore=4))
    
    # Overview Box
    meta_box = [
        [Paragraph("<b>Lesson Topic:</b> Polygons, Angle Properties, and the Derivation of Angle Formulas<br/>"
                   "<b>Core Mandate:</b> First-principles derivation, geometric proofs, diagrammatic modeling, and algebraic solutions.", body_style)]
    ]
    t_meta = Table(meta_box, colWidths=[523])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), accent_box),
        ('BOX', (0,0), (-1,-1), 0.5, border_color),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 8))
    
    # 1. Theoretical Foundations
    story.append(Paragraph("1. Conceptual Foundations and Terminology Breakdown", h1_style))
    story.append(Paragraph(
        "To build genuine geometric intuition, we examine terms from their mathematical origins. "
        "The word <b>polygon</b> stems from Greek <i>polus</i> ('many') and <i>gonia</i> ('angle/corner'). "
        "A polygon is a closed two-dimensional plane figure bounded strictly by straight line segments joined consecutively end-to-end. "
        "The bounding line segments are called <b>sides</b> or <b>edges</b>, and the sharp meeting points are called <b>vertices</b> (singular: <i>vertex</i>).",
        body_style
    ))
    
    story.append(Paragraph("Convex vs Concave Polygons:", h2_style))
    story.append(Paragraph("• <b>Convex Polygon:</b> Every interior angle measures strictly less than 180°. Every vertex points outward. Any straight line drawn between any two points inside the polygon lies entirely inside the figure. <i>All standard syllabus theorems apply to convex polygons.</i>", bullet_style))
    story.append(Paragraph("• <b>Concave Polygon:</b> Contains at least one reflex interior angle (between 180° and 360°), forming an internal 'cave' where at least one vertex points inward.", bullet_style))
    
    story.append(Paragraph("Regular vs Irregular Polygons:", h2_style))
    story.append(Paragraph("• <b>Regular Polygon:</b> A polygon that is simultaneously <b>equilateral</b> (all sides of equal length) and <b>equiangular</b> (all interior angles of equal magnitude), such as an equilateral triangle or square.", bullet_style))
    story.append(Paragraph("• <b>Irregular Polygon:</b> A polygon whose sides and/or interior angles vary in measure.", bullet_style))
    
    # Nomenclature Table
    story.append(Paragraph("Systematic Polygon Nomenclature (3 to 12 Sides):", h2_style))
    nom_data = [
        ["Sides (n)", "Name of Polygon", "Number of Diagonals (n - 3)", "Number of Triangles (n - 2)", "Interior Angle Sum"],
        ["3", "Triangle (Trigon)", "0", "1", "180°"],
        ["4", "Quadrilateral (Tetragon)", "1", "2", "360°"],
        ["5", "Pentagon", "2", "3", "540°"],
        ["6", "Hexagon", "3", "4", "720°"],
        ["7", "Heptagon (Septagon)", "4", "5", "900°"],
        ["8", "Octagon", "5", "6", "1080°"],
        ["9", "Nonagon (Enneagon)", "6", "7", "1260°"],
        ["10", "Decagon", "7", "8", "1440°"],
        ["11", "Undecagon (Hendecagon)", "8", "9", "1620°"],
        ["12", "Dodecagon", "9", "10", "1800°"],
        ["n", "n-gon", "n - 3", "n - 2", "(n - 2) × 180°"]
    ]
    t_nom = Table(nom_data, colWidths=[60, 140, 115, 110, 98])
    t_nom.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1F2937')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('ALIGN', (1,1), (1,-1), 'LEFT'),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F9FAFB')]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_nom)
    story.append(Spacer(1, 10))
    
    # 2. First-Principles Derivations
    story.append(Paragraph("2. First-Principles Derivations of Geometric Angle Formulas", h1_style))
    story.append(Paragraph(
        "Rather than accepting formulas without proof, we use the geometric principle of <b>triangulation</b>. "
        "From any single anchor vertex A in a convex polygon of n sides, we draw straight diagonals to all other non-adjacent vertices.",
        body_style
    ))
    
    proof_img_path = os.path.join(base_dir, "diagrams", "polygon_triangulation_proof.png")
    if os.path.exists(proof_img_path):
        img_table = Table([[
            Image(proof_img_path, width=170, height=170),
            Paragraph(
                "<b>The Triangulation Proof:</b><br/><br/>"
                "1. From anchor vertex A, you cannot draw diagonals to A itself or to its 2 adjacent neighbor vertices (which are exterior sides).<br/>"
                "&nbsp;&nbsp;&nbsp;<b>Diagonals from 1 vertex = n - 3</b><br/><br/>"
                "2. These diagonals divide the polygon into non-overlapping triangles:<br/>"
                "&nbsp;&nbsp;&nbsp;<b>Number of triangles = (n - 3) + 1 = n - 2</b><br/><br/>"
                "3. Each triangle possesses an angle sum of exactly 180°. Hence:<br/>"
                "&nbsp;&nbsp;&nbsp;<b>Sum of Interior Angles S = (n - 2) × 180°</b><br/><br/>"
                "4. For a regular polygon (equal angles):<br/>"
                "&nbsp;&nbsp;&nbsp;<b>Each Interior Angle = [(n - 2) × 180°] / n</b>",
                body_style
            )
        ]], colWidths=[180, 343])
        img_table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('BACKGROUND', (0,0), (-1,-1), accent_box),
            ('BOX', (0,0), (-1,-1), 0.5, border_color),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ]))
        story.append(img_table)
        story.append(Paragraph("Figure 1.1: Triangulation Proof of the Interior Angle Sum Theorem (Pentagon n = 5, n - 2 = 3 triangles).", caption_style))
    story.append(Spacer(1, 6))

    # 3. Exterior Angles & Linear Pair
    story.append(Paragraph("3. Exterior Angles and the Perimeter Tour Theorem", h1_style))
    story.append(Paragraph(
        "An <b>exterior angle</b> is formed when any side of a polygon is extended past a vertex. "
        "Because the interior angle and exterior angle sit together on a straight line, they form a linear pair.",
        body_style
    ))
    
    ext_img_path = os.path.join(base_dir, "diagrams", "polygon_exterior_angle_concept.png")
    if os.path.exists(ext_img_path):
        ext_table = Table([[
            Image(ext_img_path, width=160, height=160),
            Paragraph(
                "<b>Key Exterior Angle Theorems:</b><br/><br/>"
                "<b>1. Linear Pair Identity:</b><br/>"
                "&nbsp;&nbsp;&nbsp;<b>Interior Angle + Exterior Angle = 180°</b><br/><br/>"
                "<b>2. Exterior Angle Sum Theorem:</b><br/>"
                "For <i>any</i> convex polygon with n sides:<br/>"
                "&nbsp;&nbsp;&nbsp;<b>Sum of all Exterior Angles = 360°</b><br/>"
                "<i>Physical Intuition:</i> Walking around any closed perimeter makes one complete 360° revolution.<br/><br/>"
                "<b>3. Regular Polygon Dimensions:</b><br/>"
                "&nbsp;&nbsp;&nbsp;<b>Each Exterior Angle = 360° / n</b><br/>"
                "&nbsp;&nbsp;&nbsp;<b>Number of Sides n = 360° / (Exterior Angle)</b>",
                body_style
            )
        ]], colWidths=[170, 353])
        ext_table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('BACKGROUND', (0,0), (-1,-1), accent_box),
            ('BOX', (0,0), (-1,-1), 0.5, border_color),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ]))
        story.append(ext_table)
        story.append(Paragraph("Figure 1.2: The Linear Pair Theorem and Exterior Angle Relationships.", caption_style))
    story.append(Spacer(1, 8))

    # 4. Curriculum Exemplars
    story.append(Paragraph("4. Step-by-Step Curriculum Exemplars (from NaCCA Syllabus)", h1_style))
    
    # Exemplar 1: Hexagon Problem
    hex_img_path = os.path.join(base_dir, "diagrams", "hexagon_angles_diagram.png")
    hex_content = [
        Paragraph("<b>Exemplar 1: Irregular Hexagon Algebraic Angle Problem (PDF Page 34)</b>", h2_style),
        Paragraph("<b>Problem:</b> An irregular convex hexagon has interior angles: 120°, (5x - 6)°, (4x + 14)°, 7x°, (8x - 8)°, and 6x°. Find x and all six angles.", body_style)
    ]
    if os.path.exists(hex_img_path):
        hex_tbl = Table([[
            Image(hex_img_path, width=165, height=165),
            Paragraph(
                "<b>Worked Solution:</b><br/>"
                "1. Theoretical sum for hexagon (n = 6):<br/>"
                "&nbsp;&nbsp;&nbsp;S = (6 - 2) × 180° = 4 × 180° = <b>720°</b><br/>"
                "2. Algebraic equation:<br/>"
                "&nbsp;&nbsp;&nbsp;120 + (5x - 6) + (4x + 14) + 7x + (8x - 8) + 6x = 720<br/>"
                "3. Group variable and constant terms:<br/>"
                "&nbsp;&nbsp;&nbsp;(5x + 4x + 7x + 8x + 6x) + (120 - 6 + 14 - 8) = 720<br/>"
                "&nbsp;&nbsp;&nbsp;30x + 120 = 720 ⇒ 30x = 600 ⇒ <b>x = 20</b><br/>"
                "4. Individual angles:<br/>"
                "&nbsp;&nbsp;&nbsp;• 120°<br/>"
                "&nbsp;&nbsp;&nbsp;• 5(20) - 6 = <b>94°</b><br/>"
                "&nbsp;&nbsp;&nbsp;• 4(20) + 14 = <b>94°</b><br/>"
                "&nbsp;&nbsp;&nbsp;• 7(20) = <b>140°</b><br/>"
                "&nbsp;&nbsp;&nbsp;• 8(20) - 8 = <b>152°</b><br/>"
                "&nbsp;&nbsp;&nbsp;• 6(20) = <b>120°</b><br/>"
                "<i>Verification:</i> 120 + 94 + 94 + 140 + 152 + 120 = 720° (Exact match).",
                body_style
            )
        ]], colWidths=[175, 348])
        hex_tbl.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFFFFF')),
            ('BOX', (0,0), (-1,-1), 0.5, border_color),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ]))
        hex_content.append(hex_tbl)
        hex_content.append(Paragraph("Figure 1.3: Geometric Schema for Exemplar 1 (Irregular Hexagon Angles).", caption_style))
    story.append(KeepTogether(hex_content))
    story.append(Spacer(1, 8))

    # Exemplar 2: Triangle Exterior Angle
    tri_img_path = os.path.join(base_dir, "diagrams", "triangle_exterior_angle_diagram.png")
    tri_content = [
        Paragraph("<b>Exemplar 2: Triangle Remote Exterior Angle Theorem (PDF Page 34)</b>", h2_style),
        Paragraph("<b>Problem:</b> In triangle ABC, angle A = 25°, angle B = (x + 15)°, and remote exterior angle ACD = (3x - 10)°. Solve for x and all angles.", body_style)
    ]
    if os.path.exists(tri_img_path):
        tri_tbl = Table([[
            Image(tri_img_path, width=155, height=155),
            Paragraph(
                "<b>Worked Solution:</b><br/>"
                "1. <b>Theorem:</b> The exterior angle of a triangle equals the sum of its two remote interior angles.<br/>"
                "&nbsp;&nbsp;&nbsp;Angle ACD = Angle A + Angle B<br/>"
                "2. Algebraic equation:<br/>"
                "&nbsp;&nbsp;&nbsp;3x - 10 = 25 + (x + 15)<br/>"
                "&nbsp;&nbsp;&nbsp;3x - 10 = x + 40<br/>"
                "3. Solve for x:<br/>"
                "&nbsp;&nbsp;&nbsp;3x - x = 40 + 10 ⇒ 2x = 50 ⇒ <b>x = 25</b><br/>"
                "4. Calculate angle magnitudes:<br/>"
                "&nbsp;&nbsp;&nbsp;• Angle A = 25°<br/>"
                "&nbsp;&nbsp;&nbsp;• Angle B = 25 + 15 = <b>40°</b><br/>"
                "&nbsp;&nbsp;&nbsp;• Exterior Angle ACD = 3(25) - 10 = <b>65°</b><br/>"
                "&nbsp;&nbsp;&nbsp;• Interior Angle ACB = 180° - 65° = <b>115°</b><br/>"
                "<i>Verification:</i> 25° + 40° + 115° = 180° (Triangle sum confirmed).",
                body_style
            )
        ]], colWidths=[165, 358])
        tri_tbl.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFFFFF')),
            ('BOX', (0,0), (-1,-1), 0.5, border_color),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ]))
        tri_content.append(tri_tbl)
        tri_content.append(Paragraph("Figure 1.4: Triangle Exterior Angle Relationship Schema.", caption_style))
    story.append(KeepTogether(tri_content))
    story.append(Spacer(1, 10))

    # 5. Exercises Section (40 Questions across 8 sets)
    story.append(Paragraph("5. Practice Exercises (40 Questions across 8 Sets)", h1_style))
    story.append(Paragraph("Complete these 8 structured exercise sets to achieve master fluency in polygon geometry.", body_style))
    
    exercises_data = [
        ("Exercise 1: Nomenclature & Diagonal Triangulation", [
            "1. State the formal geometric names of polygons with: (a) 7 sides, (b) 9 sides, (c) 10 sides, (d) 11 sides, (e) 12 sides.",
            "2. How many diagonals can be drawn from a single vertex of: (a) a hexagon, (b) a nonagon, (c) a 16-gon?",
            "3. How many non-overlapping triangles are formed by diagonals from one vertex of: (a) an octagon, (b) an undecagon, (c) a 20-gon?",
            "4. A student counts 9 diagonals originating from a single vertex of a polygon. How many sides does this polygon have?",
            "5. A polygon is partitioned into 11 triangles by diagonals from one vertex. State its number of sides and formal geometric name."
        ]),
        ("Exercise 2: Sum of Interior Angles of Polygons", [
            "1. Calculate the total sum of interior angles for: (a) a heptagon, (b) an octagon, (c) a decagon.",
            "2. Determine the sum of the interior angles of a 14-sided polygon.",
            "3. The sum of the interior angles of a polygon is 1980°. How many sides does it have?",
            "4. Is it mathematically possible for a convex polygon to have an interior angle sum of 2400°? Justify rigorously.",
            "5. Three angles of a pentagon are 100°, 110°, and 125°. If the remaining two angles are equal, find the size of each remaining angle."
        ]),
        ("Exercise 3: Regular Polygons — Interior & Exterior Angles", [
            "1. Find the measure of each interior angle and each exterior angle of a regular octagon.",
            "2. Find the measure of each interior angle and each exterior angle of a regular decagon.",
            "3. Calculate the size of each exterior angle of a regular dodecagon (n = 12).",
            "4. What is the measure of each interior angle of a regular polygon with 18 sides?",
            "5. The ratio of an interior angle to an exterior angle of a regular polygon is 5 : 1. Determine both angle values."
        ]),
        ("Exercise 4: Reverse Problems — Finding the Number of Sides (n)", [
            "1. Each exterior angle of a regular polygon measures 30°. How many sides does it have?",
            "2. Each interior angle of a regular polygon is 140°. Determine its number of sides.",
            "3. Each interior angle of a regular polygon is 165°. Calculate its number of sides.",
            "4. The exterior angle of a regular polygon is 18°. What is the specific geometric name of this polygon?",
            "5. The sum of the interior angles of a regular polygon is four times the sum of its exterior angles. Find n."
        ]),
        ("Exercise 5: Solving for Variables in Irregular Polygons", [
            "1. The angles of a quadrilateral are x°, (2x + 10)°, (3x - 20)°, and (4x + 10)°. Find x and the largest angle.",
            "2. The interior angles of a pentagon are x°, (x + 20)°, (x + 40)°, (x + 60)°, and (x + 80)°. Determine x and all five angles.",
            "3. An irregular hexagon has five angles measuring 110°, 125°, 115°, 130°, and 100°. Calculate the sixth angle.",
            "4. The interior angles of a hexagon are 2x, 3x, 4x, 5x, 6x, and 7x. Find x and the smallest angle.",
            "5. In a heptagon, six of the angles each measure 130°. Calculate the measure of the seventh angle."
        ]),
        ("Exercise 6: Triangles, Parallel Lines, and Exterior Angle Theorems", [
            "1. In triangle ABC, exterior angle at C is 132°. If angle A = 54°, calculate angle B.",
            "2. The exterior angles of a triangle are in the ratio 2 : 3 : 4. Find all exterior and interior angles.",
            "3. In a triangle, two remote interior angles are (2x - 5)° and (3x + 15)°, and the exterior angle is (6x - 20)°. Solve for x.",
            "4. Two parallel lines are intersected by a transversal. If two co-interior angles are (3x + 15)° and (2x + 5)°, find x and both angles.",
            "5. In quadrilateral ABCD with AB parallel to CD, angle A = 75° and angle B = 110°. Determine angles C and D."
        ]),
        ("Exercise 7: Real-World Architecture, Tiling, and Tessellation", [
            "1. Explain mathematically why regular hexagons can tessellate a flat surface on their own, while regular octagons cannot.",
            "2. A hexagonal gazebo roof forms a regular hexagon. What angle do two adjacent boundary beams form?",
            "3. A stop sign is a regular octagon. Calculate the interior angle between any two consecutive edges.",
            "4. An architect combines regular octagons and squares to tile a floor. Prove that two octagons and one square meet seamlessly at a vertex.",
            "5. A soccer ball pairs regular pentagons and hexagons. What is the difference between their interior angles?"
        ]),
        ("Exercise 8: Challenge & Multi-Step Geometric Deduction", [
            "1. A polygon of n sides has two right angles, while the remaining (n - 2) angles each measure 150°. Determine n.",
            "2. The ratio of the interior angle of regular polygon A to polygon B is 3 : 4. If polygon A has 6 sides, how many sides has B?",
            "3. Five angles of a hexagon are each equal to x°, and the sixth angle is 80°. Calculate x.",
            "4. In a convex decagon, nine interior angles each measure 145°. What is the tenth angle? Is the decagon convex?",
            "5. The difference between an interior angle of an (n + 1)-gon and an n-gon is 4°. Find n."
        ])
    ]
    
    for title, q_list in exercises_data:
        ex_content = [Paragraph(f"<b>{title}</b>", h2_style)]
        for q in q_list:
            ex_content.append(Paragraph(q, bullet_style))
        ex_content.append(Spacer(1, 4))
        story.append(KeepTogether(ex_content))
        
    story.append(Spacer(1, 10))
    
    # 6. Worked Solutions Section
    story.append(Paragraph("6. Complete Step-by-Step Worked Solutions", h1_style))
    story.append(Paragraph("Full mathematical derivations and checks for all 40 practice problems.", body_style))
    
    solutions_data = [
        ("Solutions to Exercise 1", [
            "1. (a) Heptagon, (b) Nonagon, (c) Decagon, (d) Undecagon, (e) Dodecagon.",
            "2. Diagonals from one vertex = n - 3: (a) 6 - 3 = 3, (b) 9 - 3 = 6, (c) 16 - 3 = 13.",
            "3. Triangles = n - 2: (a) 8 - 2 = 6, (b) 11 - 2 = 9, (c) 20 - 2 = 18.",
            "4. n - 3 = 9 ⇒ n = 12 sides (Dodecagon).",
            "5. n - 2 = 11 ⇒ n = 13 sides (Tridecagon / 13-gon)."
        ]),
        ("Solutions to Exercise 2", [
            "1. S = (n - 2) × 180°: (a) Heptagon = 5 × 180° = 900°, (b) Octagon = 6 × 180° = 1080°, (c) Decagon = 8 × 180° = 1440°.",
            "2. n = 14 ⇒ S = 12 × 180° = 2160°.",
            "3. (n - 2) × 180 = 1980 ⇒ n - 2 = 11 ⇒ n = 13 sides.",
            "4. (n - 2) × 180 = 2400 ⇒ n - 2 = 13.333. Since n must be an integer, 2400° is impossible.",
            "5. Pentagon sum = 540°. Sum known = 100 + 110 + 125 = 335°. Remaining = 540 - 335 = 205°. Each angle = 205° / 2 = 102.5°."
        ]),
        ("Solutions to Exercise 3", [
            "1. Octagon (n = 8): Exterior = 360° / 8 = 45°; Interior = 180° - 45° = 135°.",
            "2. Decagon (n = 10): Exterior = 360° / 10 = 36°; Interior = 180° - 36° = 144°.",
            "3. Dodecagon (n = 12): Exterior = 360° / 12 = 30°.",
            "4. n = 18: Exterior = 360° / 18 = 20°; Interior = 180° - 20° = 160°.",
            "5. x + 5x = 180° ⇒ 6x = 180° ⇒ x = 30°. Exterior = 30°, Interior = 150°."
        ]),
        ("Solutions to Exercise 4", [
            "1. n = 360° / 30° = 12 sides.",
            "2. Exterior = 180° - 140° = 40°. n = 360° / 40° = 9 sides.",
            "3. Exterior = 180° - 165° = 15°. n = 360° / 15° = 24 sides.",
            "4. n = 360° / 18° = 20 sides (Icosagon or 20-gon).",
            "5. (n - 2) × 180 = 4 × 360 = 1440 ⇒ n - 2 = 8 ⇒ n = 10 sides (Decagon)."
        ]),
        ("Solutions to Exercise 5", [
            "1. x + (2x + 10) + (3x - 20) + (4x + 10) = 360 ⇒ 10x = 360 ⇒ x = 36. Angles: 36°, 82°, 88°, 154°. Largest = 154°.",
            "2. 5x + 200 = 540 ⇒ 5x = 340 ⇒ x = 68. Angles: 68°, 88°, 108°, 128°, 148°.",
            "3. Hexagon sum = 720°. Known sum = 110 + 125 + 115 + 130 + 100 = 580°. Sixth angle = 720 - 580 = 140°.",
            "4. 27x = 720 ⇒ x = 80/3 = 26.67°. Smallest angle = 2x = 160/3 = 53.33° (53° 20').",
            "5. Heptagon sum = 900°. Six angles = 6 × 130° = 780°. Seventh angle = 900 - 780 = 120°."
        ]),
        ("Solutions to Exercise 6", [
            "1. Exterior angle = sum of remote interior: 54° + B = 132° ⇒ B = 132 - 54 = 78°.",
            "2. Exterior ratio parts = 2 + 3 + 4 = 9. 1 part = 360° / 9 = 40°. Exterior: 80°, 120°, 160°. Interior: 100°, 60°, 20°.",
            "3. (2x - 5) + (3x + 15) = 6x - 20 ⇒ 5x + 10 = 6x - 20 ⇒ x = 30.",
            "4. Co-interior sum = 180°: (3x + 15) + (2x + 5) = 180 ⇒ 5x + 20 = 180 ⇒ 5x = 160 ⇒ x = 32. Angles: 111° and 69°.",
            "5. Co-interior: Angle D = 180 - 75 = 105°; Angle C = 180 - 110 = 70°."
        ]),
        ("Solutions to Exercise 7", [
            "1. Hexagon interior = 120°. 360° / 120° = 3 (exact integer), tiles cleanly around a vertex. Octagon interior = 135°. 360 / 135 = 2.67 (not integer), cannot tile alone.",
            "2. Regular hexagon interior angle = (6 - 2) × 180° / 6 = 120°.",
            "3. Regular octagon interior angle = (8 - 2) × 180° / 8 = 135°.",
            "4. Two octagons = 2 × 135° = 270°. One square = 90°. Total = 270° + 90° = 360° (complete tile vertex with 0 gap).",
            "5. Hexagon interior = 120°, Pentagon interior = 108°. Difference = 120 - 108 = 12°."
        ]),
        ("Solutions to Exercise 8", [
            "1. 2(90) + (n - 2)150 = (n - 2)180 ⇒ 180 + 150n - 300 = 180n - 360 ⇒ 30n = 240 ⇒ n = 8 sides (Octagon).",
            "2. Polygon A (n = 6) interior = 120°. Ratio A:B = 3:4 ⇒ Angle B = 160°. Ext angle B = 20°. Sides of B = 360° / 20° = 18 sides.",
            "3. 5x + 80 = 720 ⇒ 5x = 640 ⇒ x = 128°.",
            "4. Decagon sum = 1440°. 9 × 145 = 1305°. Tenth angle = 1440 - 1305 = 135°. Yes, convex since all angles < 180°.",
            "5. 360/n - 360/(n+1) = 4 ⇒ 90/n - 90/(n+1) = 1 ⇒ n(n+1) = 90 ⇒ n² + n - 90 = 0 ⇒ (n+10)(n-9) = 0 ⇒ n = 9 sides."
        ])
    ]
    
    for title, sol_list in solutions_data:
        sol_content = [Paragraph(f"<b>{title}</b>", h2_style)]
        for s in sol_list:
            sol_content.append(Paragraph(s, bullet_style))
        sol_content.append(Spacer(1, 4))
        story.append(KeepTogether(sol_content))
        
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully compiled publication-grade PDF: {pdf_path}")

if __name__ == "__main__":
    build_pdf()
