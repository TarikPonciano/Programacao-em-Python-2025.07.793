import psycopg2
import dotenv
import os
from conexaoDB import ConexaoDB

# Implementar o Ver Clientes e Cadastrar Cliente
# 1. Incluir as opções Ver Clientes e Cadastrar Cliente no menu
# 2. Conectar ao banco, realizar consulta e exibir clientes na tela (Ver Clientes)
# 3. Coletar dados do novo cliente, conectar ao banco e realizar insert do cliente no banco (Cadastrar Cliente)

def verLivros():

    #Operações com Banco de Dados
    #Conecta com o banco e obtém a lista de livros, guardando na variável livros
    livros = meuBanco.consultar('''SELECT id_livro, titulo_livro, ano_livro, nome_autor FROM livros
    INNER JOIN autores ON id_autor = autor_id
    ORDER BY id_livro;''', [])

    # Verifica se foi possível obter a lista de livros. Caso não tenha sido imprime uma mensagem de erro. 
    # Caso os livros tenham sido obtidos é impresso a lista de livros na tela.
    
    if livros == None:
        print("Não foi possível consultar a tabela de Livros!")
    else:
        print("Lista de Livros:")

        print("ID | Título | Ano | Autor")
        # Imprime um livro por vez da lista de livros.
        for livro in livros:
            print(f"{livro[0]} | {livro[1]} | {livro[2]} | {livro[3]}")

def cadastrarLivro():
    # Pedir ao usuário as informações livro
    # Nome, Ano, ID Autor
    # Enviar as informações ao banco
    #   - Conectar ao Banco
    #   - Executa SQL
    #   - Finaliza a conexão

    print("Cadastro de Livro")

    tituloLivro = input("Digite o título do livro:")

    anoLivro = int(input("Digite o ano de publicação do livro:"))

    autorLivro = int(input("Digite o id do autor do livro:"))

    resultado = meuBanco.manipular("INSERT INTO livros VALUES (default, %s, %s, %s);", [tituloLivro,anoLivro,autorLivro])

    if resultado == "DEU CERTO!":
        print("Livro cadastrado com sucesso!")
    else:
        print("Erro ao cadastrar livro!")

def verClientes():
    clientes = meuBanco.consultar("SELECT * FROM membros ORDER BY id_membro;", [])

    if clientes == None:
        print("Não foi possível consultar a tabela de Clientes!")
    else:
        print("Lista de Clientes")
        print("ID | Nome | Email")
        for cliente in clientes:
            print(f"{cliente[0]} | {cliente[1]} | {cliente[2]}")

def cadastrarCliente():
    print("Cadastro de Cliente")

    nomeCliente = input("Digite o nome do cliente:")
    emailCliente = input("Digite o email do cliente:")

    meuBanco.manipular("INSERT INTO membros VALUES (default, %s, %s);", [nomeCliente, emailCliente])

# Exibir a lista de alugueis com uma tabela contendo as seguintes informações (ID Aluguel, Nome Cliente, Título do Livro, Data do Aluguel, Data de Devolução)
def verAlugueis():
    alugueis = meuBanco.consultar('''
    SELECT id_aluguel, nome_membro, titulo_livro, data_aluguel, data_devolucao FROM alugueis
    INNER JOIN membros ON id_membro = membro_id
    INNER JOIN livros ON id_livro = livro_id
    ORDER BY id_aluguel                
    ;''', [])
    
    if alugueis == None:
        print("Não foi possível obter a lista de alugueis.")
    else:
        print("ID | Cliente | Livro | Data do Aluguel | Data de Devolução")
        for aluguel in alugueis:
            print(f"{aluguel[0]} | {aluguel[1]} | {aluguel[2]} | {aluguel[3]} | {aluguel[4]}")

# Pedir ao usuário o id do cliente(exibir clientes) e id do livro(exibir livros). Executar um insert na tabela aluguel. 
# 1. Exibir lista de clientes
# 2. Pedir ao usuário o id do cliente que alugou
# 3. Exibir lista de livros
# 4. Pedir ao usuário o id do livro alugado
# 5. Executar SQL de inserção do novo aluguel
def cadastrarAluguel():
    print("Cadastro de Aluguel")

    #Exibir os clientes disponíveis
    verClientes()

    idCliente = int(input("Digite o id do cliente que está alugando um livro: "))

    verLivros()

    idLivro = int(input("Digite o id do livro que está sendo alugado:"))

    meuBanco.manipular('''
INSERT INTO alugueis (membro_id, livro_id)
VALUES (%s, %s);
''', [idCliente, idLivro])


dotenv.load_dotenv(dotenv.find_dotenv())

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")
DB_HOST = os.getenv("DB_HOST")

meuBanco = ConexaoDB(DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD)
#Primeiro Objetivo: Menu com as opções "Ver Livros" e "Cadastrar Livros"

while True:
    print("Bem vindo à Biblioteca XYZ")

    print()
    print('''
Menu:
          
1. Ver Livros
2. Cadastrar Livro
3. Ver Clientes
4. Cadastrar Cliente
5. Ver Alugueis
6. Cadastrar Aluguel
0. Sair
''')
    op = input("Digite a opção desejada:")

    if op == "1":
        verLivros()
    elif op == "2":
        cadastrarLivro()
    elif op == "3":
        verClientes()
    elif op == "4":
        cadastrarCliente()
    elif op == "5":
        verAlugueis()
    elif op == "6":
        cadastrarAluguel()
    elif op == "0":
        print("Saindo da aplicação...")
        break
    else:
        print("Você escolheu uma opção inválida...")

    input("TECLE ENTER PARA CONTINUAR")