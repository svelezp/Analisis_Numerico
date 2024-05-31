import sympy as sp
import numpy as np
import math

x = sp.symbols("x")


def reglaFalsa(funcion, xi, xs, tolerancia, numero_iteraciones):
    # Se evalua la funcion en xi y xs
    x = xi
    fi = eval(funcion)
    print(fi)
    x = xs
    fs = eval(funcion)
    print(fs)
    # Si f(xi) = 0 entonces xi es raiz de f(x)
    if fi == 0:
        return xi, "es raiz de f(x)"
    # Si f(xs) = 0 entonces xs es raiz de f(x)
    elif fs == 0:
        return xs, "es raiz de f(x)"
    # Si f(xi) * f(xs) < 0 entonces existe al menos una raiz en el intervalo [xi, xs]
    elif fi * fs < 0:
        # Se calcula el punto medio del intervalo con la formula de regla falsa
        xm = xi - (fi * (xs - xi)) / (fs - fi)
        x = xm
        # Se evalua la funcion en xm
        fm = eval(funcion)
        contador = 1
        error = tolerancia + 1
        # Mientras el error sea mayor que la tolerancia y f(xm) sea diferente de 0 y el contador sea menor que el numero de iteraciones
        while error > tolerancia and fm != 0 and contador < numero_iteraciones:
            # Si f(xi) * f(xm) < 0 entonces la raiz se encuentra en el intervalo [xi, xm]
            if fi * fm < 0:
                xs = xm
                fs = fm
            # Si f(xi) * f(xm) > 0 entonces la raiz se encuentra en el intervalo [xm, xs]
            else:
                xi = xm
                fi = fm
            # Se guarda el valor anterior de xm
            xaux = xm
            # Se calcula el punto medio del intervalo con la formula de regla falsa
            xm = xi - (fi * (xs - xi)) / (fs - fi)
            x = xm
            # Se evalua la funcion en xm
            fm = eval(funcion)
            # Se calcula el error
            error = abs(xm - xaux)
            contador += 1
        # Si f(xm) = 0 entonces xm es raiz de f(x)
        if fm == 0:
            return xm, "es raiz de f(x)"
        # Si el error es menor que la tolerancia entonces xm es una aproximacion de una raiz con tolerancia
        elif error < tolerancia:
            return xm, "es una aproximacion de una raiz con tolerancia" + str(
                tolerancia
            )
        else:
            return None, "Fracaso en " + str(numero_iteraciones) + " iteraciones"
    else:
        return None, "El intervalo es inadecuado"
