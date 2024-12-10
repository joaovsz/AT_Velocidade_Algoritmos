jogadores = [
    {"nome": "João Vitor", "pontuacao": 109},
    {"nome": "Maria Eduarda", "pontuacao": 999},
    {"nome": "João Pedro", "pontuacao": 158},
    {"nome": "Pedro Ramos", "pontuacao": 963}
]

def selection_sort(jogadores):
    n = len(jogadores)
    for i in range(n - 1): 
        max_idx = i
        for j in range(i + 1, n):
            if jogadores[j]["pontuacao"] > jogadores[max_idx]["pontuacao"]:
                max_idx = j
        
        if max_idx != i:
            jogadores[i], jogadores[max_idx] = jogadores[max_idx], jogadores[i]
    
    return jogadores

jogadores_ordenados = selection_sort(jogadores)

print("Jogadores ordenado - Pontuação Maior primeiro:")
for jogador in jogadores_ordenados:
    print(f" {jogador['pontuacao']} pontos | {jogador['nome']}")
