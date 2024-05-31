def secante(x0, x1, f, tol, niter):
    X0 = x0
    X1 = x1
    Tol = tol
    Niter = niter
    Fun = f
    res = []
    res2 = "nan"
    fn = []
    xn = []
    E = []
    N = []
    # Se evalúa la función en x0 y x1
    x = X0
    f = eval(Fun)
    x = X1
    f1 = eval(Fun)
    c = 0
    Error = 100
    fn.append(f)
    fn.append(f1)
    xn.append(X0)
    xn.append(X1)
    E.append(Error)
    E.append(Error)
    N.append(c)
    c = c + 1
    N.append(c)
    while Error > Tol and f != 0 and c < Niter:
        # Se calcula X con el método de la secante y se evalúa nuevamente en f
        x = xn[c] - ((fn[c] * (xn[c] - xn[c - 1])) / (fn[c] - fn[c - 1]))
        f = eval(Fun)
        fn.append(f)
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
