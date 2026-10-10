from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def home(request):
    return render(request, "core/home.html")


def carreras(request):
    lista_carreras = [
        {"nombre": "Ingeniería en Informática", "jornada": "Diurna", "duracion": "8 semestres"},
        {"nombre": "Analista Programador", "jornada": "Vespertina", "duracion": "5 semestres"},
        {"nombre": "Ingeniería en Conectividad y Redes", "jornada": "Diurna", "duracion": "8 semestres"},
    ]
    return render(request, "core/carreras.html", {"carreras": lista_carreras})


def docentes(request):
    lista_docentes = [
        {"nombre": "Ana Pérez", "asignatura": "Taller Lenguaje de Programación"},
        {"nombre": "Carlos Soto", "asignatura": "Base de Datos"},
        {"nombre": "María Rojas", "asignatura": "Desarrollo Web"},
    ]
    return render(request, "core/docentes.html", {"docentes": lista_docentes})