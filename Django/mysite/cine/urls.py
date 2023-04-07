from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('director/', views.director, name='director'),
    re_path('peliculas/', views.peliculas, name='peliculas'),
]