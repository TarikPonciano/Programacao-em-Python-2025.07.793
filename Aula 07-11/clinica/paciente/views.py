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