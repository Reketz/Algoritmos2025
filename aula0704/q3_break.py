while(True):
    nome = input("Digite o seu nome")
    if(len(nome) > 3):
        break

while(True):
    idade = input("Digite a sua idade")
    if(idade >= 0 and idade <= 150):
        break

while(True):
    salario = input("Digite o seu salario")
    if(salario > 0):
        break

while(True):
    sexo = input("Digite o seu sexo").lower()
    if(sexo == 'm' or sexo == 'f'):
        break

while(True):
    estado = input("Digite o seu estado civil").lower()
    if(estado in 'scvd'):
        break