class Node:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

class BST:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        self.raiz = self._inserir_recursivo(self.raiz, chave)

    def _inserir_recursivo(self, node, chave):
        if node is None:
            return Node(chave)
        if chave < node.chave:
            node.esquerda = self._inserir_recursivo(node.esquerda, chave)
        elif chave > node.chave:
            node.direita = self._inserir_recursivo(node.direita, chave)
        return node

    def buscar(self, chave):
        return self._buscar_recursivo(self.raiz, chave)

    def _buscar_recursivo(self, node, chave):
        if node is None:
            return False
        if node.chave == chave:
            return True
        if chave < node.chave:
            return self._buscar_recursivo(node.esquerda, chave)
        return self._buscar_recursivo(node.direita, chave)

    def exibir_em_ordem(self, node=None):
        if node is None:
            node = self.raiz
        if node.esquerda:
            self.exibir_em_ordem(node.esquerda)
        print(node.chave, end=" ")
        if node.direita:
            self.exibir_em_ordem(node.direita)

bst = BST()
precos = [100, 50, 150, 30, 70, 130, 170]

for preco in precos:
    bst.inserir(preco)

print("Árvore BST em ordem:")
bst.exibir_em_ordem()
print()

preco_procurado = 70
if bst.buscar(preco_procurado):
    print(f"O preço de R${preco_procurado},00 está disponível na loja.")
else:
    print(f"O preço {preco_procurado} não foi encontrado.")
