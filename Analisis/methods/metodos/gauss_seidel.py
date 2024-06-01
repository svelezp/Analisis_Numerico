import numpy as np


def gauss_seidel(A, b, init, tol, n, err_type):
    # Contador
    contador = 0
    # Dispersion
    dispersion = float("inf")
    # Valor inicial
    xi = init
    # Mientras la dispersion sea mayor que la tolerancia y el contador sea menor que el número de iteraciones
    while (dispersion > tol) and (contador < n):
        # Se llama al metodo para iterar
        x, err_abs, err_rel = calcular_nuevo_seidel(A, b, xi)
        # Se reemplaza el valor de x inicial por el nuevo valor de x
        xi = x
        # Se asigna un valor al error segun el tipo de error elegido
        if err_type == "abs":
            dispersion = err_abs
        else:
            dispersion = err_rel
        # Se actualiza el contador
        contador += 1
    # Si la dispersion es menor que la tolerancia
    if dispersion < tol:
        return x, "es un valor aproximado de la solución con tolerancia: " + str(tol)
    else:
        return "No converge"


# Metodo para calcular el nuevo valor de x
def calcular_nuevo_seidel(A, b, x):
    # Tamaño de x
    n = len(x)
    # Crear un arreglo de ceros para almacenar los nuevos valores de x
    x_new = np.zeros_like(x)
    # Para cada valor de x
    for i in range(n):
        # El valor de x_new en la posición i es igual al valor de x en la posición i
        x_new[i] = x[i]
    # Para cada valor de x
    for i in range(0, n):
        # Inicializar suma
        suma = 0
        # Para cada valor de x
        for j in range(0, n):
            # Si i es diferente de j, lo que hace que se eviten los valores de la diagonal
            if i != j:
                # Sumar el valor de A[i,j] por el valor de x_new[j]
                suma += A[i, j] * x_new[j]
        errores = abs(x_new - x)
        # Calcular el error absoluto y relativo
        error_abs = max(errores)
        error_rel = max(errores / abs(x))
        # Calcular el nuevo valor de x en pa posicion i
        x_new[i] = (b[i] - suma) / A[i, i]
    return x_new, error_abs, error_rel
