import unittest

def remainder_division(dividend, divisor):

    if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
        raise TypeError("Аргументы должны быть числами")
    if divisor == 0:
        raise ZeroDivisionError("Делить на ноль нельзя.")
    return dividend % divisor

class TestRemainderDivision(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(remainder_division(10, 3), 1)

    def test_zero_remainder(self):
        self.assertEqual(remainder_division(10, 5), 0)

    def test_negative_dividend(self):
        self.assertEqual(remainder_division(-10, 3), 2)

    def test_negative_divisor(self):
        self.assertEqual(remainder_division(10, -3), -2)

    def test_zero_divisor(self):
        with self.assertRaises(ZeroDivisionError):
            remainder_division(10, 0)

    def test_non_numeric_arguments(self):
        with self.assertRaises(TypeError):
            remainder_division("10", 3)
        with self.assertRaises(TypeError):
            remainder_division(10, "3")

if __name__ == '__main__':
    unittest.main()