"""Crop label regions at full res and report dark-pixel counts."""
from pathlib import Path
from PIL import Image
import numpy as np


def crop_stats(path: Path, boxes: dict[str, tuple[int, int, int, int]]) -> None:
    im = Image.open(path).convert("L")
    print(f"\n{path.name} full={im.size}")
    for name, box in boxes.items():
        region = im.crop(box)
        a = np.array(region)
        dark = (a < 100).sum()
        print(f"  {name:20s} box={box} dark_px={dark} mean={a.mean():.1f}")
        out = path.parent / f"crop_{path.stem}_{name}.png"
        Image.open(path).convert("RGB").crop(box).save(out)


if __name__ == "__main__":
    base = Path(r"W:\StaralexSchoolStudies\_eq_review\compare")
    crop_stats(
        base / "PNG_hexagon_angles_diagram.png",
        {
            "label_120": (0, 500, 220, 620),
            "label_5x": (520, 520, 891, 650),
            "label_4x": (680, 280, 891, 420),
            "label_7x": (480, 0, 780, 120),
            "label_8x": (100, 0, 420, 120),
            "label_6x": (0, 250, 160, 400),
            "caption": (150, 620, 750, 749),
        },
    )
    crop_stats(
        base / "PNG_place_value_chart.png",
        {
            "headers": (0, 40, 758, 120),
            "digits": (0, 120, 758, 200),
            "captions": (0, 200, 758, 310),
        },
    )
    crop_stats(
        base / "PNG_congruent_triangles_schema.png",
        {
            "left_angles": (80, 0, 280, 120),
            "right_angles": (520, 0, 780, 120),
            "caption": (200, 320, 750, 393),
        },
    )
