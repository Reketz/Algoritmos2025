inscrito = input("Vc está inscrito? (Sim/Não)")

if(inscrito != "Sim" or inscrito != "sim"):
    print("Você nem aluno é!")
else:
    aulas = int(input("Digite o total das aulas"))
    aulasAssistidas = int(input("Digite o total das aulas assistidas"))
    percentual = aulasAssistidas * 0.8
    if(percentual >= aulas):
        print("Você pode emitir o certificado")
    else:
        print(f"Vocé precisa assistir {percentual - aulasAssistidas} para emitir o certificado")