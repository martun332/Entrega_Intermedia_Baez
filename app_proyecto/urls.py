from re import I
from django.urls import path
from .views import index, nosotros

urlpatterns = [
    path('', index, name='pagina_index'),
    path('nosotros/', nosotros, name='pagina_nosotros'),
]