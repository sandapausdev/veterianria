from django.db import models

# Create your models here.
class Especie(models.Model):
    nombre_especie = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_especie

class Raza(models.Model):
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    nombre_raza = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_raza

class Mascota(models.Model):
    
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    nombre_mascota = models.CharField(max_length=50)
    edad_mascota = models.IntegerField(default=0)
    color = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField("Fecha de registro de mascota")
    peso = models.IntegerField(default=0)
    estado = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nombre_mascota

class Donacion(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha_donacion = models.DateTimeField("fecha de donacion")
    nombre_cliente = models.CharField(max_length=200)
    dni = models.CharField(max_length=8)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre_cliente