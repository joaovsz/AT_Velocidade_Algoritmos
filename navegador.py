class Navegador:
    def __init__(self):
        self.histórico = [] 
        self.avanço = []
        self.página_atual = None

    def acessar_página(self, página):
        if self.página_atual:
            self.histórico.append(self.página_atual) 
        self.página_atual = página  
        self.avanço.clear()  
        print(f"Acessou: {self.página_atual}")

    def voltar(self):
        if not self.histórico:
            print("Não há páginas anteriores para voltar.")
            return
        self.avanço.append(self.página_atual)
        self.página_atual = self.histórico.pop() 
        print(f"Voltou para: {self.página_atual}")

    def avançar(self):
        if not self.avanço:
            print("Não há páginas para avançar.")
            return
        self.histórico.append(self.página_atual) 
        self.página_atual = self.avanço.pop() 
        print(f"Avançou para: {self.página_atual}")

    def exibir_status(self):
        print("\n--- Status Atual ---")
        print(f"Página atual: {self.página_atual}")
        print(f"Histórico: {self.histórico}")
        print(f"Avanço: {self.avanço}")
        print("--------------------\n")


navegador = Navegador()

navegador.acessar_página("Página 1")
navegador.acessar_página("Página 2")
navegador.acessar_página("Página 3")

navegador.voltar()
navegador.voltar()
navegador.avançar()

navegador.acessar_página("Página 4") 
navegador.voltar() 

navegador.exibir_status()
