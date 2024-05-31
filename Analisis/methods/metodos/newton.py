def newton(f, df, x0, tol, numero_iteraciones):
    x = x0
    # Se evalua la funcion
    f = eval(f)
    # Se calcula la derivada
    dif = eval(df)
    # Se inicia el contador
    Contador = 1
    error = tol + 1
    # Mientras el error sea mayor a la tolerancia, la funcion sea diferente de 0 y el contador sea menor al numero de iteraciones
    while error > tol and f != 0 and Contador < numero_iteraciones:
        # Se calcula el nuevo valor de x
        x1 = x0 - (f / dif)
        x = x1
        # Se evalua la funcion con el nuevo x
        f = eval(f)
        # Se calcula la nueva derivada
        dif = eval(df)
        # Se calcula el error absoluto
        error = abs(x1 - x0)
        # Se remplaza el valor de x0 por el nuevo x
        x0 = x1
        # Se aumenta el contador
        Contador += 1
    if f == 0:
        return f"{x0} es una raiz"
    elif error < tol:
        return f"{x0} es una aproximacion a una raiz con una tolerancia de {tol}"
    elif dif == 0:
        return f"{x0} es una posible raiz multiple"
    else:
        return f"No se encontro una raiz"
