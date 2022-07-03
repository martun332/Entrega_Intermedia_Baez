from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import familiares
from datetime import datetime

# Create your views here.

def index(request):
    
    #print(request.GET)
    nombre = request.GET.get("nombre")
    email = request.GET.get("email")
    edad = request.GET.get("edad")
    fecha_nacimiento = request.GET.get("fecha_nac")
    
    familiar1 = familiares(nombre= nombre, email=email, edad=edad, fecha_nacimiento=fecha_nacimiento, creacion=datetime.now())
    familiar1.save()
    
    return render(request, 'index.html', {'familiar1' : familiar1})


def nosotros(request):
    return render(request, 'nosotros.html', {})
