from math import *
from sympy import symbols

x = symbols("x")


def busquedasIncrementales(funcion, x_inicial, delta, num_intervalos):

    def f(x):
        f = eval(funcion)
        return f

    y_0 = f(x_inicial)
    if y_0 == 0:
        print("El punto inicial es una raíz.")
        return (x_inicial, x_inicial)
    else:
        x_actual = x_inicial
        x_siguiente = x_actual + delta
        y_1 = f(x_siguiente)
        intervalo_actual = 1

        while y_0 * y_1 > 0 and intervalo_actual < num_intervalos:
            x_actual = x_siguiente
            y_0 = y_1
            x_siguiente = x_actual + delta
            y_1 = f(x_siguiente)
            intervalo_actual = intervalo_actual + 1

            if y_1 == 0:
                print("Raíz encontrada en el punto:", x_siguiente)
                return (x_siguiente, x_siguiente)
            elif y_0 * y_1 < 0:
                print("Raíz encontrada en el intervalo:", x_actual, "-", x_siguiente)
                return (x_actual, x_siguiente)
    print("No se encontró ninguna raíz en los intervalos dados.")
    return (None, None)
