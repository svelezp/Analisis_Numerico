from django.shortcuts import render
from django.http import HttpResponse
from .forms import (
    busquedasIncrementalesForm,
    BiseccionForm,
    ReglaFalsaForm,
    PuntoFijoForm,
    MultipleRootsForm,
    NewtonForm,
    SecanteForm,
    JacobiForm,
    SeidelForm,
    GaussSimpleForm,
)
import numpy as np
from sympy import sympify, lambdify, symbols
import math
from .metodos.busquedas_incrementales import (
    busquedasIncrementales as CalculoBusquedasIncrementales,
)
from .metodos.biseccion import biseccion as CalculoBiseccion
from .metodos.regla_falsa import reglaFalsa as CalculoReglaFalsa
from .metodos.punto_fijo import punto_fijo as CalculoPuntoFijo
from .metodos.raices_multiples import raices_multiples as CalculoRaicesMultiples
from .metodos.newton import newton as CalculoNewton
from .metodos.secante import secante as CalculoSecante
from .metodos.gauss_simple import gauss_simple as CalculoGauss
from .metodos.gauss_pivoteo import gauss_pivoteo as CalculoGaussPivoteo
from .metodos.LU import LU as CalculoLU


# Create your views here.


def home(request):
    return render(request, "base.html")


def about(request):
    return render(request, "about.html")


def busquedasIncrementales(request):
    data = {
        "form": busquedasIncrementalesForm(),
    }

    if request.method == "POST":
        form = busquedasIncrementalesForm(request.POST)
        if form.is_valid():
            xi = form.cleaned_data["xi"]
            funcion = form.cleaned_data["funcion"]
            delta = form.cleaned_data["delta"]
            niter = form.cleaned_data["niter"]

            resultado = CalculoBusquedasIncrementales(funcion, xi, delta, niter)
            print("el resultado es: ", resultado)
            data["resultado"] = str(resultado)
        else:
            print("Formulario no valido")
    return render(request, "busquedas_incrementales.html", data)


def biseccion(request):
    data = {"form": BiseccionForm}

    if request.method == "POST":
        form = BiseccionForm(request.POST)
        if form.is_valid():
            xi = form.cleaned_data["xi"]
            xf = form.cleaned_data["xs"]
            funcion = form.cleaned_data["f"]
            tolerancia = form.cleaned_data["tol"]
            niter = form.cleaned_data["niter"]

            resultado = CalculoBiseccion(funcion, xi, xf, tolerancia, niter)
            data["resultado"] = str(resultado)
        else:
            print("Formulario no valido")
    return render(request, "biseccion.html", data)


def reglafalsa(request):
    data = {
        "form": ReglaFalsaForm(),
    }

    if request.method == "POST":
        form = ReglaFalsaForm(request.POST)
        if form.is_valid():
            xi = form.cleaned_data["xi"]
            xs = form.cleaned_data["xs"]
            funcion = form.cleaned_data["f"]
            tolerancia = form.cleaned_data["tol"]
            niter = form.cleaned_data["niter"]
            t_error = form.cleaned_data["t_error"]

            resultado = CalculoReglaFalsa(funcion, t_error, xi, xs, tolerancia, niter)
            data["resultado"] = str(resultado)
        else:
            print("Formulario no valido")
    return render(request, "regla_falsa.html", data)


def puntofijo(request):
    data = {
        "form": PuntoFijoForm(),
    }
    if request.method == "POST":
        form = PuntoFijoForm(request.POST)
        if form.is_valid():
            funcion = form.cleaned_data["f"]
            g = form.cleaned_data["g"]
            x0 = form.cleaned_data["x0"]
            tolerancia = form.cleaned_data["tol"]
            niter = form.cleaned_data["niter"]

            resultado = CalculoPuntoFijo(funcion, x0, tolerancia, g, niter)
            data["resultado"] = str(resultado)
        else:
            print("Formulario no valido")
    return render(request, "punto_fijo.html", data)


def raicesmultiples(request):
    data = {
        "form": MultipleRootsForm(),
    }
    if request.method == "POST":
        form = MultipleRootsForm(request.POST)
        if form.is_valid():
            funcion = form.cleaned_data["f"]
            df = form.cleaned_data["df"]
            df2 = form.cleaned_data["df2"]
            x0 = form.cleaned_data["x0"]
            tolerancia = form.cleaned_data["tol"]
            niter = form.cleaned_data["niter"]

            resultado = CalculoRaicesMultiples(x0, funcion, df, df2, tolerancia, niter)
            data["resultado"] = str(resultado)
        else:
            print("Formulario no valido")
    return render(request, "raices_multiples.html", data)


