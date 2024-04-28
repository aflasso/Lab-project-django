# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Estudiante(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    codigo = models.CharField(max_length=30)
    correo = models.EmailField()
    programa_academico = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name='estudiantes')
    materias = models.ManyToManyField(Materia, related_name='estudiantes')
    usuario = models.CharField(max_length=20)
    constrasena = models.CharField(max_length=20)
