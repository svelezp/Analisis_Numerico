import numpy as np


def sustProg(L, b, n):
    if L[0][0] == 0:
        return
    else:
        z = np.zeros(n)
        suma3 = 0
        z[0] = b[0] / L[0][0]
        for k in range(1, n):
            if L[k][k] == 0:
                print("Elemento", k, " en la diagonal de L, es cero")
                return
            else:
                for r in range(k):
                    suma3 = suma3 + (L[k][r] * z[r])
                z[k] = (b[k] - suma3) / L[k][k]
                suma3 = 0
    return z


def sustRegr(U, z, n):
    if U[0][0] == 0:
        return
    else:
        x = np.zeros(n)
        suma4 = 0
        x[n - 1] = z[n - 1] / U[n - 1][n - 1]
        for k in range(n - 2, -1, -1):
            if U[k][k] == 0:
                print("Elemento", k, " en la diagonal de U, es cero")
                return
            else:
                suma4 = 0
                for r in range(k + 1, n):
                    suma4 = suma4 + (U[k][r] * x[r])
                x[k] = (1 / U[k][k]) * (z[k] - suma4)
    return x
