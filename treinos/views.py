from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import RegistroTreino
from .forms import TreinoForm

class TreinoCreateView(LoginRequiredMixin, CreateView):
    model = RegistroTreino
    form_class = TreinoForm
    template_name = 'treinos/cadastro_treino.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    

class DashboardView(LoginRequiredMixin, ListView):
    model = RegistroTreino
    template_name = 'treinos/dashboard.html'
    context_object_name = 'treinos'

    def get_queryset(self):
        return RegistroTreino.objects.filter(usuario=self.request.user)
    

class TreinoUpdadeView(LoginRequiredMixin, UpdateView):
    model = RegistroTreino
    form_class = TreinoForm
    template_name = 'treinos/editar_treino.html'
    success_url = reverse_lazy('dashboard')

    def get_queryset(self):
        return RegistroTreino.objects.filter(usuario=self.request.user)
    
class TreinoDeleteView(LoginRequiredMixin, DeleteView):
    model = RegistroTreino
    template_name = 'treinos/confirmar_exclusao.html'
    success_url = reverse_lazy('dashboard')

    def get_queryset(self):
        return RegistroTreino.objects.filter(usuario=self.request.user)
    
@login_required
def reset_treios_view(request):
    RegistroTreino.objects.filter(usuario=request.user).delete()
    return redirect('dashboard')
