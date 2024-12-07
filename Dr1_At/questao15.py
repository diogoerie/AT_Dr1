class Tree:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
def inserir(branch, valor):
    if branch is None:
        return Tree(valor)
    if valor < branch.valor:
        branch.esquerda = inserir(branch.esquerda, valor)
    else:
        branch.direita = inserir(branch.direita, valor)
    return branch
def ordercao(branch):
    if branch:
        ordercao(branch.esquerda)
        ordercao(branch.direita)
def encontrar_menor(branch):
    while branch.esquerda:
        branch = branch.esquerda
    return print(f"Nota mínima: {branch.valor}")
def encontrar_maior(branch):
    while branch.direita:
        branch = branch.direita
    return print(f"Nota máxima: {branch.valor}")
notas = [85, 70, 95, 60, 75, 90, 100]
branch = None
for valor in notas:
    branch = inserir(branch, valor)
encontrar_menor(branch)
encontrar_maior(branch)



