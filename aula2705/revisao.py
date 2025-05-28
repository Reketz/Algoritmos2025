caminho = 'C:\\armazenamento\\dados.csv'

def converterDicionario(aluno):
    return aluno['nome'] + ',' + str(aluno['av1']) + ',' + str(aluno['av2']) + ',' + str(aluno['av3'])
def converterAluno(linha):
    dados = linha.split(',')
    aluno = {
        'nome': dados[0],
        'av1': dados[1],
        'av2': dados[2],
        'av3': dados[3],
    }
    return aluno

def listarAlunos():
    alunos = []
    with open(caminho, 'r') as arquivo:
        for indice, linha in enumerate(arquivo):
            if(indice != 0):
                aluno = converterAluno(linha)
                alunos.append(aluno)
            
    return alunos

def imprimirAlunos():
    alunos = listarAlunos()
    for a in alunos:
        print("Nome: ", a['nome'])

def adicionarAluno():
    nome = input("Digite o nome: ")
    av1 = float(input("Digite a nota 1: "))
    av2 = float(input("Digite a nota 2: "))
    av3 = float(input("Digite a nota 3: "))
    aluno = {
        'nome': nome,
        'av1': av1,
        'av2': av2,
        'av3': av3
    }
    with open(caminho, '+a') as arquivo:
        arquivo.write(converterDicionario(aluno))

def salvarDados(alunos):
    with open(caminho, 'w') as arquivo:
        arquivo.write('Nome,AV1,AV2,AV3\n')
        for aluno in alunos:
            arquivo.write(converterDicionario(aluno).strip() + "\n")

def alterarAluno():
    nome = input("Digite o nome do aluno: ")
    alunos = listarAlunos()
    for a in alunos:
        if(a['nome'] == nome):
            a['av1'] = float(input("Digite a nota 1: "))
            a['av2'] = float(input("Digite a nota 2: "))
            a['av3'] = float(input("Digite a nota 3: "))
            salvarDados(alunos)
            break


def excluirAluno():
    nome = input("Digite o nome do aluno: ")
    alunos = listarAlunos()
    alunosAtual = []
    for a in alunos:
        if(a['nome'] != nome):
            alunosAtual.append(a)

    salvarDados(alunosAtual)
    

excluirAluno()

#alterarAluno()

#adicionarAluno()
