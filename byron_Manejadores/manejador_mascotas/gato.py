from byron_Manejadores.manejador_mascotas.mascota import Mascota


class Gato(Mascota):
    def __init__(self, nombre=None):
        super().__init__(nombre, tipo='gato')

    def conviene_Comer(self, posx, posy, peso):
        if self.energia == 0:
            return f'{self.nombre}, ya me mori'
        elif self.energia >= int(self.energiaAdejar(posx, posy, peso)):
            return f'{self.nombre}, Si me conviene comerme al gato'
        elif self.energia < int(self.energiaAdejar(posx, posy, peso)):
            return f'{self.nombre}, Esta muy lejos. No me conviene.'

    def comer_raton(self, posx, posy, peso):
        if self.energia == 0:
            return f'{self.nombre}, ya me mori'
        elif self.energia >= self.energiaAdejar(posx, posy, peso):
            self.energia = self.energia - self.energiaAdejar(posx, posy, peso)
            self.posx = posx
            self.posy = posy
            if self.energia == 0:
                self.estado = 'muerto'
            return f'{self.nombre}, Ya me comí al ratón, ahora mi energía es {self.energia}'
        elif self.energia < self.energiaAdejar(posx, posy):
            return f'{self.nombre}, Estoy exhausto. Dame de comer {self.energiaNecesitada(posx, posy, peso)} para ir.'