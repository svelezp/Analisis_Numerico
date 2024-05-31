import numpy as np


def gauss_simple(a, b, n):
    # Se crea la matriz aumentada
    ab = to_aug(a, b)
    # Primer loop, numero de etapas K
    for k in range(n - 1):
        # Segundo loop, numero de filas i
        for i in range(k + 1, n):
            # Se calcula el multiplicador
            multiplicador = ab[i][k] / ab[k][k]
            # Tercer loop, numero de columnas j
            for j in range(k, n + 1):
                # Se realiza la operacion de eliminacion a base del multiplicador
                ab[i][j] -= multiplicador * ab[k][j]
    xvalues = regressive_substitution(ab, n)
    return ab, xvalues


def to_aug(a, b):
    # Se convierte la matriz a en una matriz aumentada
    return np.column_stack((a, b))


def regressive_substitution(ab, n):
    # Incializa el array de x con el numero de X de la matriz
    x = np.zeros(n)
    # Se calcula el valor de la primera x
    x[n] = ab[n][n + 1] / ab[n][n]
    # Loop de la sustitucion regresiva, decrementa cada vez en -1
    for i in range(n - 1, 0, -1):
        # Se inicializa la sumatoria
        sumatoria = 0
        for p in range(i + 1, n):
            # Se multiplica los elementos de la fila por el x de p, es decir, por el x ya calculado
            sumatoria += ab[i][p] * x[p]
        # Se calcula el valor de x[i], correspondiente a las x distintas de xn, siendo n la ultima fila de la matriz
        x[i] = (ab[i][n + 1] - sumatoria) / ab[i][i]
    # Retorna el array de x
    return x
