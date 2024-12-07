def mochila_pesada(valores, pesos, capacidade):
    for i in range(len(pesos) - 1, -1, -1):
        if pesos[i] > capacidade:
            pesos.pop(i)
            valores.pop(i)
    itens = len(valores)
    dp = []
    for i in range(itens + 1):
        linha = [0 for _ in range(capacidade + 1)]
        dp.append(linha)
    for i in range(1, itens + 1):
        for j in range(1, capacidade + 1):
            if pesos[i - 1] <= j:
                itemsempreco = dp[i - 1][j]
                itemcompreco = valores[i - 1] + dp[i - 1][j - pesos[i - 1]]
                dp[i][j] = max(itemsempreco, itemcompreco)
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[itens][capacidade]
valores = [22,53,120,80,45]
pesos = [8,12,7,18,15]
capacidade = 20
resultado = mochila_pesada(valores, pesos, capacidade)
print(f"O maior valor que pode ser carregado na mochila é {resultado}")
