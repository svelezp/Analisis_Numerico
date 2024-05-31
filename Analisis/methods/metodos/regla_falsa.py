def reglaFalsa(f, t_error, xi, xs, tol, niter):
    x = xi
    fxinf = eval(f)
    x = xs
    res2 = "nan"
    fxsup = eval(f)
    resultados = []  # matriz para guardar resultados

    # Se verifica si alguno de los límites del intervalo es raíz
    if fxinf == 0:
        res2 = (xi, " es raiz")
    elif fxsup == 0:
        res2 = (xs, " es raiz")
    elif fxinf * fxsup < 0:
        # Si ninguno de los extremos es raíz, se verifica el cambio de signo

        # Se calcula el punto medio con la fórumla de la regla falsa y se almacena la función evaluada en ese punto, el error y el niter.
        xm = xi - ((fxinf * (xs - xi)) / float(fxsup - fxinf))
        x = xm
        fxm = eval(f)
        contador = 1
        error = float(tol) + 1
        resultados.append([contador, xi, xs, xm, fxm, "nan"])
        while fxm != 0 and error > tol and contador < niter:
            if fxinf * fxm < 0:
                # Si hay un camnbio de signo entre el f(Xm) y f(xi), Xs pasa a ser el punto medio
                xs = xm
                fxsup = fxm
            else:
                xi = xm
                fxinf = fxm

            # Se calcula de nuevo Xm y f(Xm) para esta iteración
            temp = xm
            xm = xi - ((fxinf * (xs - xi)) / float(fxsup - fxinf))
            x = xm
            fxm = eval(f)
            # Dependiendo del tipo de error (relativo o absoluto) se calcula y se guarda en la tabla
            if t_error == 1:
                error = abs(xm - temp)
            else:
                error = abs((xm - temp) / xm)
            contador += 1
            resultados.append([contador, xi, xs, xm, fxm, error])
        if fxm == 0:
            res2 = "xm es raiz"
        elif error <= tol:
            res2 = (xm, " se aproxima a una raiz con una tolerancia de ", tol)
        else:
            res2 = "Maximo de iteraciones alcanzado"
    else:
        res2 = "El intervalo es inadecuado"
    return resultados, res2
