from django.shortcuts import render

# Create your views here.

from .models import Book, Author, BookInstance, Genre


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_authors = Author.objects.all().count()
    num_genres = Genre.objects.all().count()

    disponibles = BookInstance.objects.filter(status__exact='a').all().count()

    return  render(
        request,
        'index.html',
        context={
            'num_books': num_books,
            'num_instances': num_instances,
            'num_authors': num_authors,
            'num_genres': num_genres,
            'disponibles': disponibles
        }
    ) 