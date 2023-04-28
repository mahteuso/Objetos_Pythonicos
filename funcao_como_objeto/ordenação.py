alunos = [("Mateus", 8), ("Marco", 6), ("Roger", 3)]
alunos.sort(key=lambda aluno: aluno[0])

for al in alunos:
    print(al)

def soma(*args):
    result = 0
    for a in args:
        result += a
    return result


print(soma(1, 2, 3, 4, 5, 6, 7))

def sum(*args):
    return args

print(sum(1, 2, 3, 4, 5))

lista = [-1, 4, 7, 9, 10]

def min_lista(*args):
    return min(args)

print(min_lista(*lista))

def max_lista(*args):
    return max(args)

print(max_lista(*lista))