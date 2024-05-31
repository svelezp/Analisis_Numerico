import numpy as np


def LU(a, b, n):
    # Se inicializan las matrices L y U
    L, U = np.zeros((n, n)), np.zeros((n, n))
    # Se calculan las matrices L y U
    L, U = gauss_modificado(a, n)
    print("L es" + str(L))
    print("U es" + str(U))
    # Se hace la sustitucion progresiva y regresiva
    z = progressive_substitucion(L, b, n)
    x = regressive_substitution(U, z, n)
    return "Los valores de x  son: " + str(x)


def progressive_substitucion(L, b, n):
    Lb = to_aug(L, b)
    # Inicializa el array de x con el número de X de la matriz
    x = np.zeros(n)
    # Se calcula el valor de la primera x
    x[0] = Lb[0][n] / Lb[0][0]
    # Loop de la sustitución progresiva, incrementa cada vez en +1
    for i in range(1, n):
        # Se inicializa la sumatoria
        sumatoria = 0
        for p in range(i):
            # Se multiplica los elementos de la fila por el x de p, es decir, por el x ya calculado
            sumatoria = sumatoria + Lb[i][p] * x[p]
        # Se calcula el valor de x[i], correspondiente a las x distintas de x0, siendo 0 la primera fila de la matriz
        x[i] = (Lb[i][n] - sumatoria) / Lb[i][i]
    # Retorna el array de x
    print("los valores de x son: " + str(x))
    return x


def regressive_substitution(U, z, n):
    Un = to_aug(U, z)
    # Inicializa el array de x con el número de X de la matriz
    x = np.zeros(n)
    # Se calcula el valor de la última x (índice n-1)
    x[n - 1] = Un[n - 1][n] / Un[n - 1][n - 1]
    # Loop de la sustitución regresiva, decrementa cada vez en -1
    for i in range(n - 2, -1, -1):
        # Se inicializa la sumatoria
        sumatoria = 0
        for p in range(i + 1, n):
            # Se multiplica los elementos de la fila por el x de p, es decir, por el x ya calculado
            sumatoria += Un[i][p] * x[p]
        # Se calcula el valor de x[i], correspondiente a las x distintas de xn, siendo n la última fila de la matriz
        x[i] = (Un[i][n] - sumatoria) / Un[i][i]
    # Retorna el array de x
    return x


def gauss_modificado(a, n):
    Lvalues = np.zeros((n, n))

    # Primer loop, numero de etapas K
    for k in range(n - 1):
        # Segundo loop, numero de filas i
        for i in range(k + 1, n):
            # Se calcula el multiplicador
            multiplicador = a[i][k] / a[k][k]
            # Se guarda el multiplicador en la matriz L
            Lvalues[i][k] = multiplicador
            # Tercer loop, numero de columnas j
            for j in range(k, n):
                # Se realiza la operacion de eliminacion a base del multiplicador
                a[i][j] -= multiplicador * a[k][j]
    # Se llena la diagonal de la matriz L con 1
    np.fill_diagonal(Lvalues, 1)

    return Lvalues, a


def to_aug(a, b):
    # Se convierte la matriz a en una matriz aumentada
    return np.column_stack((a, b))
