#Q1
tamanhoPipoca = input("Digite o tamanho da pipoca: P - pequena, M - Média, G - Grande: ")
temRefrigerante = input("A compra inclui refrigerente: S - sim, N - não: ")
desconto = 0
total = 0

if(tamanhoPipoca == "P"):
    total = 5
elif(tamanhoPipoca == "M"):
    total = 8
elif(tamanhoPipoca == "G"):
    total = 10

if(temRefrigerante == "S"):
    total += 5
    desconto = total * 0.1

print(f"Valor total: {total}")
print(f"Valor desconto: {desconto}")
print(f"Valor total com desconto: {total - desconto}")

#Q2
saltoGean = float(input("Qual tamanho do salto de Gean: "))
saltoGustavo = float(input("Qual tamanho do salto de Gustavo: "))

if(saltoGean > saltoGustavo):
    print(f"Gean ganhou com um salto de {saltoGean} metros")
elif(saltoGustavo > saltoGean):
    print(f"Gustavo ganhou com um salto de {saltoGustavo} metros")
else:
    print("Ambos empataram")

#Q3
nome = input("Qual seu nome? ")
altura = float(input("Qual sua altura? "))
idade = int(input("Qual sua idade? "))

if(nome == "messi" or (altura > 1.6 and idade > 17)):
    print("Você joga no meu time")

#Q4
idade = int(input("Digite sua idade: "))
if(idade < 16):
    print("Não pode votar")
elif(idade == 16 or idade == 17 or idade > 70):
    print("Voto totalmente opcional")
elif(idade >= 18 and idade <= 70):
    print("Voto é obrigatório!")