from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import Instructor

# Create your views here.

def instructores(request):
    lista_instructores = Instructor.objects.all().values()
    template = loader.get_template('lista_instructores.html')
    
    context = {
        'lista_instructores': lista_instructores,
        'total_instructores': lista_instructores.count(),
    }
    return HttpResponse(template.render(context, request))

def detalle_instructores(request, id_instructores):
  instructores = Instructor.objects.get(id=id_instructores)
  template = loader.get_template('detalle_instructores.html')
  context = {
    'instructores': instructores,
  }
  return HttpResponse(template.render(context, request))