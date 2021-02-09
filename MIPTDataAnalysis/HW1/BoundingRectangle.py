class BoundingRectangle:
    def __init__(self):
        self.RIGHT = [None, None]
        self.TOP = [None, None]
        self.LEFT = [None, None]
        self.BOTTOM = [None, None]

    def add_point(self, x, y):
        if self.RIGHT[0] is None or x > self.RIGHT[0]:
            self.RIGHT = [x, y]
        if self.TOP[1] is None or y > self.TOP[1]:
            self.TOP = [x, y]
        if self.LEFT[0] is None or x < self.LEFT[0]:
            self.LEFT = [x, y]
        if self.BOTTOM[1] is None or y < self.BOTTOM[1]:
            self.BOTTOM = [x, y]

    def width(self):
        return self.RIGHT[0] - self.LEFT[0]

    def height(self):
        return self.TOP[1] - self.BOTTOM[1]

    def bottom_y(self):
        return self.BOTTOM[1]

    def top_y(self):
        return self.TOP[1]

    def left_x(self):
        return self.LEFT[0]

    def right_x(self):
        return self.RIGHT[0]


