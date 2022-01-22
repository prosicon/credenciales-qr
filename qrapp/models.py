from django.db import models

# Create your models here.

class Empleado(models.Model):
    ide = models.PositiveSmallIntegerField()
    id_of = models.CharField(max_length=10)
    paterno = models.CharField(max_length=50)
    materno = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    descripcion_puesto = models.CharField(max_length=50)
    descripcion_nivel_puesto = models.CharField(max_length=100)
    descripcion_nivel = models.CharField(max_length=100)
    #fecha_creacion = models.DateTimeField(auto_now=True)
    #ultima_act = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.nombre)
