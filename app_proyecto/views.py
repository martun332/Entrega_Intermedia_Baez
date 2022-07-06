from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader

from .forms import BuscarFamiliar, FormCrearFamiliar
from .models import familiares
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,'index.html',{})


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
            
            return redirect('pagina_familia')
        else:
            return render(request, 'crearfamiliar.html', {'form_crear_familiar':form23})
        
    form_crear_familiar= FormCrearFamiliar()
    return render(request, 'crearfamiliar.html', {'form_crear_familiar':form_crear_familiar})



def familia(request):
    datonombre= request.GET.get('nombre')
    
    if datonombre:
        lista_familiares = familiares.objects.filter(nombre__icontains=datonombre)
    else:
        lista_familiares= familiares.objects.all
        
    form25= BuscarFamiliar()
    return render(request, 'familia.html', {'lista_familiares': lista_familiares, 'formget':form25})



def nosotros(request):
    return render(request, 'nosotros.html', {})