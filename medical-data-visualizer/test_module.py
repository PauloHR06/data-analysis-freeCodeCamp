import unittest
import medical_data_visualizer
import matplotlib as mpl


# Teste para o gráfico categórico
class TestCategoricalPlot(unittest.TestCase):
    def setUp(self):
        # Configurar o gráfico categórico
        self.fig = medical_data_visualizer.draw_categorical_plot()
        self.ax = self.fig.axes[0]
    
    def test_categorical_plot_labels(self):
        # Verificar se os rótulos do gráfico estão corretos
        xlabel_actual = self.ax.get_xlabel()
        xlabel_expected = "variable"
        self.assertEqual(xlabel_actual, xlabel_expected, "Expected xlabel to be 'variable'")

        ylabel_actual = self.ax.get_ylabel()
        ylabel_expected = "count"
        self.assertEqual(ylabel_actual, ylabel_expected, "Expected ylabel to be 'count'")

        # Verificar os rótulos do eixo X
        xtick_labels = [label.get_text() for label in self.ax.get_xticklabels()]
        expected_labels = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
        self.assertEqual(xtick_labels, expected_labels, "Expected x-axis labels to be 'active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'.")

    def test_categorical_plot_bar_count(self):
        # Verificar o número de barras no gráfico
        bar_count_actual = len([rect for rect in self.ax.get_children() if isinstance(rect, mpl.patches.Rectangle)])
        bar_count_expected = 13  # Valor esperado (verifique se esse valor está correto)
        self.assertEqual(bar_count_actual, bar_count_expected, "Expected a different number of bars in the plot.")


# Teste para o mapa de calor
class TestHeatmapPlot(unittest.TestCase):
    def setUp(self):
        # Configurar o gráfico de mapa de calor
        self.fig = medical_data_visualizer.draw_correlation_heatmap()
        self.ax = self.fig.axes[0]

    def test_heatmap_labels(self):
        # Verificar os rótulos do mapa de calor
        xtick_labels_actual = [label.get_text() for label in self.ax.get_xticklabels()]
        xtick_labels_expected = ['id', 'age', 'gender', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio', 'overweight']
        self.assertEqual(xtick_labels_actual, xtick_labels_expected, "Expected heatmap x-axis labels to match.")

    def test_heatmap_values(self):
        # Verificar os valores no mapa de calor
        heatmap_values_actual = [text.get_text() for text in self.ax.get_default_bbox_extra_artists() if isinstance(text, mpl.text.Text)]
        print(heatmap_values_actual)
        heatmap_values_expected = ['0.0', '0.0', '-0.0', '0.0', '-0.1', '0.5', '0.0', '0.1', '0.1', '0.3', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.2', '0.1', '0.0', '0.2', '0.1', '0.0', '0.1', '-0.0', '-0.1', '0.1', '0.0', '0.2', '0.0', '0.1', '-0.0', '-0.0', '0.1', '0.0', '0.1', '0.4', '-0.0', '-0.0', '0.3', '0.2', '0.1', '-0.0', '0.0', '0.0', '-0.0', '-0.0', '-0.0', '0.2', '0.1', '0.1', '0.0', '0.0', '0.0', '0.0', '0.3', '0.0', '-0.0', '0.0', '-0.0', '-0.0', '-0.0', '0.0', '0.0', '-0.0', '0.0', '0.0', '0.0', '0.2', '0.0', '-0.0', '0.2', '0.1', '0.3', '0.2', '0.1', '-0.0', '-0.0', '-0.0', '-0.0', '0.1', '-0.1', '-0.1', '0.7', '0.0', '0.2', '0.1', '0.1', '-0.0', '0.0', '-0.0', '0.1']
        self.assertEqual(heatmap_values_actual, heatmap_values_expected, "Expected specific values in the heatmap.")


# Rodar os testes
if __name__ == "__main__":
    unittest.main()
