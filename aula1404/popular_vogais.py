vogais = []
while True:
    if(len(vogais) == 5 or len(vogais) == 6):
        break
    
    vogal = input("Digite o nome da vogal: ")
    if(vogal in 'aeiouy'):
        vogais.append(vogal)

    print(vogais)