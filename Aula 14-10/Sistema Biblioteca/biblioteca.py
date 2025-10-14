import psycopg2
import dotenv
import os

def verLivros():
    livros = None

    #Operações com Banco de Dados
    #Conecta com o banco e obtém a lista de livros, guardando na variável livros
    try:
        con = psycopg2.connect(dbname=DB_NAME, host=DB_HOST, password=DB_PASSWORD, port=DB_PORT, user=DB_USER)
        cursor = con.cursor()

        cursor.execute("SELECT * FROM livros ORDER BY id_livro ASC;")
        livros = cursor.fetchall() 

        cursor.close()
        con.close()
    except Exception as e:
        print("OCORREU UM ERRO NA CONSULTA -",e)

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

    try:
        con = psycopg2.connect(dbname=DB_NAME, host=DB_HOST, password=DB_PASSWORD, port=DB_PORT, user=DB_USER)

        cursor = con.cursor()
        
        cursor.execute('''
INSERT INTO livros 
VALUES (default, %s, %s, %s)''', [tituloLivro, anoLivro, autorLivro])
        con.commit()
        cursor.close()
        con.close()
        print("Livro cadastrado com sucesso!")
    except Exception as e:
        print("ERRO NO CADASTRO DE LIVRO -",e)


dotenv.load_dotenv(dotenv.find_dotenv())

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")
DB_HOST = os.getenv("DB_HOST")

#Primeiro Objetivo: Menu com as opções "Ver Livros" e "Cadastrar Livros"

while True:
    print("Bem vindo à Biblioteca XYZ")

    print()
    print('''
Menu:
          
1. Ver Livros
2. Cadastrar Livro
0. Sair
''')
    op = input("Digite a opção desejada:")

    if op == "1":
        verLivros()
    elif op == "2":
        cadastrarLivro()
    elif op == "0":
        print("Saindo da aplicação...")
        break
    else:
        print("Você escolheu uma opção inválida...")

    input("TECLE ENTER PARA CONTINUAR")