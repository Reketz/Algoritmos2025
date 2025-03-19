nome = input("Digite o seu nome: ")
contadorVogal = 0
contadorConsoante = 0
for letra in nome:
    if(letra in 'aeiouyAEIOUY'):
        contadorVogal = contadorVogal + 1
    else:
        contadorConsoante = contadorConsoante + 1

print(f"Seu nome tem: {contadorVogal} vogal(is)")
print(f"Seu nome tem: {contadorConsoante} consoante(s)")