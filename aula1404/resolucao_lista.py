numeros = [5, 10, 2, 8, 3, 20, 7,51, 33, 49, 99]
# soma = 0
# for i in numeros:
#     soma += i

# print(soma)
# contPares = 0
# for i in numeros:
#     if(i % 2 == 0):
#         contPares += 1

# for i in numeros:
#     if(i > 10):
#         print(i)

# ultimaPosicao = len(numeros) - 1
# for i in numeros:
#     print(numeros[ultimaPosicao])
#     ultimaPosicao -= 1

# nomes = ["Ana", "Carlos", "Maria", "João",  "Guilherme", "José", "Rikelme", "Letícia", "Thierry"]
# nome = input("Digite um nome: ")

# if(nome.capitalize() in nomes):
#     print("O nome está na lista")
# else:
#     print("O nome não está na lista")

# for n in numeros:
#     if(n == 7):
#         print("Número 7 encontrado! Encerrando o programa....")
#         break

# for n in numeros:
#     if(n < 5):
#         continue
#     print(n)

frutas = ['maçã','banana','pera', 
        'uva','morango', 'tomate',
        'goiaba', 'maracuja', 'siriguela']

indice = 0
while indice < len(frutas):
    print(f"Índice {indice}: {frutas[indice]}  ")
    indice += 1