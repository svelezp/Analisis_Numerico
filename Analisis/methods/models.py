from django.db import models


# Create your models here.
class modelo1(models.Model):
    Xi = models.FloatField()
    funcion = models.TextField(blank=True, null=True)
    delta = models.FloatField()
    NumeroIteraciones = models.IntegerField()

    def __str__(self):
        return self.nombre


class modelo2(models.Model):
    Xi = models.FloatField(blank=True, null=True)
    Xf = models.FloatField(blank=True, null=True)
    funcion = models.TextField(blank=True, null=True)
    tolerancia = models.FloatField()
    NumeroIteraciones = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class modelo3(models.Model):
    Xi = models.FloatField()
    Xf = models.FloatField()
    funcion = models.TextField(blank=True, null=True)
    tolerancia = models.FloatField()
    NumeroIteraciones = models.IntegerField()

    def __str__(self):
        return self.nombre


class modelo4(models.Model):
    funcion = models.TextField(blank=True, null=True)
    Xi = models.FloatField()
    tolerancia = models.FloatField()
    g = models.TextField(blank=True, null=True)
    NumeroIteraciones = models.IntegerField()

    def __str__(self):
        return self.nombre


class modelo5(models.Model):
    Xi = models.FloatField()
    funcion = models.TextField(blank=True, null=True)
    tolerancia = models.FloatField()
    NumeroIteraciones = models.IntegerField()

    def __str__(self):
        return self.nombre


class modelo6(models.Model):
    A = models.TextField(blank=True, null=True)
    n = models.IntegerField()

    def __str__(self):
        return self.nombre


class modelo7(models.Model):
    A = models.TextField(blank=True, null=True)
    b = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class modelo8(models.Model):
    A = models.TextField(blank=True, null=True)
    b = models.TextField(blank=True, null=True)
    tolerancia = models.FloatField()
    NumeroIteraciones = models.IntegerField()

    def __str__(self):
        return self.nombre
