def decorador(func):
    print(func.__name__)
    def interna(x, y):
        if isinstance(x, int) and isinstance(y, int):
            return func(x, y)
        else:
            raise ValueError('Entre somente com números')
    return interna

@decorador
def interna(x, y):
    return x + y

print(interna(2, "Mateus"))




