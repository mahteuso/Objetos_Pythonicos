from interruptor import Interruptor
from typing import Type

class Pessoa():

    def acender(self, interruptor: Type[Interruptor]) -> None:
        interruptor.ligar()

    def apagar(self, interruptor: Type[Interruptor]) -> None:
        interruptor.desligar()