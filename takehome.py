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
        self.start_x = start_x
        self.end_x = end_x
        self.width = (end_x-start_x) + 1
        self.start_y = start_y
        self.end_y = end_y
        self.height = (end_y-start_y) + 1
        self.fill_char = fill_char
        self.shape = []
        row_num = self.end_y
        for num in range(self.end_y+1):
            if row_num < (self.start_y):
                row_str = " " * self.width
            else:
                row_str = (" " * (self.start_x)) + \
                    (fill_char * (self.width))
            self.shape.append(row_str)
            row_num -= 1

    def change_fill_char(self, char):
        pass

    def translate(self, axis, num):
        pass


s = Shape(1, 2, 3, 4, 'a')
for row in s.shape:
    print(row)
