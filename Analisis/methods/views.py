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
            xi = form.cleaned_data["Xi"]
            xf = form.cleaned_data["Xf"]
            funcion = form.cleaned_data["funcion"]
            tolerancia = form.cleaned_data["tolerancia"]
            niter = form.cleaned_data["NumeroIteraciones"]

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
    return render(request, "gauss.html")


def gauss_parcial(request):
    return render(request, "gauss_parcial.html")


def lu(request):
    return render(request, "lu.html")


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