"""Draw the VA lesson figures (schoolbook style, white background, labelled)."""
from PIL import Image, ImageDraw, ImageFont
import math
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "CAD" / "va-figures"
OUT.mkdir(parents=True, exist_ok=True)

FONT = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 26)
FONT_S = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 20)
FONT_B = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 26)


def canvas(w, h):
    im = Image.new("RGB", (w, h), "white")
    dr = ImageDraw.Draw(im)
    return im, dr


def label(dr, xy, text, font=FONT, fill="black", anchor="mm"):
    dr.text(xy, text, font=font, fill=fill, anchor=anchor)


def frame(dr, boxes, title=None):
    for b in boxes:
        dr.rectangle(b, outline="#888888", width=3)


def centre(dr, left, top, w, h):
    return (left + (w - dr.textlength("x", font=FONT)) / 2, top + h / 2)


# ---------------- colour wheel ----------------
def colour_wheel():
    im, dr = canvas(1200, 780)
    cx, cy, r = 430, 400, 280
    cols = [  # RYB 12-part wheel
        (228, 40, 40), (233, 87, 41), (240, 130, 34), (247, 166, 20),
        (250, 200, 25), (155, 193, 60), (60, 160, 75), (30, 150, 140),
        (35, 100, 165), (75, 60, 150), (120, 50, 135), (175, 55, 110),
    ]
    names = ["Red", "Red-orange", "Orange", "Yellow-\norange", "Yellow", "Yellow-\ngreen",
             "Green", "Blue-\ngreen", "Blue", "Blue-\nviolet", "Violet", "Red-violet"]
    seg = 30
    for i, c in enumerate(cols):
        a0 = math.radians(-90 - seg - i * seg)
        a1 = a0 + math.radians(seg + 0.6)
        dr.pieslice([cx - r, cy - r, cx + r, cy + r], math.degrees(a0), math.degrees(a1),
                    fill=c, outline="white", width=2)
    dr.ellipse([cx - 70, cy - 70, cx + 70, cy + 70], fill="white", outline="#888888", width=3)
    label(dr, (cx, cy - 28), "Primary", font=FONT_S)
    label(dr, (cx, cy + 4), "3", font=FONT)
    label(dr, (cx, cy + 36), "colours", font=FONT_S)
    ang = math.radians(-90 - seg / 2)
    for i, name in enumerate(names):
        a = math.radians(-90 - seg - i * seg - seg / 2)
        px, py = cx + 1.42 * r * math.cos(a), cy + 1.5 * r * math.sin(a)
        label(dr, (px, py), name, font=FONT_S)
    x = 880
    for i, (name, col) in enumerate([("Red", (228, 40, 40)), ("Yellow", (250, 200, 25)), ("Blue", (35, 100, 165))]):
        y = 130 + i * 90
        dr.ellipse([x, y, x + 60, y + 60], fill=col, outline="#444444", width=2)
        label(dr, (x + 80, y + 30), f"Primary — {name}", anchor="lm")
    label(dr, (x + 30, 390), "Secondary:", font=FONT_S, anchor="lm")
    label(dr, (x + 30, 420), "mixed from two primaries", font=FONT_S, anchor="lm")
    label(dr, (x + 30, 470), "Tertiary: primary + next-door", font=FONT_S, anchor="lm")
    label(dr, (x + 30, 498), "secondary mix", font=FONT_S, anchor="lm")
    dr.rectangle([x - 20, 60, x + 265, 530], outline="#CCCCCC", width=2)
    im.save(OUT / "colour-wheel.png")


