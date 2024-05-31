def raices_multiples(x0, funcion, df1, df2, tolerancia, niter):
    x = x0
    # Se evalua la funcion
    f = eval(funcion)
    # Se calcula la derivada
    df1 = eval(df1)
    # Se calcula la segunda derivada
    df2 = eval(df2)
    # Se inicia el contador
    contador = 1
    # Se calcula el error
    error = tolerancia + 1
    # Mientras el error sea mayor a la tolerancia, la funcion sea diferente de 0 y el contador sea menor al numero de iteraciones
    while f != 0 and error > tolerancia and contador < niter:
        if df1 == 0:
            return f"{x0} es una posible raiz multiple"
        # Se calcula el denominador
        denominador = df1**2 - f * df2

        if denominador == 0:
            return f"{x0} es una posible raiz multiple"

        # Se calcula el valor de el siguiente x
        x1 = x0 - f * df1 / denominador

        # Se calcula el error absoluto
        error = abs(x1 - x0)

        # Se remplaza el valor de x0 por el nuevo x
        x0 = x1

        # Se aumenta el contador
        contador += 1

        # Se evaluan las funciones con el nuevo x
        x = x0
        f = eval(funcion)
        df1 = eval(df1)
        df2 = eval(df2)
    if f == 0:
        return f"{x0} es raiz en la iteracion" + str(contador)
    elif error < tolerancia:
        return f"{x0} es una aproximacion a una raiz con una tolerancia de " + str(
            tolerancia
        )
    else:
        return f"No se encontro una raiz"
