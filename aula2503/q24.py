# soma subtração divisão multiplação e elevação
numero1 = float(input("Digite um número 1: "))
numero2 = float(input("Digite um número 2: "))
operacao = input("Digite uma operação: "
"\n1 - Soma \n2 - Subtração \n3 - Divisão "
"\n4 - Multiplicação \n5 - Elevação\n")
resultado = 0

if(operacao == "1"):
    resultado = numero1 + numero2
elif(operacao == "2"):
    resultado = numero1 - numero2
elif(operacao == "3"):
    resultado = numero1 / numero2
elif(operacao == "4"):
    resultado = numero1 * numero2
elif(operacao == "5"):
    resultado = numero1 ** numero2

if(resultado % 2 == 0):
    print(f"O {resultado} é par")
else:
    print(f"O {resultado} é ímpar")

if(resultado > 0):
    print(f"O {resultado} é positivo")
else:
    print(f"O {resultado} é negativo")

if(resultado == int(resultado)):
    print(f"O {resultado} é inteiro")
else:
    print(f"O {resultado} é decimal")

