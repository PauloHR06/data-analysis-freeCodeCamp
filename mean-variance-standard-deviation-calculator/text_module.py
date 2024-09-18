import unittest
import mean_var_std

class UnitTests(unittest.TestCase):

    # teste 1: valida os cálculos.
    def test_calculate(self):
        actual = mean_var_std.calculate([3, 7, 1, 9, 2, 4, 6, 5, 8])
        expected = {
            'mean': [[6.0, 4.666666666666667, 4.333333333333333], 
                     [3.6666666666666665, 5.0, 6.333333333333333], 
                     5.0],
            'variance': [[6.0, 6.888888888888889, 9.555555555555555], 
                         [7.555555555555555, 6.666666666666667, 4.222222222222222], 
                         6.888888888888889],
            'standard deviation': [[2.449489742783178, 2.6246692913372702, 3.091206165165235], 
                                   [2.748737083745107, 2.581988897471611, 2.0548046676563256], 
                                   2.6246692913372702],
            'max': [[9, 7, 8], 
                    [7, 9, 8], 
                    9],
            'min': [[3, 2, 1], 
                    [1, 2, 4], 
                    1],
            'sum': [[18, 14, 13], 
                    [11, 15, 19], 
                    45]
        }
        self.assertAlmostEqual(actual, expected, "Resultado diferente do esperado ao chamar 'calculate()' com '[3,7,1,9,2,4,6,5,8]'")

    # teste 2: erro quando a lista tem menos de 9 elementos.
    def test_calculate_with_few_digits(self):
        self.assertRaisesRegex(ValueError, "List must contain nine numbers.", mean_var_std.calculate, [3, 7, 1, 9, 2, 4, 6])

if __name__ == "__main__":
    unittest.main()
