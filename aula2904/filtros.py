usuarios = [
    {'nome': 'Ana', 'email': 'a@emial.com', 'senha': '123'},
    {'nome': 'Joao', 'email': 'j@hotmail.com', 'senha': '123'},
    {'nome': 'Guilherme', 'email': 'gui@gmail.com', 'senha': '1234'}
]

caronasReservadas = []

usuarioExiste = [ usu for usu in usuarios if usu["email"] == "gui@gmail.com" ]

if(len(usuarioExiste) > 0):
    print("Usuário já existe")