from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('inicio/', inicio),
    path('cursos/', cursos, name="Cursos"),
    path('entregables/', entregables, name="Entregables"),
    path('profesores/', profesores, name="Profesores"),
    path('estudiantes/', estudiantes, name="Estudiantes"),
    path('setEstudiante/', setEstudiante, name= "setEstudiante"),
    path('getEstudiante/', getEstudiante, name= "getEstudiante"),
    path('buscarEstudiante/', buscarEstudiante, name="buscarEstudiante"),
    path('eliminarEstudiante/<nombre_estudiante>', eliminarEstudiante, name="eliminarEstudiante"),
    path('editarEstudiante/<nombre_estudiante>', editarEstudiante, name="editarEstudiante")
]
