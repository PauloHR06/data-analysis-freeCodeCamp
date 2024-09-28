import time_series_visualizer # importa o código do visualizador de séries temporais.
from unittest import main # testes unitários

# testa as funções criadas
time_series_visualizer.draw_line_plot()
time_series_visualizer.draw_bar_plot()
time_series_visualizer.draw_box_plot()

# roda os testes unitários
main(module='test_module', exit=False)