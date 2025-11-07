from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "paciente/home.html")

def cadastrar_paciente(request):


    if request.method == "GET":
        return render(request, "paciente/cadastro.html")
    
    if request.method == "POST":


        return HttpResponse(f'''
                            CADASTRO COM SUCESSO
Nome: {request.POST.get('nome')}
Especie: {request.POST.get('especie')}
Cor: {request.POST.get('cor')}
''')