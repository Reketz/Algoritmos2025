# importa todas as funções do arquivo calculadora.py
import calculadora
# importa somente a função exponencial
# esse trecho significa: a partir do arquivo calculadora_avancada importe a função: exponencial
from calculadora_avancada import exponencial

num1 = float(input("Digite o número 1: "))
num2 = float(input("Digite o número 2: "))
operacao = input("Digite a operação (+ - / *): ")

resultado = None

if(operacao == '+'):
    resultado = calculadora.somar(num1, num2)
elif(operacao == '-'):
    resultado = calculadora.subtrair(num1, num2)
elif(operacao == '/'):
    resultado = calculadora.dividir(num1, num2)
elif(operacao == '*'):
    resultado = calculadora.multiplicar(num1, num2)
elif(operacao == 'E'):
    resultado = exponencial(num1, num2)
else:
    print("Erro! Opção inválida!")

if(resultado != None):
    print(f'Resultado = {resultado}')