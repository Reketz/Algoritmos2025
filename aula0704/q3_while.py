# a. Nome: maior que 3 caracteres; 
# b. Idade: entre 0 e 150; 
# c. Salário: maior que zero; 
# d. Sexo: 'f' ou 'm'; 
# e. Estado Civil: 's', 'c', 'v', 'd'; 

nome = input("Digite seu nome: ")

while (len(nome) <= 3):
    nome = input("Digite seu nome: ")

idade = int(input("Digite a idade: "))

while(idade < 0 or idade > 150):
    idade = int(input("Digite a idade: "))

salario = float(input("Digite o salario"))

while(salario <= 0):
    salario = float(input("Digite o salario"))

sexo = input("Digite o seu sexo: m ou f: ").lower()

while(sexo != 'm' and sexo != 'f'):
    sexo = input("Digite o seu sexo: m ou f: ").lower()

estado = input("Digite o estado civil: ('s', 'c', 'v', 'd')").lower()

while(estado not in 'scvd'):
    estado = input("Digite o estado civil: ('s', 'c', 'v', 'd')").lower()