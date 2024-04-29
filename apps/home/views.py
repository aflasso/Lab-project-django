# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from .models import Materia
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms


@login_required(login_url="/landing/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/landing_page.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/landing/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

def home_page(request):
    footer_template = loader.get_template('home/footer.html')
    footer_html = footer_template.render({}, request)
    html_template = loader.get_template('home/landing_page.html')
    return HttpResponse(html_template.render({'footer_html': footer_html}, request))

def user_select(request):

    html_template = loader.get_template('accounts/login_select.html')
    return HttpResponse(html_template.render({}, request))

class MateriasListado(ListView):
    model = Materia

class MateriaCrear(SuccessMessageMixin, CreateView):
    model = Materia
    form = Materia
    fields = '__all__'
    success_message = 'Materia creada exitosamente'

    def get_success_url(self):        
        return reverse('home_estudiante') # Redireccionamos a la vista principal 'leer'

class MateriaDetalle(DetailView):
    model = Materia

class MateriaActualizar(SuccessMessageMixin, UpdateView):
    model = Materia
    form = Materia
    fields = '__all__'
    success_message = 'Materia Actualizada'

    def get_success_url(self):        
        return reverse('home_estudiante')
    
class MateriaEliminar(SuccessMessageMixin, DetailView):
    model = Materia
    form = Materia
    fields = '__all__'

    def get_success_url(self): 
        success_message = 'Materia Eliminada Correctamente !' # Mostramos este Mensaje luego de Editar una Arepa 
        messages.success(self.request, (success_message))       
        return reverse('home_estudiante') # Redireccionamos a la vista principal 'leer'

    

def ver_materia(request):
    header_template = loader.get_template('home/header.html')
    header_html = header_template.render({}, request)

    footer_template = loader.get_template('home/footer.html')
    footer_html = footer_template.render({}, request)
    html_template = loader.get_template('home/horario-estudiante.html')
    return HttpResponse(html_template.render({'header_html': header_html,'footer_html': footer_html}, request))

def agregar_materia(request):
    header_template = loader.get_template('home/header.html')
    header_html = header_template.render({}, request)

    footer_template = loader.get_template('home/footer.html')
    footer_html = footer_template.render({}, request)
    
    html_template = loader.get_template('home/agregar-materia.html')
    return HttpResponse(html_template.render({'header_html': header_html,'footer_html': footer_html}, request))

def eliminar_materia(request):
    header_template = loader.get_template('home/header.html')
    header_html = header_template.render({}, request)

    footer_template = loader.get_template('home/footer.html')
    footer_html = footer_template.render({}, request)
    html_template = loader.get_template('home/eliminar-materia.html')
    return HttpResponse(html_template.render({'header_html': header_html,'footer_html': footer_html}, request))
