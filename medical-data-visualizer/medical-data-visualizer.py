import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Carregar os dados
dados = pd.read_csv("medical_examination.csv")

# Adicionar a coluna 'sobrepeso'
IMC = dados['weight'] / ((dados['height'] / 100) ** 2)
dados['sobrepeso'] = (IMC > 25).astype(int)

# Normalizar os dados, fazendo com que 0 seja sempre bom e 1 sempre ruim. Se o valor de 'colesterol' ou 'glicose' for 1, o valor se torna 0. Se for maior que 1, o valor se torna 1.
dados['colesterol'] = dados['cholesterol'].replace([1, 2, 3], [0, 1, 1])
dados['glicose'] = dados['gluc'].replace([1, 2, 3], [0, 1, 1])

# Função para desenhar gráfico categórico
def desenhar_grafico_categorico():
    # Criar DataFrame para o gráfico categórico usando `pd.melt` com apenas os valores de 'colesterol', 'glicose', 'fumante', 'alco', 'ativo' e 'sobrepeso'.
    df_categoria = pd.melt(dados, id_vars=['cardio'], value_vars=['colesterol', 'glicose', 'smoke', 'alco', 'active', 'sobrepeso'])

    # Agrupar e reformatar os dados para separá-los por 'cardio'. Mostrar as contagens de cada característica. Você precisará renomear uma das colunas para que o gráfico funcione corretamente.
    df_categoria = pd.DataFrame(df_categoria.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total'))

    # Desenhar o gráfico categórico com 'sns.catplot()'
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_categoria, kind='bar').fig

    # Não modifique as duas próximas linhas
    fig.savefig('catplot.png')
    return fig


# Função para desenhar o mapa de calor
def desenhar_mapa_calor():
    # Limpar os dados
    df_mapa = dados[(dados['ap_lo'] <= dados['ap_hi'])
                    & (dados['height'] >= dados['height'].quantile(0.025))
                    & (dados['height'] <= dados['height'].quantile(0.975))
                    & (dados['weight'] >= dados['weight'].quantile(0.025))
                    & (dados['weight'] <= dados['weight'].quantile(0.975))]

    # Calcular a matriz de correlação
    correlacao = df_mapa.corr()

    # Gerar uma máscara para o triângulo superior
    mascara = np.zeros_like(correlacao)
    mascara[np.triu_indices_from(mascara)] = True

    # Configurar a figura do matplotlib
    fig, ax = plt.subplots(figsize=(12, 12))

    # Desenhar o mapa de calor com 'sns.heatmap()'
    ax = sns.heatmap(correlacao, linewidths=.5, annot=True, fmt='.1f', mask=mascara, square=True, center=0, vmin=-0.1, vmax=0.25, cbar_kws={'shrink': .45, 'format': '%.2f'})

    # Não modifique as duas próximas linhas
    fig.savefig('heatmap.png')
    return fig
