from django.urls import path
from django.contrib.auth import views as auth_views
from .views import perfil_usuario, confirmacion_asistencia, post_login

urlpatterns = [
    path('perfil/<int:user_id>/', perfil_usuario, name='perfil_usuario'),
    path('confirmacion/', confirmacion_asistencia, name='confirmacion_asistencia'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('post-login/', post_login, name='post_login'),
]
