from django.contrib import admin
from .models import Usuario, RegistroAsistencia

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono', 'empresa')
    search_fields = ('nombre', 'apellido', 'email')

@admin.register(RegistroAsistencia)
class RegistroAsistenciaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'fecha_hora')
    search_fields = ('usuario__nombre', 'usuario__apellido')
