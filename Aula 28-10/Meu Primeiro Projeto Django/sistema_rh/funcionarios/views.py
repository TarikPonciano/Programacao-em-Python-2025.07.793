from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse

funcionarios = [
    {"nome": "Jefferson", "cargo": "Vendedor", "departamento": "RH", "salario": 5500}
]



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
        salario = float(request.POST.get("salario", 0))

        novoFuncionario = {
            "nome": nome,
            "cargo": cargo,
            "departamento": departamento,
            "salario": salario
        }

        funcionarios.append(novoFuncionario)

        print(funcionarios)
        
        
        return redirect("cadastro")
        
def ver_funcionarios(request):
    context = {
        "funcionarios": funcionarios,
        "saudacao": "Seja Bem Vindo!"
    }
    return render(request, "funcionarios/funcionarios.html", context)
    
    