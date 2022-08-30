import datetime
from django.shortcuts import render, redirect
from AppCoder.models import Curso, Entregable
from AppCoder.forms import CursoForm, busquedaCamadaForm


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


def cursoFormulario(request):
    if request.method == 'POST':
        MiFormulario = CursoForm(request.POST)
        if MiFormulario.is_valid():
            data = MiFormulario.cleaned_data
            curso1 = Curso(nombre=data.get('nombre'), camada=data.get('camada'))
            curso1.save()
            return redirect('AppCodercursoFormulario')

    cursos = Curso.objects.all()

    contexto = {
        'form': CursoForm(),
        'cursos': cursos
    }
    return render(request, "AppCoder/cursoFormulario.html", contexto)


def busquedaCamada(request):
    contexto = {
        'form': busquedaCamadaForm(),
    }
    return render(request, 'AppCoder/busquedaCamada.html', contexto)


def busquedaCamada_post(request):
    camada = request.GET.get('camada')

    cursos = Curso.objects.filter(camada__icontains=camada)
    contexto = {
        'cursos': cursos
    }

    return render(request, "AppCoder/cursoFiltrado.html", contexto)

