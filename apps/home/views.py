# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


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

def home_estudiante(request):
    header_template = loader.get_template('home/header.html')
    header_html = header_template.render({}, request)

    footer_template = loader.get_template('home/footer.html')
    footer_html = footer_template.render({}, request)

    html_template = loader.get_template('home/home_estudiante.html')
    return HttpResponse(html_template.render({'header_html': header_html,'footer_html': footer_html}, request))

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
