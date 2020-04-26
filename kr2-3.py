from PIL import ImageDraw


class PierrotCapImageDraw(ImageDraw.ImageDraw):
    def __init__(self, img):
        super().__init__(img)
        self.img = img

    def cap(self, xy, fill):
        x, y, w, h = xy
        d = w // 5
        b = h // 3
        dr = ImageDraw.Draw(self.img)
        dr.polygon(((x, y),
                    (x + w / 2, y - h),
                    (x + w, y)),
                   fill=fill[1])
        dr.polygon(((x, y),
                    (x + w / 2, y - h),
                    (x + w / 2, y)),
                   fill=fill[0])
        dr.ellipse(((x + (w / 2 - d / 2), y - (b + d / 2)),
                    (x + (w / 2 + d / 2), y - (b - d / 2))),
                   fill=fill[-1])
        dr.ellipse(((x + (w / 2 - d / 2), y - (2 * b + d / 2)),
                    (x + (w / 2 + d / 2), y - (2 * b - d / 2))),
                   fill=fill[-1])
        dr.ellipse(((x + (w / 2 - d / 2), y - (h + d / 2)),
                    (x + (w / 2 + d / 2), y - (h - d / 2))),
                   fill=fill[-1])


img = Image.new('RGB', (200, 200), '#000000')
drw = PierrotCapImageDraw(img)
drw.cap((40, 190, 120, 160), ('#999999', '#ffffff', '#666666'))
img.save('result.png')