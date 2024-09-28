import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters

# conversores do matplotlib
register_matplotlib_converters()

# carrega o dataframe.
data = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# filtra os dados e remove outliers
data_filtered = data[(data['value'] > data['value'].quantile(0.025)) & 
                     (data['value'] < data['value'].quantile(0.975))]

# método para criar um gráfico de linha
def create_line_plot():
    plt.figure(figsize=(18, 6))
    plt.plot(data_filtered, color='darkred')
    plt.title('Visualizações diárias do FreeCodeCamp Forum (05/2016 - 12/2019)')
    plt.xlabel('Data')
    plt.ylabel('Visualizações de página')

    # salva o gráfico.
    plt.savefig('line_plot_restructured.png')
    return plt.gcf()

# método para criar um gráfico de barras
def create_bar_plot():
    # duplica o dataframe.
    data_bar = data_filtered.copy()
    data_bar['Ano'] = data_bar.index.year
    data_bar['Mês'] = data_bar.index.month_name()

    # define a ordem dos meses
    ordem_meses = ["January", "February", "March", "April", "May", "June", "July", "August", 
                   "September", "October", "November", "December"]
    data_bar['Mês'] = pd.Categorical(data_bar['Mês'], categories=ordem_meses)

    # calcular a média de visualizações por ano e mês
    tabela_pivot = pd.pivot_table(data_bar, values='value', index='Ano', columns='Mês', aggfunc=np.mean) # tabela dinâmica

    # criar o gráfico de barras
    fig = tabela_pivot.plot(kind='bar', figsize=(10, 6)).get_figure()
    plt.xlabel('Anos')
    plt.ylabel('Média de Visualizações')
    plt.legend(title='Meses')

    # salvar o gráfico
    fig.savefig('bar_plot_restructured.png')
    return fig

# método para criar um gráfico de boxplot
def create_box_plot():
    # prepara os dados 
    data_box = data_filtered.copy().reset_index()
    data_box['Ano'] = data_box['date'].dt.year
    data_box['Mês'] = data_box['date'].dt.strftime('%b')

    # ordem dos meses abreviados
    meses_abreviados = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    data_box['Mês'] = pd.Categorical(data_box['Mês'], categories=meses_abreviados)

    # cria os box plots lado a lado
    fig, axes = plt.subplots(1, 2, figsize=(18, 6))
    
    sns.boxplot(x=data_box['Ano'], y=data_box['value'], ax=axes[0])
    axes[0].set_title('Box Plot por Ano (Tendência)')
    axes[0].set_xlabel('Ano')
    axes[0].set_ylabel('Visualizações de Página')

    sns.boxplot(x=data_box['Mês'], y=data_box['value'], ax=axes[1])
    axes[1].set_title('Box Plot por Mês (Sazonalidade)')
    axes[1].set_xlabel('Mês')
    axes[1].set_ylabel('Visualizações de Página')

    # salvar o gráfico
    fig.savefig('box_plot_restructured.png')
    return fig
