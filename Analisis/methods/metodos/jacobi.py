import numpy as np


def jacobi(A, b, tol, maxIte):
    n, m = A.shape
    if m != n:
        print("La matriz no es cuadrada")
        return
    else:
        x0 = []
        for i in range(n):
            x0.append(2)
        xin = np.zeros(n, dtype=float)
        diferencia = np.ones(n, dtype=float)
        error = 2 * tol
        itera = 0
        while error > tol and itera <= maxIte:
            for i in range(0, n, 1):
                suma = b[i]
                for j in range(0, m, 1):
                    if i != j:
                        suma = suma - A[i, j] * x0[j]
                suma = suma / A[i, i]
                diferencia[i] = np.abs(suma - x0[i])
                xin[i] = suma
            error = np.max(diferencia)
            x0 = np.copy(xin)
            itera = itera + 1
        if itera > maxIte:
            x0 = np.nan
            print("El método no converge")
        return x0, itera, error


def Jacobi(A, b, tol, maxIte):
    x0, itera, error = jacobi(A, b, tol, maxIte)
    ans = []
    for i in range(len(x0)):
        ans.append("x" + str(i) + " = " + str(x0[i]) + "   ")
    return ans
