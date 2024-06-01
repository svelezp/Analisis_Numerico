from django import forms


class busquedasIncrementalesForm(forms.Form):
    f = forms.CharField(label="Función f(x)")
    xi = forms.FloatField(label="Valor inicial xi")
    delta = forms.FloatField(label="Delta")
    niter = forms.IntegerField(label="Número de iteraciones")

    def clean(self):
        cleaned_data = super().clean()
        xi = cleaned_data.get("xi")
        delta = cleaned_data.get("delta")
        niter = cleaned_data.get("niter")

        if delta <= 0:
            raise forms.ValidationError("El delta debe ser mayor que cero")

        if niter <= 0:
            raise forms.ValidationError(
                "El número de iteraciones debe ser mayor que cero"
            )

        return cleaned_data


class BiseccionForm(forms.Form):
    f = forms.CharField(label="Función f(x)")
    xi = forms.FloatField(label="Valor inicial xi")
    xs = forms.FloatField(label="Valor inicial xs")
    tol = forms.FloatField(label="Tolerancia")
    niter = forms.IntegerField(label="Número de iteraciones")

    def clean(self):
        cleaned_data = super().clean()
        xi = cleaned_data.get("xi")
        xs = cleaned_data.get("xs")
        tol = cleaned_data.get("tol")
        niter = cleaned_data.get("niter")

        if xi >= xs:
            raise forms.ValidationError("El valor inicial xi debe ser menor que xs")

        if tol <= 0:
            raise forms.ValidationError("La tolerancia debe ser mayor que cero")

        if niter <= 0:
            raise forms.ValidationError(
                "El número de iteraciones debe ser mayor que cero"
            )

        return cleaned_data


class ReglaFalsaForm(forms.Form):

    f = forms.CharField(label="Función f(x)")
    xi = forms.FloatField(label="Valor inicial xi")
    xs = forms.FloatField(label="Valor inicial xs")
    tol = forms.FloatField(label="Tolerancia")
    niter = forms.IntegerField(label="Número de iteraciones")

    def clean(self):
        cleaned_data = super().clean()
        xi = cleaned_data.get("xi")
        xs = cleaned_data.get("xs")
        tol = cleaned_data.get("tol")
        t_error = cleaned_data.get("t_error")
        niter = cleaned_data.get("niter")

        if xi >= xs:
            raise forms.ValidationError("El valor inicial xi debe ser menor que xs")

        if tol <= 0:
            raise forms.ValidationError("La tolerancia debe ser mayor que cero")

        if niter <= 0:
            raise forms.ValidationError(
                "El número de iteraciones debe ser mayor que cero"
            )

        # Aquí podrías realizar otras validaciones si es necesario

        return cleaned_data


# def punto_fijo(f, g, x0, tol, niter):
class PuntoFijoForm(forms.Form):
    f = forms.CharField(label="Función f(x)")
    g = forms.CharField(label="Función g(x)")
    x0 = forms.FloatField(label="Valor inicial x0")
    tol = forms.FloatField(label="Tolerancia")
    niter = forms.IntegerField(label="Número de iteraciones")

    def clean(self):
        cleaned_data = super().clean()
        x0 = cleaned_data.get("x0")
        tol = cleaned_data.get("tol")
        niter = cleaned_data.get("niter")

        if tol <= 0:
            raise forms.ValidationError("La tolerancia debe ser mayor que cero")

        if niter <= 0:
            raise forms.ValidationError(
                "El número de iteraciones debe ser mayor que cero"
            )

        # Aquí podrías realizar otras validaciones si es necesario

        return cleaned_data


# def newton(f, df, x0, tol, niter):
class NewtonForm(forms.Form):
    f = forms.CharField(label="Función f(x)")
    df = forms.CharField(label="Derivada de f(x)")
    x0 = forms.FloatField(label="Valor inicial x0")
    tol = forms.FloatField(label="Tolerancia")
    niter = forms.IntegerField(label="Número de iteraciones")

    def clean(self):
        cleaned_data = super().clean()
        x0 = cleaned_data.get("x0")
        tol = cleaned_data.get("tol")
        niter = cleaned_data.get("niter")

        if tol <= 0:
            raise forms.ValidationError("La tolerancia debe ser mayor que cero")

        if niter <= 0:
            raise forms.ValidationError(
                "El número de iteraciones debe ser mayor que cero"
            )

        # Aquí podrías realizar otras validaciones si es necesario

        return cleaned_data


