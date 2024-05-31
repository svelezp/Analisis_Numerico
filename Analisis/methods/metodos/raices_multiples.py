import sympy as sm
import math

x = sm.Symbol("x")


def raices_multiples(x0, f, df, df2, tol, niter):
    X0 = x0
    Tol = tol
    Niter = niter
    Fun = f

    # print("derivate Function df:")
    df = df
    df2 = df2
    res2 = "nan"
    fn = []
    xn = []
    E = []
    N = []
    x = X0
    d1 = []
    d2 = []
    res = []
    # f=eval(Fun)
    # derivada=eval(df)
    # derivada2=eval(df2)
    x = X0
    f = eval(Fun)
    x = X0
    derivada = eval(df)
    x = X0
    derivada2 = eval(df2)
    c = 0
    Error = 100
    fn.append(f)
    d1.append(derivada)
    d2.append(derivada2)
    xn.append(x)
    E.append(Error)
    N.append(c)

    while Error > Tol and derivada != 0 and c < Niter:
        # cálculo de x y los términos necesarios para calcular X desde el método de Newthon
        arriba = f * derivada
        abajo = ((derivada) ** 2) - ((f) * (derivada2))
        x = x - (arriba / abajo)
        # derivada=eval(df)
        # f=eval(Fun)
        f = eval(Fun)
        derivada = eval(df)
        derivada2 = eval(df2)
        fn.append(f)
        d1.append(derivada)
        d2.append(derivada2)
        xn.append(x)
        c = c + 1
        Error = abs(xn[c] - xn[c - 1])
        N.append(c)
        E.append(Error)
    if f == 0:
        s = x
        res2 = (s, "es raiz de f(x)")
    elif Error < Tol:
        s = x
        res2 = (s, "es una aproximacion de un raiz de f(x) con una tolerancia", Tol)

    else:
        s = x
        res2 = ("Fracaso en ", Niter, " iteraciones ")

    for i in range(0, len(N)):
        res.append([N[i], xn[i], fn[i], E[i]])
    for i in res:
        print(i)
    return res, res2
