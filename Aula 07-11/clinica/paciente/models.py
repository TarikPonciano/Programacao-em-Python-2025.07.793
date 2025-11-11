from django.db import models

# Create your models here.

#Sempre que realizar modificações no models.py, lembrar de rodar o comando:
# python manage.py makemigrations
# python manage.py migrate

class Paciente(models.Model):

    # Não precisa realizar essa etapa, somente se quiser alterar o nome do atributo
    # idPaciente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, null=False)

    listaEspecies = [
        ("Cachorro", "Cachorro"),
        ("Gato", "Gato"),
        ("Outro", "Outro"),
        ("Indefinido", "Idenfinido")
    ]

    especie = models.CharField(max_length=255, null=False, default="Indefinido", choices=listaEspecies)

    cor = models.CharField(max_length=255, null=False)


    def __str__(self):
        return f"Nome: {self.nome} - Especie: {self.especie} <br>"