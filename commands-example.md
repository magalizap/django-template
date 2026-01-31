# Django Shell Commands Example

## Creating and saving models

```python
from core.models import Estudiante, Profesor, Curso

# Create an Estudiante
estudiante1 = Estudiante(nombre="Pablo", apellido="Lopez", email="pablito@correp.com")
estudiante1.save()

# Create a Profesor
profesor = Profesor(nombre="Lautaro", apellido="Rodriguez", email="proflauty@correo.com", profesion="Profesor")
profesor.save()

# Create a Curso
curso = Curso(nombre="Python", camada=84730)
curso.save()
```
