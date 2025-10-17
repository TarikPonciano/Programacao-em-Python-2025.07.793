from conexaoDB import ConexaoDB
import dotenv
import os

import customtkinter as ctk
from tkinter import ttk, messagebox

dotenv.load_dotenv(dotenv.find_dotenv())

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_NAME")

meuBanco = ConexaoDB(DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("Cadastro de Livros")
janela.geometry("600x900")
janela.resizable(width=False, height=False)

formulario_livro = ctk.CTkFrame(janela)
formulario_livro.pack(fill="x", padx = 10, pady = 10)

formulario_livro_titulo_label = ctk.CTkLabel(formulario_livro, text="CADASTRAR LIVRO", font=ctk.CTkFont(size=24, weight="bold"))
formulario_livro_titulo_label.grid(row=0, column=0, columnspan=2, pady=(0,10))

label_titulo_livro = ctk.CTkLabel(formulario_livro, text="TITULO:")
label_titulo_livro.grid(row=1, column=0, sticky="w", padx=5, pady=5)

campo_titulo_livro = ctk.CTkEntry(formulario_livro, width=300, placeholder_text="Digite o titulo do livro:")
campo_titulo_livro.grid(row=1, column=1, padx=5, pady=5)



janela.mainloop()