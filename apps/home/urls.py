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
    path("home_estudiante/", views.home_estudiante, name='home_estudiante'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
