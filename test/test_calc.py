import unittest

from src.calc import Calculator

P_NUMBER_1 = 3
P_NUMBER_2 = 2
N_NUMBER_1 = -3
N_NUMBER_2 = -2


class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_last_answer_init(self):
        value = self.calc.last_answer
        self.assertEqual(value, 0.0)

    def test_add(self):
        value = self.calc.add(P_NUMBER_1, P_NUMBER_2)
        self.assertEqual(value, 5.0)
        self.assertEqual(value, self.calc.last_answer)

    def test_add_with_negative_number(self):
        value = self.calc.add(N_NUMBER_1, N_NUMBER_2)
        self.assertEqual(value, -5.0)
        self.assertEqual(value, self.calc.last_answer)

    def test_add_with_string(self):
        self.assertRaises(TypeError, self.calc.add, P_NUMBER_1, 'text')

    def test_subtract(self):
        self.assertRaises(TypeError, self.calc.subtract, P_NUMBER_1, None)

    def test_subtract_negative(self):
        value = self.calc.subtract(P_NUMBER_2, P_NUMBER_1)
        self.assertEqual(value, -1.0)
        self.assertEqual(value, self.calc.last_answer)

    def test_subtract_with_negative(self):
        value = self.calc.subtract(N_NUMBER_1, N_NUMBER_2)
        self.assertEqual(value, -1.0)
        self.assertEqual(value, self.calc.last_answer)

    def test_add_with_string(self):
        self.assertRaises(TypeError, self.calc.divide, P_NUMBER_1, 'text')

    def test_multiply(self):
        value = self.calc.multiply(P_NUMBER_1, P_NUMBER_2)
        self.assertEqual(value, 6.0)
        self.assertEqual(value, self.calc.last_answer)

    def test_divide(self):
        value = self.calc.divide(P_NUMBER_1, P_NUMBER_2)
        self.assertEqual(value, 1.5)
        self.assertEqual(value, self.calc.last_answer)

    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, self.calc.divide, P_NUMBER_1, 0)

    def test_max_greater(self):
        value = self.calc.maximum(P_NUMBER_1, P_NUMBER_2)
        self.assertEqual(value, P_NUMBER_1)
        self.assertEqual(value, self.calc.last_answer)

    def test_max_less(self):
        value = self.calc.maximum(P_NUMBER_2, P_NUMBER_1)
        self.assertEqual(value, P_NUMBER_1)
        self.assertEqual(value, self.calc.last_answer)

    def test_max_equal(self):
        value = self.calc.maximum(P_NUMBER_1, P_NUMBER_1)
        self.assertEqual(value, P_NUMBER_1)
        self.assertEqual(value, self.calc.last_answer)

    def test_min_greater(self):
        value = self.calc.minimum(P_NUMBER_1, P_NUMBER_2)
        self.assertEqual(value, P_NUMBER_2)
        self.assertEqual(value, self.calc.last_answer)

    def test_min_less(self):
        value = self.calc.minimum(P_NUMBER_2, P_NUMBER_1)
        self.assertEqual(value, P_NUMBER_2)
        self.assertEqual(value, self.calc.last_answer)

    def test_min_equal(self):
        value = self.calc.minimum(P_NUMBER_2, P_NUMBER_2)
        self.assertEqual(value, P_NUMBER_2)
        self.assertEqual(value, self.calc.last_answer)
