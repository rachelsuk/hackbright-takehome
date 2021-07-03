class Canvas():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.canvas = []
        for num in range(self.height):
            row_str = " " * self.width
            self.canvas.append(row_str)

    def add_shape(self, shape):
        pass

    def clear_shapes(self):
        pass


class Shape():
    def __init__(self, start_x, start_y, end_x, end_y, fill_char):
        pass

    def change_fill_char(self, char):
        pass

    def translate(self, axis, num):
        pass
