from django.shortcuts import render, get_object_or_404, redirect
from .models import Estudiante, Profesor, Curso, Entregable
from .forms import CursoForm

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')


def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'lista_estudiantes.html', context={'estudiantes': estudiantes})


def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'detalle_estudiante.html', context={'estudiante': estudiante})

def lista_cursos(request):
    buscar = request.GET.get('buscar', '')
    cursos = Curso.objects.all()
    if buscar:
        cursos = cursos.filter(nombre__icontains=buscar)
    else:
        cursos = Curso.objects.all()
    return render(request, 'lista_cursos.html', context={'cursos': cursos})

def detalle_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, 'detalle_curso.html', context={'curso': curso})

def curso_form(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = form.save(commit=False)
            if request.user.is_authenticated:
                curso.autor = request.user
                curso.save()
                return redirect('lista_cursos')
            else:
                form.add_error(None, "Debe iniciar sesión para crear un curso.")
    else:
        form = CursoForm()
    return render(request, 'curso_form.html', context={'form': form})
