import pymupdf
from PIL import Image
import pathlib

out = pathlib.Path(r'data\extracted_questions\ict2020_pages')
d = pymupdf.open(r'data\harvested\Computing_ICT\pdf\Computing_ICT_2021_BECE-ICT-2020-QUESTIONS_e1044fc8.pdf')
for i in [6, 7, 8, 9]:
    pix = d[i].get_pixmap(dpi=150, colorspace=pymupdf.csGRAY)
    img = Image.frombytes('L', (pix.width, pix.height), pix.samples)
    # auto-contrast so faint strokes show, then crop to dark bbox
    import numpy as np
    a = np.asarray(img)
    dark = a < 170
    ys, xs = dark.nonzero()
    print(i + 1, 'dark px', int(dark.sum()), end=' ')
    if len(xs):
        pad = 30
        box = (max(0, int(xs.min()) - pad), max(0, int(ys.min()) - pad),
               min(img.width, int(xs.max()) + pad), min(img.height, int(ys.max()) + pad))
        img.crop(box).save(out / f'crop_{i+1:02d}.png')
        print('crop', box)
    else:
        print('blank')
