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
