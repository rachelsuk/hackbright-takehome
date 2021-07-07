class Canvas():
    """A Canvas."""

    def __init__(self, height, width):
        """Initialize Canvas object"""
        self.height = height
        self.width = width
        self.shapes = []
        self.canvas_matrix = []
        self.clear_shapes()

    def print_canvas(self):
        """Print canvas drawing (with shapes) to console."""
        for row in self.canvas_matrix:
            print("".join(row))

    def add_shape(self, added_shape):
        """Add a shape object to the canvas."""
        self.shapes.append(added_shape)
        # clear canvas of all existing shapes and re-draw all shapes on canvas to
        # allow for correct rendering of shapes that were translated.
        self.clear_shapes()
        canvas_matrix = self.canvas_matrix
        # for each shape, go row by row in the canvas
        for shape in self.shapes:
            new_shape = shape.shape_matrix
            for index, row in enumerate(canvas_matrix):
                if index >= len(new_shape):
                    continue
                # start at end of new_shape array (bottom of the shape)
                shape_row = new_shape[-(index+1)]
                shape_index = 0
                while (shape_index < len(shape_row)) & (shape_index < len(row)):
                    if shape_row[shape_index] != ".":
                        row[shape_index] = shape_row[shape_index]
                    shape_index += 1
        # flip the canvas 180 degrees b/c bottom of the shape is at the top of
        # the canvas
        canvas_matrix.reverse()

        self.canvas_matrix = canvas_matrix

    def clear_shapes(self):
        """Clears canvas of all shapes."""
        self.canvas_matrix = []
        for num in range(self.height):
            row_str = ["." for x in range(self.width)]
            self.canvas_matrix.append(row_str)


class Shape():
    """A Shape."""

    def __init__(self, start_x, start_y, end_x, end_y, fill_char):
        """Initializes Shape object."""
        self.start_x = start_x
        self.end_x = end_x
        self.width = (end_x-start_x) + 1
        self.start_y = start_y
        self.end_y = end_y
        self.height = (start_y-end_y) + 1
        self.fill_char = fill_char
        self.create_shape()

    def print_shape(self):
        """Prints shape drawing to console."""
        for row in self.shape_matrix:
            print("".join(row))

    def create_shape(self):
        """Creates the shape drawing."""
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
        """Changes the fill character of the shape drawing."""
        self.fill_char = char
        self.create_shape()

    def translate(self, axis, num):
        """Translates the shape drawing."""
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


def create_canvas(height, width):
    """Creates blank canvas given height and width. Returns Canvas object."""
    new_canvas = Canvas(height, width)
    return new_canvas


def render_canvas(canvas):
    """Prints canvas drawing to console."""
    canvas.print_canvas()


def add_shape_to_canvas(canvas, shape):
    """Adds Shape object to Canvas."""
    canvas.add_shape(shape)


def clear_shapes(canvas):
    """Clears all shapes from canvas."""
    canvas.clear_shapes()
    canvas.shapes = []


def create_rectangle(start_x, start_y, end_x, end_y, fill_char):
    """Creates rectangle. Returns Rectangle object."""
    new_rect = Shape(start_x, start_y, end_x, end_y, fill_char)
    return new_rect


def change_fill_char(canvas, rect, char):
    """Changes fill char of a rectangle and sends changes to canvas."""
    canvas.shapes.remove(rect)
    rect.change_fill_char(char)
    canvas.add_shape(rect)


def translate(canvas, rect, axis, num):
    """Translates rectangle and sends changes to canvas."""
    canvas.shapes.remove(rect)
    rect.translate(axis, num)
    canvas.add_shape(rect)
