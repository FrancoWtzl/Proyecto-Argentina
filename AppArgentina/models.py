from django.db import models

class Cuerpo_tecnico (models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    puesto= models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + self.apellido + "-" + self.puesto

class Jugadores (models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    posicion= models.CharField(max_length=50)
    dorsal= models.IntegerField

    def __str__(self):
        return self.nombre + self.apellido + "-" + self.posicion + "-" + self.dorsal

class Competicion (models.Model):
    nombre= models.CharField(max_length=50)
    pais= models.CharField(max_length=50)