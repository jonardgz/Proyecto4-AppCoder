import datetime

from django.shortcuts import render
from AppCoder.models import Curso, Entregable


def inicio(request):
    return render(request, 'index.html')


def curso(request):
    curso1 = Curso(nombre="Python", camada=31095)
    curso1.save()
    contexto = {
        'curso': curso1
    }
    return render(request, 'AppCoder/Curso.html', contexto)


def entregable(request):
    entregable1 = Entregable(
        nombre="Jona",
        fecha_de_entrega=datetime.datetime.now(),
        entregado =True
    )
    entregable1.save()

    contexto = {
        'entregable': entregable1
    }

    return render(request, 'AppCoder/Entregable.html', contexto)
