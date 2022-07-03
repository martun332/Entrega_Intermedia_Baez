from django.db import models

# Create your models here.

class familiares(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField(null=True)
    creacion = models.DateField(null=True)