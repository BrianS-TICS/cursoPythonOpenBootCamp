from django.contrib import admin

# Register your models here.

from .models import Pelicula, Director
admin.site.register(Pelicula)
admin.site.register(Director)
