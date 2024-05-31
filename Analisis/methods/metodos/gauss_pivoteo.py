import numpy as np


def sustitucionRegresiva(Ab, n):
    x = np.zeros(n)

    n = n - 1

    k = Ab[n - 1][n + 1] / Ab[n][n]

    x[n] = Ab[n][n + 1] / Ab[n][n]

    for i in range(n - 1, -1, -1):
        sum = 0
        for p in range(i + 1, n + 1):
            k = x[p]
            sum = sum + (Ab[i][p] * x[p])

        x[i] = (Ab[i][n + 1] - sum) / Ab[i][i]

    return x


def pivoteoParcial(Ab, n):
    # Para cada fila en AB
    for i in range(0, n - 1, 1):
        # columna desde diagonal i en adelante
        columna = abs(Ab[i:, i])
        max = np.argmax(columna)

        # max no está en diagonal
        if max != 0:
            temporal = np.copy(Ab[i, :])
            Ab[i, :] = Ab[max + i, :]
            Ab[max + i, :] = temporal

    return Ab


def eliminacionPivoteoParcial(Ab, n):

    for k in range(n):

        Ab = pivoteoParcial(Ab, n)

        for i in range(k + 1, n):

            if Ab[k][k] == 0:
                print("División por 0, no es posible realizar eliminación Gaussiana")
                return Ab
                break

            multiplicador = Ab[i][k] / Ab[k][k]

            for j in range(k, n + 1):
                Ab[i, j] = Ab[i, j] - multiplicador * Ab[k, j]

    return Ab


def eliminacionGaussianaPivoteoParcial(A, b, n):
    Ab = np.append(A, b, axis=1)
    Ab = eliminacionPivoteoParcial(Ab, n)
    x = sustitucionRegresiva(Ab, n)
    ans = []
    for i in range(1, 5):
        ans.append("x" + str(i) + " = " + str(x[i - 1]))
    return ans
