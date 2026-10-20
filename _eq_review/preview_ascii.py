"""Coarse ASCII preview of each PNG so we can 'see' layout without vision."""
from pathlib import Path
from PIL import Image
import numpy as np


def preview(path: Path, cols: int = 72) -> None:
    im = Image.open(path).convert("L")
    im.thumbnail((cols, 36))
    a = np.array(im)
    chars = " .:-=+*#%@"
    print(f"\n===== {path.name}  ({Image.open(path).size}) =====")
    for row in a:
        line = "".join(chars[min(9, (255 - int(v)) * 10 // 256)] for v in row)
        print(line)


if __name__ == "__main__":
    base = Path(r"W:\StaralexSchoolStudies\_eq_review\compare")
    for name in [
        "PNG_hexagon_angles_diagram.png",
        "PNG_probability_tree_two_stage.png",
        "PNG_place_value_chart.png",
        "PNG_congruent_triangles_schema.png",
        "PNG_pie_chart_salary.png",
        "PNG_parallel_lines_find_mon_57_105.png",
    ]:
        preview(base / name)
