# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here

class estudiante():
    pass
class Materia():
    nombreMateria = models.CharField(max_length=100) 
    codigoMateria = models.CharField(max_length=100)
    profesorAsignado = models.CharField(max_length=100)
    cantCantidad = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    valoracion = models.CharField(max_length=100)
    puntuacion = models.CharField(max_length=100)
    
class Programa(models.Model):
    nombre = models.CharField(max_length=100)
    pass

class Semestre(models.Model):
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name="semestres")
    numeroSemestre = models.IntegerField()
    cantidadCreditos = models.IntegerField()
    materias = models.
    
