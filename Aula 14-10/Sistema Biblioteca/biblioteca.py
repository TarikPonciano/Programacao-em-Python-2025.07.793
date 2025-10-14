import psycopg2
import dotenv
import os

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
        print("Ver Livros")
    elif op == "2":
        print("Cadastrar Livro")
    elif op == "0":
        print("Saindo da aplicação...")
        break
    else:
        print("Você escolheu uma opção inválida...")

    input("TECLE ENTER PARA CONTINUAR")