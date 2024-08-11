from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Usuario, RegistroAsistencia

@login_required
@user_passes_test(lambda u: u.is_staff)  # Solo usuarios autorizados (ej. admin)
def perfil_usuario(request, user_id):
    usuario = get_object_or_404(Usuario, id=user_id)

    if request.method == 'POST':
        RegistroAsistencia.objects.create(usuario=usuario)
        return redirect('confirmacion_asistencia')

    return render(request, 'accesoapp/perfil.html', {'usuario': usuario})

@login_required
def confirmacion_asistencia(request):
    return render(request, 'accesoapp/confirmacion.html')

@login_required
def post_login(request):
    return render(request, 'accesoapp/post_login.html')