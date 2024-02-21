from django.http import HttpResponse
from .models import Estudiantes, Task, Calificaciones, Anuncios
from django.shortcuts import render, redirect
#from django.shortcuts import get_object_or_404 #la funcion permite traer un objeto si no esxiste va a devolver una pagina de 404
from .forms import CreateNewTask


# Create your views here.
#funcion recibe un parametro request
#render es enviar

def index(request):
    #hacemos un diccionario para que se vea en html
    title = 'WELCOME'
    return render(request,'index.html',{
        'title': title
    })


def hello(request, username):
    # print(type(id))
    # result = id + 100 *2 otra manera de manera entero en el return ya iria en el parametro %result
    return HttpResponse("<h1>Hello %s</h1>" %username)#%sparametros llamdno usename concadena con %

def profile(request):
    #return HttpResponse("profile")
    profile = 'Welcome teacher'
    return render(request, 'profile.html',{
        'profile': profile
    })

def estudiantes(request):
    #estudiantes = list(Estudiantes.objects.values())
    # return JsonResponse(estudiantes, safe=False)
    estudiantes = Estudiantes.objects.all()
    return render(request, 'estudiantes.html',{
        'estudiantes' : estudiantes
    })

def tasks(request):
    #task = Task.objects.get(id=id)
    #task = Task.objects.get(title=title)
    #task = get_object_or_404(Task, id=id)# si no encuentra la tarea va a cabar alli mismo
    tasks = Task.objects.all()
    #return HttpResponse("task: %s" % task.title)
    return render (request, 'tasks.html',{
        'tasks': tasks
    })


def calificaciones(request):
    calificacion = Calificaciones.objects.all()
    #return HttpResponse("calificacion: %s" % calificacion)
    return render (request, 'calificaciones.html',{
        'calificacion': calificacion
    })

def anuncios(request):

    anuncio = Anuncios.objects.all()
    return render(request, 'anuncios.html',{
        'anuncio': anuncio #le pasamos un parametro 'anuncio'
    })

def create_task(request):
    return render(request, 'crear.html',{
        'form': CreateNewTask
    }) 

def create_or_update_task(request):
    if request.method == 'POST':
        form = CreateNewTask(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            # Realiza alguna lógica para determinar si la tarea está aprobada o no
            if task.done:
                task.estado = True  # Marca la tarea como aprobada si está completada
            else:
                task.estado = False
            task.save()
            return redirect('tasks')
    else:
        form = CreateNewTask()
    return render(request, 'crear.html', {'form': form})

def calificar(request, tarea_id):
    tarea = Task.objects.get(pk=tarea_id)# Obtener la tarea por su ID
    if request.method == 'POST':
        # Obtener la calificación del formulario (suponiendo que tienes un formulario para la calificación)
        calificacion = request.POST.get('calificacion')
        # Actualizar la tarea con la calificación
        tarea.calificacion = calificacion
        tarea.save()
        # Redireccionar a alguna página, por ejemplo, la lista de tareas
        return redirect('tasks')
    else:
        tarea = Task.objects.get(pk=tarea_id)# Obtener la tarea por su ID
        # Si no es una solicitud POST, renderiza el formulario de calificación
        return render(request, 'calificaciones.html', {'tarea': tarea})
