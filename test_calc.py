import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(10, 5)

        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)
        self.assertEqual(result, 15)

    def test_subtract(self):
        result = calc.subtract(10, 5)

        self.assertEqual(result, 5)
        self.assertEqual(calc.subtract(-5, 3), -8)
        self.assertEqual(calc.subtract(-3, -3), 0)

    def test_multiply(self):
        result = calc.multiply(5, 5)

        self.assertEqual(result, 25)
        self.assertEqual(calc.multiply(3, -3), -9)
        self.assertEqual(calc.multiply(-2, -2), 4)

    def test_divide(self):
        result = calc.divide(6, 2)

        self.assertEqual(result, 3)
        self.assertEqual(calc.divide(-25, 5), -5)
        self.assertEqual(calc.divide(-36, -6), 6)
        self.assertEqual(calc.divide(5, 2), 2.5)

        with self.assertRaises(ValueError):  # use this context manager rather
            calc.divide(10, 0)


# To run unittest automatically when running the file.
if __name__ == "__main__":
    unittest.main()
