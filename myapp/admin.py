from django.contrib import admin
from .models import Estudiantes, Task, Calificaciones, Anuncios

# Register your models here.
admin.site.register(Estudiantes)
admin.site.register(Task)
admin.site.register(Calificaciones)
admin.site.register(Anuncios)
