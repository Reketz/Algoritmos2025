cacadores = [
    ["Cha Hae-In", 450],
    ["Sung Jin-Woo",  10],
    ["Choi Jong-In", 3800],
    ["Cleitinho", 80],
    ["Marivaldo", 180]
] 
maior = 0
nomeCacadorMaisForte = ''
for i in cacadores:
    nomeCacador = i[0]
    valorDePoder = i[1]
    if(valorDePoder > maior):
        maior = valorDePoder
        nomeCacadorMaisForte = nomeCacador
        
print(f'O nome do caçador mais forte é: {nomeCacadorMaisForte}')
# maior = 0 
# nome = ''
# for i in cacadores:
#     if i[1] > maior:
#         maior = i[1]
#         nome = i[0]

# print(f"Valor de força maior {maior}")
# print(f"E o nome do caçado(a)r {nome}")