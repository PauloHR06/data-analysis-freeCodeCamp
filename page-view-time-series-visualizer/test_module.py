import unittest
import time_series_visualizer
import matplotlib as mpl

# teste a criação do gráfico de linhas
class TestLinePlot(unittest.TestCase):
    def setUp(self):
        self.figure = time_series_visualizer.create_line_plot() # atributo da figura
        self.axis = self.figure.axes[0] # atributo dos eixos

    # teste para checkar se o nome está ok.
    def test_line_plot_title(self):
        actual_title = self.axis.get_title()
        expected_title = "Visualizações diárias do FreeCodeCamp Forum (05/2016 - 12/2019)"
        self.assertEqual(actual_title, expected_title, "O título do gráfico de linha deve ser 'Visualizações diárias do FreeCodeCamp Forum (05/2016 - 12/2019)'")

    # teste se o eixo X e Y
    def test_line_plot_axis_labels(self):
        actual_xlabel = self.axis.get_xlabel()
        expected_xlabel = "Data"
        self.assertEqual(actual_xlabel, expected_xlabel, "O rótulo do eixo X deve ser 'Data'")
        
        actual_ylabel = self.axis.get_ylabel()
        expected_ylabel = "Visualizações de Página"
        self.assertEqual(actual_ylabel, expected_ylabel, "O rótulo do eixo Y deve ser 'Visualizações de Página'")

    # teste do número de pontos no gráfico
    def test_line_plot_data_points(self):
        actual_data_points = len(self.axis.lines[0].get_ydata())
        expected_data_points = 1238
        self.assertEqual(actual_data_points, expected_data_points, "O número de pontos de dados no gráfico de linha deve ser 1238.")

class TestBarPlot(unittest.TestCase):
    def setUp(self):
        self.figure = time_series_visualizer.create_bar_plot() # atributo da figura
        self.axis = self.figure.axes[0] # atributo dos eixos

    # verifica a legenda
    def test_bar_plot_legend(self):
        actual_labels = [label.get_text() for label in self.axis.get_legend().get_texts()]
        expected_labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        self.assertEqual(actual_labels, expected_labels, "Os rótulos da legenda devem ser os meses do ano.")

    # verifica o eixo X e Y
    def test_bar_plot_axes_labels(self):
        actual_xlabel = self.axis.get_xlabel()
        expected_xlabel = "Anos"
        self.assertEqual(actual_xlabel, expected_xlabel, "O rótulo do eixo X deve ser 'Anos'")
        
        actual_ylabel = self.axis.get_ylabel()
        expected_ylabel = "Média de Visualizações"
        self.assertEqual(actual_ylabel, expected_ylabel, "O rótulo do eixo Y deve ser 'Média de Visualizações'")

    def test_bar_plot_x_axis_ticks(self):
        actual_ticks = [tick.get_text() for tick in self.axis.get_xaxis().get_majorticklabels()]
        expected_ticks = ['2016', '2017', '2018', '2019']
        self.assertEqual(actual_ticks, expected_ticks, "Os rótulos no eixo X devem ser '2016', '2017', '2018', '2019'.")

    # teste do número de barras
    def test_bar_plot_number_of_bars(self):
        actual_bars = len([element for element in self.axis.get_children() if isinstance(element, mpl.patches.Rectangle)])
        expected_bars = 49
        self.assertEqual(actual_bars, expected_bars, "O número esperado de barras no gráfico deve ser 49.")

# teste do gráfico boxplot
class TestBoxPlot(unittest.TestCase):
    def setUp(self):
        self.figure = time_series_visualizer.create_box_plot() # figuta
        self.axis_year = self.figure.axes[0] # eixo 'ano'
        self.axis_month = self.figure.axes[1] # eixo 'mês'

    # número de gráficos
    def test_number_of_plots(self):
        actual_plots = len(self.figure.get_axes())
        expected_plots = 2
        self.assertEqual(actual_plots, expected_plots, "O número de gráficos deve ser 2.")

    # teste dos eixos
    def test_box_plot_labels(self):
        actual_xlabel_year = self.axis_year.get_xlabel()
        expected_xlabel_year = "Ano"
        self.assertEqual(actual_xlabel_year, expected_xlabel_year, "O rótulo do eixo X do gráfico de anos deve ser 'Ano'.")
        
        actual_ylabel_year = self.axis_year.get_ylabel()
        expected_ylabel_year = "Visualizações de Página"
        self.assertEqual(actual_ylabel_year, expected_ylabel_year, "O rótulo do eixo Y do gráfico de anos deve ser 'Visualizações de Página'.")

        actual_xlabel_month = self.axis_month.get_xlabel()
        expected_xlabel_month = "Mês"
        self.assertEqual(actual_xlabel_month, expected_xlabel_month, "O rótulo do eixo X do gráfico de meses deve ser 'Mês'.")
        
        actual_ylabel_month = self.axis_month.get_ylabel()
        expected_ylabel_month = "Visualizações de Página"
        self.assertEqual(actual_ylabel_month, expected_ylabel_month, "O rótulo do eixo Y do gráfico de meses deve ser 'Visualizações de Página'.")

    # teste dos títulos
    def test_box_plot_titles(self):
        actual_title_year = self.axis_year.get_title()
        expected_title_year = "Box Plot por Ano (Tendência)"
        self.assertEqual(actual_title_year, expected_title_year, "O título do gráfico de anos deve ser 'Box Plot por Ano (Tendência)'.")

        actual_title_month = self.axis_month.get_title()
        expected_title_month = "Box Plot por Mês (Sazonalidade)"
        self.assertEqual(actual_title_month, expected_title_month, "O título do gráfico de meses deve ser 'Box Plot por Mês (Sazonalidade)'.")

    # teste do número de boxplot
    def test_number_of_boxes(self):
        actual_boxes_year = len(self.axis_year.lines) // 6  # Cada boxplot tem 6 linhas
        expected_boxes_year = 4
        self.assertEqual(actual_boxes_year, expected_boxes_year, "O número esperado de boxplots no gráfico de anos deve ser 4.")

        actual_boxes_month = len(self.axis_month.lines) // 6
        expected_boxes_month = 12
        self.assertEqual(actual_boxes_month, expected_boxes_month, "O número esperado de boxplots no gráfico de meses deve ser 12.")

if __name__ == "__main__":
    unittest.main()
