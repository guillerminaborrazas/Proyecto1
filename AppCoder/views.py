from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def inicio(request):
    return(render(request, "AppCoder/inicio.html"))

def cursos(request):
    return(render(request, "AppCoder/cursos.html"))

def profesores(request):
    return(render(request, "AppCoder/profesores.html"))

def estudiantes(request):
    return("Vista estudiante")

def entregables(request):
    return("Vista entregables")