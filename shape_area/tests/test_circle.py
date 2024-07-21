import unittest
from shapes.circle import Circle

class TestCircle(unittest.TestCase):
    def test_area(self):
        circle = Circle(3)
        self.assertAlmostEqual(circle.area(), 28.274333882308138, places=5)

if __name__ == '__main__':
    unittest.main()