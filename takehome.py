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
        self.height = (start_y-end_y) + 1
        self.fill_char = fill_char
        self.create_shape()

    def create_shape(self):
        self.shape = []
        for num in range(self.start_y+1):
            if num < (self.end_y):
                row_str = " " * self.width
            else:
                row_str = (" " * (self.start_x)) + \
                    (self.fill_char * (self.width))
            self.shape.append(row_str)

    def change_fill_char(self, char):
        self.fill_char = char
        self.create_shape()

    def translate(self, axis, num):
        if axis == "x":
            if (self.start_x + num) < 0:
                print("x coordinate cannot be a negative number")
            else:
                self.start_x += num
                self.end_x += num
        elif axis == "y":
            if (self.end_y + num) < 0:
                print("y coordinate cannot be a negative number")
            else:
                self.start_y += num
                self.end_y += num
        self.create_shape()


s = Shape(1, 4, 3, 2, 'a')
for row in s.shape:
    print(row)
s.change_fill_char('b')
for row in s.shape:
    print(row)
s.translate('x', -5)
for row in s.shape:
    print(row)
