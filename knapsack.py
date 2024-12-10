def knapsack(valores, pesos, capacidade):
    n = len(valores)
    dp = [[0] * (capacidade + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacidade + 1):
            if pesos[i - 1] <= w:
                dp[i][w] = max(valores[i - 1] + dp[i - 1][w - pesos[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacidade]

valores = [35, 99, 113]
pesos = [5, 10, 15]
capacidade = 60

resultado = knapsack(valores, pesos, capacidade)
print("Valor máximo na mochila:", resultado)
