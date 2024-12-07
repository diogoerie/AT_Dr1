def navegar():
    historico = ["home", "perfil", "produto_01", "produto_02", "produto_03", "produto_04", "produto_05"]
    indice_atual = 0
    while True:
        print(f"Você está na página: {historico[indice_atual]}")
        comando = input("Digite 'next' para avançar ou 'back' para voltar: ")
        if comando == "back":
            if indice_atual > 0:
                indice_atual -= 1
                print(f"Voltando para: {historico[indice_atual]}")
            else:
                print("Você já está na primeira página!")

        elif comando == "next":
            if indice_atual < len(historico) - 1:
                indice_atual += 1
                print(f"Avançando para: {historico[indice_atual]}")
            else:
                print("Você já está na última página!")
        else:
            print("Comando não reconhecido. Use 'next' ou 'back'.")
navegar()