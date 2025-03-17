idade = int(input("Digite sua idade: "))
acompanhado = input("Você está acompanhado? (s / n)")

if(idade >= 18 or acompanhado == 's'):
    print("Você pode assistir o filme a vontade!")
else:
    print("Você não pode assistir esse filme! MUITO VIOLENTO!")