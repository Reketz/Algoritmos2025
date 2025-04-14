qtdRefeicao = int(input("Digite quantas refeições você fez por dia: "))
somaCalorias = 0
maiorCaloria = 0
maiorRefeicao = ''

while(qtdRefeicao > 0):
    nome = input("Nome da refeição: ")
    calorias = float(input("Quantas calorias: "))
    if(calorias > maiorCaloria):
        maiorCaloria = calorias
        maiorRefeicao = nome
    somaCalorias += calorias
    qtdRefeicao -= 1

print("Fim do programa")
print(f"A refeição com maior caloria é {maiorRefeicao} com {maiorCaloria} calorias")
print(f"A quantidade total de calorias é: {somaCalorias}")