def newton(request):
    data = {
        "form": NewtonForm(),
    }
    if request.method == "POST":
        form = NewtonForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data["f"]
            df = form.cleaned_data["df"]
            x0 = form.cleaned_data["x0"]
            tol = form.cleaned_data["tol"]
            niter = form.cleaned_data["niter"]

            resultado = CalculoNewton(f, df, x0, tol, niter)
            data["resultado"] = str(resultado)
    return render(request, "newton.html", data)


def secante(request):
    data = {
        "form": SecanteForm(),
    }
    if request.method == "POST":
        form = SecanteForm(request.POST)
        if form.is_valid():
            x0 = form.cleaned_data["x0"]
            x1 = form.cleaned_data["x1"]
            f = form.cleaned_data["f"]
            tol = form.cleaned_data["tol"]
            niter = form.cleaned_data["niter"]

            resultado = CalculoSecante(x0, x1, f, tol, niter)
            data["resultado"] = str(resultado)
    return render(request, "secante.html", data)


def gauss(request):
    data = {
        "form": GaussSimpleForm(),
    }
    if request.method == "POST":
        form = GaussSimpleForm(request.POST)
        if form.is_valid():
            aux = form.cleaned_data["aux"]
            a = form.cleaned_data["a"]
            b = form.cleaned_data["b"]
            filasA = a.split(",")
            filasB = b.split(",")
            if (len(filasA) == aux) and (len(filasB) == aux):
                # Convierte las matrices A y B en arrays de NumPy
                matriz_lista = [list(map(float, fila.split())) for fila in filasA]
                matriz_numpy = np.array(matriz_lista)
                ind_lista = [list(map(float, fila.split())) for fila in filasB]
                ind_numpy = np.array(ind_lista)
                resultado = CalculoGauss(matriz_numpy, ind_numpy, aux)
                data["resultado"] = str(resultado)
            else:
                data["resultado"] = "Las dimensiones de las matrices no coinciden"
    return render(request, "gauss.html", data)


def gauss_parcial(request):
    data = {
        "form": GaussSimpleForm(),
    }

    if request.method == "POST":
        form = GaussSimpleForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data["aux"]
            a = form.cleaned_data["a"]
            b = form.cleaned_data["b"]
            filasA = a.split(",")
            filasB = b.split(",")
            if len(filasA) == n:
                # Convierte las matrices A y B en arrays de NumPy
                matriz_lista = [list(map(float, fila.split())) for fila in filasA]
                matriz_numpy = np.array(matriz_lista)
                ind_lista = [list(map(float, fila.split())) for fila in filasB]
                ind_numpy = np.array(ind_lista)
                resultado = CalculoGaussPivoteo(matriz_numpy, ind_numpy, n)
                data["resultado"] = str(resultado)
            else:
                data["resultado"] = "Las dimensiones de las matrices no coinciden"
    return render(request, "gauss_parcial.html", data)


def lu(request):
    data = {
        "form": GaussSimpleForm(),
    }
    if request.method == "POST":
        form = GaussSimpleForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data["aux"]
            a = form.cleaned_data["a"]
            b = form.cleaned_data["b"]
            filasA = a.split(",")
            filasB = b.split(",")
            if len(filasA) == n:
                # Convierte las matrices A y B en arrays de NumPy
                matriz_lista = [list(map(float, fila.split())) for fila in filasA]
                matriz_numpy = np.array(matriz_lista)
                ind_lista = [list(map(float, fila.split())) for fila in filasB]
                ind_numpy = np.array(ind_lista)
                resultado = CalculoLU(matriz_numpy, ind_numpy, n)
                data["resultado"] = str(resultado)

            else:
                data["resultado"] = "Las dimensiones de las matrices no coinciden"

    return render(request, "lu.html", data)


def crout(request):
    return render(request, "crout.html")


def cholesky(request):
    return render(request, "cholesky.html")


def doolittle(request):
    return render(request, "doolittle.html")


def jacobi(request):
    return render(request, "jacobi.html")


def gaussseidel(request):
    return render(request, "gauss_seidel.html")
