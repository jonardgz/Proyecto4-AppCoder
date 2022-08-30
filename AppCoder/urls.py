from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('', inicio, name='AppCoderInicio'),
    path('curso/', curso, name='AppCoderCurso'),
    path('entregable/', entregable, name='AppCoderEntregable'),
    path('cursoFormulario/', cursoFormulario, name='AppCodercursoFormulario'),
    path('busquedaCamada/', busquedaCamada, name='AppCoderBusquedaCamada'),
    path('busquedaCamadaPost/', busquedaCamada_post, name='AppCoderBusquedaCamadaPost'),

]
