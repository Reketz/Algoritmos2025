# poder de ataque
def Expelliarmus(poderAtaque):
    return poderAtaque * 2

# poder defeza
def Protego(poderDefesa):
    return poderDefesa * 2.5

def lutar(nomeBruxoAtacante, poderBruxoAtacante, bruxoVitima, defesaVitima):
    if(poderBruxoAtacante == defesaVitima):
        print("ninguém ganhou nadaa")
    elif(poderBruxoAtacante > defesaVitima):
        print(f"""{nomeBruxoAtacante} com 
              poder de ataque {poderBruxoAtacante} 
              ganhou do {bruxoVitima} com defesa {defesaVitima}""")
    else:
        print(f"""{bruxoVitima} com poder de defesa {defesaVitima} 
              ganhou do {nomeBruxoAtacante} com poder de ataque 
              {poderBruxoAtacante}""")


pa = Expelliarmus(50)
pd = Protego(40)
lutar('Harry', pa, 'Malfoy', pd)
