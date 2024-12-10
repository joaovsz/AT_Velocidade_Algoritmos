from collections import deque

class SistemaAtendimento:
    def __init__(self):
        self.fila = deque()

    def adicionar_chamado(self, chamado):
        self.fila.append(chamado)
        print(f"\n[INFO] Chamado '{chamado}' adicionado à fila.")

    def atender_chamado(self):
        if self.fila:
            chamado = self.fila.popleft()
            print(f"\n[INFO] Chamado '{chamado}' foi atendido.")
        else:
            print("\n[WARNING] Nenhum chamado na fila para atender.")

    def exibir_fila(self):
        if self.fila:
            print("\n--- Fila de Chamados ---")
            for i, chamado in enumerate(self.fila, start=1):
                print(f"{i}. {chamado}")
            print("------------------------\n")
        else:
            print("\n[INFO] A fila de chamados está vazia.\n")

sistema = SistemaAtendimento()

sistema.adicionar_chamado("Chamado 1: Problema ao tentar acessar o sistema")
sistema.adicionar_chamado("Chamado 2: Solicitação para mudança de senha")

sistema.exibir_fila()

sistema.atender_chamado()
sistema.atender_chamado()

sistema.exibir_fila()

sistema.adicionar_chamado("Chamado 3: Solicitação para suporte técnico")
sistema.exibir_fila()
sistema.atender_chamado()
sistema.atender_chamado()
sistema.atender_chamado()
