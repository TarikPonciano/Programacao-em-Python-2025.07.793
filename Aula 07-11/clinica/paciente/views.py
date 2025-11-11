from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Paciente

# Create your views here.
def home(request):
    return render(request, "paciente/home.html")

def cadastrar_paciente(request):


    if request.method == "GET":
        return render(request, "paciente/cadastro.html")
    
    if request.method == "POST":

       nomePaciente = request.POST.get("nome")
       
       especiePaciente = request.POST.get("especie")

       corPaciente = request.POST.get("cor")

       Paciente.objects.create(
           nome=nomePaciente,
           especie=especiePaciente,
           cor=corPaciente
       )

       return redirect('cadastro')
    
def listar_pacientes(request):
    pacientes = Paciente.objects.all()

    context = {
        "pacientes": pacientes
    }

    return render(request, "paciente/lista_pacientes.html", context)

def ver_paciente(request, id):
    paciente = Paciente.objects.filter(id=id).first()

    context = {
        "paciente": paciente
    }

    if request.method == "GET":
        return render(request, "paciente/ver_paciente.html", context)
        
    if request.method == "POST":
        nome = request.POST.get("nome")
        especie = request.POST.get("especie")
        cor = request.POST.get("cor")

        paciente.nome = nome
        paciente.especie = especie
        paciente.cor = cor
        paciente.save()

        return redirect("pacientes")
    
# def remover_paciente(request, id):
#     paciente = Paciente.objects.filter(id=id).first()
#     paciente.delete()
#     return redirect("pacientes")