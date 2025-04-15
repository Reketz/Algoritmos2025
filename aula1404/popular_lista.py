import random
nomes = []

while True:
    nome = input("Digite o nome do cantidato: ")
    if(nome.lower() == 'sair'):
        break

    nomes.append(nome)

posicaoVencedora = random.randint(0, len(nomes))
print(f'O grande vencedor é {nomes[posicaoVencedora]}!!!!!!!!!!')