from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    profesion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.profesion}"
    

class Curso(models.Model):
    class Estado(models.TextChoices):
        ACTIVO = 'AC', 'Activo'
        INACTIVO = 'IN', 'Inactivo'
        FINALIZADO = 'FI', 'Finalizado'
    nombre = models.CharField(max_length=100)
    camada = models.IntegerField()
    fecha_inicio = models.DateField(default=timezone.now)
    duracion_meses = models.IntegerField(default=1)
    estado = models.CharField(
        max_length=2,
        choices=Estado.choices,
        default=Estado.INACTIVO,
    )
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre
    

class Entregable(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return self.nombre
