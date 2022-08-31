from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('', inicio, name='AppCoderInicio'),
    path('curso/', CursoList.as_view(), name='AppCoderCurso'),
    path('entregable/', entregable, name='AppCoderEntregable'),
    path('cursoFormulario/', cursoFormulario, name='AppCodercursoFormulario'),
    path('busquedaCamada/', busquedaCamada, name='AppCoderBusquedaCamada'),
    path('busquedaCamadaPost/', busquedaCamada_post, name='AppCoderBusquedaCamadaPost'),
    path('eliminarCurso/<int:camada>', eliminar_Curso, name='AppCoderEliminarCurso'),
    path('editarCurso/<int:camada>', editar_curso, name='AppCoderEditarCurso'),
]