# ---------------- design elements ----------------
def design_elements():
    im, dr = canvas(1400, 460)
    label(dr, (700, 40), "Elements of design in Grade 7 — dots, lines, shapes", font=FONT_B)
    boxes = [(120, 110, 480, 400), (520, 110, 880, 400), (920, 110, 1280, 400)]
    frame(dr, boxes)
    u = boxes[0]
    label(dr, ((u[0] + u[2]) / 2, u[1] + 30), "Dots", font=FONT_S)
    import random
    random.seed(7)
    for _ in range(26):
        x = random.randint(u[0] + 30, u[2] - 30)
        y = random.randint(u[1] + 70, u[3] - 20)
        rr = random.choice([4, 6, 9, 13])
        dr.ellipse([x - rr, y - rr, x + rr, y + rr], fill=(40, 40, 40))
    u = boxes[1]
    label(dr, ((u[0] + u[2]) / 2, u[1] + 30), "Lines", font=FONT_S)
    y = u[1] + 80
    for weight in [2, 5, 10, 16]:
        dr.line([(u[0] + 40, y), (u[2] - 40, y)], fill="black", width=weight)
        y += 52
    dr.line([(u[0] + 40, y), (u[2] - 40, y)], fill="black", width=6)
    y += 46
    dr.arc([u[0] + 40, y - 30, u[0] + 140, y + 50], 180, 0, fill="black", width=5)
    dr.line([(u[0] + 140, y + 10), (u[2] - 40, y - 10)], fill="black", width=5)
    y += 44
    dr.line([(u[0] + 40, y), (u[0] + 130, y - 22)], fill="black", width=5)
    dr.line([(u[0] + 130, y - 22), (u[0] + 220, y)], fill="black", width=5)
    dri = ImageDraw.Draw(im)
    dri.line([(u[0] + 220, y), (u[0] + 310, y - 22)], fill="black", width=5)
    dri.line([(u[0] + 310, y - 22), (u[0] + 400, y)], fill="black", width=5)
    u = boxes[2]
    label(dr, ((u[0] + u[2]) / 2, u[1] + 30), "Shapes", font=FONT_S)
    dr.polygon([(950, 220), (1010, 150), (1070, 220)], fill=(70, 110, 170))
    dr.rectangle([1100, 160, 1180, 240], fill=(220, 150, 60))
    dr.ellipse([960, 260, 1040, 330], fill=(90, 160, 90))
    dr.polygon([(1080, 330), (1120, 260), (1160, 330), (1120, 245)], fill=(170, 90, 110))
    label(dr, ((u[0] + u[2]) / 2, u[3] + 25), "Free shapes made of lines and curves", font=FONT_S)
    im.save(OUT / "design-elements.png")


# ---------------- design principles ----------------
def design_principles():
    im, dr = canvas(1400, 460)
    label(dr, (700, 40), "Principles of design in Grade 7 — balance, rhythm, repetition", font=FONT_B)
    boxes = [(120, 110, 480, 400), (520, 110, 880, 400), (920, 110, 1280, 400)]
    frame(dr, boxes)
    u = boxes[0]
    label(dr, ((u[0] + u[2]) / 2, u[1] + 30), "Balance (symmetry)", font=FONT_S)
    cxm = (u[0] + u[2]) / 2
    dr.rectangle([cxm - 14, u[3] - 60, cxm + 14, u[3] - 24], fill=(60, 60, 60))
    for dx in (-70, 70):
        dr.polygon([(cxm + dx, u[3] - 130), (cxm + dx + 40, u[3] - 190), (cxm + dx + 80, u[3] - 130)],
                   fill=(80, 130, 190))
        dr.rectangle([cxm + dx - 6, u[3] - 130, cxm + dx + 86, u[3] - 110], fill=(160, 160, 160))
    dr.line([(cxm, u[1] + 80), (cxm, u[3] - 20)], fill="#BBBBBB", width=2)
    u = boxes[1]
    label(dr, ((u[0] + u[2]) / 2, u[1] + 30), "Rhythm (repeated movement)", font=FONT_S)
    y = (u[1] + u[3]) / 2 + 20
    x = u[0] + 60
    for i, rr in enumerate([14, 22, 14, 22, 14, 22, 14]):
        dr.ellipse([x, y - rr, x + 2 * rr, y + rr], outline=(40, 40, 40), width=4,
                   fill=(200, 60, 60) if i % 2 else (60, 90, 180))
        x += 90
    dr.arc([u[0] + 50, y - 90, u[2] - 50, y + 60], 190, 350, fill="#AAAAAA", width=3)
    u = boxes[2]
    label(dr, ((u[0] + u[2]) / 2, u[1] + 30), "Repetition (same unit again)", font=FONT_S)
    for r_ in range(4):
        for c_ in range(5):
            x = u[0] + 60 + c_ * 66
            yy = u[1] + 90 + r_ * 56
            dr.ellipse([x, yy, x + 34, yy + 34], fill=(250, 200, 25) if (r_ + c_) % 2 else (60, 110, 170),
                       outline="#666666", width=2)
    im.save(OUT / "design-principles.png")


