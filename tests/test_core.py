import unittest
import sympy as sp
from numerix.core import complex_numbers, algebra, calculus, matrices, statistics

class CoreTests(unittest.TestCase):
    def test_complex_add(self):
        self.assertEqual(complex_numbers.calculate("2+3*i","1-i","Add")["result"], 3+2*sp.I)
    def test_complex_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            complex_numbers.calculate("1+i","0","Divide")
    def test_factor(self):
        x=sp.Symbol("x")
        self.assertEqual(algebra.factor("x**2-4"), (x-2)*(x+2))
    def test_solve(self):
        self.assertEqual(set(algebra.solve("x**2-4=0")), {-2,2})
    def test_derivative(self):
        x=sp.Symbol("x")
        self.assertEqual(calculus.differentiate("x**3"), 3*x**2)
    def test_integral(self):
        x=sp.Symbol("x")
        self.assertEqual(calculus.integrate("2*x"), x**2)
    def test_determinant(self):
        self.assertEqual(matrices.calculate("1,2;3,4","","Determinant"), -2)
    def test_statistics_mean(self):
        self.assertEqual(statistics.describe([1,2,3])["Mean"], 2.0)

if __name__ == "__main__":
    unittest.main()
