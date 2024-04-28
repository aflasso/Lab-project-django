# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    path('landing/', views.home_page, name='landing_page'),

    path("selecUser/", views.user_select, name='user_select'),
    










































    path("horario/", views.ver_materia, name='ver_materia'),
    path("agregarMateria/", views.agregar_materia, name='agregar_materia'),
    path("eliminarMateria/", views.eliminar_materia, name='eliminar_materia'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
