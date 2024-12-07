lista = range(1, 100000)
def busca_binaria(lista, numero):
    esquerdo = 0
    direito = len(lista) - 1

    while esquerdo <= direito:
        meio = (esquerdo + direito) // 2
        if lista[meio] == numero:
            return True
        elif lista[meio] < numero:
            esquerdo = meio + 1
        else:
            direito = meio - 1

    return False
numero = int(input("Digite o número do livro: "))
if busca_binaria(lista, numero):
    print(f"Número {numero} encontrado!")
else:
    print(f"Número {numero} não encontrado.")
