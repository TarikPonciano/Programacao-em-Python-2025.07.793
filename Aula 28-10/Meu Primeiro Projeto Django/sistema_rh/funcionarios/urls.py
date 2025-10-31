from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name="home"),
    path('cadastro/', views.cadastro_funcionario, name="cadastro"),
    path('funcionarios/', views.ver_funcionarios, name="lista_funcionarios"),
    path('hello/', views.hello_world, name="hello")
]