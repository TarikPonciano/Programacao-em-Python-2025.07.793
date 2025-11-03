from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse

funcionarios = [
    {"id": 1, "nome": "Jefferson", "cargo": "Vendedor", "departamento": "Financeiro", "salario": 5500}
]

idAtual = 1


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
        global idAtual
        novoFuncionario = {
            "id": idAtual+1,
            "nome": nome,
            "cargo": cargo,
            "departamento": departamento,
            "salario": salario
        }

        funcionarios.append(novoFuncionario)
        idAtual += 1

        print(funcionarios)
        
        
        return redirect("cadastro")
        
def ver_funcionarios(request):
    context = {
        "funcionarios": funcionarios
    }
    return render(request, "funcionarios/funcionarios.html",context)
    
def ver_detalhes_funcionario(request, id):
    funcionario_escolhido = None

    for func in funcionarios:
        if func['id'] == id:
            funcionario_escolhido = func
            break

    if funcionario_escolhido == None:
        return HttpResponse("FUNCIONÁRIO NÃO ENCONTRADO")
    
    context={
        "funcionario": funcionario_escolhido
    }

    return render(request, "funcionarios/funcionario.html", context)

def atualizar_funcionario(request, id):

    posicao_funcionario = None

    for func in funcionarios:
        if func["id"] == id:
            posicao_funcionario = funcionarios.index(func)
            break
    
    if posicao_funcionario == None:
        return HttpResponse("Não foi possível Atualizar Funcionario! ID inválido!")
    
    funcionarios[posicao_funcionario]["nome"] = request.POST.get('nome', '')
    funcionarios[posicao_funcionario]["cargo"] = request.POST.get('cargo', '')
    funcionarios[posicao_funcionario]["departamento"] = request.POST.get('departamento', '')
    funcionarios[posicao_funcionario]["salario"] = request.POST.get('salario', '')

    return redirect('lista_funcionarios')