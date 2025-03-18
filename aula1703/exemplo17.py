ano = int(input("Digite o ano: "))

eBissexto = "N"

if(ano % 4 == 0):
    eBissexto = "S"
    if(ano % 100 == 0 and ano % 400 != 0):
        eBissexto = "N"

if(eBissexto == "S"):
    print("O ano é bissexto!")
else:
    print("O ano não é bissexto!")