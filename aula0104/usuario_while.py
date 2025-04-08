contador = int(input("Quantos números você quer somar: "))
soma = 0
num = 0
while(contador > 0):
    num += 1
    nota = float(input(f"Digite a {num}ª nota: "))
    soma += nota
    contador -= 1

media = soma / (num)
print(f"Valor da média é {media}")