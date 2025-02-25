genero = input("Digite o seu genero: (m = Masculino) (f = Feminino)")
h = float(input('Digite sua altura: '))

if(genero == 'm'):
  print((72.7*h) - 58)
else:
  print((62.1*h) - 44.7)
