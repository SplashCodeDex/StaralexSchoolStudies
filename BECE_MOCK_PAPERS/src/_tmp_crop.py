import pymupdf
import numpy as np

d = pymupdf.open(r'data\harvested\Computing_ICT\pdf\Computing_ICT_2021_BECE-ICT-2020-QUESTIONS_e1044fc8.pdf')
for i in [6, 7, 8, 9]:
    pix = d[i].get_pixmap(dpi=100, colorspace=pymupdf.csGRAY)
    a = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.stride)[:, :pix.width]
    dark = a < 200
    ys, xs = dark.nonzero()
    if len(xs):
        print(i + 1, 'dark px', int(dark.sum()), 'bbox',
              int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max()))
        # crop that region and save enlarged
        x0, y0, x1, y1 = xs.min(), ys.min(), xs.max(), ys.max()
        pad = 20
        crop = a[max(0, y0 - pad):y1 + pad, max(0, x0 - pad):x1 + pad]
        out = pymupdf.Pixmap(pymupdf.csGRAY, pymupdf.IRect(0, 0, crop.shape[1], crop.shape[0]))
        out.set_rect(out.irect, 255)
        sub = bytearray(crop.tobytes())
        pix_img = pymupdf.Pixmap(pymupdf.csGRAY, pymupdf.IRect(0, 0, crop.shape[1], crop.shape[0]), False)
        pix_img.clear_with(255)
        # simpler: save via PIL-free numpy->png using pymupdf from buffer
        img = pymupdf.Pixmap(pymupdf.csGRAY, pymupdf.IRect(0, 0, crop.shape[1], crop.shape[0]), True)
        img.set_rect(img.irect, 255)
        # write bytes manually
        import pathlib
        arr = np.full(img.height * img.stride, 255, np.uint8)
        arr = arr.reshape(img.height, img.stride)
        arr[:crop.shape[0], :crop.shape[1]] = crop
        p2 = pymupdf.Pixmap(pymupdf.csGRAY, pymupdf.IRect(0, 0, crop.shape[1], crop.shape[0]))
        p2.set_rect(p2.irect, 255)
        png = pymupdf.Pixmap(np.array([255]) and p2)  # placeholder
        pathlib.Path(rf'data\extracted_questions\ict2020_pages\crop_{i+1:02d}.png').write_bytes(
            pymupdf.Pixmap(pymupdf.csGRAY, pymupdf.IRect(0, 0, crop.shape[1], crop.shape[0])) and b'')
    else:
        print(i + 1, 'dark px 0')
