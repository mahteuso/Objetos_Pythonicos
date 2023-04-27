alunos = [("Mateus", 8), ("Marco", 6), ("Roger", 3)]
alunos.sort(key=lambda aluno: aluno[0])

for al in alunos:
    print(al)