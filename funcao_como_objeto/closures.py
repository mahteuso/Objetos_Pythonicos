def externa(func):
    def interna():
        return func
    return interna


@externa
def desenha():
    print("Desenhando")

