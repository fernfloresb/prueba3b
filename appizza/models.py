from django.db import models

class Tamano(models.Model):
    descripcion=models.CharField(max_length=50)
    def __str__(self):
        return self.descripcion

class Ingrediente(models.Model):
    nombre=models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Pizza(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    ingredientes=models.ManyToManyField('Ingrediente', related_name='ingredientes')
    tamano=models.CharField(max_length=50)
    def __str__(self):
        return self.nombre


