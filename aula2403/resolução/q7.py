media = 0
soma = 0
maiorNota = 0

for i in range(5):
    nota = float(input("Digite a nota: "))
    soma += nota
    if(nota > maiorNota):
        maiorNota = nota

print(f"A média: {soma / 5}")
print(f"O valor da maior nota é: {maiorNota}")