from django.urls import path
from .views import inicio, lista_cursos, lista_estudiantes, detalle_estudiante, curso_form, detalle_curso

urlpatterns = [
    path('', inicio, name='inicio'),
    path('lista/estudiantes/', lista_estudiantes, name='lista_estudiantes'),
    path('detalle/estudiante/<int:pk>/', detalle_estudiante, name='detalle_estudiante'),
    path('lista/cursos/', lista_cursos, name='lista_cursos'),
    path('detalle/curso/<int:pk>/', detalle_curso, name='detalle_curso'),
    path('curso/form/', curso_form, name='curso_form'),
]