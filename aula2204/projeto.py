import os

usuarios = list()

print("*" * 50)
print("Bem vindo!")
print("*" * 50)
while True:
    opcao = input("Escolha uma das opções\n\n" \
    "1 - Cadastrar usuário\n" \
    "2 - Listar usuários\n" \
    "3 - Buscar usuário por email\n" \
    "4 - Remover usuário por email\n" \
    "5 - Atualizar usuário por email\n" \
    "0 - Sair\n\nOpção: ")

    if(opcao == '0'):
        break

    if(opcao == '1'):
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        usuarios.append([nome, email, senha])
        print("Usuário cadastrado com sucesso!")
        os.system('cls' if os.name == 'nt' else 'clear')
    
    if(opcao == '2'):
        print("\nLista de usuários\n")
        for usu in usuarios:
            print(f"Nome: {usu[0]}")
            print(f"Email: {usu[1]}")     
            print("-" * 50) 

        print("\n")  

    if(opcao == '3'):
        emailBusca = input("Digite um email para busca: ")
        encontrado = False
        for usu in usuarios:
            if(emailBusca == usu[1]):
                encontrado = True
                print("Encontrou o usuário\n\n")
                print("-" * 50)
                print(f"Nome: {usu[0]}")
                print(f"Email: {usu[1]}")
                print("-" * 50)

        if(not encontrado):
            print("Usuário não existe!\n\n")
    if(opcao == '4'):
        emailBusca = input("Digite um email para remover: ")
        indice = -1
        for ind in range(len(usuarios)):
            if(emailBusca == usuarios[ind][1]):
                indice = ind

        if(indice == -1):
            print("Não encontrou o usuário!")
        else:
            usuarios.pop(indice)
        
    if(opcao == '5'):
        emailBusca = input("Digite um email para atualizar: ")
        indice = -1
        for ind in range(len(usuarios)):
            if(emailBusca == usuarios[ind][1]):
                indice = ind

        if(indice == -1):
            print("Não encontrou o usuário!")
        else:
            nomeNovo = input("Digite seu novo nome: ")
            senhaNova = input("Digite sua nova senha: ")

            usuarios[indice][0] = nomeNovo
            usuarios[indice][2] = senhaNova
