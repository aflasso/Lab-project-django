# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here

class estudiante():
    pass
class Materia(models.Model):
    nombreMateria = models.CharField(max_length=100) 
    codigoMateria = models.CharField(max_length=100)
    profesorAsignado = models.CharField(max_length=100)
    cantCantidad = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    valoracion = models.CharField(max_length=100)
    puntuacion = models.CharField(max_length=100)

class Valoracion(models.Model):
    asunto = models.CharField(max_length=100)
    comentario = models.CharField(max_length=100)
    puntuacion = models.CharField(max_length=100)
