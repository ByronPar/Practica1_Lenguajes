class Pajaro(Mascota):
    tipo = "Pajaro"

    def __init__(self, nombre):
        Mascota.__init__(self, nombre)
        self.tipo = "Pajaro"

    def puedeEntregarMensaje(self, nombre, posx, posy):
        global listaMascotas
        for i in listaMascotas:

            mascota = i
            if mascota.nombre == nombre:
                if mascota.tipo == "Pajaro":
                    distanciaAdeja = mascota.CalcDistancia(int(mascota.posX), int(posx), int(mascota.posY),
                                                           int(posy))  # distancia en kilometros
                    energiaAdejar = 10 + distanciaAdeja
                    if mascota.energia == 0:
                        return "muerto"
                    elif mascota.energia >= energiaAdejar:
                        return "si"
                    elif mascota.energia < energiaAdejar:
                        return "comida"

    def enviarMensaje(self, nombre, posx, posy):
        global listaMascotas
        indice = 0
        est = "muerto"
        for i in listaMascotas:
            mascota = i
            if mascota.nombre == nombre:
                if mascota.tipo == "Pajaro":
                    distanciaAdeja = mascota.CalcDistancia(int(mascota.posX), int(posx), int(mascota.posY), int(posy))
                    energiaAdejar = 10 + int(distanciaAdeja)
                    if mascota.energia == 0:
                        return "muerto"
                    elif mascota.energia >= energiaAdejar:
                        mascota.energia = mascota.energia - energiaAdejar
                        mascota.posX = posx
                        mascota.posY = posy
                        if mascota.energia == 0:
                            mascota.estado = est
                            listaMascotas[indice] = mascota
                            return "si"
                        else:
                            listaMascotas[indice] = mascota
                            return "si"
                    elif mascota.energia < energiaAdejar:
                        return "comida"
            indice = indice + 1

    def energiaNecesitada(self, nombre, posx, posy):
        global listaMascotas
        for i in listaMascotas:
            mascota = i
            if mascota.nombre == nombre:
                if mascota.tipo == "Pajaro":
                    distanciaAdeja = mascota.CalcDistancia(int(mascota.posX), int(posx), int(mascota.posY), int(posy))
                    energiaAdejar = 10 + int(distanciaAdeja)
                    necesito = energiaAdejar - mascota.energia
                    return necesito