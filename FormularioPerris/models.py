from django.db import models

# Create your models here.
class Rescatado(models.Model):
    codigo = models.CharField(max_length=10)
    nombre =  models.CharField(max_length=30)
    tamano = models.CharField(max_length=30)
    peso = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    descripción = models.TextField()
    fechaRescate = models.DateField()
    op=(('R', 'Rescatado'),('D','Disponible'),('A','Adoptado'))
    estado= models.CharField(max_length=1, choices=op,default='R')

class Adoptante(models.Model):
    correo = models.CharField(max_length=60)
    rut =  models.CharField(max_length=11)
    nombres = models.CharField(max_length=90)
    pefechaNacimiento = models.CharField(max_length=12)
    telefono = models.CharField(max_length=12)
    region = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=30)
    tipoVivienda= models.CharField(max_length=50)