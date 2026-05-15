from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import RegistroTreino

@admin.register(RegistroTreino)
class RegistroTreinoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'exercicio', 'dia_semana', 'grupoMuscular', 'carga')

    list_filter = ('usuario', 'dia_semana', 'grupoMuscular')

    search_fields = ('exercicio', 'usuario__username')

    list_per_page = 20