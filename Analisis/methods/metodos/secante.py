def secante(x0, x1, funcion, tol, niter):
    x = x0
    # Se evalua la funcion
    f = eval(funcion)
    if f == 0:
        return f"{x0} es raiz de la funcion"
    else:

        x = x1
        # Se evalua la funcion en x1
        f1 = eval(funcion)
        # Se inicia el contador
        contador = 0
        # Se calcula el error
        error = tol + 1
        # Se calcula el denominador
        den = f1 - f
        # Mientras el error sea mayor que la tolerancia, f1 sea diferente de 0, el denominador sea diferente de 0 y el contador sea menor que el numero de iteraciones
        while error > tol and f1 != 0 and den != 0 and contador < niter:
            # Se calcula el siguiente x
            x2 = x1 - f1 * (x1 - x0) / den
            # Se calcula el error
            error = abs(x2 - x1)
            # Se remplaza el valor de x0 por x1
            x0 = x1
            # Se remplaza el valor de la primera funcion por la segunda funcion
            f = f1
            # Se remplaza el valor de x1 por el nuevo x
            x1 = x2
            x = x1
            # Se evalua la funcion en x1
            f1 = eval(funcion)
            # Se calcula el denominador
            den = f1 - f
            # Se aumenta el contador
            contador += 1
        if f1 == 0:
            return f"{x1} es raiz de la funcion"
        elif error < tol:
            return f"{x1} es una aproximacion con una tolerancia de {tol}"
        elif den == 0:
            return f"{x1} es una posible raiz multiple"
        else:
            return f"Fracaso en {niter} iteraciones"
