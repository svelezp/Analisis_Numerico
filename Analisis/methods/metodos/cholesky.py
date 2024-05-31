import numpy as np
import utilidades as utils


def cholesky(A, b):
    n, m = A.shape
    if n != m:
        print("La matriz no es cuadrada")
        return
    else:
        L = np.transpose(np.tri(n, n))

        for i in range(n):
            suma = 0
            for k in range(i):
                suma = suma + ((L[k][i]) ** 2)
            L[i][i] = (A[i][i] - suma) ** (1 / 2)

            for j in range(i + 1, n):
                suma = 0
                for k in range(i):
                    suma = suma + (L[k][i] * L[k][j])
                L[i][j] = (1 / L[i][i]) * (A[i][j] - suma)

    return np.transpose(L), L, n


def resolverChol(A, b):
    L, U, n = cholesky(A, b)
    z = utils.sustProg(L, b, n)
    x = utils.sustRegr(U, z, n)
    ans = []
    for i in range(len(x)):
        ans.append("x" + str(i) + " = " + str(x[i]) + "   ")
    return L, U, ans
