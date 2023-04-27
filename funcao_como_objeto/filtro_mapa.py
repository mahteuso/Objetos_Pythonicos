alunos = [("Mateus", 8), ("Marco", 6), ("Roger", 3), ("Cleiton", 9)]

print([(marco, nota) for marco, nota in alunos if nota > 5])

print(list(filter(lambda aluno: (aluno[1] / 2) >= 2.5, alunos)))

