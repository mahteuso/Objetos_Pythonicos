"""
>>> def ola():
...     print("Olá")
...
>>> executar(ola)
Olá
>>> executar(ola, 2)
Olá
Olá
>>> executar(ola, 3)
Olá
Olá
Olá
"""
def ola():
    print("Olá")

f = ola()

def executar(f, n=1):
    for _ in range(n):
        f()
