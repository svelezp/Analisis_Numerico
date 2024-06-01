import numpy as np


def Crout(A, b, n):
    # Se inicializan las matrices L y U como una matriz identidad
    L = np.identity(n, dtype=np.float64)
    U = np.identity(n, dtype=np.float64)
    # Se recorre la matriz A
    for k in range(0, n):
        # Se inicializan la sumatoria1
        suma1 = 0
        # Para cada elemento de la diagonal de la matriz A
        for p in range(0, k):
            # Se realiza la sumatoria de los elementos de la matriz L y U
            suma1 += L[k][p] * U[p][k]
        L[k][k] = A[k][k] - suma1

        # Se recorre la matriz A
        for i in range(k + 1, n):
            # Se inicializa la sumatoria2
            suma2 = 0
            # Se recorre la matriz A
            for p in range(0, k):
                # Sumatoria de la multiplicacion de la fila i de L por la columna k de U
                suma2 += L[i][p] * U[p][k]
            # Se calcula los valores debajo de la diagonal de L
            L[i][k] = (A[i][k] - suma2) / U[k][k]

        # Se recorre la matriz A
        for j in range(k + 1, n):
            # Se inicializa la sumatoria3
            suma3 = 0
            # Se recorre la matriz A
            for p in range(0, k):
                # Sumatoria de la multiplicacion de la fila k de L por la columna j de U
                suma3 += L[k][p] * U[p][j]
            # Se calcula los valores arriba del al diagonal de U
            U[k][j] = (A[k][j] - suma3) / L[k][k]
    # Se hallan los z con sustitucion orogresiva, y posteriormente los x con sustitucion regresiva
    z = progressive_substitucion(L, b, n)
    x = regressive_substitution(U, z, n)
    return "El resultado es " + str(x)


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
    print("los valores de z son: " + str(x))
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


def to_aug(a, b):
    # Se convierte la matriz a en una matriz aumentada
    return np.column_stack((a, b))
