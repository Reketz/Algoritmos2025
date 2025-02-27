# Crie um algoritmo que peça 
# um numero para o usuário
#   se: esse número for maior ou igual que 12
#   ou esse numero for negativo
#   ou esse numero for 100 ou 200
#   imprima: "Alou Brasil"
#   se não imprima: "Não atende as condições"

numero = int(input("Digite um numero: "))

if(numero >= 12 
   or numero < 0 
   or numero == 100 
   or numero == 200):
  print("Alou Brasil")
else:
  print("Não atende as condições")