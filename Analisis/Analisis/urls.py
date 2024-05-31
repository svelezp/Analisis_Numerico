"""
URL configuration for Analisis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from methods import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home),
    path("about/", views.about, name="about"),
    path(
        "busquedas_Incrementales/",
        views.busquedasIncrementales,
        name="busquedas_incrementales",
    ),
    path("biseccion/", views.biseccion, name="biseccion"),
    path("regla_falsa/", views.reglafalsa, name="regla_falsa"),
    path("newton/", views.newton, name="newton"),
    path("secante/", views.secante, name="secante"),
    path("punto_fijo/", views.puntofijo, name="punto_fijo"),
    path("raices_multiples/", views.raicesmultiples, name="raices_multiples"),
    path("jacobi/", views.jacobi, name="jacobi"),
    path("gauss_seidel/", views.gaussseidel, name="gauss_seidel"),
    path("lu/", views.lu, name="lu"),
    path("cholesky/", views.cholesky, name="cholesky"),
    path("crout/", views.crout, name="crout"),
    path("doolittle/", views.doolittle, name="doolittle"),
    path("gauss_parcial/", views.gauss_parcial, name="gauss_parcial"),
    path("gauss/", views.gauss, name="gauss"),
]
