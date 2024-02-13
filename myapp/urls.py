from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index),
    path('profile/', views.profile),
    path('hello/<str:username>', views.hello), #<username> es una especie de variable
    path('estudiantes/', views.estudiantes),
    path('tasks/', views.tasks),
    path('calificaciones/', views.calificaciones),
    path('anuncios/', views.anuncios),
 
]
