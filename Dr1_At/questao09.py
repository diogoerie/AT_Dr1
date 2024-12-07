usuarios = {"joaozinho123": {"nome": "João Marcelo", "idade": 21},"maria2024": {"nome": "Maria Fernanda", "idade": 22},
    "pedrogamer": {"nome": "Pedro Henrique", "idade": 19},"analulinda": {"nome": "Ana Luiza", "idade": 23,},
    "carlosdev": {"nome": "Carlos Eduardo", "idade": 28},"larastar": {"nome": "Lara Cristina", "idade": 20},
    "lucasart": {"nome": "Lucas Gabriel", "idade": 24},"dudafly": {"nome": "Maria Eduarda", "idade": 21},
    "thiagotech": {"nome": "Thiago Augusto", "idade": 27},"rafaelafit": {"nome": "Rafaela Silva", "idade": 26}
}

def recuperar_perfil(username):
    if username in usuarios:
        return usuarios[username]
    else:
        return "Usuário não encontrado."

usuario = "lucasart"
perfil = recuperar_perfil(usuario)
print(f"Perfil de {usuario}: {perfil}")