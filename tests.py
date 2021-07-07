import unittest
from takehome import Canvas, Shape
import takehome


class ShapeTestCase(unittest.TestCase):
    def test_create_shape(self):
        s = Shape(1, 1, 2, 0, "$")
        test_shape_matrix = [[" ", "$", "$"], [" ", "$", "$"]]
        self.assertEqual(s.shape_matrix, test_shape_matrix)

    def test_add_shape(self):
        c = Canvas(2, 3)
        s = Shape(1, 1, 2, 0, "$")
        takehome.add_shape_to_canvas(c, s)
        test_canvas_matrix = [[" ", "$", "$"], [" ", "$", "$"]]
        self.assertEqual(c.canvas_matrix, test_canvas_matrix)


if __name__ == "__main__":
    unittest.main()
