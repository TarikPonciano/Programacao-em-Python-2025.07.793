class Aluno:
    def __init__(self,nome,media,idade):
        self.nome = nome
        self.media = media
        self.idade = idade

    def mostrar_informacoes(self):
        print(f'''
Informações do Aluno:

Nome: {self.nome}
Media: {self.media}
Idade: {self.idade}
-----------------------------------------
''')


aluno1 = Aluno('Michael', 9.3, 23)
aluno2 = Aluno("Maria", 7.9, 20)

aluno1.mostrar_informacoes()
aluno2.mostrar_informacoes()
