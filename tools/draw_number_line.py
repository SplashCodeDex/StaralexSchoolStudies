#!/usr/bin/env python3
"""Draw textbook number lines as PNG.

Layout (locked with user):
- The number line (axis with ticks and labels) is the base.
- The SOLUTION RAY (dot + arrow) sits slightly ABOVE the axis.
- No caption text is drawn into the image.
- Positions are exact: pass numeric values, not eyeballed pixel offsets.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

FONT = Path(r"C:\Windows\Fonts\cambria.ttc")


def _font(size: int):
    try:
        return ImageFont.truetype(str(FONT), size, index=0)
    except Exception:
        return ImageFont.load_default()


def draw_number_line(
    out: Path,
    lo: float = -3,
    hi: float = 5,
    ticks: list[float] | None = None,
    solid: dict[float, bool] | None = None,
    arrow: str = "right",
    ray: tuple[float, float] | None = None,
    labels: dict[float, str] | None = None,
    width: int = 1200,
    height: int = 170,
) -> None:
    """ray=(start, end): the solution interval drawn ABOVE the axis.

    solid: {value: True=filled dot, False=open circle}
    """
    solid = solid or {}
    img = Image.new("RGB", (width, height), "white")
    d = ImageDraw.Draw(img)
    font = _font(26)
    font_s = _font(20)

    pad_l, pad_r = 55, 55
    y_axis = height - 55  # axis near the bottom; solution ray above
    y_ray = y_axis - 38   # slightly above the axis
    x0, x1 = pad_l, width - pad_r
    span = (hi - lo) or 1

    def px(v: float) -> float:
        return x0 + (v - lo) / span * (x1 - x0)

    # ---- solution ray above the axis ----
    if ray:
        a, b = ray
        d.line([(px(a), y_ray), (px(b), y_ray)], fill="#1F4E79", width=7)
        # arrow head at the open end of the ray
        if arrow == "right" and b >= hi - 1e-9:
            d.polygon(
                [(px(b) + 14, y_ray), (px(b), y_ray - 10), (px(b), y_ray + 10)],
                fill="#1F4E79",
            )
        elif arrow == "left" and a <= lo + 1e-9:
            d.polygon(
                [(px(a) - 14, y_ray), (px(a), y_ray - 10), (px(a), y_ray + 10)],
                fill="#1F4E79",
            )

    # ---- dots on the ray ----
    for v, filled in solid.items():
        x = px(v)
        r = 12
        if filled:
            d.ellipse([x - r, y_ray - r, x + r, y_ray + r], fill="#1F4E79", outline="#1F4E79", width=3)
        else:
            d.ellipse([x - r, y_ray - r, x + r, y_ray + r], fill="white", outline="#1F4E79", width=3)

    # ---- axis ----
    d.line([(x0, y_axis), (x1, y_axis)], fill="#1A1A1A", width=3)
    if arrow in ("right", "both"):
        d.polygon([(x1 + 2, y_axis), (x1 - 14, y_axis - 8), (x1 - 14, y_axis + 8)], fill="#1A1A1A")
    if arrow in ("left", "both"):
        d.polygon([(x0 - 2, y_axis), (x0 + 14, y_axis - 8), (x0 + 14, y_axis + 8)], fill="#1A1A1A")

    # ---- ticks + labels ----
    if ticks is None:
        step = 1 if span <= 12 else max(1, int(round(span / 8)))
        ticks = []
        v = int(lo)
        while v <= hi + 1e-9:
            ticks.append(float(v))
            v += step
    for v in ticks:
        x = px(v)
        d.line([(x, y_axis - 7), (x, y_axis + 7)], fill="#1A1A1A", width=2)
        lbl = (labels or {}).get(v, str(int(v)) if float(v).is_integer() else str(v))
        w = d.textbbox((0, 0), lbl, font=font_s)[2]
        d.text((x - w / 2, y_axis + 12), lbl, fill="#1A1A1A", font=font_s)

    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out)

    # ---- self-check (see tools/README-figures.md §3) ----
    issues = []
    if labels:
        issues.append("labels= is deprecated; axis ticks are drawn automatically — do not bake extra text into figures")
    if solid and ray is None:
        issues.append("dots given without --ray: the solution ray must sit above the axis")
    if ray is not None:
        a, b = ray
        for v in solid:
            if not (min(a, b) - 1e-6 <= v <= max(a, b) + 1e-6):
                issues.append(f"dot at {v} lies outside the ray {ray}")
    if issues:
        print("SELF-CHECK:")
        for s in issues:
            print("  !", s)
    else:
        print("self-check: ok (no baked captions, ray above axis, dots on ray)")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("out")
    p.add_argument("--lo", type=float, default=-3)
    p.add_argument("--hi", type=float, default=5)
    p.add_argument("--solid", default="", help="comma values with filled dots")
    p.add_argument("--open", default="", help="comma values with open circles")
    p.add_argument("--ray", default="", help="start,end of the solution ray above the axis")
    p.add_argument("--arrow", default="right", choices=["right", "left", "none", "both"])
    args = p.parse_args()

    solid: dict[float, bool] = {}
    for v in args.solid.split(","):
        if v.strip():
            solid[float(v)] = True
    for v in args.open.split(","):
        if v.strip():
            solid[float(v)] = False
    ray = None
    if args.ray:
        a, b = args.ray.split(",")
        ray = (float(a), float(b))
    draw_number_line(
        Path(args.out), lo=args.lo, hi=args.hi, solid=solid, arrow=args.arrow, ray=ray
    )
    print("wrote", args.out)
