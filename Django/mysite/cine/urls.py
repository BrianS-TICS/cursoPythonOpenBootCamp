from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('peliculas/<int:director_id>/', views.peliculas, name='peliculas'),
    re_path('director/', views.director, name='director'),
]   