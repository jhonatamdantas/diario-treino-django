# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect 

def custom_404(request, exception):
    return redirect('login')

urlpatterns = [
    path('admin/', admin.site.urls),

    # App Home: Cuida da raiz do site, Login e Cadastro de Usuário
    path('', include('home.urls')), 

    # App Treinos: Cuida de toda a lógica de exercícios e rotinas
    path('treinos/', include('treinos.urls')),
]

handler404 = custom_404