from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path("novo/", views.TreinoCreateView.as_view(), name='novo_treino'),

    path("<int:pk>/editar/", views.TreinoUpdadeView.as_view(), name='editar_treino'),

    path("<int:pk>/apagar/", views.TreinoDeleteView.as_view(), name='apagar_treino'),

    path('reset/', views.reset_treios_view, name='reset_treinos')
]
