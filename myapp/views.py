from django.http import HttpResponse
from .models import Estudiantes, Task, Calificaciones
from django.shortcuts import render
#from django.shortcuts import get_object_or_404 #la funcion permite traer un objeto si no esxiste va a devolver una pagina de 404



# Create your views here.
#funcion recibe un parametro request
#render es enviar

def index(request):
    #hacemos un diccionario para que se vea en html
    title = 'welcome'
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

def tasks(request, title):
    #task = Task.objects.get(id=id)
    #task = Task.objects.get(title=title)
    #task = get_object_or_404(Task, id=id)# si no encuentra la tarea va a cabar alli mismo
    #return HttpResponse("task: %s" % task.title)
    return render (request, tasks.html)
def calificaciones(request):
    calificacion = calificacion.objects.get(id=id)
    #return HttpResponse("calificacion: %s" % calificacion)
    return render (request, calificacion.html)
