# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    codigo = models.CharField(max_length=30)
    facultad = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)

class Programa(models.Model):
    nombre = models.CharField(max_length=100)

class Semestre(models.Model):
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name="semestres")
    numeroSemestre = models.IntegerField()
    cantidadCreditos = models.IntegerField()

class Materia(models.Model):
    nombreMateria = models.CharField(max_length=100) 
    codigoMateria = models.CharField(max_length=100)
    profesorAsignado = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='materias')
    cantCreditos = models.IntegerField()
    horario = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    puntuacion = models.CharField(max_length=100)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE, related_name='materias')

class Estudiante(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    codigo = models.CharField(max_length=30)
    correo = models.EmailField()
    programa_academico = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name='estudiantes')
    materias = models.ManyToManyField(Materia, through='Inscripcion', related_name='estudiantes')
    usuario = models.CharField(max_length=20)
    constrasena = models.CharField(max_length=20)


class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    aprobado = models.BooleanField(default=False)
    cursando = models.BooleanField()

class Valoracion(models.Model):
    asunto = models.CharField(max_length=100)
    comentario = models.CharField(max_length=100)
    puntuacion = models.CharField(max_length=100)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='valoraciones')
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='valoraciones')
