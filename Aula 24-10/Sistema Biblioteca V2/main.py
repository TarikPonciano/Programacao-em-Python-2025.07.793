import customtkinter as ctk
from telaMenu import MenuInicial
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
class App:
    def __init__(self):
        self.janela = ctk.CTk()
        self.janela.title = "Sistema Biblioteca"
        self.janela.geometry("800x600")

        self.container_conteudo = ctk.CTkFrame(self.janela)
        self.container_conteudo.pack(fill="both", expand=True)

        self.tela_atual = MenuInicial(self.container_conteudo)

app = App()

app.janela.mainloop()
