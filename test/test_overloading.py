import unittest

from overloading import overload


class OverloadingTest(unittest.TestCase):

    def test_func(self):
        @overload
        def divide(x: int, y: int) -> int:
            return x // y

        @overload
        def divide(x: float, y: float) -> float:
            return x / y

        self.assertEqual(divide(1, 2), 0)
        self.assertEqual(divide(1.0, 2.0), 0.5)

    def test_method(self):
        class Calculator:
            @overload
            def divide(self, x: int, y: int) -> int:
                return x // y

            @overload
            def divide(self, x: float, y: float) -> float:
                return x / y

        calc = Calculator()

        self.assertEqual(calc.divide(1, 2), 0)
        self.assertEqual(calc.divide(1.0, 2.0), 0.5)


if __name__ == "__main__":
    unittest.main()
