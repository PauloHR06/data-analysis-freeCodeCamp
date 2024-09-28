import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def generate_sea_level_plot():
    # carregar o dataframe.
    data = pd.read_csv('epa-sea-level.csv')

    # gera gráfico de dispersão
    fig, ax = plt.subplots()
    ax.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], s=8, color='blue')

    # primeira linha
    regression1 = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years_projection1 = np.arange(data['Year'].min(), 2051, 1)
    sea_levels_projection1 = regression1.intercept + regression1.slope * years_projection1
    ax.plot(years_projection1, sea_levels_projection1, label='Linha de Ajuste 1880-2050', color='firebrick')

    # Segunda linha  após 2000
    recent_data = data[data['Year'] >= 2000]
    regression2 = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    years_projection2 = np.arange(recent_data['Year'].min(), 2051, 1)
    sea_levels_projection2 = regression2.intercept + regression2.slope * years_projection2
    ax.plot(years_projection2, sea_levels_projection2, label='Linha de Ajuste 2000-2050', color='mediumseagreen')

    # rótulos e titutos do gráfico
    ax.set_xlabel('Ano')
    ax.set_ylabel('Nível do Mar (polegadas)')
    ax.set_title('Aumento do Nível do Mar')

    # salva o gráfico
    plt.legend()
    fig.savefig('sea_level_plot.png')
    return ax
