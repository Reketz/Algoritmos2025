import os
usuarios = list()

print("*" * 50)
print("Bem vindo!")
print("*" * 50)

while True:
    opcao = input("Escolha uma das opções\n\n" \
    "1 - Cadastrar\n" \
    "2 - Login\n" \
    "0 - Sair\n\nOpção: ")
    if(opcao == '0'):
        break

    elif(opcao == '1'):
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        
        emailExiste = False
        for usu in usuarios:
            if(email == usu["email"]):
                print("E-email já existe")
                emailExiste = True
        
        if (emailExiste == True):
            continue

        senha = input("Digite sua senha: ")
        usuario = {
            'nome': nome,
            'email': email,
            'senha': senha
        }
        usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!")
        os.system('cls' if os.name == 'nt' else 'clear')
    elif(opcao == '2'):
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        usuLogado = None
        for usu in usuarios:
            if(usu['email'] == email and usu['senha'] == senha):
                usuLogado = usu
                break
        
        if(usuLogado != None):
            while True:
                opcao = input(f"Menu principal - {usuLogado['nome']} \n\n" \
                    "1 - Cadastrar carona\n" \
                    "2 - Alterar carona\n" \
                    "3 - Excluir carona\n" \
                    "0 - Sair\n\nOpção: ")
                if(opcao == '0'):
                    break
        else:
            print('Email ou senha inválido. Tente novamente!')
            