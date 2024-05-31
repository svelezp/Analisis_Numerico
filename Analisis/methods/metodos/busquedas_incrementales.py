from math import *
from sympy import symbols

x = symbols("x")


def busquedasIncrementales(funcion, x_inicial, delta, num_intervalos):

    def f(x):
        f = eval(funcion)
        return f

    # Se evalúa la función en el punto inicial
    y_0 = f(x_inicial)
    # Si es 0 se considera raiz y sale del metodo
    if y_0 == 0:
        print("El punto inicial es una raíz.")
        return (x_inicial, x_inicial)
    else:
        # Se remplazan las variables para evaluar en el siguiente punto
        x_actual = x_inicial
        x_siguiente = x_actual + delta
        y_1 = f(x_siguiente)
        intervalo_actual = 1

        # Mientras el producto entre las funciones sea mayor que 0, y el intervalo actual sea menor al número de intervalos
        while y_0 * y_1 > 0 and intervalo_actual < num_intervalos:
            x_actual = x_siguiente
            y_0 = y_1
            x_siguiente = x_actual + delta
            # Se vuelve a evaluar en la siguiente x
            y_1 = f(x_siguiente)
            intervalo_actual = intervalo_actual + 1

            # Si Y1 es raiz, sale del metodo
            if y_1 == 0:
                print("Raíz encontrada en el punto:", x_siguiente)
                return x_siguiente
            # Si el producto entre las funciones es menor que 0, se encontró una raíz y sale del metodo.
            elif y_0 * y_1 < 0:
                print("Raíz encontrada en el intervalo:", x_actual, "-", x_siguiente)
                return (x_actual, x_siguiente)
    # Si no se encontró ninguna raíz en los intervalos dados, se imprime un mensaje y se retorna None
    print("No se encontró ninguna raíz en los intervalos dados.")
    return (None, None)
