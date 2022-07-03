from django.db import models

# Create your models here.

class nombredelmodelo(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    
    # despues de crear mi modelo ejecutar el 'py manage.py migrate' para pasarle el modelo a la BD