from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
#from .models import <nombredelmodelo>  (para importar modelos)

# Create your views here.

def index(request):
    return render(request, 'index.html', {})


def nosotros(request):
    return render(request, 'nosotros.html', {})
