# def imprimirMenu():
#     print('*' * 50)
#     print(f"Bem vindo! ")
#     print('*' * 50)
#     print("Selecione uma das opções:")

# imprimirMenu()

usuarios = []

def addUsuario(usuario):
    usuarios.append(usuario)

def listarUsuarios():
    for usu in usuarios:
        print(usu['nome'])
        print(usu['email'])

addUsuario({'nome': 'Thierry', 'email': 'thierry@hotmail.com'})
addUsuario({'nome': 'Allan', 'email': 'rpgallan@dd.com'})
addUsuario({'nome': 'Mariana', 'email': 'mari@you.com'})

listarUsuarios()