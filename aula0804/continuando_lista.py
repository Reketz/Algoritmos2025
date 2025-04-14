frutas = ['maçã','banana','pera', 
        'uva','morango', 'tomate',
        'goiaba', 'maracuja', 'siriguela']
print(f"O tamanho da lista é {len(frutas)}")

indice = 0

while(True):
    if(len(frutas) == indice):
        break
    if(indice % 2 == 0):
        print(f"{frutas[indice]}")
    
    indice += 1