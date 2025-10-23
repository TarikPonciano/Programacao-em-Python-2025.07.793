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
DB_PORT = os.getenv("DB_PORT")

def cadastrar_livro():
    titulo = campo_titulo_livro.get().strip()
    ano = campo_ano_livro.get().strip()
    autor = lista_autor_livro.get().strip()

    if not titulo:
        messagebox.showerror("ERRO DE VALIDAÇÃO", "Título é obrigatório!")

        campo_titulo_livro.focus_set()
        return

    if not ano:
        messagebox.showerror("ERRO DE VALIDAÇÃO", "Ano é obrigatório!")

        campo_ano_livro.focus_set()
        return
    else:
        try:
            ano = int(ano)
        except:
            messagebox.showerror("ERRO DE VALIDAÇÃO", "Ano precisa ser numérico!")
            campo_ano_livro.focus_set()
            return
        
        if ano < 1000 or ano > 2025:
            messagebox.showerror("ERRO DE VALIDAÇÃO", "Ano precisa estar entre 1000 e 2025!")
            campo_ano_livro.focus_set()
            return

    if not autor:
        messagebox.showerror("ERRO DE VALIDAÇÃO", "Autor é obrigatório!")

        lista_autor_livro.focus_set()
        return
    
    # Trecho de código responsável por determinar ID do Autor

    # Percorremos a lista de autores buscando algum autor que tenha o nome idêntico ao autor selecionado. Se encontrar, salvamos o ID e utilizamos em nosso SQL

    idAutor = None

    for elemento in autores:
        if elemento[1] == autor:
            idAutor = elemento[0]
            break

    meuBanco.manipular('''
INSERT INTO livros
VALUES (default, %s, %s, %s);
''', [titulo, ano, idAutor])
    
    campo_titulo_livro.delete(0, 'end')
    campo_ano_livro.delete(0,'end')
    lista_autor_livro.set('Tolkien')

    messagebox.showinfo("CADASTRADO COM SUCESSO", "LIVRO CADASTRADO COM SUCESSO")

    carregar_livros()

def atualizar_livro(idLivro):
    titulo = campo_titulo_livro.get().strip()
    ano = campo_ano_livro.get().strip()
    autor = lista_autor_livro.get().strip()

    if not titulo:
        messagebox.showerror("ERRO DE VALIDAÇÃO", "Título é obrigatório!")

        campo_titulo_livro.focus_set()
        return

    if not ano:
        messagebox.showerror("ERRO DE VALIDAÇÃO", "Ano é obrigatório!")

        campo_ano_livro.focus_set()
        return
    else:
        try:
            ano = int(ano)
        except:
            messagebox.showerror("ERRO DE VALIDAÇÃO", "Ano precisa ser numérico!")
            campo_ano_livro.focus_set()
            return
        
        if ano < 1000 or ano > 2025:
            messagebox.showerror("ERRO DE VALIDAÇÃO", "Ano precisa estar entre 1000 e 2025!")
            campo_ano_livro.focus_set()
            return

    if not autor:
        messagebox.showerror("ERRO DE VALIDAÇÃO", "Autor é obrigatório!")

        lista_autor_livro.focus_set()
        return
    
    # Trecho de código responsável por determinar ID do Autor

    # Percorremos a lista de autores buscando algum autor que tenha o nome idêntico ao autor selecionado. Se encontrar, salvamos o ID e utilizamos em nosso SQL

    idAutor = None

    for elemento in autores:
        if elemento[1] == autor:
            idAutor = elemento[0]
            break

    meuBanco.manipular('''
UPDATE livros
SET
titulo_livro = %s,
ano_livro = %s,
autor_id = %s
WHERE id_livro = %s;
''', [titulo, ano, idAutor, idLivro])
    
    limpar_formulario()

    messagebox.showinfo("ATUALIZADO COM SUCESSO", "LIVRO ATUALIZADO COM SUCESSO")

    carregar_livros()


def carregar_autores():
    '''
    1. Obter do banco a lista de autores -> [(id, nome)]
    2. Transformar a lista de autores em uma lista de nomes -> ["nome1", "nome2", "nome3"]
    3. Carregar a lista no elemento "lista_autor_livro"
    4. Selecionar o primeiro autor da lista como elemento padrão
    '''
    global autores
    autores = meuBanco.consultar('''
    SELECT * FROM autores ORDER BY id_autor ASC;
''', [])

    nomesAutores = []

    for autor in autores:
        nomesAutores.append(autor[1])
    print(nomesAutores)
    lista_autor_livro.configure(values=nomesAutores)
    lista_autor_livro.set(nomesAutores[0])

def carregar_livros():
    # Antes de inserir os livros do banco, é necessário limpar nossa tabela.
    for linha in tabela_livros.get_children():
        tabela_livros.delete(linha)

    '''
    1. Consultar o banco para obter a lista de livros
    2. Para cada livro na lista de livros, inserir o livro na tabela
    '''
    livros = meuBanco.consultar('''
SELECT id_livro, titulo_livro, ano_livro, nome_autor FROM livros 
INNER JOIN autores ON id_autor = autor_id     
ORDER BY id_livro ASC;
''', []) 
    
    for livro in livros:
        tabela_livros.insert("", "end", values=livro)

