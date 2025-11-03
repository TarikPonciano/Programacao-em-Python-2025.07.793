from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name="home"),
    path('cadastro/', views.cadastro_funcionario, name="cadastro"),
    path('funcionarios/', views.ver_funcionarios, name="lista_funcionarios"),
    path('funcionarios/<int:id>', views.ver_detalhes_funcionario, name="detalhes_funcionario"),
    path('funcionarios/<int:id>/update/', views.atualizar_funcionario, name="atualizar_funcionario"),
    path('hello/', views.hello_world, name="hello")
]