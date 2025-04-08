# crie um algoritmo que pergunte 
# ao usuário quantos litros de gasolina
# tem no tanque.
# Quantos km o carro consome de gasolina por litro

# Depois pergunte quantos quilometros ele rodou
# até acabar a gasolina

# Considere que a reserva do carro é 5L

# Perguntar se quer abastecer quando entrar na reserva
# O valor do tanque não pode passar de 100L

tanque = float(input("Digite quantos litros tem no tanque: "))
litrosPorKm = float(input("Quantos litros consome por km: "))

while(True):
    rodou = float(input("Digite quanto km já rodou: "))
    tanque -= litrosPorKm * rodou

    if(tanque <= 5):
        print("O carro está na reserva")
        abastecer = input("Deseja abastecer (s / n): ").lower()
        if(abastecer == 's'):
            litros = float(input("Digite o valor dos litros: "))
            maxLitros = litros + tanque
            while(maxLitros > 100):
                print("O valor máximo excedido. O tanque não pode possuir mais de 100L")
                litros = float(input("Digite o valor dos litros: "))
                maxLitros = litros + tanque
            

    if(tanque <= 0):
        print("O carro parou, você não pode mais viajar")
        break