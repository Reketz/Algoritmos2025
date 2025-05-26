# alias - apelido
import alunos.operacoes as op_aluno
import professores.operacoes as op_professor

while True:
    print("Bem vindo ao sistema P1")
    print("1 - Alunos")
    print("2 - Professores")
    print("3 - Cursos")
    print("0 - Sair")
    opc = input("Digite a opção: ")

    if(opc == '0'):
        break

    elif(opc == '1'):
        while True:
            print("1 - Cadastrar")
            print("2 - Listar")
            print("0 - Sair")
            opc = input("Digite a opção: ")
            if(opc == '0'):
                break
            elif(opc == '1'):
                matricula = input("Digitar o número da matricula: ")
                nome = input("Digite o nome do aluno: ")
                op_aluno.cadastrar_aluno(matricula, nome)
            elif(opc == '2'):
                op_aluno.listar_alunos()
    elif(opc == '2'):
        while True:
            print("1 - Cadastrar")
            print("2 - Listar")
            print("0 - Sair")
            opc = input("Digite a opção: ")
            if(opc == '0'):
                break
            elif(opc == '1'):
                cpf = input("Digite o seu cpf: ")
                nome = input("Digite o seu nome: ")
                curso = input("Digite o seu curso: ")
                op_professor.cadastrar_professor(cpf, nome, curso)
            elif(opc == '2'):
                op_professor.listar_professores()