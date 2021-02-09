class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def intersection(self, rect2):
        new_x = max(self.x, rect2.x)
        new_y = max(self.y, rect2.y)
        new_h = min(self.y + self.h, rect2.y + rect2.h) - new_y
        new_w = min(self.x + self.w, rect2.x + rect2.w) - new_x
        if new_h <= 0 or new_w <= 0:
            return None
        return Rectangle(new_x, new_y, new_w, new_h)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_w(self):
        return self.w

    def get_h(self):
        return self.h
