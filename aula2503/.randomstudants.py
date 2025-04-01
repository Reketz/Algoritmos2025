import random

# Lista de alunos (pode ser alterada conforme necessário)
alunos = [
"Adryhan Miguel de Melo Sarmento",
"Edglan Xavier Martins",
"Gabriel De Andrade Bernardo",
"Gabriel Ribeiro Mendes Pinto",
"Guilherme Abrantes Cezarino",
"Joelderson Keven Soares da Silva",
"Nicolas Casimiro Sarmento",
"Sadhielly Claucia Vital Fernandes",
"Gabriel Moreira",
"João pedro"
]

# Embaralha a lista de alunos
random.shuffle(alunos)

# Forma as duplas
print("Duplas formadas:")
for i in range(0, len(alunos) - 1, 2):
    print(f"- {alunos[i]} || {alunos[i+1]}")

# Caso o número de alunos seja ímpar, o último aluno forma um trio com a última dupla
if len(alunos) % 2 == 1:
    print(f"- {alunos[-3]}, {alunos[-2]} e {alunos[-1]}")
