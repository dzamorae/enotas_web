from django.urls import path
from . import views

urlpatterns = [
    path('', views.home) ,
    path('gestionCurso/', views.home) ,
    path('registrarCurso/', views.registrarCurso) ,
    path('edicionCurso/<codigo>', views.edicionCurso) ,
    path('editarCurso/', views.editarCurso) ,
    path('eliminarCurso/<codigo>', views.eliminarCurso),

    path('gestionAlumnos/', views.gestionAlumno) ,
    path('registrarAlumno/', views.registrarAlumno) ,
    path('edicionAlumno/<codigo>', views.edicionAlumno) ,
    path('editarAlumno/', views.editarAlumno) ,
    path('eliminarAlumno/<codigo>', views.eliminarAlumno),
]