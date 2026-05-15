from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class RegistroTreino(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Usuário'
    )

    GRUPO_MUSCULAR = [
        ('PEITO', 'Peito'),
        ('COSTAS', 'Costas'),
        ('PERNAS', 'Pernas'),
        ('BRACOS', 'Braços'),
        ('OMBROS', 'Ombros'),
    ]

    DIA_SEMANA_CHOICES = [
        ('1_SEG', 'Segunda-feira'),
        ('2_TER', 'Terça-feira'),
        ('3_QUA', 'Quarta-feira'),
        ('4_QUI', 'Quinta-feira'),
        ('5_SEX', 'Sexta-feira'),
        ('6_SAB', 'Sábado'),
        ('7_DOM', 'Domingo'),
    ]

    dia_semana = models.CharField(
        max_length=5,
        choices=DIA_SEMANA_CHOICES,
        default='1_SEG',
        verbose_name='Dia da Semana'
    )

    exercicio = models.CharField(max_length=100, verbose_name='Nome Exercício')
    grupoMuscular = models.CharField(
        max_length=20,
        choices=GRUPO_MUSCULAR,
        default="PEITO"
    )

    carga = models.DecimalField(
        max_digits=5, decimal_places=1,
        help_text="Carga em Kg",
    )

    series = models.PositiveIntegerField(verbose_name="Séries")
    repeticoes = models.PositiveIntegerField(verbose_name="Repetições")

    # dataTreino = models.DateField(auto_now=True)

    class Meta:
        ordering = ['dia_semana']

    def __str__(self):
        return f"{self.get_dia_semana_display()} - {self.exercicio}" #type: ignore