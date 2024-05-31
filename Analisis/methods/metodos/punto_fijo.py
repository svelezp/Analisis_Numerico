import sympy as sm
import math

x = sm.Symbol("x")


def punto_fijo(f, x0, tol, g, niter):

    X0 = x0
    Tol = tol
    Niter = niter
    Fun = f
    g = g
    res = []
    res2 = "nan"
    fn = []
    xn = []
    E = []
    N = []
    gx = []
    x = X0
    f = eval(Fun)
    c = 0
    Error = 100
    fn.append(f)
    xn.append(x)
    E.append(Error)
    N.append(c)

    # Si la función evaluada en X0 es diferente de cero...
    while Error > Tol and f != 0 and c < Niter:
        # Se calcula x evaluando la función auxiliar con el x actual
        x = eval(g)
        gx.append(x)

        # Se evalúa la función original con el nuevo x calculado a partir de G
        fe = eval(Fun)
        fn.append(fe)
        xn.append(x)
        c = c + 1
        Error = abs(xn[c] - xn[c - 1])
        N.append(c)
        E.append(Error)
    gx.append(x)
    if fe == 0:
        s = x
        res2 = (s, "es raiz de f(x)")
    elif Error < Tol:
        s = x
        res2 = (s, "es una aproximacion de un raiz de f(x) con una tolerancia", Tol)

    else:
        s = x
        res2 = ("Fracaso en ", Niter, " iteraciones ")

    for i in range(0, len(N)):
        res.append([N[i], xn[i], fn[i], gx[i], E[i]])
    for i in res:
        print(i)
    return res, res2
