import numpy as np


def gauss_pivoteo(a, b, n):
    # Se crea la matriz aumentada
    ab = to_aug(a, b)
    # Primer loop, numero de etapas K
    for k in range(n - 1):
        ab = pivoteo(ab, n, k)
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


def pivoteo(ab, n, k):
    # Se inicializa el mayor y la fila mayor
    mayor = abs(ab[k][k])
    fila_mayor = k
    # Loop para encontrar en la columna k el mayor valor
    for s in range(k + 1, n):
        # Si el valor absoluto de la fila s y columna k es mayor al mayor actual
        if abs(ab[s][k]) > mayor:
            # Se actualiza el mayor y la fila mayor
            mayor = abs(ab[s][k])
            fila_mayor = s
    # Si el mayor es 0, el sistema no tiene solucion unica
    if mayor == 0:
        return "El sistema no tiene solucion unica"
    else:
        # Si la fila mayor es distinta de k
        if fila_mayor != k:
            # Se intercambian las filas k y fila_mayor en la matriz aumentada
            ab[[k, fila_mayor]] = ab[[fila_mayor, k]]
        return ab
