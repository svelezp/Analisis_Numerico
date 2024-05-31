import sympy as sm
import math

x = sm.Symbol("x")


def punto_fijo(funcion, x0, tolerancia, g, numero_iteraciones):
    x = x0
    # Se evalua la funcion F en x0
    f = eval(funcion)
    Contador = 1
    error = tolerancia + 1
    # Mientras el error sea mayor que la tolerancia y f(x) sea diferente de 0 y el contador sea menor que el numero de iteraciones
    while f != 0 and error > tolerancia and Contador < numero_iteraciones:
        # Se evalua la funcion g en x
        xn = eval(g)
        x = xn
        # Se evalua la funcion F en x
        f = eval(funcion)
        # Se calcula el error absoluto
        error = abs(xn - x0)
        # Se remplaza el valor de x0 por el x resultado de evaluar G en x0
        x0 = xn
        Contador += 1
    if f == 0:
        return x, "es raiz de f(x) en el intervalo " + str(Contador)
    elif error < tolerancia:
        return x, "es una aproximacion de una raiz con tolerancia " + str(tolerancia)
    else:
        return None, "Fracaso en " + str(numero_iteraciones) + " iteraciones"
