from PIL import Image
import numpy as np
from pathlib import Path


def analyze(path: Path) -> None:
    im = Image.open(path).convert("L")
    a = np.array(im)
    h, w = a.shape
    dark = a < 80

    horiz = 0
    for y in range(h):
        run = 0
        for x in range(w):
            if dark[y, x]:
                run += 1
                if run > horiz:
                    horiz = run
            else:
                run = 0

    vert = 0
    for x in range(w):
        run = 0
        for y in range(h):
            if dark[y, x]:
                run += 1
                if run > vert:
                    vert = run
            else:
                run = 0

    # Estimate "text-like" density: many small dark blobs
    # Sample 8x8 blocks
    bh, bw = max(1, h // 8), max(1, w // 8)
    textish = 0
    blocks = 0
    for by in range(0, h - bh + 1, bh):
        for bx in range(0, w - bw + 1, bw):
            block = dark[by : by + bh, bx : bx + bw]
            dens = block.mean()
            blocks += 1
            if 0.05 < dens < 0.45:
                textish += 1

    print(
        f"{path.name}: {w}x{h} dark%={dark.mean()*100:.1f} "
        f"h_run={horiz} v_run={vert} textish_blocks={textish}/{blocks}"
    )


if __name__ == "__main__":
    base = Path(r"W:\StaralexSchoolStudies\_eq_review")
    for p in sorted(base.glob("*.png")):
        analyze(p)
    print("--- lesson diagrams ---")
    root = Path(r"W:\StaralexSchoolStudies\Grade9-Maths")
    for p in sorted(root.rglob("diagrams/*.png")):
        analyze(p)
