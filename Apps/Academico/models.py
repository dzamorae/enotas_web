from django.db import models

# Create your models here.

class Curso(models.Model):
    codigo = models.CharField(primary_key=True,max_length=5)
    nombre = models.CharField(max_length=50)

    def __str__(self) -> str:
        texto = "{0}"
        return texto.format(self.nombre)
    
# Modelo para representar a los estudiantes
class Alumno(models.Model):
    codigo = models.CharField(primary_key=True,max_length=8)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self) -> str:
        texto = "{0} {1}"
        return texto.format(self.nombre, self.apellido)
