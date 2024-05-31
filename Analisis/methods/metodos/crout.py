import numpy as np
import utilidades as utils


def Crout(A, b):
    n, m = A.shape
    if n != m:
        print("La matriz no es cuadrada")
        return
    else:
        L = np.zeros((n, n))
        U = np.zeros((n, n))
        suma1 = 0
        suma2 = 0
        for i in range(n):
            L[i][0] = A[i][0]
            U[i][i] = 1
        for j in range(1, n):
            U[0][j] = A[0][j] / L[0][0]

        for k in range(1, n):
            for i in range(k, n):
                for r in range(k):
                    suma1 = suma1 + (L[i][r] * U[r][k])
                    L[i][k] = A[i][k] - suma1
                suma1 = 0
            for j in range(k + 1, n):
                for r in range(k):
                    suma2 = suma2 + (L[k][r] * U[r][j])
                    U[k][j] = (A[k][j] - suma2) / L[k][k]
                suma2 = 0
    return L, U, n


def resolverCrout(A, b):
    L, U, n = Crout(A, b)
    z = utils.sustProg(L, b, n)
    x = utils.sustRegr(U, z, n)
    ans = []
    for i in range(len(x)):
        ans.append("x" + str(i) + " = " + str(x[i]) + "   ")
    return L, U, ans
