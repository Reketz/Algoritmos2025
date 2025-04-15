produtos = [
    ["Camisa M", 22.98], 
    ["Calça M adolecente", 399], 
    ["Camisa polo G", 120], 
    ["Calça saruel", 123]
]

totalCompra = 0
print("*" * 50)
print("Bem vindo a loja Sua Moda")
print("Escolha nossos produtos no catálogo abaixo")
print("*" * 50)
while True:
    indice = 0
    for prod in produtos:
        print('Código', indice + 1,
            'Nome:', prod[0],
            'Valor:', prod[1])
        indice += 1

    codigo = int(input("Qual produto você deseja comprar? (Digite o código) "))
    codigo -= 1

    prodSelecionado = produtos[codigo]

    print(f"Você escolheu o produto {prodSelecionado[0]}")
    valorProduto = prodSelecionado[1]

    quant = int(input("Quantas unidades você deseja? "))

    totalCompra += valorProduto * quant
    continuar = input("Deseja continuar comprando? (S/N)")
    if(continuar.upper() != 'S'):
        break


print(f"Sua compra deu R${totalCompra:.2f}")