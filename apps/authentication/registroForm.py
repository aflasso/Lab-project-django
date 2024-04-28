from django import forms

from django import forms
from apps.home.models import Estudiante
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(forms.Form):

    usuario = UserCreationForm()
    nombre = forms.CharField()
    apellido = forms.CharField()
    programa_academico_id = forms.IntegerField()
