class Calculator(object):
    def __init__(self):
        self._last_answer = 0.0

    @property
    def last_answer(self):
        return self._last_answer

    def add(self, a, b):
        try:
            self._last_answer = a + b
        except TypeError:
            raise TypeError("Only integers are allowed")
        return self.last_answer

    def subtract(self, a, b):
        try:
            self._last_answer = a - b
        except TypeError:
            raise TypeError("Only integers are allowed")
        return self.last_answer

    def multiply(self, a, b):
        try:
            self._last_answer = a * b
        except TypeError:
            raise TypeError("Only integers are allowed")
        return self.last_answer

    def divide(self, a, b):
        try:
            self._last_answer = a / b
        except ZeroDivisionError:
            raise ZeroDivisionError("Can not divide by 0")
        return self.last_answer

    def maximum(self, a, b):
        try:
            self._last_answer = a if a >= b else b
        except TypeError:
            raise TypeError("Only integers are allowed")
        return self.last_answer

    def minimum(self, a, b):
        try:
            self._last_answer = a if a <= b else b
        except TypeError:
            raise TypeError("Only integers are allowed")
        return self.last_answer
