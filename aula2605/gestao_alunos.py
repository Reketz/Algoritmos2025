caminho = 'C:\\Users\\guilherme.estevao_sa\\Documents\\FACULDADE\\alunos.csv'

ignoraPrimeira = False

alunos = []

with open(caminho, 'r', encoding='utf8') as arquivo:
    for linha in arquivo:
        if(ignoraPrimeira == False):
            ignoraPrimeira = True
            continue

        dados = linha.split(';')
        aluno = {
           'nome': dados[0],
           'turma': dados[1],
           'curso': dados[2]
        }

        alunos.append(aluno)

for a in alunos:
    if(a['curso'] == 'Computação'):
        print(f'{a['nome']} - {a['curso']}')