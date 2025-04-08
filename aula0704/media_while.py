"""
crie um algoritmo que peça o quantos numeros o usuário
quer somar
"""

contador = int(input("Digite o numero de notas: "))
numElementos = contador
soma = 0
while(contador > 0):
    valor = float(input("Digite o valor qualquer: "))
    soma += valor
    contador -= 1

media = soma / numElementos
print(f"A soma é {soma}")