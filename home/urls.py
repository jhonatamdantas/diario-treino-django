from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='home/login.html'), name='login'),
    path("cadastro/", views.CadastrarUsuarioView.as_view(), name="cadastro_usuario"),

    path("sair/", auth_views.LogoutView.as_view(), name='logout')
]
