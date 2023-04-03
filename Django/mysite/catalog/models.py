from django.db import models
from django.urls import reverse
# Create your models here.


class Genere (models.Model):
    name = models.CharField(
        max_length=64, help_text="Pon el nombre de genero")

    def __str__(self):
        return self.name

class Libro (models.Model) :
    title = models.CharField(max_length=32)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=100, help_text="Escribe la sintesis del libro")
    isbn = models.CharField('ISBN', max_length=13, help_text="ISBN de 13 caracteres")
    genere = models.ManyToManyRel(Genere)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self) :
        return reverse('book-detail', args=[str(self.id)])
    
