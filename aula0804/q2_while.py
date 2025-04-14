somaPares = 0
somaImpares = 0

while(True):
    numero = int(input("Digite um numero: "))
    if(numero == 0):
        break

    if(numero % 2 == 0):
        somaPares += numero
    else:
        somaImpares += numero

print(f"Soma dos pares é {somaPares}")
print(f"Soma dos impares é {somaImpares}")