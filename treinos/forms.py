from django import forms
from .models import RegistroTreino

class TreinoForm(forms.ModelForm):
    class Meta:
        model = RegistroTreino

        fields = [
            'dia_semana',
            'exercicio', 
            'grupoMuscular', 
            'carga', 
            'series', 
            'repeticoes']

        widgets = {
            'dia_semana': forms.Select(attrs={'class': 'form-control'}),
            'exercicio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Supino Reto'}),
            'carga': forms.NumberInput(attrs={'class': 'form-control'}),
            'series': forms.NumberInput(attrs={'class': 'form-control'}),
            'repeticoes': forms.NumberInput(attrs={'class': 'form-control'}),
        }