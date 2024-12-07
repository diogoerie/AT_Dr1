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
def novo_produto(branch, valor):
    return inserir(branch, valor)
def localizar_produto(branch, valor):
    if branch is None:
        return False
    if branch.valor == valor:
        return True
    elif valor < branch.valor:
        return localizar_produto(branch.esquerda, valor)
    else:
        return localizar_produto(branch.direita, valor)
precos = [100, 50, 150, 30, 70, 130, 170]
branch = None
for valor in precos:
    branch = inserir(branch, valor)
novoProduto = float(input('Digite o valor do produto a ser adicionado: '))
branch = novo_produto(branch, novoProduto)
ordercao(branch)
valorBusca = float(input('Digite o valor do produto a localizar: '))
if localizar_produto(branch, valorBusca):
    print(f"O produto com valor {valorBusca} foi encontrado.")
else:
    print(f"O produto com valor {valorBusca} não foi encontrado.")
