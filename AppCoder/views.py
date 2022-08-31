import datetime, django

from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from AppCoder.models import Curso, Entregable
from AppCoder.forms import CursoForm, busquedaCamadaForm


def inicio(request):
    return render(request, 'index.html')


class CursoList(ListView):
    model = Curso
    template_name = 'AppCoder/Curso.html'


#def curso(request):
#    cursos = Curso.objects.all()
#    contexto = {
#        'cursos': cursos
#    }
#    }
#
#    return render(request, 'AppCoder/Curso.html', contexto)


def editar_curso(request, camada):
    curso_editar = Curso.objects.get(camada=camada)

    if request.method == 'POST':
        MiFormulario = CursoForm(request.POST)

        if MiFormulario.is_valid():
            data = MiFormulario.cleaned_data
            curso_editar.nombre = data.get('nombre')
            curso_editar.camada = data.get('camada')

            try:
                curso_editar.save()

            except django.db.utils.IntegrityError:
                messages.error(request, "La modificacion fallo por la camada ya existe.")

            return redirect('AppCoderCurso')

    contexto = {
        'form': CursoForm(
            initial={
                "nombre": curso_editar.nombre,
                "camada": curso_editar.camada
            }
        )
    }

    return render(request, "AppCoder/cursoFormulario.html", contexto)


def eliminar_Curso(request, camada):
    curso_elimnar = Curso.objects.get(camada=camada)
    curso_elimnar.delete()

    messages.info(request, f"El Curso {curso_elimnar} fue eliminado")

    return redirect('AppCoderCurso')


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

            return redirect('AppCoderCurso')

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

