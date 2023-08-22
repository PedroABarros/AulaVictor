#codigo para professores:

def somaNotas(x):
    soma = 0
    for i in x:
        soma += i
    return soma

def somaMedia(x, y):
    media = x/len(y)
    return media

notasAlunos = []

for i in range(5):
    notasAlunos.append(float(input(f"Digite a nota da prova 1, do aluno{i+1}: ")))

totalNotas = somaNotas(notasAlunos)
media = somaMedia(totalNotas, notasAlunos)

print(notasAlunos)
print(f"A media dos alunos na prova foi de {media}")
