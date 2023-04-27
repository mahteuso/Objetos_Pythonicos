'''
def dobro(x):
    return x * 2


dobro2 = lambda x: x * 2
'''

def ola():
    print('printei')

def executar(o, n=1):
    for _ in range(n):
        o()

executar(ola)
'''
def ver(x, n):
    for _ in range(n):
        print(x)

ver("oi", 3)
'''