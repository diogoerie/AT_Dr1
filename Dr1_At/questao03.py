lista = [{"Ana": "98856-1234"}, {"Dana": "97542-9876"}, {"Beatriz": "98123-4567"}, {"Pedro": "99341-2345"}, {"Mariana": "97654-3210"}]

def localizar_contatos(nome, lista):
    for contato in lista:
        if nome in contato:
            numero = contato[nome]
            print(f"O nome do contato é {nome}, e o número do contato é {numero}")
            return
    print("Contato não encontrado.")

nome = input("Digite o nome do contato: ")
localizar_contatos(nome, lista)