# ---------------- design process ----------------
def design_process():
    im, dr = canvas(1400, 660)
    label(dr, (700, 40), "The design process — steps that turn a problem into an artefact", font=FONT_B)
    steps = ["Define", "Brief", "Research", "Ideation", "Invent", "Prototype", "Testing", "Refine"]
    n = len(steps)
    cx, cy, rx, ry = 700, 360, 360, 210
    rr = 62
    centres = []
    for i in range(n):
        a = math.radians(-90 + i * 360 / n)
        px, py = cx + rx * math.cos(a), cy + ry * math.sin(a)
        centres.append((px, py))
    for i in range(n):
        p1, p2 = centres[i], centres[(i + 1) % n]
        x0, y0 = p1
        x1, y1 = p2
        ux, uy = x1 - x0, y1 - y0
        ln = math.hypot(ux, uy)
        ux, uy = ux / ln, uy / ln
        dr.line([(x0 + ux * rr, y0 + uy * rr), (x1 - ux * (rr + 16), y1 - uy * (rr + 16))],
                fill="#777777", width=4)
        ang = math.atan2(uy, ux)
        tx, ty = x1 - ux * rr, y1 - uy * rr
        for da in (2.7, 3.6):
            dr.line([(tx, ty), (tx + 20 * math.cos(ang + da), ty + 20 * math.sin(ang + da))],
                    fill="#777777", width=4)
    for i, (p, s) in enumerate(zip(centres, steps)):
        col = [ (229, 57, 53), (245, 124, 0), (188, 170, 164), (161, 136, 127),
                (255, 202, 40), (121, 134, 203), (46, 125, 50), (215, 204, 200) ][i]
        fill = col if i not in (2,) else col
        dr.ellipse([p[0] - rr, p[1] - rr, p[0] + rr, p[1] + rr], fill=fill, outline="#555555", width=3)
        label(dr, p, s, font=FONT_S)
    label(dr, (cx, cy - 26), "Start at Define,", font=FONT_S)
    label(dr, (cx, cy + 2), "walk the circle,", font=FONT_S)
    label(dr, (cx, cy + 30), "stop when testing passes", font=FONT_S)
    im.save(OUT / "design-process.png")


