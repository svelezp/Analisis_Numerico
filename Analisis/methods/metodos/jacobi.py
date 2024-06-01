import numpy as np


def jacobi(A, b, init, tol, n, err_type):
    # Contador
    contador = 0
    # Dispersion
    dispersion = float("inf")
    # Valor inicial
    xi = init
    # Mientras la dispersion sea mayor que la tolerancia y el contador sea menor que el número de iteraciones
    while (dispersion > tol) and (contador < n):
        # Llamar al metodo para iterar
        x, error_abs, error_rel = calcular_nuevo_jacobi(A, b, xi)
        # Reemplazar el valor del x inicial por el nuevo valor de x
        xi = x
        # Asignar un valor al error segun el tipo de error elegido
        if err_type == "abs":
            dispersion = error_abs
        else:
            dispersion = error_rel
        # Actualizar el contador
        contador += 1
    # Si la dispersion es menor que la tolerancia
    if dispersion < tol:
        return x + "es un valor aproximado de la solución con tolerancia: " + str(tol)
    else:
        return "No converge"


# Metodo para calcular el nuevo valor de x
def calcular_nuevo_jacobi(A, b, x):
    # Tamaño de x
    n = len(x)
    # Crear un arreglo de ceros para almacenar los nuevos valores de x
    x_new = np.zeros_like(x)
    # Para cada valor de x
    for i in range(0, n):
        # Inicializar suma
        suma = 0
        # Para cada valor de x
        for j in range(0, n):
            # Si i es diferente de j, lo que hace que se eviten los valores de la diagonal
            if i != j:
                # Sumar el valor de A[i,j] por el valor de x[j]
                suma += A[i, j] * x[j]
        # Calcular el nuevo valor de x
        x_new[i] = (b[i] - suma) / A[i, i]
    # Calcular los errores
    errores = abs(x_new - x)
    # Calcular el error absoluto y relativo
    error_abs = np.max(np.abs(errores))
    error_rel = np.max(errores / np.abs(x_new))
    return x_new, error_abs, error_rel
