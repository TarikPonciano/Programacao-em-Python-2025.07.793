from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastrar_paciente, name='cadastro'),
    path('pacientes/', views.listar_pacientes, name='pacientes'),
    path('pacientes/<int:id>/', views.ver_paciente, name='ver_paciente')
]