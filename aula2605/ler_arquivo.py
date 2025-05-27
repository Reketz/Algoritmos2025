caminho = 'C:\\Users\\guilherme.estevao_sa\\Documents\\FACULDADE\\alunos.txt'

arquivo = open(caminho, 'r') #read
conteudo = arquivo.read()
print(conteudo)

arquivo.close()