from django.urls import path
from .views import lista_estudiantes, detalle_estudiante

urlpatterns = [
    path('lista_estudiantes/', lista_estudiantes, name='lista_estudiantes'),
    path('detalle_estudiante/<int:pk>/', detalle_estudiante, name='detalle_estudiante')
]