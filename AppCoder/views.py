from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppCoder.models import Estudiante
from AppCoder.forms import formSetEstudiante
# Create your views here.

def inicio(request):
    return(render(request, "AppCoder/inicio.html"))

def cursos(request):
    return(render(request, "AppCoder/cursos.html"))

def profesores(request):
    return(render(request, "AppCoder/profesores.html"))

def estudiantes(request):
    return(render(request, "AppCoder/estudiantes.html"))

def entregables(request):
    return(render(request, "AppCoder/entregables.html"))

def setEstudiante(request):
    if request.method == 'POST':
        miFormulario = formSetEstudiante(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data
            estudiante = Estudiante(nombre = data["nombre"], apellido = data["apellido"], email = data["email"])
            estudiante.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = formSetEstudiante
        return(render(request, "AppCoder/setEstudiante.html", {"miFormulario": miFormulario}))

    """if request.method == 'POST':
        estudiante = Estudiante(nombre = request.POST["nombre"], apellido = request.POST["apellido"], email = request.POST["email"])
        estudiante.save()
        return render(request, "AppCoder/inicio.html")
    return(render(request, "AppCoder/setEstudiante.html"))"""
def getEstudiante(request):

    return(render(request, "AppCoder/getEstudiante.html"))

def buscarEstudiante(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        estudiantes = Estudiante.objects.filter(nombre=nombre)

        return render(request, "AppCoder/getEstudiante.html", {"estudiantes": estudiantes})
    else:
        respuesta = "No se enviaron datos"
        return HttpResponse(respuesta)

