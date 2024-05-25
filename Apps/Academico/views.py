from django.shortcuts import render, redirect
from .models import Curso, Alumno
from django.contrib import messages

# Create your views here.

def home(request):
    cursosListado = Curso.objects.all()
    return render(request, "gestionCursos.html", {"cursos": cursosListado})

def gestionCurso(request):
    cursosListado = Curso.objects.all()
    return render(request, "gestionCursos.html", {"cursos": cursosListado})

def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']

    curso = Curso.objects.create(codigo=codigo, nombre=nombre)
    messages.success(request, '¡El curso ha sido registrado!')
    return redirect('/')

def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})

def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.save()

    messages.success(request, '¡El curso ha sido modificado!')

    return redirect('/')


def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    messages.success(request, '¡El curso ha sido eliminado!')
    return redirect('/')

#Alumnos
def gestionAlumno(request):
    alumnosListado = Alumno.objects.all()
    return render(request, "gestionAlumnos.html", {"alumnos": alumnosListado})

def registrarAlumno(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    fecha_nacimiento = request.POST['fcNacimiento']

    alumno = Alumno.objects.create(codigo=codigo, nombre=nombre,apellido=apellido,fecha_nacimiento=fecha_nacimiento)
    messages.success(request, '¡El alumno ha sido registrado!')

    alumnosListado = Alumno.objects.all()
    return render(request, "gestionAlumnos.html", {"alumnos": alumnosListado})

def edicionAlumno(request, codigo):
    alumno = Alumno.objects.get(codigo=codigo)
    return render(request, "edicionAlumno.html", {"alumno": alumno})

def editarAlumno(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    fecha_nacimiento = request.POST['fcNacimiento']

    alumno = Alumno.objects.get(codigo=codigo)
    alumno.nombre = nombre
    alumno.apellido = apellido
    alumno.fecha_nacimiento = fecha_nacimiento
    alumno.save()

    messages.success(request, '¡El alumno ha sido modificado!')

    alumnosListado = Alumno.objects.all()
    return render(request, "gestionAlumnos.html", {"alumnos": alumnosListado})


def eliminarAlumno(request, codigo):
    alumno = Alumno.objects.get(codigo=codigo)
    alumno.delete()
    messages.success(request, '¡El alumno ha sido eliminado!')
    
    alumnosListado = Alumno.objects.all()
    return render(request, "gestionAlumnos.html", {"alumnos": alumnosListado})