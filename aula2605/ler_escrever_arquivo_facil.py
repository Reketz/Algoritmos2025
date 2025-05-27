caminho = 'C:\\Users\\guilherme.estevao_sa\\Documents\\FACULDADE\\alunos.txt'

alunos = []

with open(caminho, 'r') as arquivo:
    for linha in arquivo:
        alunos.append(linha.strip())


alunos.append('Pamela')
alunos.append('Gabriel')

with open(caminho, 'w') as arquivo:
    for alu in alunos:
        arquivo.write(alu + '\n')