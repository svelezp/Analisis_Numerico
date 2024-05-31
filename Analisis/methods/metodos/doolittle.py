import numpy as np
import utilidades as utils


def doolittle(A, b):
    n, m = A.shape
    if n != m:
        print("La matriz no es cuadrada")
        return
    else:
        L = np.zeros((n, n))
        U = np.zeros((n, n))
        for i in range(n):
            L[i][i] = 1
            if i == 0:
                U[0][0] = A[0][0]
                for j in range(1, n):
                    U[0][j] = A[0][j]
                    L[j][0] = A[j][0] / U[0][0]
            else:
                for j in range(i, n):
                    suma = 0
                    for k in range(0, i):
                        suma = suma + (L[i][k] * U[k][j])
                    U[i][j] = A[i][j] - suma
                for j in range(i + 1, n):
                    suma = 0
                    for k in range(0, i):
                        suma = suma + (L[j][k] * U[k][i])
                    L[j][i] = (A[j][i] - suma) / U[i][i]
    return L, U, n


def resolverDool(A, b):
    L, U, n = doolittle(A, b)
    z = utils.sustProg(L, b, n)
    x = utils.sustRegr(U, z, n)
    ans = []
    for i in range(len(x)):
        ans.append("x" + str(i) + " = " + str(x[i]) + "   ")
    return L, U, ans
