#Administrador de vistas
from django.http import HttpResponse
from django.template import Template, Context, loader
import datetime

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def segunda_vista(request):
    return HttpResponse("<br><br> <h1>Agregando otra vista<h1>")

def diaDeHoy(request):
    dia = datetime.datetime.now()
    documentoDeTexto = f"Hoy es dia <br> {dia}"
    return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre):
    documentoDeTexto = f"Mi nombre es <br> <h1>{nombre}<h1>"
    return HttpResponse(documentoDeTexto)

def probandoTemplate(self):
    nombre = "Guillermina"
    apellido = "Borrazas"

    nameList = ["Gabriel", "Jimena", "Guillermina", "Ignacio", "Patricia"]

    diccionario = {"Nombre":nombre, 
                   "Apellido": apellido,
                   "NameList": nameList,
    }
    #miHtml = open("C:/Users/PC/Documents/CODER PYTHON/PythonProjecto1/Proyecto1/Proyecto1/plantillas/template1.html") #Se puede mejorar
    plantilla = loader.get_template("template1.html")
    #plantilla = Template(miHtml.read()) #Mi html es la direccion donde apunta la template
    #miHtml.close()
    #miContext = Context(diccionario)
    #documento = plantilla.render(miContext) #Renderizar, darle vida al diseño
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def curso():
    pass