def remover_livro():
    '''
    1. Obter qual linha está selecionada
        1.1 Se não houver linha selecionada, exibir mensagem de erro
    2. Extrair informação da linha (id livro)
    3. Manipular o banco com um sql DELETE
    4. Exibir mensagem de confirmação
    '''

    linhas_selecionadas = tabela_livros.selection()

    if not linhas_selecionadas:
        messagebox.showerror("ERRO DE SELEÇÃO", "VOCÊ DEVE SELECIONAR UM LIVRO ANTES DE CONTINUAR!")
        return

    # print(linhas_selecionadas)

    livro_selecionado = tabela_livros.item(linhas_selecionadas[0], 'values')
    print(livro_selecionado)
    id_livro = int(livro_selecionado[0])

    resultado = meuBanco.manipular('''
DELETE FROM livros
WHERE id_livro = %s;
''', [id_livro])
    
    if resultado == "DEU CERTO!":
        messagebox.showinfo("REMOÇÃO CONCLUÍDA", "LIVRO REMOVIDO COM SUCESSO!")
    else:
        messagebox.showerror("REMOÇÃO ABORTADA", "HOUVE UM ERRO AO REMOVER O LIVRO!")
    
    carregar_livros()

def limpar_formulario():
    campo_titulo_livro.delete(0, "end")
    campo_ano_livro.delete(0, "end")
    lista_autor_livro.set(autores[0][1])

    campo_titulo_livro.focus_set()

    livros_selecionados = tabela_livros.selection()

    for livro in livros_selecionados:
        tabela_livros.selection_remove(livro)
def ativar_modo_atualizar():
    '''
    0. Obter o livro selecionado pelo usuário
    1. Mudar o título do formulário para "Atualizar Livro"
        1.1 Incluir no título o id do livro a ser atualizado
    2. Preencher o campo título com o titulo do livro selecionado
    3. Preencher o campo ano de lançamento com a informação do livro selecionado
    4. Preencher o campo autor com o autor do livro selecionado
    5. Reconfigurar o botão de enviar, para executar a função de atualizar
    '''

    livros_selecionado = tabela_livros.selection()

    if not livros_selecionado:
        messagebox.showerror("ERRO AO ATUALIZAR!", "PARA ATUALIZAR UM LIVRO PRIMEIRO SELECIONE O LIVRO NA LISTA")
        return
    
    livro_selecionado = tabela_livros.item(livros_selecionado[0], "values")
    
    limpar_formulario()

    formulario_livro_titulo_label.configure(text=f"ATUALIZANDO LIVRO - #{livro_selecionado[0]}")
    campo_titulo_livro.insert(0, livro_selecionado[1])
    campo_ano_livro.insert(0, livro_selecionado[2])
    lista_autor_livro.set(livro_selecionado[3])

    botao_cadastrar_livro.configure(command=lambda: atualizar_livro(livro_selecionado[0]))




autores = []

meuBanco = ConexaoDB(DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()

posx = (janela.winfo_screenwidth()/2) - (600/2)

janela.title("Cadastro de Livros")

janela.geometry(f"600x900+{int(posx)}+0")
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
carregar_autores()

botao_cadastrar_livro = ctk.CTkButton(formulario_livro, text="Enviar", command=cadastrar_livro)
botao_cadastrar_livro.grid(row=4, column=1, sticky="e", padx=5, pady=5)

container_tabela_livros = ctk.CTkFrame(janela)
container_tabela_livros.pack(fill="both", expand=True, padx=10, pady=(0,10))

colunas = ["ID", "Titulo", "Ano", "Autor"]
tabela_livros = ttk.Treeview(container_tabela_livros, columns=colunas, show="headings", height=15)

tabela_livros.heading("ID", text="ID Livro")
tabela_livros.heading("Titulo", text="Título")
tabela_livros.heading("Autor", text="Autor")
tabela_livros.heading("Ano", text="Ano")

tabela_livros.column("ID", width=50)
tabela_livros.column("Titulo", width=300)
tabela_livros.column("Ano", width=100)
tabela_livros.column("Autor", width=150)

carregar_livros()

#DESAFIO: Ao cadastrar um livro, exibir o novo livro na tabela

tabela_livros.pack(fill="both", expand=True)

container_botoes = ctk.CTkFrame(janela)
container_botoes.pack(fill='x', padx=10, pady=(0,5))

container_botoes.columnconfigure(0,weight=1)
container_botoes.columnconfigure(1,weight=1)
container_botoes.columnconfigure(2,weight=1)
container_botoes.columnconfigure(3,weight=1)

botao_cadastrar = ctk.CTkButton(container_botoes, text="✔️ CADASTRAR")
botao_cadastrar.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

botao_atualizar = ctk.CTkButton(container_botoes, text = "🚩 ATUALIZAR")
botao_atualizar.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
botao_atualizar.configure(command=ativar_modo_atualizar)

botao_deletar = ctk.CTkButton(container_botoes, text="🗑️ REMOVER")
botao_deletar.grid(row=0, column=2, sticky="ew", padx=5, pady=5)
botao_deletar.configure(command=remover_livro)

botao_limpar = ctk.CTkButton(container_botoes, text= "🧹 LIMPAR")
botao_limpar.grid(row=0, column=3, sticky="ew", padx=5, pady=5)
botao_limpar.configure(command=limpar_formulario)


janela.mainloop()