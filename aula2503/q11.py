salario = float(input("Digite o salário: "))
aumento = 0
porcentagem = ""

if(salario > 0 and salario <= 280):
    aumento = salario * 0.2
    porcentagem = "20%"
elif(salario > 280 and salario <= 700):
    aumento = salario * 0.15
    porcentagem = "15%"
elif(salario > 700 and salario <= 1500):
    aumento = salario * 0.1
    porcentagem = "10%"
elif(salario > 1500):
    aumento = salario * 0.05
    porcentagem = "5%"

print(f"O salário atual {salario}")
print(f"O percentual {porcentagem}")
print(f"O valor do aumento {aumento}")
print(f"O salário final {salario + aumento}")
