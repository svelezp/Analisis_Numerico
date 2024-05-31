import sympy as sp
import numpy as np
import math

x = sp.symbols("x")


def biseccion(funcion, xi, xf, tolerancia, numero_iteraciones):
    Xi = xi
    Xs = xf
    Tol = tolerancia
    Niter = numero_iteraciones
    Fun = funcion
    res = []
    fm = []
    E = []
    xn = []
    N = []
    a = []
    b = []
    c = 0
    # Se evalúa la función en el límite inferior (Xi) y el superior (Xs) y se guardan los valores
    x = Xi
    fi = eval(Fun)
    x = Xs
    fs = eval(Fun)
    Error = 0
    res2 = "nan"

    # Se verifica si alguna de las funciones evaluadas da cero, es decir, si Xi o Xs es raíz.
    if fi == 0:
        s = Xi
        E = 0
        res2 = (Xi, "es raiz de f(x)")
    elif fs == 0:
        s = Xs
        E = 0
        res2 = (Xs, "es raiz de f(x)")
    elif fs * fi < 0:
        # Se verifica que haya un cambio de signo
        c = 0

        # Si lo hay, se encuentra el punto medio entre los límites Xi y Xs
        Xm = (Xi + Xs) / 2
        x = Xm
        fe = eval(Fun)
        fm.append(fe)
        N.append(c)
        E.append(100)
        xn.append(x)

        # Si el punto medio NO es raíz, se continúa con el ciclo.
        while E[c] > Tol and fe != 0 and c < Niter:
            a.append(Xi)
            b.append(Xs)
            # Si entre f(Xi) y f(Xm) (punto medio) hay un cambio de signo, se asume que en ese intervalo está la raíz y Xm pasa a
            # ser el límite superior de un intervalo
            if fi * fe < 0:
                Xs = Xm
                x = Xs
                fs = eval(Fun)
            else:
                # Si entre f(Xi) y f(Xm) no hay un cambio de signo, se asume que la raíz está en el intervalo [Xm, Xs], reemplazando Xi con Xm.
                Xi = Xm
                x = Xi
                fs = eval(Fun)

            # Se calcula el punto medio nuevamente y se almacena en X para la tabla, así como el cáculo del error y el número de la iteración.
            Xa = Xm
            Xm = (Xi + Xs) / 2
            x = Xm
            fe = eval(Fun)
            fm.append(fe)
            xn.append(x)
            Error = abs(Xm - Xa)
            E.append(Error)
            c = c + 1
            N.append(c)
        a.append(Xi)
        b.append(Xs)
        if fe == 0:
            s = x
            res2 = (s, "es raiz de f(x)")
        elif Error < Tol:
            s = x
            res2 = (s, "es una aproximacion de un raiz de f(x) con una tolerancia", Tol)
        else:
            s = x
            res2 = ("Fracaso en ", Niter, " iteraciones")
    else:
        res2 = "El intervalo es inadecuado"

    for i in range(0, len(N)):
        res.append([N[i], a[i], xn[i], b[i], fm[i], E[i]])
    return res, res2
