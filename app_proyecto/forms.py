from django import forms

class FormCrearFamiliar(forms.Form):
    nombre = forms.CharField(max_length=30)
    email = forms.EmailField()
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField()
    fecha_creacion = forms.DateField(required=False)


class BuscarFamiliar(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)
    