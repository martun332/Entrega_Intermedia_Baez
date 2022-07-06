from django.db import models

# Create your models here.

class familiares(models.Model):
    nombre = models.CharField(max_length=30, null=True)
    email = models.EmailField(null=True)
    edad = models.IntegerField(null=True)
    fecha_nacimiento = models.DateField(null=True)
    creacion = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return f'Nombre del familiar: {self.nombre}'