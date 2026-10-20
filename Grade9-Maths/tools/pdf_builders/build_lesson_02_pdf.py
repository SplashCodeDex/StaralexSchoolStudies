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
            self.drawRightString(559, 806, "Sub-strand 1: Shapes and Space (Lesson 2)")
            self.setStrokeColor(colors.HexColor('#D1D5DB'))
            self.setLineWidth(0.5)
            self.line(36, 800, 559, 800)
            
        # Footer (All pages)
        self.setStrokeColor(colors.HexColor('#D1D5DB'))
        self.setLineWidth(0.5)
        self.line(36, 42, 559, 42)
        self.drawString(36, 30, "Lesson 2: Congruence and Similarity in Triangles")
        self.drawRightString(559, 30, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()

def build_pdf():
    base_dir = r"W:\StaralexSchoolStudies\Grade9-Maths\Strand-3-Geometry-And-Measurement\Substrand-1-Shapes-And-Space\Lesson-02-Congruence-And-Similarity"
    pdf_path = os.path.join(base_dir, "Lesson_02_Congruence_and_Similarity.pdf")
    
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=46,
        bottomMargin=46
    )
    
    styles = getSampleStyleSheet()
    
    primary_color = colors.HexColor('#1E3A8A')
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
    
    caption_style = ParagraphStyle(
        'CaptionStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8,
        leading=10,
        alignment=1,
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
            Paragraph("<b>Content Standard: B9.3.1.1</b><br/><b>Indicator: B9.3.1.1.2</b>", ParagraphStyle('RCur', parent=body_style, alignment=2))
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
        [Paragraph("<b>Lesson Topic:</b> Congruence and Similarity in Triangles<br/>"
                   "<b>Core Mandate:</b> Rigorous criteria (SSS, SAS, ASA, AAS, RHS vs AA, SAS, SSS), Thales intercept theorem, scale factor relationships, and 40 practice questions (with 15% cumulative spiral review).", body_style)]
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
    
    # 1. Theoretical Foundations: Congruence
    story.append(Paragraph("1. Conceptual Foundations: Congruence vs Similarity", h1_style))
    story.append(Paragraph(
        "In geometry, precision in defining shape and size is paramount. "
        "Two geometric figures are <b>congruent</b> (symbol: ≅) if and only if they possess identical shape AND identical size. "
        "Congruence is an <i>isometry</i> (rigid transformation): translating, rotating, or reflecting the figure preserves all side lengths and angle measures. "
        "In contrast, two figures are <b>similar</b> (symbol: ~) if they have identical shape but differ in size (a dilation/scaling transformation).",
        body_style
    ))
    
    cong_img_path = os.path.join(base_dir, "diagrams", "congruent_triangles_schema.jpg")
    if os.path.exists(cong_img_path):
        img_tbl = Table([[
            Image(cong_img_path, width=160, height=160),
            Paragraph(
                "<b>The 5 Valid Congruence Criteria for Triangles:</b><br/><br/>"
                "• <b>SSS (Side-Side-Side):</b> All 3 corresponding sides are equal.<br/>"
                "• <b>SAS (Side-Angle-Side):</b> 2 sides and the <b>included</b> angle are equal.<br/>"
                "• <b>ASA (Angle-Side-Angle):</b> 2 angles and the <b>included</b> side are equal.<br/>"
                "• <b>AAS (Angle-Angle-Side):</b> 2 angles and a non-included side are equal.<br/>"
                "• <b>RHS (Right-angle, Hypotenuse, Side):</b> Right-angled triangles with equal hypotenuses and one equal leg.<br/><br/>"
                "<b>Warning Fallacies:</b><br/>"
                "• <i>ASS/SSA is invalid:</i> Produces the ambiguous case (two distinct triangles).<br/>"
                "• <i>AAA is NOT congruence:</i> Proves similarity only (not identical size).",
                body_style
            )
        ]], colWidths=[170, 353])
        img_tbl.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('BACKGROUND', (0,0), (-1,-1), accent_box),
            ('BOX', (0,0), (-1,-1), 0.5, border_color),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ]))
        story.append(img_tbl)
        story.append(Paragraph("Figure 2.1: Triangle Congruence Criteria Schema (Matching Tick and Arc Marks).", caption_style))
    story.append(Spacer(1, 8))

    # 2. Similarity Criteria & Scale Factors
    story.append(Paragraph("2. Triangle Similarity Criteria and Scale Factors", h1_style))
    story.append(Paragraph(
        "Two triangles are similar (ΔABC ~ ΔDEF) if their corresponding angles are equal and their corresponding sides are proportional by a linear scale factor k: "
        "<b>k = DE/AB = EF/BC = DF/AC</b>.",
        body_style
    ))
    
    sim_img_path = os.path.join(base_dir, "diagrams", "similar_triangles_schema.jpg")
    if os.path.exists(sim_img_path):
        sim_tbl = Table([[
            Image(sim_img_path, width=160, height=160),
            Paragraph(
                "<b>The 3 Valid Similarity Criteria:</b><br/><br/>"
                "• <b>AA (Angle-Angle):</b> Two pairs of equal angles guarantee similarity (the 3rd angle must be equal by the 180° theorem).<br/>"
                "• <b>SAS Similarity:</b> One angle equal and enclosing sides in the same ratio.<br/>"
                "• <b>SSS Similarity:</b> All three pairs of sides in the same ratio.<br/><br/>"
                "<b>Dimensional Scaling Laws:</b><br/>"
                "• <b>Linear Dimensions (Lengths, Perimeters):</b> Scale by <b>k</b>.<br/>"
                "• <b>Surface Area:</b> Scales by <b>k²</b>.<br/>"
                "&nbsp;&nbsp;&nbsp;<i>Area(new) = k² × Area(original)</i>",
                body_style
            )
        ]], colWidths=[170, 353])
        sim_tbl.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('BACKGROUND', (0,0), (-1,-1), accent_box),
            ('BOX', (0,0), (-1,-1), 0.5, border_color),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ]))
        story.append(sim_tbl)
        story.append(Paragraph("Figure 2.2: Triangle Similarity and the Parallel Intercept Theorem.", caption_style))
    story.append(Spacer(1, 8))

    # 3. Curriculum Exemplars
    story.append(Paragraph("3. Step-by-Step Curriculum Exemplars (NaCCA Syllabus Page 35)", h1_style))
    
    # Exemplar 1
    story.append(Paragraph("<b>Exemplar 1: Parallel Intercept in Triangle PQR</b>", h2_style))
    story.append(Paragraph(
        "<b>Problem:</b> In ΔPQR, segment ST is parallel to base QR. Given PS = 6 cm, SQ = 9 cm, ST = 8 cm, Angle P = 45°, and Angle PQR = 65°. Find missing angles and length QR.<br/>"
        "<b>Solution:</b><br/>"
        "1. <i>Similarity Proof:</i> Angle SPT = Angle QPR = 45° (common). Angle PST = Angle PQR = 65° (corresponding angles on ST ∥ QR). By AA similarity, <b>ΔPST ~ ΔPQR</b>.<br/>"
        "2. <i>Angle PTS:</i> In ΔPST, angle sum = 180° ⇒ Angle PTS = 180° - (45° + 65°) = <b>70°</b>. Thus Angle PRQ = 70°.<br/>"
        "3. <i>Base QR:</i> Side PQ = PS + SQ = 6 + 9 = 15 cm. Linear scale factor k = PQ / PS = 15 / 6 = 2.5.<br/>"
        "&nbsp;&nbsp;&nbsp;Base QR = ST × k = 8 × 2.5 = <b>20 cm</b>.",
        body_style
    ))
    story.append(Spacer(1, 6))

    # Exemplar 3: Compound Trapezoid
    comp_img_path = os.path.join(base_dir, "diagrams", "similarity_compound_shape_diagram.jpg")
    comp_content = [
        Paragraph("<b>Exemplar 2: Compound Similarity in Trapezoids (PDF Page 35)</b>", h2_style),
        Paragraph("<b>Problem:</b> Trapezoids PQRS and WXYZ are mathematically similar with bases c = 8 cm, WX = 12 cm, ZY = 20 cm, and slant side WZ = 15 cm. Angles are 70° and 110°. Find scale factor k, and lengths b and a in PQRS.", body_style)
    ]
    if os.path.exists(comp_img_path):
        comp_tbl = Table([[
            Image(comp_img_path, width=160, height=160),
            Paragraph(
                "<b>Worked Solution:</b><br/>"
                "1. <i>Co-interior Angles:</i> Since WX ∥ ZY, Angle WZY and Angle ZWX are co-interior: 70° + 110° = 180°.<br/>"
                "2. <i>Scale Factor k:</i> Top base c = 8 cm corresponds to WX = 12 cm.<br/>"
                "&nbsp;&nbsp;&nbsp;<b>k = 12 / 8 = 1.5</b><br/>"
                "3. <i>Bottom Base b:</i> ZY = 20 cm corresponds to base b.<br/>"
                "&nbsp;&nbsp;&nbsp;ZY / b = 1.5 ⇒ <b>b = 20 / 1.5 = 13.33 cm (40/3 cm)</b><br/>"
                "4. <i>Slant Side a:</i> WZ = 15 cm corresponds to side a.<br/>"
                "&nbsp;&nbsp;&nbsp;WZ / a = 1.5 ⇒ <b>a = 15 / 1.5 = 10 cm</b>.",
                body_style
            )
        ]], colWidths=[170, 353])
        comp_tbl.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFFFFF')),
            ('BOX', (0,0), (-1,-1), 0.5, border_color),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ]))
        comp_content.append(comp_tbl)
        comp_content.append(Paragraph("Figure 2.3: Compound Geometric Similarity in Trapezoids Schema.", caption_style))
    story.append(KeepTogether(comp_content))
    story.append(Spacer(1, 10))

    # 4. Practice Exercises (40 Questions across 8 sets)
    story.append(Paragraph("4. Practice Exercises (40 Questions across 8 Sets)", h1_style))
    story.append(Paragraph("Includes a 15% cumulative spiral review of Lesson 1 (Polygon angles) in Exercise 7.", body_style))
    
    exercises_data = [
        ("Exercise 1: Identifying Congruence Criteria", [
            "1. Triangle ABC has sides 6, 8, 10 cm; Triangle PQR has sides 8, 6, 10 cm. State congruence and criterion.",
            "2. In ΔDEF and ΔXYZ, DE = XY, EF = YZ, and Angle E = Angle Y = 62°. State the criterion.",
            "3. In ΔKLM and ΔRST, Angle K = Angle R = 40°, Angle L = Angle S = 75°, and LM = ST = 9 cm. State the criterion.",
            "4. Two right-angled triangles each have hypotenuse 13 cm and one leg 5 cm. State criterion and find the third side.",
            "5. A student says triangles with angles 30°, 60°, 90° must be congruent. Is the student correct? Explain."
        ]),
        ("Exercise 2: Solving for Unknowns in Congruent Triangles", [
            "1. Given ΔABC ≅ ΔDEF with BC = 2x + 7 and EF = 3x - 1. Solve for x and find length BC.",
            "2. Given ΔPQR ≅ ΔSTU with Angle P = (5y - 15)° and Angle S = (3y + 25)°. Solve for y and find the angle.",
            "3. In ΔGHI ≅ ΔJKL, GH = 4a - 3, JK = 2a + 9, and Angle H = (5b + 20)°, Angle K = (2b + 56)°. Solve for a and b.",
            "4. In isosceles ΔABC (AB = AC), an altitude AD is drawn perpendicular to BC. Prove ΔABD ≅ ΔACD.",
            "5. In the figure above, if BC = 16 cm and AB = 10 cm, find length BD and height AD."
        ]),
        ("Exercise 3: Proving and Using Triangle Similarity", [
            "1. Triangle A has angles 50° and 65°. Triangle B has angles 65° and 65°. Are they similar? Explain.",
            "2. Sides of ΔABC are 4, 6, 8 cm; sides of ΔDEF are 10, 15, 20 cm. Prove similarity and state scale factor k.",
            "3. In ΔPQR, PQ = 6, PR = 9, Angle P = 54°. In ΔXYZ, XY = 10, XZ = 15, Angle X = 54°. Prove similarity.",
            "4. If ΔABC ~ ΔDEF with AB = 5 cm, DE = 12.5 cm, and BC = 8 cm, calculate the length of EF.",
            "5. A triangle has sides 7, 9, 12 cm. The shortest side of a similar triangle is 21 cm. Find its perimeter."
        ]),
        ("Exercise 4: Parallel Transversals and Intercept Theorems", [
            "1. In ΔABC, DE ∥ BC with D on AB, E on AC. If AD = 3, DB = 5, and DE = 4.5 cm, calculate BC.",
            "2. In the same triangle, if total length AC = 16 cm, calculate lengths AE and EC.",
            "3. In an hourglass figure, AB ∥ CD through intersection point O. If OA = 4, OC = 10, AB = 6 cm, find CD.",
            "4. In ΔPQR, ST ∥ QR. If PS = x, SQ = x + 2, PT = 4, and TR = 6, solve for x.",
            "5. In ΔXYZ, MN ∥ YZ with XM = 8, MY = 4, XN = y + 6, and NZ = y + 1. Calculate y."
        ]),
        ("Exercise 5: Linear Scale Factor vs Area Scale Factor", [
            "1. Linear scale factor k = 3. If area of smaller triangle is 14 cm², find area of the larger triangle.",
            "2. The areas of two similar triangles are 25 cm² and 81 cm². Find the linear scale factor k.",
            "3. Small triangle has base 6 cm and area 24 cm². Corresponding base of similar triangle is 15 cm. Find its area.",
            "4. Similar prints have perimeters 30 cm and 45 cm. If smaller print needs 50 cm² glass, how much does larger need?",
            "5. Triangular park has 16 times the area of a display garden. If garden path is 12 m, find park path length."
        ]),
        ("Exercise 6: Real-World Surveying and Shadow Problems", [
            "1. Flagpole casts 12 m shadow when a 1.8 m student casts a 2.4 m shadow. Find flagpole height.",
            "2. River width measurement: Baseline stakes 15 m apart; 5 m further back requires 20 m line. Find river width.",
            "3. A 35 mm slide is projected onto a 1.4 m canvas. Find the magnification scale factor k.",
            "4. Streetlight is 6 m high. Person 1.5 m tall stands 9 m from base. Calculate shadow length.",
            "5. Roof truss has 10 m span and 3 m height. Vertical strut is placed 2 m from edge. Find strut height."
        ]),
        ("Exercise 7: Spiral Cumulative Review (Lesson 1 Polygons)", [
            "1. Calculate the total sum of the interior angles of a nonagon (n = 9).",
            "2. Each exterior angle of a regular polygon is 24°. Find the number of sides and its formal name.",
            "3. An irregular pentagon has angles x, 2x, 3x, 4x, and 5x. Find x and the largest angle.",
            "4. Prove interior angle of regular octagon is 135°, and explain why it cannot tile a plane alone.",
            "5. Interior angle sum of a polygon is 2340°. How many diagonals can be drawn from a single vertex?"
        ]),
        ("Exercise 8: Challenge & Multi-Step Geometric Deduction", [
            "1. In right ΔABC (Angle B = 90°), altitude BD ⊥ AC. Prove ΔABD ~ ΔBCD ~ ΔABC.",
            "2. In the figure above, if AD = 4 cm and DC = 9 cm, calculate altitude BD (Geometric Mean Theorem).",
            "3. Two similar triangles have scale factor k = 3/2. If area difference is 65 cm², find both areas.",
            "4. In ΔABC, D and E are midpoints of AB and AC. Find area ratio of ΔADE to ΔABC and trapezoid BCED.",
            "5. Equilateral triangle perimeter is 36 cm. Midpoints form an inner triangle. Find its perimeter and area ratio."
        ])
    ]
    
    for title, q_list in exercises_data:
        ex_content = [Paragraph(f"<b>{title}</b>", h2_style)]
        for q in q_list:
            ex_content.append(Paragraph(q, bullet_style))
        ex_content.append(Spacer(1, 4))
        story.append(KeepTogether(ex_content))
        
    story.append(Spacer(1, 10))

    # 5. Complete Worked Solutions Section
    story.append(Paragraph("5. Complete Step-by-Step Worked Solutions", h1_style))
    story.append(Paragraph("Detailed derivations and arithmetic proofs for all 40 questions.", body_style))
    
    solutions_data = [
        ("Solutions to Exercise 1", [
            "1. Matching sides: AB = QR = 6, BC = PQ = 8, AC = PR = 10. Congruent: ΔABC ≅ ΔQRP by SSS.",
            "2. Two sides and included angle: DE = XY, EF = YZ, Angle E = Angle Y = 62°. Congruent by SAS.",
            "3. Two angles and non-included side: Angle K = Angle R, Angle L = Angle S, LM = ST. Congruent by AAS.",
            "4. Right angle, hypotenuse 13, leg 5. Congruent by RHS. Other leg = √(13² - 5²) = √144 = 12 cm.",
            "5. No. Three equal angles prove AAA (Similarity), which guarantees same shape but not same size."
        ]),
        ("Solutions to Exercise 2", [
            "1. BC = EF ⇒ 2x + 7 = 3x - 1 ⇒ x = 8. Length BC = 2(8) + 7 = 23 cm.",
            "2. Angle P = Angle S ⇒ 5y - 15 = 3y + 25 ⇒ 2y = 40 ⇒ y = 20. Angle = 5(20) - 15 = 85°.",
            "3. GH = JK ⇒ 4a - 3 = 2a + 9 ⇒ 2a = 12 ⇒ a = 6. Angle H = Angle K ⇒ 5b + 20 = 2b + 56 ⇒ 3b = 36 ⇒ b = 12.",
            "4. In ΔABD & ΔACD: AB = AC, AD common, Angle ADB = Angle ADC = 90°. Congruent by RHS.",
            "5. BD = BC / 2 = 16 / 2 = 8 cm. Height AD = √(AB² - BD²) = √(10² - 8²) = √36 = 6 cm."
        ]),
        ("Solutions to Exercise 3", [
            "1. Triangle A 3rd angle = 180 - (50 + 65) = 65°. Triangle B 3rd angle = 50°. Both have 50°, 65°, 65°. Similar by AA.",
            "2. Ratios: 10/4 = 2.5, 15/6 = 2.5, 20/8 = 2.5. Proportional sides ⇒ Similar by SSS similarity with k = 2.5.",
            "3. Side ratios: 10/6 = 5/3, 15/9 = 5/3. Included Angle P = Angle X = 54°. Similar by SAS similarity.",
            "4. k = DE / AB = 12.5 / 5 = 2.5. EF = k × BC = 2.5 × 8 = 20 cm.",
            "5. k = 21 / 7 = 3. Perimeter small = 7 + 9 + 12 = 28 cm. Perimeter large = 3 × 28 = 84 cm."
        ]),
        ("Solutions to Exercise 4", [
            "1. AB = AD + DB = 3 + 5 = 8 cm. k = AB / AD = 8/3. BC = DE × k = 4.5 × (8/3) = 12 cm.",
            "2. AE = AC / k = 16 / (8/3) = 6 cm. EC = AC - AE = 16 - 6 = 10 cm.",
            "3. Alternate angles equal ⇒ ΔOAB ~ ΔOCD by AA. k = OC / OA = 10/4 = 2.5. CD = AB × 2.5 = 6 × 2.5 = 15 cm.",
            "4. Thales: PS / SQ = PT / TR ⇒ x / (x + 2) = 4/6 = 2/3 ⇒ 3x = 2x + 4 ⇒ x = 4.",
            "5. XM / MY = XN / NZ ⇒ 8/4 = (y + 6)/(y + 1) ⇒ 2(y + 1) = y + 6 ⇒ 2y + 2 = y + 6 ⇒ y = 4."
        ]),
        ("Solutions to Exercise 5", [
            "1. Area factor = k² = 3² = 9. Area large = 9 × 14 = 126 cm².",
            "2. k² = 81 / 25 ⇒ k = √(81/25) = 9/5 = 1.8.",
            "3. k = 15 / 6 = 2.5 ⇒ k² = 6.25. Area large = 6.25 × 24 = 150 cm².",
            "4. k = 45 / 30 = 1.5 ⇒ k² = 2.25. Glass needed = 2.25 × 50 = 112.5 cm².",
            "5. k² = 16 ⇒ k = 4. Park pathway = 4 × 12 = 48 m."
        ]),
        ("Solutions to Exercise 6", [
            "1. Height / 1.8 = 12 / 2.4 = 5 ⇒ Height = 5 × 1.8 = 9 m.",
            "2. (w + 5) / w = 20 / 15 = 4/3 ⇒ 3w + 15 = 4w ⇒ river width w = 15 m.",
            "3. Canvas = 1.4 m = 1400 mm. Scale factor k = 1400 / 35 = 40 (40x magnification).",
            "4. 6 / 1.5 = (9 + s) / s ⇒ 4 = (9 + s) / s ⇒ 4s = 9 + s ⇒ 3s = 9 ⇒ shadow s = 3 m.",
            "5. Truss half-base = 5 m. At 2 m from edge: h / 3 = 2 / 5 ⇒ h = 6/5 = 1.2 m."
        ]),
        ("Solutions to Exercise 7 (Lesson 1 Spiral Review)", [
            "1. S = (n - 2) × 180° = (9 - 2) × 180° = 7 × 180° = 1260°.",
            "2. n = 360° / 24° = 15 sides (Pentadecagon).",
            "3. 15x = 540° ⇒ x = 36°. Largest angle = 5(36°) = 180°.",
            "4. Each interior = (8 - 2) × 180° / 8 = 135°. 360 / 135 = 2.67 (not integer), leaves 90° gap.",
            "5. (n - 2) × 180 = 2340 ⇒ n - 2 = 13 ⇒ n = 15 sides. Diagonals from 1 vertex = n - 3 = 15 - 3 = 12."
        ]),
        ("Solutions to Exercise 8", [
            "1. ΔABD & ΔABC share Angle A with 90° angle ⇒ ΔABD ~ ΔABC. Similarly ΔBCD ~ ΔABC. Thus ΔABD ~ ΔBCD ~ ΔABC.",
            "2. BD / AD = CD / BD ⇒ BD² = AD × CD = 4 × 9 = 36 ⇒ BD = 6 cm (Altitude Geometric Mean Theorem).",
            "3. k² = (3/2)² = 9/4 = 2.25. 2.25A - A = 65 ⇒ 1.25A = 65 ⇒ A = 52 cm². Large area = 52 + 65 = 117 cm².",
            "4. ΔADE ~ ΔABC with k = 1/2 ⇒ Area ratio = (1/2)² = 1/4. Trapezoid BCED occupies 1 - 1/4 = 3/4 (75%) of total area.",
            "5. Side = 36 / 3 = 12 cm. Inner triangle side = 6 cm, perimeter = 18 cm. Area ratio = (1/2)² = 1/4."
        ])
    ]
    
    for title, sol_list in solutions_data:
        sol_content = [Paragraph(f"<b>{title}</b>", h2_style)]
        for s in sol_list:
            sol_content.append(Paragraph(s, bullet_style))
        sol_content.append(Spacer(1, 4))
        story.append(KeepTogether(sol_content))
        
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully compiled Lesson 2 PDF: {pdf_path}")

if __name__ == "__main__":
    build_pdf()
