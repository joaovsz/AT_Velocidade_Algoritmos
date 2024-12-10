class HashTable:
    def __init__(self, capacidade=10):
        self.capacidade = capacidade
        self.tabela = [[] for _ in range(capacidade)]
        self.size = 0

    def hash(self, chave):
        return hash(chave) % self.capacidade
    def inserir(self, chave, valor):
        indice = self.hash(chave)
        for par in self.tabela[indice]:
            if par[0] == chave:
                par[1] = valor
                return
        self.tabela[indice].append([chave, valor])
        self.size += 1

    def buscar(self, chave):
        indice = self.hash(chave)
        for par in self.tabela[indice]:
            if par[0] == chave:
                return par[1]
        return None

    def __str__(self):
        resultado = []
        for lista in self.tabela:
            for par in lista:
                resultado.append(f"{par[0]}: {par[1]}")
        return "{ " + ", ".join(resultado) + " }"

def verificar_duplicatas(lista):
    tabela_hash = HashTable()
    for item in lista:
        if tabela_hash.buscar(item) is not None: 
            return True 
        tabela_hash.inserir(item, True) 
    return False  

lista1 = [1, 2, 3, 4, 5, 3]
lista2 = [1, 2, 3, 4, 5]

print("Há duplicatas em lista1?", verificar_duplicatas(lista1)) 
print("Há duplicatas em lista2?", verificar_duplicatas(lista2)) 