# def secante(x0, x1, f, tol, niter)
class SecanteForm(forms.Form):
    f = forms.CharField(label="Función f(x)")
    x0 = forms.FloatField(label="Valor inicial x0")
    x1 = forms.FloatField(label="Valor x1")
    tol = forms.FloatField(label="Tolerancia")
    niter = forms.IntegerField(label="Número de iteraciones")

    def clean(self):
        cleaned_data = super().clean()
        x0 = cleaned_data.get("x0")
        x1 = cleaned_data.get("x1")
        tol = cleaned_data.get("tol")
        niter = cleaned_data.get("niter")

        if x0 >= x1:
            raise forms.ValidationError("El valor inicial x0 debe ser menor que x1")

        if tol <= 0:
            raise forms.ValidationError("La tolerancia debe ser mayor que cero")

        if niter <= 0:
            raise forms.ValidationError(
                "El número de iteraciones debe ser mayor que cero"
            )

        # Aquí podrías realizar otras validaciones si es necesario

        return cleaned_data


# multiple_roots(x0, f, df, df2, tol, niter)
class MultipleRootsForm(forms.Form):
    f = forms.CharField(label="Función f(x)")
    df = forms.CharField(label="Derivada de f(x)")
    df2 = forms.CharField(label="Segunda derivada de f(x)")
    x0 = forms.FloatField(label="Valor inicial x0")
    tol = forms.FloatField(label="Tolerancia")
    niter = forms.IntegerField(label="Número de iteraciones")

    def clean(self):
        cleaned_data = super().clean()
        x0 = cleaned_data.get("x0")
        tol = cleaned_data.get("tol")
        niter = cleaned_data.get("niter")

        if tol <= 0:
            raise forms.ValidationError("La tolerancia debe ser mayor que cero")

        if niter <= 0:
            raise forms.ValidationError(
                "El número de iteraciones debe ser mayor que cero"
            )

        # Aquí podrías realizar otras validaciones si es necesario

        return cleaned_data


class GaussSimpleForm(forms.Form):
    aux = forms.IntegerField(label="Tamaño de la matriz cuadrada")
    a = forms.CharField(label="Matriz de coeficientes A")
    b = forms.CharField(label="Términos independientes b")

    def clean(self):
        cleaned_data = super().clean()
        aux = cleaned_data.get("aux")

        if (aux <= 1) or (aux > 7):
            raise forms.ValidationError(
                "La matriz cuadrada nxn debe ser al menos 2x2 y máximo 7x7"
            )

        # Aquí podrías realizar otras validaciones si es necesario

        return cleaned_data


# jacobi(a, b, init, tol, n, err_type="abs"):
class JacobiForm(forms.Form):
    OPCIONES_ERROR = [
        ("abs", "Error absoluto"),
        ("rel", "Error relativo"),
    ]

    aux = forms.IntegerField(label="Tamaño de la matriz cuadrada")
    a = forms.CharField(label="Matriz de coeficientes A")
    b = forms.CharField(label="Términos independientes b")
    init = forms.FloatField(label="Valor inicial")
    err_type = forms.ChoiceField(choices=OPCIONES_ERROR, label="Tipo de Error")
    tol = forms.FloatField(label="Tolerancia")
    n = forms.IntegerField(label="Número de iteraciones")

    def clean(self):
        cleaned_data = super().clean()
        tol = cleaned_data.get("tol")
        n = cleaned_data.get("n")
        aux = cleaned_data.get("aux")

        if tol <= 0:
            raise forms.ValidationError("La tolerancia debe ser mayor que cero")

        if n <= 0:
            raise forms.ValidationError(
                "El número de iteraciones debe ser mayor que cero"
            )

        if (aux <= 1) or (aux > 7):
            raise forms.ValidationError(
                "La matriz cuadrada nxn debe ser al menos 2x2 y máximo 7x7"
            )

        # Aquí podrías realizar otras validaciones si es necesario

        return cleaned_data


# seidel(a, b, init, tol, n, err_type)
class SeidelForm(forms.Form):
    OPCIONES_ERROR = [
        ("abs", "Error absoluto"),
        ("rel", "Error relativo"),
    ]

    aux = forms.IntegerField(label="Tamaño de la matriz cuadrada")
    a = forms.CharField(label="Matriz de coeficientes A")
    b = forms.CharField(label="Términos independientes b")
    init = forms.FloatField(label="Valor inicial")
    err_type = forms.ChoiceField(choices=OPCIONES_ERROR, label="Tipo de Error")
    tol = forms.FloatField(label="Tolerancia")
    n = forms.IntegerField(label="Número de iteraciones")

    def clean(self):
        cleaned_data = super().clean()
        tol = cleaned_data.get("tol")
        n = cleaned_data.get("n")
        aux = cleaned_data.get("aux")

        if tol <= 0:
            raise forms.ValidationError("La tolerancia debe ser mayor que cero")

        if n <= 0:
            raise forms.ValidationError(
                "El número de iteraciones debe ser mayor que cero"
            )

        if (aux <= 1) or (aux > 7):
            raise forms.ValidationError(
                "La matriz cuadrada nxn debe ser al menos 2x2 y máximo 7x7"
            )

        # Aquí podrías realizar otras validaciones si es necesario

        return cleaned_data
