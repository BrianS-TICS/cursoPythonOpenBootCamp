from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Pelicula, Director


def director(request):

    directores = Director.objects.all()

    return render(
        request,
        'director.html',
        context={
            'directores': directores,
        }
    )


def peliculas(request, director_id):

    director = get_object_or_404(Director, id=director_id)
    peliculas = Pelicula.objects.filter(director=director)

    return render(
        request,
        'peliculas.html',
        context={
            'peliculas': peliculas
        }
    )
