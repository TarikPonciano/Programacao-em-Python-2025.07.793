from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

def hello_world(request):
    soma = 30+30


    return HttpResponse(f'''
    <h1 style="color:red">Hello World - {soma}</h1>
    <button onclick="alert('Teste')">Clique aqui</button>
    ''')

# Crie a rota raiz '' nessa rota raiz execute uma função que exibe na tela "Bem vindo ao meu primeiro projeto Django!"