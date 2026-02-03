import unittest
from app.operations import add, sub, mul, div

class TestOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_sub(self):
        self.assertEqual(sub(5, 2), 3)

    def test_mul(self):
        self.assertEqual(mul(4, 3), 12)

    def test_div(self):
        self.assertEqual(div(10, 2), 5)

    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(1, 0)
