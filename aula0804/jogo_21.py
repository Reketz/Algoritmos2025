import random
jogador1 = input("Digite seu nome: ")
pontuacaoJogador1 = 0

while(True):
    carta = random.randint(2, 10)
    print(f"Carta aleatoria: {carta}")
    pontuacaoJogador1 += carta
    if(pontuacaoJogador1 > 21):
        print(f"Você perdeu o jogo com {pontuacaoJogador1} pontos!")
        break
    if(pontuacaoJogador1 == 21):
        print("VocÊ ganhou!!")
        break

    resp = input("Voce quer continuar? ").lower()
    if(resp == 's'):
        continue

    print(f"Jogador {jogador1}")
    print(f"Sua pontuação {pontuacaoJogador1}")
    break