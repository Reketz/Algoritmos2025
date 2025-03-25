maiorNumero = int(input("Digite um numero: "))
for i in range(4):
    numero = int(input("Digite um numero: "))
    if(numero > maiorNumero):
        maiorNumero = numero
    print(f"O numero digitado {numero} e o maior por enquanto é: {maiorNumero}")
        

print(f"O maior número é: {maiorNumero}")