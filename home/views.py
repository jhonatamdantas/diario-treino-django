from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

class CadastrarUsuarioView(CreateView):
    form_class = UserCreationForm

    template_name = 'home/cadastro.html'
    success_url = reverse_lazy('login')