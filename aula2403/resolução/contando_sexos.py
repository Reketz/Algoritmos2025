contadorHomem = 0
contadorMulher = 0

for i in range(10):
    sexo = input("Qual seu sexo (M ou F): ")
    if(sexo == "m" or sexo == "M"):
        contadorHomem += 1
    elif(sexo == "f" or sexo == "F"):
        contadorMulher += 1
    else:
        print("Sexo inválido")

print(f"O total de homens são: {contadorHomem}")
print(f"O total de mulheres são: {contadorMulher}")