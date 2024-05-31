import numpy as np


def gaussSeidel(A, b, tol, maxIte):
    n, m = A.shape
    x0 = np.zeros(n)
    # valores inciales
    X = np.copy(x0)
    diferencia = np.ones(n)
    error = 2 * tol
    itera = 0
    while error > tol and itera <= maxIte:
        for i in range(0, n, 1):
            suma = 0
            for j in range(0, n, 1):
                if j != i:
                    suma = suma + A[i, j] * X[j]
            nuevo = (b[i] - suma) / A[i, i]
            diferencia[i] = np.abs(nuevo - X[i])
            X[i] = nuevo
        error = np.max(diferencia)
        itera = itera + 1
    if itera > maxIte:
        X = []
        print("El método no converge")
    return X, itera, error


def Seidel(A, b, tol, maxIte):
    X, itera, error = gaussSeidel(A, b, tol, maxIte)
    ans = []
    print(X)
    for i in range(len(X)):
        ans.append("x" + str(i) + " = " + str(X[i]) + "   ")
    return ans
