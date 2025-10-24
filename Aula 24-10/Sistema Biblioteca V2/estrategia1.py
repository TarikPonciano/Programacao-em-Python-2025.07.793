import customtkinter as ctk

def finalizar_programa():
    janela.destroy()

def renderizar_tela_menu():
    global tela_atual
    if tela_atual:
        tela_atual.destroy()

    tela_menu = ctk.CTkFrame(container_conteudo)
    tela_menu.pack(fill="both", expand=True)

    titulo_menu = ctk.CTkLabel(tela_menu, text="Sistema Biblioteca", font=ctk.CTkFont(size=48, weight="bold"))
    titulo_menu.pack(fill="x")

    faixa_botoes = ctk.CTkFrame(tela_menu)
    faixa_botoes.pack(fill="both",expand=True, padx=400, pady=100)

    faixa_botoes.columnconfigure(0, weight=1)
    faixa_botoes.rowconfigure(0, weight=2)
    faixa_botoes.rowconfigure(1, weight=2)
    faixa_botoes.rowconfigure(2, weight=2)
    faixa_botoes.rowconfigure(3, weight=2)
    faixa_botoes.rowconfigure(4, weight=1)

    espaco_x = 20
    espaco_y = 15

    botao_membros = ctk.CTkButton(faixa_botoes, text="Gerenciar Membros")
    botao_membros.grid(row=0, column=0, sticky="nsew", padx=espaco_x, pady=espaco_y)

    botao_livros = ctk.CTkButton(faixa_botoes, text="Gerenciar Livros")
    botao_livros.grid(row=1, column=0, sticky="nsew", padx=espaco_x, pady=espaco_y)

    botao_alugueis = ctk.CTkButton(faixa_botoes, text="Gerenciar Alugueis")
    botao_alugueis.grid(row=2, column=0, sticky="nsew", padx=espaco_x, pady=espaco_y)

    botao_autores = ctk.CTkButton(faixa_botoes, text="Gerenciar Autores")
    botao_autores.grid(row=3, column=0, sticky="nsew", padx=espaco_x, pady=espaco_y)

    botao_sair = ctk.CTkButton(faixa_botoes, text="Sair")
    botao_sair.grid(row=4, column=0, sticky="nsew", padx=espaco_x, pady=espaco_y)

    botao_membros.configure(command=renderizar_tela_membros)
    botao_sair.configure(command=finalizar_programa)

    tela_atual = tela_menu

def renderizar_tela_membros():

    global tela_atual

    if tela_atual:
        tela_atual.destroy()

    tela_membros = ctk.CTkFrame(container_conteudo)
    tela_membros.pack(fill="both", expand=True)

    titulo_membros = ctk.CTkLabel(tela_membros, text="GERENCIAMENTO DE MEMBROS", font=ctk.CTkFont(size=36, weight="bold"))
    titulo_membros.pack(fill="x")

    botao_voltar = ctk.CTkButton(tela_membros, text="VOLTAR", command=renderizar_tela_menu)
    botao_voltar.pack()

    tela_atual = tela_membros

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


janela = ctk.CTk()
janela.title("Sistema de Biblioteca V2")
janela.geometry("1024x728")
janela.resizable(width=False, height=False)

container_conteudo = ctk.CTkFrame(janela)
container_conteudo.pack(fill="both", expand=True)

tela_atual = None

renderizar_tela_menu()

janela.mainloop()