import customtkinter as ctk

# configurando a cor
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class TrabalhoADS(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Trabalho de ADS - Parte 6")
        self.geometry("450x400")
        
        # abas do programa
        self.minhas_abas = ctk.CTkTabview(self, width=400, height=330)
        self.minhas_abas.pack(pady=10)

        self.minhas_abas.add("Par ou Impar")
        self.minhas_abas.add("Contador")
        self.minhas_abas.add("Soma")

        # --- PARTE DO PAR OU IMPAR ---
        self.tab1 = self.minhas_abas.tab("Par ou Impar")
        
        self.txt1 = ctk.CTkLabel(self.tab1, text="Calculadora Par ou Impar", font=("Arial", 16))
        self.txt1.pack(pady=10)
        
        self.entrada1 = ctk.CTkEntry(self.tab1, placeholder_text="numero...")
        self.entrada1.pack(pady=5)

        self.btn1 = ctk.CTkButton(self.tab1, text="Verificar", command=self.checar)
        self.btn1.pack(pady=10)

        self.resultado1 = ctk.CTkLabel(self.tab1, text="")
        self.resultado1.pack()

        # --- PARTE DO CONTADOR ---
        self.tab2 = self.minhas_abas.tab("Contador")
        
        self.btn2 = ctk.CTkButton(self.tab2, text="Contar ate 10", command=self.contagem)
        self.btn2.pack(pady=20)

        self.caixa = ctk.CTkTextbox(self.tab2, width=150, height=100)
        self.caixa.pack()

        # --- PARTE DA SOMA ---
        self.tab3 = self.minhas_abas.tab("Soma")
        self.total_guardado = 0 
        
        self.txt3 = ctk.CTkLabel(self.tab3, text="Somador acumulado")
        self.txt3.pack(pady=5)

        self.entrada3 = ctk.CTkEntry(self.tab3, placeholder_text="valor")
        self.entrada3.pack(pady=5)

        self.btn3 = ctk.CTkButton(self.tab3, text="Somar", command=self.fazer_soma)
        self.btn3.pack(pady=10)

        self.resultado3 = ctk.CTkLabel(self.tab3, text="Total: 0", font=("Arial", 18))
        self.resultado3.pack()

    # aqui embaixo ficam os comandos dos botoes

    def checar(self):
        try:
            n = int(self.entrada1.get())
            if n % 2 == 0:
                self.resultado1.configure(text="E par", text_color="green")
            else:
                self.resultado1.configure(text="E impar", text_color="yellow")
        except:
            self.resultado1.configure(text="erro!")

    def contagem(self):
        self.caixa.delete("0.0", "end")
        texto = ""
        for i in range(1, 11):
            texto = texto + str(i) + " "
        self.caixa.insert("0.0", texto)

    def fazer_soma(self):
        try:
            valor = float(self.entrada3.get())
            if valor == 0:
                self.total_guardado = 0
            else:
                self.total_guardado = self.total_guardado + valor
            
            self.resultado3.configure(text=f"Total: {self.total_guardado}")
            self.entrada3.delete(0, 'end')
        except:
            self.resultado3.configure(text="Erro no valor!", text_color="red")

if __name__ == "__main__":
    app = TrabalhoADS()
    app.mainloop()
