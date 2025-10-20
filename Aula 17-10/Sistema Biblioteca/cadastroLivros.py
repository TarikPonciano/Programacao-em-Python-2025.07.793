from conexaoDB import ConexaoDB
import dotenv
import os

import customtkinter as ctk
import tkinter
from tkinter import ttk, messagebox

dotenv.load_dotenv(dotenv.find_dotenv())

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_NAME")

def cadastrar_livro():
    print("Cadastro de livro acionado")

meuBanco = ConexaoDB(DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("Cadastro de Livros")
janela.geometry("600x900")
janela.resizable(width=False, height=False)

formulario_livro = ctk.CTkFrame(janela)
formulario_livro.pack(fill="x", padx = 10, pady = 10)

formulario_livro.columnconfigure(0, weight=0, minsize=120)
formulario_livro.columnconfigure(1, weight=1)


formulario_livro_titulo_label = ctk.CTkLabel(formulario_livro, text="CADASTRAR LIVRO", font=ctk.CTkFont(size=24, weight="bold"))
formulario_livro_titulo_label.grid(row=0, column=0, columnspan=2, pady=(0,10))

label_titulo_livro = ctk.CTkLabel(formulario_livro, text="TITULO:")
label_titulo_livro.grid(row=1, column=0, sticky="w", padx=5, pady=5)

campo_titulo_livro = ctk.CTkEntry(formulario_livro, width=300, placeholder_text="Digite o titulo do livro:")
campo_titulo_livro.grid(sticky= "ew",row=1, column=1, padx=5, pady=5)


label_ano_livro = ctk.CTkLabel(formulario_livro, text="ANO DE LANÇAMENTO:")
label_ano_livro.grid(row=2, column=0, sticky="w", padx=5, pady=5)

campo_ano_livro = ctk.CTkEntry(formulario_livro, width=300, placeholder_text="Digite o ano de lançamento do Livro:" )
campo_ano_livro.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

label_autor_livro = ctk.CTkLabel(formulario_livro, text="AUTOR:")
label_autor_livro.grid(row=3, column=0, sticky="w", padx=5, pady=5)

lista_autor_livro = ctk.CTkComboBox(formulario_livro, width=300, state="readonly")
lista_autor_livro.grid(row=3, column=1, sticky="ew", padx=5, pady=5)
lista_autor_livro.configure(values=["Tolkien", "Machado de Assis", "George R. Martin"])
lista_autor_livro.set('Tolkien')

botao_cadastrar_livro = ctk.CTkButton(formulario_livro, text="Enviar", command=cadastrar_livro)
botao_cadastrar_livro.grid(row=4, column=1, sticky="e", padx=5, pady=5)


janela.mainloop()