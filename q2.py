salario = float(input("Digite o seu salario: "))
porcentagem = float(input("Digite a porcentagem do IR"))

print(f"O seu salário é: {salario} reais")
print(f"a porcentagem do seu imposto de renda é: {porcentagem}")

salario_liquido = salario - (salario * porcentagem / 100)
print(salario_liquido)