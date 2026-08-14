import unittest
from main import evaluator

class TestEvaluator(unittest.TestCase):

    # ---------- Basic arithmetic ----------
    def test_addition(self):
        self.assertEqual(evaluator.evaluate("2 + 3"), 5)

    def test_subtraction(self):
        self.assertEqual(evaluator.evaluate("10 - 4"), 6)

    def test_multiplication(self):
        self.assertEqual(evaluator.evaluate("6 * 7"), 42)

    def test_division(self):
        self.assertEqual(evaluator.evaluate("15 / 3"), 5)

    def test_float_division(self):
        self.assertEqual(evaluator.evaluate("7 / 2"), 3.5)

    # ---------- Operator precedence ----------
    def test_operator_precedence(self):
        self.assertEqual(evaluator.evaluate("2 + 3 * 4"), 14)

    def test_precedence_with_division(self):
        self.assertEqual(evaluator.evaluate("10 - 6 / 2"), 7)

    def test_left_to_right_same_precedence(self):
        self.assertEqual(evaluator.evaluate("20 / 2 / 2"), 5)
        self.assertEqual(evaluator.evaluate("10 - 4 - 2"), 4)
        self.assertEqual(evaluator.evaluate("24 / 2 / 3 / 2"), 2)
        self.assertEqual(evaluator.evaluate("10 - 2 + 3"), 11)

    # ---------- Parentheses ----------
    def test_parentheses(self):
        self.assertEqual(evaluator.evaluate("(2 + 3) * 4"), 20)

    def test_nested_parentheses(self):
        self.assertEqual(evaluator.evaluate("((2 + 3) * (4 - 1))"), 15)

    def test_parentheses_change_precedence(self):
        self.assertEqual(evaluator.evaluate("2 * (3 + 4)"), 14)

    # ---------- Edge cases ----------
    def test_single_number(self):
        self.assertEqual(evaluator.evaluate("42"), 42)

    def test_zero(self):
        self.assertEqual(evaluator.evaluate("0"), 0)

    def test_negative_result(self):
        self.assertEqual(evaluator.evaluate("3 - 10"), -7)

    # ---------- Division by zero ----------
    def test_division_by_zero_raises(self):
        with self.assertRaises(Exception):
            evaluator.evaluate("5 / 0")

    def test_division_by_zero_expression(self):
        with self.assertRaises(Exception):
            evaluator.evaluate("(2 + 3) / (5 - 5)")

    # ---------- Variables ----------
    def test_variable_assignment(self):
        self.assertEqual(evaluator.evaluate("x = 5"), 5)
        self.assertEqual(evaluator.evaluate("x * 2"), 10)

    def test_variable_reassignment(self):
        self.assertEqual(evaluator.evaluate("y = 10"), 10)
        self.assertEqual(evaluator.evaluate("y = 20"), 20)
        self.assertEqual(evaluator.evaluate("y"), 20)

    def test_multiple_variables(self):
        self.assertEqual(evaluator.evaluate("a = 3"), 3)
        self.assertEqual(evaluator.evaluate("b = 4"), 4)
        self.assertEqual(evaluator.evaluate("a + b"), 7)

    def test_variable_in_expression(self):
        self.assertEqual(evaluator.evaluate("n = 8"), 8)
        self.assertEqual(evaluator.evaluate("(n + 2) * 3"), 30)

    def test_undefined_variable(self):
        with self.assertRaises(Exception):
            evaluator.evaluate("undefined_var + 1")

if __name__ == "__main__":
    unittest.main()