import numpy as np
import utilidades as utils


def LUGauss(A, b):
    n, m = A.shape
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    U[0] = A[0]
    for k in range(n - 1):
        L[k, k] = 1
        for i in range(k + 1, n):
            m = A[i, k] / A[k, k]
            L[i, k] = m
            for j in range(k, n):
                A[i, j] = A[i, j] - m * A[k, j]
                U[i, j] = A[i, j]
    L[n - 1, n - 1] = 1
    z = utils.sustProg(L, b, n)
    x = utils.sustRegr(U, z, n)

    return L, U, x


def LUGaus(A, b):
    L, U, x = LUGauss(A, b)
    ans = []
    for i in range(x.size):
        ans.append("x" + str(i) + " = " + str(x[i]) + "   ")
    return ans
