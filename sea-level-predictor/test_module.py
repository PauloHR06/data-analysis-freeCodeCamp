import unittest
import sea_level_predictor
import numpy as np


class TestSeaLevelPlot(unittest.TestCase):

    def setUp(self):
        self.ax = sea_level_predictor.draw_plot() # gráfico

    def test_plot_title(self):
        # teste do título do gráfico
        title = self.ax.get_title()
        expected_title = "Rise in Sea Level"
        self.assertEqual(title, expected_title, "O título do gráfico deveria ser 'Rise in Sea Level'.")

    def test_plot_labels(self):
        # verifica os labels
        xlabel = self.ax.get_xlabel()
        expected_xlabel = "Year"
        self.assertEqual(xlabel, expected_xlabel, "O rótulo do eixo X deveria ser 'Year'.")

        ylabel = self.ax.get_ylabel()
        expected_ylabel = "Sea Level (inches)"
        self.assertEqual(ylabel, expected_ylabel, "O rótulo do eixo Y deveria ser 'Sea Level (inches)'.")

        # testa os valores no eixo X
        x_ticks = self.ax.get_xticks().tolist()
        expected_ticks = [1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0]
        self.assertEqual(x_ticks, expected_ticks, "Os valores esperados para os ticks do eixo X não correspondem.")

    def test_plot_data_points(self):
        # verifica se os pontos do gráfico estão corretos
        points = self.ax.get_children()[0].get_offsets().tolist()
        expected_points = [
            [1880.0, 0.0], [1881.0, 0.22], [1882.0, -0.44], [1883.0, -0.23], [1884.0, 0.59],
            [1885.0, 0.53], [1886.0, 0.44], [1887.0, 0.22], [1888.0, 0.30], [1889.0, 0.36], 
        ]
        np.testing.assert_almost_equal(points, expected_points, decimal=2, err_msg="Os pontos do gráfico estão incorretos.")

    def test_plot_trend_lines(self):
        # verifica os valores da primeira linha de tendência
        line1_data = self.ax.get_lines()[0].get_ydata().tolist()
        expected_line1 = [
            -0.54, -0.48, -0.42, -0.35, -0.29, -0.23, -0.16, -0.10, -0.04, 0.03,
        ]
        np.testing.assert_almost_equal(line1_data, expected_line1, decimal=2, err_msg="A primeira linha de tendência está incorreta.")

        # verifica os valores da segunda linha de tendência
        line2_data = self.ax.get_lines()[1].get_ydata().tolist()
        expected_line2 = [
            7.06, 7.23, 7.39, 7.56, 7.73, 7.89, 8.06, 8.23, 8.39, 8.56,
        ]
        np.testing.assert_almost_equal(line2_data, expected_line2, decimal=2, err_msg="A segunda linha de tendência está incorreta.")


if __name__ == "__main__":
    unittest.main()
