soma = 0
numero = 0
while(numero != -1):
    numero = float(input("Digite um número ou -1 para parar: "))
    if(numero != -1):
        operacao = input("Digite a operação: + ou -")
        if(operacao == "+"):
            soma += numero
        elif(operacao == "-"):
            soma -= numero

print(f"O resultado da soma é {soma}")