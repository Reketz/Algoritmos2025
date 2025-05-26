professores = []

def cadastrar_professor(cpf, nome, curso):
    professor =  {
        'cpf': cpf,
        'nome': nome,
        'curso': curso
    }

    professores.append(professor)

def listar_professores():
    print("*" * 50)
    print("Lista de professores")
    print("*" * 50)
    for prof in professores:
        print(f'{prof['nome']} - {prof['curso']}')

    print("*" * 50)