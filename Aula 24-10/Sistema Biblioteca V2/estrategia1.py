import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


janela = ctk.CTk()
janela.title("Sistema de Biblioteca V2")
janela.geometry("1024x728")
janela.resizable(width=False, height=False)

container_conteudo = ctk.CTkFrame(janela)
container_conteudo.pack(fill="both", expand=True)

tela_atual = None

tela_menu = ctk.CTkFrame(container_conteudo)
tela_menu.pack(fill="both", expand=True)

titulo_menu = ctk.CTkLabel(tela_menu, text="Sistema Biblioteca", font=ctk.CTkFont(size=48, weight="bold"))
titulo_menu.pack(fill="x")

faixa_botoes = ctk.CTkFrame(tela_menu)
faixa_botoes.pack(fill="both",expand=True, padx=400, pady=100)



janela.mainloop()