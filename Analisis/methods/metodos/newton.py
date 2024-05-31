def newton(f, df, x0, tol, niter):
    X0 = x0
    Tol = tol
    Niter = niter
    Fun = f
    df = df
    res = []
    res2 = "nan"
    fn = []
    xn = []
    E = []
    N = []
    x = X0
    # f=eval(Fun)
    f = eval(Fun)
    derivada = eval(df)

    # derivada=eval(df)
    c = 0
    Error = 100
    fn.append(f)
    xn.append(x)
    E.append(Error)
    N.append(c)
    while Error > Tol and f != 0 and derivada != 0 and c < Niter:
        # Se recalcula X según la fórmula de Newthon-Rhapson y se reevalúa en f y f' hasta que f sea igual a cero o cumpla las demás condiciones de parada
        x = x - f / derivada
        f = eval(Fun)
        derivada = eval(df)
        fn.append(f)
        xn.append(x)
        c = c + 1
        Error = abs(xn[c] - xn[c - 1])  ##Decimales correctos
        # Error=abs((xn[c]-xn[c-1])/xn[c]) ## Cifras significativas
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
