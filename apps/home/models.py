# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here

class estudiante():
    pass

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    codigo = models.CharField(max_length=30)
    facultad = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)
    materias = models.ManyToManyField(Materia, related_name = 'profesor')


class Materia(models.Model):
    nombreMateria = models.CharField(max_length=100) 
    codigoMateria = models.CharField(max_length=100)
    profesorAsignado = models.CharField(max_length=100)
    cantCantidad = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    valoracion = models.CharField(max_length=100)
    puntuacion = models.CharField(max_length=100)

