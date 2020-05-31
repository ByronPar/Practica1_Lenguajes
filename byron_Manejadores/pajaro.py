from byron_Manejadores.mascota import Mascota
from byron_Manejadores.mascota import CalcDistancia


class Pajaro(Mascota):
    def __init__(self, nombre):
        super().__init__(nombre, tipo='pajaro')

    def puedeEntregarMensaje(self, posx, posy):
        if self.__energia == 0:
            return f'{self.__nombre}, ya me mori'
        elif self.__energia >= self.energiaAdejar(posx, posy):
            return f'{self.__nombre}, si Puedo ir a dejar el mensaje'
        elif self.__energia < self.energiaAdejar(posx, posy):
            return f'{self.__nombre}, Estoy exhausto. Dame de comer {self.energiaNecesitada(posx, posy)} para ir.'

    def enviarMensaje(self, posx, posy):
        if self.__energia == 0:
            return f'{self.__nombre}, ya me mori'
        elif self.__energia >= self.energiaAdejar(posx, posy):
            self.__energia = self.__energia - self.energiaAdejar(posx, posy)
            self.__posx = posx
            self.__posy = posy
            if self.__energia == 0:
                self.__estado = 'muerto'
            return f'{self.__nombre}, Ya fui a dejar el mensaje a ( {posx} , {posy} )'
        elif self.__energia < self.energiaAdejar(posx, posy):
            return f'{self.__nombre}, Estoy exhausto. Dame de comer {self.energiaNecesitada(posx, posy)} para ir.'
