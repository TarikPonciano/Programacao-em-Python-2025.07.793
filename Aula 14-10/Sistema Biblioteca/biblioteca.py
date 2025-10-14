import psycopg2
import dotenv
import os

def verLivros():
    livros = None

    #Operações com Banco de Dados
    try:
        con = psycopg2.connect(dbname=DB_NAME, host=DB_HOST, password=DB_PASSWORD, port=DB_PORT, user=DB_USER)
        cursor = con.cursor()

        cursor.execute("SELECT * FROM livros ORDER BY id_livro ASC;")
        livros = cursor.fetchall() 

        cursor.close()
        con.close()
    except Exception as e:
        print("OCORREU UM ERRO NA CONSULTA -",e)

    if livros == None:
        print("Não foi possível consultar a tabela de Livros!")
    else:
        print("Lista de Livros:")

        print("ID | Título | Ano | Autor")

        for livro in livros:
            print(f"{livro[0]} | {livro[1]} | {livro[2]} | {livro[3]}")

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
        print("Cadastrar Livro")
    elif op == "0":
        print("Saindo da aplicação...")
        break
    else:
        print("Você escolheu uma opção inválida...")

    input("TECLE ENTER PARA CONTINUAR")