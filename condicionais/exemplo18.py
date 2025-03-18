data = input("Digite uma data no formato: dd/mm/yyyy")
dia = int(data[0:2]) #12
mes = int(data[3:5]) #09 -> 9
ano = int(data[6:10])#2025
validado = 'N'
eBissexto = "N"

if(ano % 4 == 0):
    eBissexto = "S"
    if(ano % 100 == 0 and ano % 400 != 0):
        eBissexto = "N"

if(mes == 1 
   or mes == 3 
   or mes == 5 
   or mes == 7
   or mes == 8
   or mes == 10
   or mes == 12):
    if(dia >= 1 and dia <= 31):
        validado = 'S'
elif(mes == 4 
     or mes == 6 
     or mes == 9 
     or mes == 11):
    if(dia >= 1 and dia <= 30):
        validado = 'S'
elif(mes == 2):
    if(eBissexto == 'S' and dia >= 1 and dia <= 29):
        validado = 'S'
    elif(dia >= 1 and dia <= 28):
        validado = 'S'


if(validado == 'S'):
    print('É uma data válida')
else:
    print("É uma data inválida")
