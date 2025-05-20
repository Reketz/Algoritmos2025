def somar(x, y):
    print(x + y)

def subtrair(x, y):
    print(x - y)

def multiplacao(x, y):
    print(x * y)

def dividir(x, y):
    print(x / y)

num1 = float(input("Digite o número 1: "))
num2 = float(input("Digite o número 2: "))
operacao = input("Digite a operação (+ - / *): ")

if(operacao == '+'):
    somar(num1, num2)
elif(operacao == '-'):
    subtrair(num1, num2)
elif(operacao == '/'):
    dividir(num1, num2)
elif(operacao == '*'):
    multiplacao(num1, num2)
else:
    print("Erro! Opção inválida!")