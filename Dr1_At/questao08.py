jogadores = {"Leo": 9, "Juca": 10, "Maria": 8, "Celia": 9}
def selection_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j][1] < lista[min_idx][1]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
def exibir_jogadores(jogadores_ordenados):
    for jogador, pontuacao in jogadores_ordenados:
        print(f"{jogador}: {pontuacao}")
if __name__ == "__main__":
    jogadores_lista = list(jogadores.items())
    selection_sort(jogadores_lista)
    exibir_jogadores(jogadores_lista)
