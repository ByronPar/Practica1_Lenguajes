from byron_Manejadores.manejador_mascotas.mascota import Mascota


class Pajaro(Mascota):
    def __init__(self, nombre=None):
        super().__init__(nombre, tipo='pajaro')

    def puedeEntregarMensaje(self, posx, posy):
        if self.energia == 0:
            return f'{self.nombre}, ya me mori'
        elif self.energia >= self.energiaAdejar(posx, posy):
            return f'{self.nombre}, si Puedo ir a dejar el mensaje'
        elif self.energia < self.energiaAdejar(posx, posy):
            return f'{self.nombre}, Estoy exhausto. Dame de comer {self.energiaNecesitada(posx, posy)} para ir.'

    def enviarMensaje(self, posx, posy):
        if self.energia == 0:
            return f'{self.nombre}, ya me mori'
        elif self.energia >= self.energiaAdejar(posx, posy):
            self.energia = self.energia - self.energiaAdejar(posx, posy)
            self.posx = posx
            self.posy = posy
            if self.energia == 0:
                self.estado = 'muerto'
            return f'{self.nombre}, Ya fui a dejar el mensaje a ( {posx} , {posy} )'
        elif self.energia < self.energiaAdejar(posx, posy):
            return f'{self.nombre}, Estoy exhausto. Dame de comer {self.energiaNecesitada(posx, posy)} para ir.'