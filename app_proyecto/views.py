from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .forms import BuscarFamiliar, FormCrearFamiliar
from .models import familiares
from datetime import datetime

# Create your views here.
def index(request):
    render(request,'index.html', {})


def crear_familiar(request):
    if request.method == 'POST':
        form23 = FormCrearFamiliar(request.POST)
        
        if form23.is_valid():
            data= form23.cleaned_data
            
            fecha= data.get('fecha_creacion')
            if not fecha:
                fecha= datetime.now()
            
            familiar23 = familiares(
            nombre=data.get('nombre'),
            email=data.get('email'),
            edad=data.get('edad'),
            fecha_nacimiento=data.get('fecha_nacimiento'),
            creacion=fecha
            )
            familiar23.save()
            
            lista_familiares= familiares.objects.all
            
            return render(request, 'familia.html', {'lista_familiares': lista_familiares})
        else:
            return render(request, 'crearfamiliar.html', {'form_crear_familiar':form23})
        
    form_crear_familiar= FormCrearFamiliar()
    return render(request, 'crearfamiliar.html', {'form_crear_familiar':form_crear_familiar})



def familia(request):
    lista_familiares= familiares.objects.all
    return render(request, 'familia.html', {'lista_familiares': lista_familiares})



def nosotros(request):
    return render(request, 'nosotros.html', {})