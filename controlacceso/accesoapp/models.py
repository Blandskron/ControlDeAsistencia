from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    empresa = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class RegistroAsistencia(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.nombre} {self.usuario.apellido} - {self.fecha_hora}'
