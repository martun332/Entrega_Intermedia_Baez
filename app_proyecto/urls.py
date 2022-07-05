from re import I
from django.urls import path
from .views import index, nosotros, familia, crear_familiar

urlpatterns = [
    path('', index, name='pagina_index'),
    path('creacion/', crear_familiar, name='pagina_crear_familiar'),
    path('familia/', familia, name='pagina_familia'),
    path('nosotros/', nosotros, name='pagina_nosotros'),
]