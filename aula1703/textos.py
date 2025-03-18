numero = int(input("Digite um número positivo de maças: "))
messagem = ""

if(numero > 1):
    messagem = messagem + f" {numero} maças "
elif(numero == 1):
    messagem = messagem + f" {numero} maçã "

print(messagem)