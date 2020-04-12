from math import sin, cos, pi
from PIL import ImageDraw
from PIL import Image


class MyImageDraw(ImageDraw.ImageDraw):

    def regular_polygon(self, center, sides, radius, rotation=0.0, fill=None, outline=None):
        ink, fill = self._getink(outline, fill)
        u = []
        ug = 2 * pi / sides
        a = rotation
        for i in range(sides):
            u.append(a)
            a += ug
        points = [(radius * sin(i) + center[0], radius * cos(i) + center[1]) for i in u]
        if fill is not None:
            self.draw.draw_polygon(points, fill, 1)
        if ink is not None and ink != fill:
            self.draw.draw_polygon(points, ink, 0)


im = Image.new('RGB', (400, 400))
dr = MyImageDraw(im)
dr.regular_polygon((200, 200), 5, 100, fill='blue', outline='white')
im.save('res.jpg')