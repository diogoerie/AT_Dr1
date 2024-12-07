fila = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def atendimento(fila):
    if len(fila) >= 1:
        atendido = fila.pop(0)
        print(f"Atendendo: {atendido}")
        return fila
    else:
        print("A fila está vazia!")
        return fila
def adicionar(fila, novo):
    fila.append(novo)
    print(f"{novo} foi adicionado na fila.")
    return fila
print("Fila inicial:", fila)
fila = atendimento(fila)
print("Fila depois do atendimento:", fila)
fila = adicionar(fila, 10)
print("Fila depois de adionar cliente:", fila)

