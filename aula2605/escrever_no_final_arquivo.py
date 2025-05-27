caminho = 'C:\\Users\\guilherme.estevao_sa\\Documents\\FACULDADE\\alunos.txt'

alunos = []

alunos.append('João')
alunos.append('Joel')

with open(caminho, '+a') as arquivo:
    for alu in alunos:
        arquivo.write(alu + '\n')