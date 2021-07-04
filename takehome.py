class Canvas():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.canvas_matrix = []
        for num in range(self.height):
            row_str = ["." for x in range(self.width)]
            self.canvas_matrix.append(row_str)

    def add_shape(self, shape):
        new_shape = shape.shape_matrix
        canvas_matrix = self.canvas_matrix
        canvas_matrix.reverse()
        new_canvas_matrix = []
        for row in canvas_matrix:
            new_row = row
            if new_shape == []:
                new_canvas_matrix.append(new_row)
                continue
            shape_row = new_shape.pop()
            shape_index = 0
            while shape_index < len(shape_row):
                if shape_row[shape_index] != ".":
                    new_row[shape_index] = shape_row[shape_index]
                shape_index += 1
            new_canvas_matrix.append(new_row)

        new_canvas_matrix.reverse()

        self.canvas_matrix = new_canvas_matrix

    def clear_shapes(self):
        self.canvas_matrix = []
        for num in range(self.height):
            row_str = ["." for x in range(self.width)]
            self.canvas_matrix.append(row_str)


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
        self.shape_matrix = []
        row_num = self.start_y
        for num in range(self.start_y+1):
            if row_num < (self.end_y):
                row_str = ["." for x in range(self.end_x + 1)]
            else:
                row_str = ["." for x in range(self.start_x)] + \
                    [self.fill_char for x in range(self.width)]
            self.shape_matrix.append(row_str)
            row_num -= 1

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


c = Canvas(10, 10)
# for row in c.canvas_matrix:
#     print(row)
s = Shape(1, 4, 3, 2, 'a')
for row in s.shape_matrix:
    print(row)
s.change_fill_char('b')
# for row in s.shape_matrix:
#     print(row)
s.translate('y', 6)
# for row in s.shape_matrix:
#     print(row)
c.add_shape(s)
for row in c.canvas_matrix:
    print(row)
s2 = Shape(2, 5, 3, 2, 'a')
for row in s2.shape_matrix:
    print(row)
c.add_shape(s2)
for row in c.canvas_matrix:
    print(row)
c.clear_shapes()
for row in c.canvas_matrix:
    print(row)
