import unittest
from takehome import Canvas, Shape


class ShapeTestCase(unittest.TestCase):
    def test_create_shape(self):
        s = Shape(1, 1, 2, 0, "$")
        test_shape_matrix = [[".", "$", "$"], [".", "$", "$"]]
        self.assertEqual(s.shape_matrix, test_shape_matrix)


if __name__ == "__main__":
    unittest.main()
