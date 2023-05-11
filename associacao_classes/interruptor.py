class Interruptor:
    def __init__(self, comodo):
        self.__comodo = comodo

    def ligar(self):
        print(f'Ligando a luz do {self.__comodo}')

    def desligar(self):
        print(f'Desligando a luz do {self.__comodo}')
