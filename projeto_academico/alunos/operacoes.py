import alunos.validador as validador

alunos = []

def cadastrar_aluno(matricula, nome):
    if(validador.verificar_matricula_existente(matricula)):
        print("Matricula já existe, informe outra!")
    else:
        aluno = {
            'matricula': matricula,
            'nome': nome
        }

        alunos.append(aluno)
        print("Aluno cadastrado com sucesso!")

def listar_alunos():
    for alu in alunos:
        print(f'{alu['nome']} - {alu['matricula']}')

