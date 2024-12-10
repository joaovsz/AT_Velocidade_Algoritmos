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
    
hash_table = HashTable()

hash_table.inserir("user1", {"nome": "João Vitor Souza", "idade": 22, "cidade": "Goiânia"})
hash_table.inserir("user2", {"nome": "Thiago Angelo", "idade": 32, "cidade": "Goiânia"})
hash_table.inserir("user3", {"nome": "Welington Melo", "idade": 39, "cidade": "Goiânia"})

print("Usuário 1:", hash_table.buscar("user1"))
print("Usuário 2:", hash_table.buscar("user2"))
print("Usuário :", hash_table.buscar("user3"))