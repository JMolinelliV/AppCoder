from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso
from AppCoder.forms import CursoFormulario
# Create your views here.

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

def cursos(request):
    
    if request.method == "POST":

        miFormulario = CursoFormulario(request.POST) #me llega la información del HTML

        print(miFormulario)

        if miFormulario.is_valid: #si paso la validación de Django

            informacion = miFormulario.cleaned_data
            curso = Curso (nombre=informacion['curso'], camada=informacion['camada'])
            curso.save()
            return render(request, 'AppCoder/inicio.html') #vuelvo al inicio
    
    else:
        
        miFormulario = CursoFormulario() #Formulario vacío para construir el HTML

    return render(request, 'AppCoder/cursoFormulario.html', {'miFormulario':miFormulario})

def busquedaCamada(request):
    return render(request, 'AppCoder/busquedaCamada.html')

def buscar(request):
    
    if request.GET["camada"]:

        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada) #filter busca en la base de datos

        return render(request, "AppCoder/resultadosPorBusqueda.html", {"cursos":cursos, "camada":camada})
    
    else:

        respuesta = "No enviaste datos"

    return render(request, "AppCoder/inicio.html", {"respuesta":respuesta})