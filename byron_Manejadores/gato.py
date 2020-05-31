from byron_Manejadores.mascota import Mascota


class Gato(Mascota):
    def __init__(self, nombre):
        super().__init__(nombre, tipo='gato')

    def conviene_Comer(self, posx, posy, peso):
        if self.__energia == 0:
            return f'{self.__nombre}, ya me mori'
        elif self.__energia >= int(self.energiaAdejar(posx, posy, peso)):
            return f'{self.__nombre}, Si me conviene comerme al gato'
        elif self.__energia < int(self.energiaAdejar(posx, posy, peso)):
            return f'{self.__nombre}, Esta muy lejos. No me conviene.'

    def comer_raton(self, posx, posy, peso):
        if self.__energia == 0:
            return f'{self.__nombre}, ya me mori'
        elif self.__energia >= self.energiaAdejar(posx, posy, peso):
            self.__energia = self.__energia - self.energiaAdejar(posx, posy, peso)
            self.__posx = posx
            self.__posy = posy
            if self.__energia == 0:
                self.__estado = 'muerto'
            return f'{self.__nombre}, Ya me comí al ratón, ahora mi energía es {self.__energia}'
        elif self.__energia < self.energiaAdejar(posx, posy):
            return f'{self.__nombre}, Estoy exhausto. Dame de comer {self.energiaNecesitada(posx, posy, peso)} para ir.'