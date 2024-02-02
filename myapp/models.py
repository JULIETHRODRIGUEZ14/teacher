from django.db import models

# Create your models here.
#tabla llamada estudiantes
class Estudiantes (models.Model):
    name = models.CharField(max_length=200)

    def __str__(self): #metodo
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()#textfields es para etxtos largos
    estudiantes = models.ForeignKey(Estudiantes, on_delete=models.CASCADE)#si se borra un projecto derivado a este se borra en cascada

    def __str__(self):
        return self.title + "-" + self.estudiantes.name #concadenamos para que nos muestre todo

class Anuncios (models.Model):
    title = models.CharField(max_length=100)
    mensaje = models.TextField()
    fecha = models.DateTimeField
    horas = models.IntegerField
    remitente = models.CharField(max_length=20)
    acciones = models.CharField(max_length=200)

class Calificaciones (models.Model):
   estudiantes = models.ForeignKey(Estudiantes, on_delete=models.CASCADE)
   calificacion = models.CharField(max_length=15)

   #campo para representar el estado de aprobacion
   estado_aprobacion = models.IntegerField(choices=[(0, 'No aprobo'), (1, 'Aprobo')])

   def __str__(self):
       return f'{self.estudiantes} - {self.calificacion} - {self.get_estado_aprobacion_display()}'
   

