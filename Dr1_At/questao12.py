import os

def navegar_diretorios(caminho):
    try:
        with os.scandir(caminho) as entradas:
            for entrada in entradas:
                if entrada.is_dir(follow_symlinks=False):
                    print(entrada.path)
                    navegar_diretorios(entrada.path)
    except PermissionError:
        print(f"Permissão negada para acessar: {caminho}")

caminho_inicial = "C:/Users/Howard8Gr/Documents/codigosfac"
navegar_diretorios(caminho_inicial)
