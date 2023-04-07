from django.db import models

# Create your models here.


class Pelicula (models.Model):
    nombre = models.CharField(
        max_length=64, help_text="Escribe el nombre la pelicula"
    )

    fecha_estreno = models.DateField(null=True, blank=True)

    descripcion = models.CharField(
        max_length=200,  help_text="Escribe el descripción la pelicula")

    def __str__(self):
        return self.nombre


class Director (models.Model):
    nombre = models.CharField(
        max_length=64, help_text="Escribe el nombre del director"
    )

    apelido = models.CharField(
        max_length=64, help_text="Escribe el nombre del director"
    )

    fecha_nacimiento = models.DateField(null=True, blank=True)

    peliculas = models.ManyToManyField('Pelicula')

    def __str__(self):
        return self.nombre
