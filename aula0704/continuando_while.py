# # while quer dizer enquanto
# # enquanto a condição for verdadeira execute o algoritmo

# contador = 10
# while(contador > 0):
#     print(f"Estou contando {contador}")
#     contador -= 1

# print("Fim do programa")

# print("Ainda não acabou")

# while(contador <= 10):
#     print(f"Estou contando {contador}")
#     contador += 1

# print("Agora simmmm")

numNotas = int(input('Digite o numero de notas'))
numElementos = numNotas
soma = 0
while (numNotas > 0):
    nota = float(input("Digite a nota: "))
    soma += nota
    numNotas -= 1

media = soma / numElementos
print(f"Valor da média é: {media}")