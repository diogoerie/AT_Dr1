lista = {"a": 10, "b": 20, "c": 30,"d": 10, "e": 20,
         "f": 30,"g": 10, "h": 20, "i": 30}
def verificar_duplicatas(N):
    unicos = set()
    for valor in N.values():
        if valor in unicos:
            return True
        unicos.add(valor)
    return False
print(verificar_duplicatas(lista))