# ---------------- shading techniques ----------------
def shading_techniques():
    im, dr = canvas(1600, 500)
    label(dr, (800, 40), "Five shading techniques", font=FONT_B)
    names = ["Hatching", "Cross-hatching", "Stippling", "Smoothing", "Mass shading"]
    bw, bh, gapx = 270, 330, 300
    x0, y0 = 60, 110
    for i, name in enumerate(names):
        x = x0 + i * gapx
        b = (x, y0, x + bw - 20, y0 + bh)
        frame(dr, [b])
        label(dr, (x + (bw - 20) / 2, y0 + 24), name, font=FONT_S)
        inner = (x + 20, y0 + 60, x + bw - 40, y0 + bh - 25)
        if name == "Hatching":
            step = 10
            for k, yy in enumerate(range(inner[1], inner[3], step)):
                shade = 30 + k * 14
                dr.line([(inner[0], yy), (inner[2], yy - 12)], fill=(shade, shade, shade), width=3)
        elif name == "Cross-hatching":
            ystep = 16
            for k, yy in enumerate(range(inner[1], inner[3], ystep)):
                shade = 40 + k * 12
                dr.line([(inner[0], yy), (inner[2], yy - 16)], fill=(shade, shade, shade), width=3)
            # cross layer
            xx = inner[0] + 8
            while xx < inner[2]:
                shade = 70 + (xx - inner[0]) // 4
                shade = max(0, min(255, shade))
                dr.line([(xx, inner[3]), (xx + 40, inner[1])], fill=(shade, shade, shade), width=3)
                xx += 46
        elif name == "Stippling":
            import random
            random.seed(3)
            yy = inner[1]
            while yy < inner[3]:
                xx = inner[0]
                while xx < inner[2]:
                    x = xx
                    y = yy
                    t = (x - inner[0]) / (inner[2] - inner[0])
                    if random.random() < 0.75 * (1 - t * 0.85):
                        shade = 20
                        dr.ellipse([x, y, x + 6, y + 6], fill=(shade, shade, shade))
                    t2 = (x - inner[0]) / (inner[2] - inner[0])
                    xx += 9
                yy += 9
        elif name == "Smoothing":
            w = inner[2] - inner[0]
            for k in range(w):
                shade = int(20 + 225 * k / w)
                dr.line([(inner[0] + k, inner[1]), (inner[0] + k, inner[3])], fill=(shade, shade, shade))
        elif name == "Mass shading":
            w = inner[2] - inner[0]
            for k in range(w // 3):
                shade = int(20 + 200 * k / (w // 3))
                for j in range(3):
                    xx = inner[0] + k * 3 + j
                    dr.line([(xx, inner[1]), (xx, inner[3])], fill=(shade, shade, shade))
    im.save(OUT / "shading-techniques.png")


# ---------------- shading sphere ----------------
def shading_sphere():
    im, dr = canvas(1200, 560)
    label(dr, (600, 40), "Light and shadow on a sphere (value)", font=FONT_B)
    cx, cy, r = 480, 320, 190
    # graded tone: bright top-left to dark bottom-right
    steps = 90
    for k in range(r, 0, -1):
        for j in range(0, r * 2, 2):
            pass
    # radial rings from top-left offset centre
    lx, ly = cx - r * 0.45, cy - r * 0.45
    for k in range(steps, 0, -1):
        shade = int(235 - 200 * (1 - k / steps) ** 0.8)
        rr = r * k / steps
        dr.ellipse([lx - rr / 2, ly - rr / 2, cx + rr, cy + rr], fill=(shade, shade, shade))
    dr.ellipse([cx - r, cy - r, cx + r, cy + r], outline="#555555", width=3)
    # dedraw outer ring clean
    dr.ellipse([cx - r, cy - r, cx + r, cy + r], outline="#555555", width=3)
    # highlight
    hl = (cx - r * 0.5, cy - r * 0.5)
    dr.ellipse([cx - r * 0.62, cy - r * 0.62, cx - r * 0.2, cy - r * 0.2], fill=(250, 250, 250))
    # cast shadow ellipse
    dr.ellipse([cx - r * 0.85, cy + r * 0.88, cx + r * 0.75, cy + r * 1.05], fill=(60, 60, 60))
    dr.ellipse([cx - r * 0.55, cy + r * 0.94, cx + r * 0.5, cy + r * 1.04], fill=(240, 240, 240))
    dr.line([(cx - r - 60, cy - r - 20), (cx - r + 10, cy - r + 30)], fill=(250, 150, 30), width=6)
    label(dr, (cx - r - 30, cy - r - 55), "light source", font=FONT_S, fill=(200, 90, 20))
    xtext = 900
    ytext = 190
    items = ["A.  Highlight — light falls directly", "B.  Mid-tone", "C.  Core shadow (darkest)", "D.  Reflected light (rim)",
             "E.  Cast shadow on the table"]
    for i, t in enumerate(items):
        label(dr, (xtext, ytext + i * 46), t, font=FONT_S, anchor="lm")
    label(dr, (xtext, ytext + 46 * 5 + 20), "Value = how light or dark an area is.", font=FONT_S, fill="#555555")
    label(dr, (cx, cy + r + 120), "The circle becomes a ball only when the tone is graded from light to dark.", font=FONT_S)
    im.save(OUT / "shading-sphere.png")


# ---------------- still life setup ----------------
def still_life_setup():
    im, dr = canvas(1200, 620)
    label(dr, (600, 40), "A simple still-life set-up", font=FONT_B)
    table_y = 430
    dr.rectangle([140, table_y, 1050, table_y + 26], fill=(230, 220, 200), outline="#999999", width=3)
    dr.line([(200, table_y + 26), (200, 560)], fill="#999999", width=6)
    dr.line([(1000, table_y + 26), (1000, 560)], fill="#999999", width=6)
    # jug
    dr.ellipse([320, table_y - 120, 420, table_y], fill=(200, 210, 220), outline="#666666", width=3)
    dr.polygon([(430, table_y - 95), (430, table_y - 50), (375, table_y - 85), (375, table_y - 105)],
               fill=(200, 210, 220), outline="#666666")
    dr.polygon([(345, table_y - 195), (395, table_y - 195), (382, table_y - 120), (358, table_y - 120)],
               fill=(190, 205, 215), outline="#666666")
    mid = dr
    # bowl
    mid.pieslice([560, table_y - 90, 740, table_y + 40], 0, 180, fill=(225, 200, 170), outline="#666666", width=3)
    mid.ellipse([560, table_y - 90, 740, table_y - 50], fill=(240, 220, 200), outline="#666666", width=3)
    # fruit
    mid.ellipse([800, table_y - 85, 890, table_y - 5], fill=(220, 80, 60), outline="#774444", width=2)
    mid.ellipse([870, table_y - 70, 950, table_y], fill=(230, 150, 40), outline="#775520", width=2)
    # light direction
    dr.line([(180, 140), (260, 260)], fill=(250, 150, 30), width=6)
    dr.polygon([(244, 238), (268, 272), (232, 268)], fill=(250, 150, 30))
    label(dr, (160, 110), "Light comes", font=FONT_S, fill=(200, 90, 20))
    label(dr, (160, 140), "from one side", font=FONT_S, fill=(200, 90, 20))
    label(dr, (600, 560), "Objects are arranged third-back-to-front: jug (tallest), bowl, fruits — overlap them for depth, then match tones.", font=FONT_S)
    label(dr, (600, 592), "Objects look solid only where tone shifts from light (top-left) to dark (bottom-right).", font=FONT_S, fill="#666666")
    im.save(OUT / "still-life-setup.png")


# ---------------- hand building ----------------
def hand_building():
    im, dr = canvas(1400, 470)
    label(dr, (700, 40), "Hand-building techniques — pinch pot, coiling, slab building", font=FONT_B)
    def box(x):
        b = (x, 110, x + 400, 410)
        frame(dr, [b])
        return x
    x0 = 60
    label(dr, (x0 + 200, 140), "Pinch pot", font=FONT_S)
    dr.ellipse([x0 + 70, 220, x0 + 330, 380], fill=(200, 160, 130), outline="#7a5a45", width=3)
    dr.ellipse([x0 + 100, 240, x0 + 300, 330], fill=(230, 200, 175), outline="#7a5a45", width=3)
    label(dr, (x0 + 200, 300), "thumb pressed into a ball", font=FONT_S)
    x0 = 500
    label(dr, (x0 + 200, 140), "Coiling", font=FONT_S)
    for i, (w, yy) in enumerate([(180, 360), (240, 320), (300, 280), (360, 240)]):
        dr.arc([x0 + 200 - w / 2, yy, x0 + 200 + w / 2, yy + 40], 0, 180, fill=(150, 110, 80), width=10)
    label(dr, (x0 + 200, 300), "worms of clay stacked", font=FONT_S)
    x0 = 940
    label(dr, (x0 + 200, 140), "Slab building", font=FONT_S)
    dr.rectangle([x0 + 120, 250, x0 + 280, 380], fill=(210, 170, 140), outline="#7a5a45", width=3)
    dr.line([(x0 + 200, 250), (x0 + 200, 380)], fill="#7a5a45", width=3)
    dr.rectangle([x0 + 120, 210, x0 + 280, 250], fill=(225, 190, 160), outline="#7a5a45", width=3)
    label(dr, (x0 + 200, 165), "flat sheets joined at edges", font=FONT_S)
    im.save(OUT / "hand-building.png")


# ---------------- pattern techniques ----------------
def pattern_techniques():
    im, dr = canvas(1600, 500)
    label(dr, (800, 40), "Pattern making techniques with paint", font=FONT_B)
    names = ["Dabbing", "Spraying", "Spattering", "Sponging", "Wax-resist / batik", "Marbling"]
    bw, bh, gapx = 250, 330, 260
    x0, y0 = 40, 110
    import random
    for i, name in enumerate(names):
        x = x0 + i * gapx
        b = (x, y0, x + bw - 20, y0 + bh)
        frame(dr, [b])
        label(dr, (x + (bw - 20) / 2, y0 + 24), name, font=FONT_S)
        inner = (x + 16, y0 + 60, x + bw - 36, y0 + bh - 24)
        random.seed(i * 5 + 1)
        if name == "Dabbing":
            for _ in range(160):
                x_ = random.randint(inner[0], inner[2])
                y_ = random.randint(inner[1], inner[3])
                rr = random.randint(10, 26)
                col = (250, 180, 30) if random.random() < 0.5 else (60, 110, 170)
                dr.ellipse([x_ - rr / 2, y_ - rr / 2, x_ + rr / 2, y_ + rr / 2], fill=col)
        elif name == "Spraying":
            for j in range(5):
                cxm = (inner[0] + inner[2]) / 2 + (j - 2) * 26
                for k in range(14):
                    y_ = inner[1] + 20 + k * 12
                    dr.ellipse([cxm - 8 + k, y_ - 3, cxm + 8 + k, y_ + 3], fill=(70, 130, 180))
        elif name == "Spattering":
            for _ in range(120):
                x_ = random.randint(inner[0], inner[2])
                y_ = random.randint(inner[1], inner[3])
                rr = random.randint(2, 7)
                col = (200, 60, 60) if random.random() < 0.6 else (40, 40, 40)
                dr.ellipse([x_, y_, x_ + rr, y_ + rr], fill=col)
        elif name == "Sponging":
            for _ in range(220):
                x_ = random.randint(inner[0], inner[2])
                y_ = random.randint(inner[1], inner[3])
                rc = random.randint(8, 18)
                col = (130, 170, 80)
                dr.ellipse([x_, y_, x_ + rc, y_ + rc // 2], fill=col)
        elif name == "Wax-resist / batik":
            for k in range(6):
                dr.line([(inner[0] + 20 + k * 36, inner[1]), (inner[0] + 20 + k * 36 + 26, inner[3])],
                        fill=(245, 245, 220), width=9)
            dr.rectangle([inner[0], inner[1], inner[2], inner[3]], fill=(40, 90, 160))
            for k in range(7):
                dr.line([(inner[0] + 14 + k * 30, inner[1]), (inner[0] + 14 + k * 30 + 34, inner[3])],
                        fill="white", width=6)
        elif name == "Marbling":
            for _ in range(90):
                x_ = random.randint(inner[0], inner[2])
                y_ = random.randint(inner[1], inner[3])
                rw = random.randint(14, 44)
                x2 = x_ + rw
                y2 = y_ + random.randint(-8, 8)
                col = random.choice([(70, 40, 140), (200, 60, 130), (255, 170, 0)])
                dr.arc([min(x_, x2), min(y_, y2), max(x_, x2), max(y_, y2) + 10], 200, 320, fill=col, width=3)
    im.save(OUT / "pattern-techniques.png")


# ---------------- plain weave ----------------
def weave_plain():
    im, dr = canvas(1200, 620)
    label(dr, (600, 40), "Plain weave — the simplest over-and-under pattern", font=FONT_B)
    x0, y0, w, h = 240, 120, 720, 400
    nw, nhh = 12, 7
    dx, dy = w / nw, h / nhh
    # wefts horizontal
    for r_ in range(nhh):
        yy = y0 + r_ * dy + 8
        dr.rectangle([x0, yy, x0 + w, yy + dy - 16], fill=(240, 200, 60) if r_ % 2 == 0 else (70, 120, 170))
    # warps vertical over
    for c_ in range(nw + 1):
        xx = x0 + c_ * dx
        # draw warp segments over weft with alternating over/under
        for r_ in range(nhh):
            if (c_ + r_) % 2 == 0:
                yy = y0 + r_ * dy + 6
                dr.rectangle([xx - 3, yy, xx + 3, yy + dy - 12], fill=(200, 60, 60))
    label(dr, (x0 + w + 40, y0 + h / 2 - 14), "WARP =", font=FONT_S, anchor="lm")
    label(dr, (x0 + w + 40, y0 + h / 2 + 14), "vertical threads", font=FONT_S, anchor="lm")
    label(dr, ((x0 + w / 2), y0 - 30), "WEFT = horizontal threads", font=FONT_S)
    label(dr, (600, 560), "Over one, under one — plain weave. Twill and satin change the counting pattern (2/2, 4/1) to make diagonal or lustrous faces.", font=FONT_S)
    im.save(OUT / "weave-plain.png")


# ---------------- colour warm cool ----------------
def colour_warm_cool():
    im, dr = canvas(1200, 460)
    label(dr, (600, 40), "Warm and cool colours", font=FONT_B)
    warm = [(229, 57, 53), (240, 130, 34), (250, 200, 25), (231, 111, 81)]
    cool = [(35, 100, 165), (30, 150, 140), (75, 60, 150), (120, 50, 135)]
    for i, c in enumerate(warm):
        x = 180 + i * 110
        dr.ellipse([x, 140, x + 90, 230], fill=c, outline="#555555", width=3)
    for i, c in enumerate(cool):
        x = 180 + i * 110
        dr.ellipse([x, 280, x + 90, 370], fill=c, outline="#555555", width=3)
    label(dr, (140, 185), "Warm:", font=FONT_S, anchor="rm")
    label(dr, (140, 325), "Cool:", font=FONT_S, anchor="rm")
    label(dr, (600, 415), "Warm colours advance (come forward); cool colours recede (fall back).", font=FONT_S)
    im.save(OUT / "colour-warm-cool.png")


# ---------------- clay and pulp prep ----------------
def clay_pulp_prep():
    im, dr = canvas(1400, 460)
    label(dr, (700, 40), "Preparing clay and paper pulp", font=FONT_B)
    def box(k, title):
        x = 60 + k * 460
        frame(dr, [(x, 110, x + 420, 410)])
        label(dr, (x + 210, 140), title, font=FONT_S)
        return x
    x = box(0, "Clay — before use")
    for i in range(7):
        y = 190 + i * 8
        dr.ellipse([x + 60 + (i % 2) * 6, y, x + 320 - (i % 2) * 6, y + 22], fill=(200, 160, 130), outline="#7a5a45")
    label(dr, (x + 210, 300), ".remove air bubbles by kneading", font=FONT_S)
    label(dr, (x + 210, 330), "and wedging on a board", font=FONT_S)
    x = box(1, "Paper pulp")
    dr.ellipse([x + 90, 200, x + 330, 380], fill=(235, 230, 220), outline="#999999", width=3)
    for _ in range(60):
        import random
        random.seed()
        xx = random.randint(x + 110, x + 310)
        yy = random.randint(215, 360)
        dr.line([(xx, yy), (xx + random.randint(-16, 16), yy + random.randint(-6, 6))], fill="#BBBBBB", width=2)
    label(dr, (x + 210, 330), "shred paper, soak, squeeze, blend", font=FONT_S)
    label(dr, (x + 210, 358), "with water and glue", font=FONT_S)
    x = box(2, "Mould a form")
    mid = dr
    mid.ellipse([x + 120, 230, x + 320, 380], fill=(160, 130, 110), outline="#6a4a35", width=3)
    label(dr, (x + 220, 300), "build over a form, dry,", font=FONT_S)
    label(dr, (x + 220, 330), "then paint", font=FONT_S)
    im.save(OUT / "clay-pulp-prep.png")


# ---------------- assemblage / casting / folding ----------------
def caf_techniques():
    import random
    im, dr = canvas(1500, 470)
    label(dr, (750, 40), "Casting, folding, assemblage", font=FONT_B)
    def box(k, title):
        x = 50 + k * 500
        frame(dr, [(x, 110, x + 460, 410)])
        label(dr, (x + 230, 140), title, font=FONT_S)
        return x
    x = box(0, "Casting (hump / hollow)")
    dr.ellipse([x + 120, 220, x + 340, 350], fill=(180, 170, 160), outline="#665550", width=3)
    dr.ellipse([x + 150, 240, x + 280, 320], fill=(210, 200, 190), outline="#665550", width=2)
    dr.rectangle([x + 120, 380, x + 340, 398], fill=(120, 120, 120))
    label(dr, (x + 230, 375), "mould filled with paste, turned out", font=FONT_S)
    x = box(1, "Folding (crease, pleat, knot)")
    for i in range(7):
        dr.polygon([(x + 90 + i * 40, 360), (x + 110 + i * 40, 220), (x + 130 + i * 40, 360)],
                   fill=(120, 160, 200) if i % 2 == 0 else (150, 190, 230), outline="#557799")
    label(dr, (x + 230, 175), "paper or fabric pleated", font=FONT_S)
    x = box(2, "Assemblage / construction")
    random.seed(11)
    dr.rectangle([x + 150, 250, x + 330, 340], fill=(170, 120, 70), outline="#775533")
    for _ in range(10):
        xx = random.randint(x + 160, x + 320)
        yy = random.randint(255, 335)
        rw = random.randint(18, 40)
        dr.ellipse([xx, yy, xx + rw, yy + 14], fill=random.choice([(70, 130, 180), (200, 60, 60), (240, 190, 40)]))
    label(dr, (x + 230, 175), "found objects stitched, glued, stapled", font=FONT_S)
    im.save(OUT / "caf-techniques.png")


if __name__ == "__main__":
    colour_wheel()
    design_elements()
    design_principles()
    design_process()
    shading_techniques()
    shading_sphere()
    still_life_setup()
    hand_building()
    pattern_techniques()
    weave_plain()
    colour_warm_cool()
    clay_pulp_prep()
    caf_techniques()
    for f in sorted(OUT.glob("*.png")):
        print(f.name, f.stat().st_size)
