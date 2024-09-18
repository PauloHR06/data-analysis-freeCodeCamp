import numpy as np

def calculate(list):
    # verifica a prsença de 9 elementos.
    if len(list) != 9:
        raise ValueError("A lista deve conter exatamente nove elementos.")
    
    # matriz 3x3
    matrix_3x3 = np.array(list).reshape(3, 3)

    # resultados.
    status = {}

    # média.
    status['media'] = [matrix_3x3.mean(axis=0).tolist(),
                      matrix_3x3.mean(axis=1).tolist(),
                      matrix_3x3.mean()]

    # variância.
    status['variancia'] = [matrix_3x3.var(axis=0).tolist(),
                          matrix_3x3.var(axis=1).tolist(),
                          matrix_3x3.var()]

    # desvio padrão.
    status['desvio_padrao'] = [matrix_3x3.std(axis=0).tolist(),
                              matrix_3x3.std(axis=1).tolist(),
                              matrix_3x3.std()]

    # V max
    status['maximo'] = [matrix_3x3.max(axis=0).tolist(),
                       matrix_3x3.max(axis=1).tolist(),
                       matrix_3x3.max()]

    # V min
    status['minimo'] = [matrix_3x3.min(axis=0).tolist(),
                       matrix_3x3.min(axis=1).tolist(),
                       matrix_3x3.min()]

    # soma.
    status['soma'] = [matrix_3x3.sum(axis=0).tolist(),
                     matrix_3x3.sum(axis=1).tolist(),
                     matrix_3x3.sum()]

    return status;
