class BoundingRectangle:
    def __init__(self):
        self.points = []

    def add_point(self, x, y):
        self.points.append([x, y])

    def width(self):
        x = [i[0] for i in self.points]
        return max(x) - min(x)

    def height(self):
        y = [i[1] for i in self.points]
        return max(y) - min(y)

    def bottom_y(self):
        return min([i[1] for i in self.points])

    def top_y(self):
        return max([i[1] for i in self.points])

    def left_x(self):
        return min([i[0] for i in self.points])

    def right_x(self):
        return max([i[0] for i in self.points])


rect = BoundingRectangle()
rect.add_point(-1, -2)
rect.add_point(3, 4)
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())