clienteNovo = input("Você é um cliente novo? (s / n)")
valorCompras = float(input("Digite o valor total das compras: "))

if(clienteNovo == 's' and valorCompras > 50):
    desconto = valorCompras * 0.1
    print(f"O seu desconto é de {desconto}")
else:
    print("Você não ganhou desconto...")