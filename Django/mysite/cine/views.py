from django.shortcuts import render

# Create your views here.

from .models import Pelicula, Director


def director(request):
    peliculas = Pelicula.objects.all()
    directores = Director.objects.all()

    return render(
        request,
        'director.html',
        context={
            'peliculas': peliculas,
            'directores': directores,
        }
    )


def peliculas(request):
    peliculas = Pelicula.objects.filter()
    return render(
        request,
        'peliculas.html',
        context={
            'peliclas' : peliculas
        }
    )
