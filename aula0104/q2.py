start = "S"
while(start != "N"):
    num = int(input("Digite um número: "))
    if(num > 0):
        if(num % 2 == 0):
            print(f"{num} é par")
        else:
            print(f"{num} é ímpar")
        start = input("Deseja continuar? (S / N)")
    else:
        print("Valor inválido")
    
print("Boa noite")