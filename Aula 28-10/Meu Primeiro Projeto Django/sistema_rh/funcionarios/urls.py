from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name="home"),
    path('hello/', views.hello_world, name="hello")
]