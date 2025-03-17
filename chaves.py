chavePorta = input("Você possui a chave da porta? (s / n) ")
chaveCadeado = input("Você possui a chave do cadeado? (s / n) ")
alguemNaCasa = input("Tem alguem na casa? (s / n) ")

if((chavePorta == 's' and chaveCadeado == 's') or alguemNaCasa == 's'):
    print("Você pode entrar na sua casa")
else:
    print("VAi dormir no banco da praça!!")