"""High-res ASCII of one image region to inspect label legibility."""
from pathlib import Path
from PIL import Image
import numpy as np
import sys


def show(path: Path, box=None, cols=100) -> None:
    im = Image.open(path).convert("L")
    if box:
        im = im.crop(box)
    im.thumbnail((cols, 40))
    a = np.array(im)
    chars = " .:-=+*#%@"
    print(f"--- {path.name} crop={box} ---")
    for row in a:
        print("".join(chars[min(9, (255 - int(v)) * 10 // 256)] for v in row))


if __name__ == "__main__":
    png = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
        r"W:\StaralexSchoolStudies\Grade9-Maths\Strand-3-Geometry-And-Measurement\Substrand-1-Shapes-And-Space\Lesson-01-Polygons-And-Angle-Properties\diagrams\hexagon_angles_diagram.png"
    )
    show(png, cols=100)
    # label bands
    w, h = Image.open(png).size
    show(png, (0, 0, w, h // 4), cols=100)  # top labels
    show(png, (0, 3 * h // 4, w, h), cols=100)  # bottom labels
