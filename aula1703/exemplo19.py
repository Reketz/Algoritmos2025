numero = int(input("Digite um número maior que 0 e menor que 1000: "))
centenas = 0
dezenas = 0
unidades = 0
saida = ""

if(numero > 99):
    centenas = numero // 100
    numero = numero % 100

if(numero > 9):
    dezenas = numero // 10
    numero = numero % 10

unidades = numero

if(centenas > 1):
    saida = saida + f" {centenas} centenas, "
elif(centenas == 1):
    saida = saida + f" {centenas} centena, "

print(f"O número de centenas: {centenas}")
print(f"O número de dezenas: {dezenas}")
print(f"O número de unidades: {unidades}")