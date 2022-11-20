import unittest

from src.calc import Calculator

NUMBER_1 = 3
NUMBER_2 = 2


class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_last_answer_init(self):
        value = self.calc.last_answer
        self.assertEqual(value, 0.0)

    def test_add(self):
        value = self.calc.add(NUMBER_1, NUMBER_2)
        self.assertEqual(value, 5.0)
        self.assertEqual(value, self.calc.last_answer)

    def test_subtract(self):
        value = self.calc.subtract(NUMBER_1, NUMBER_2)
        self.assertEqual(value, 1.0)
        self.assertEqual(value, self.calc.last_answer)

    def test_subtract_negative(self):
        value = self.calc.subtract(NUMBER_2, NUMBER_1)
        self.assertEqual(value, -1.0)
        self.assertEqual(value, self.calc.last_answer)

    def test_multiply(self):
        value = self.calc.multiply(NUMBER_1, NUMBER_2)
        self.assertEqual(value, 6.0)
        self.assertEqual(value, self.calc.last_answer)

    def test_divide(self):
        value = self.calc.divide(NUMBER_1, NUMBER_2)
        self.assertEqual(value, 1.5)
        self.assertEqual(value, self.calc.last_answer)


