from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse

def hello_world(request):
    soma = 30+30

    return HttpResponse(f'''
    <h1 style="color:red">Hello World - {soma}</h1>
    <button onclick="alert('Teste')">Clique aqui</button>
    ''')

# Crie a rota raiz '' nessa rota raiz execute uma função que exibe na tela "Bem vindo ao meu primeiro projeto Django!"

def home(request):
    return render(request, "funcionarios/home.html")

def cadastro_funcionario(request):
    if request.method == "GET":
        return render(request, "funcionarios/cadastro.html")
    elif request.method == "POST":

        nome = request.POST.get("nome", '')
        cargo = request.POST.get("cargo", '')
        departamento = request.POST.get("departamento", '')
        salario = request.POST.get("salario",'')

        print(f'''Funcionário Cadastrado
            Nome: {nome}
            Cargo: {cargo}
            Departamento: {departamento}
            Salário: R$ {salario}''')
        return redirect("cadastro")
    