from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Empleado
import datetime

# Create your views here.
def inicio(request):
    template = loader.get_template('inicio.html')
    context = {
        None: None,
    }
    return HttpResponse(template.render(context, request))

def index(request, prm):
    try:
        empleado = Empleado.objects.get(id_of = prm)
        template = loader.get_template('index.html')
        fecha_actual = datetime.datetime.now()
        context = {
            "id_of": empleado.id_of,
            "nombre": empleado.nombre,
            "paterno": empleado.paterno,
            "materno": empleado.materno,
            "descripcion_puesto": empleado.descripcion_puesto,
            "descripcion_nivel": empleado.descripcion_nivel,
            "fecha": fecha_actual,
        }
    except Empleado.DoesNotExist:
        template = loader.get_template('noidentificado.html')
        context = {
            None: None,
        }
    return HttpResponse(template.render(context, request))

def noidentificado(request):
    template = loader.get_template('noidentificado.html')
    context = {
        None: None,
    }
    return HttpResponse(template.render(context, request))

def manejar_not_found(request, exception):
    return render(request, '404.html')
