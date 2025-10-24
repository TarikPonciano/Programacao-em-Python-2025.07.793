import customtkinter as ctk

class MenuInicial(ctk.CTkFrame):
    def __init__ (self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True)

        self.titulo_menu = ctk.CTkLabel(self, text="Menu Inicial")
        self.titulo_menu.pack(fill="x")

        self.faixa_opcoes = ctk.CTkFrame(self)
        self.faixa_opcoes.pack(fill="both", expand=True, padx=400, pady=100)