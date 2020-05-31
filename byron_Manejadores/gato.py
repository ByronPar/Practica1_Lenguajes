class Gato(Mascota):
    tipo = "Gato"

    def __init__(self, nombre):
        Mascota.__init__(self, nombre)
        self.tipo = "Gato"

    def convieneComer(self, nombre, posx, posy, peso):
        global listaMascotas
        for i in listaMascotas:
            mascota = i
            if mascota.nombre == nombre:
                if mascota.tipo == "Gato":
                    if int(peso) == 0:
                        distanciaAdeja = mascota.CalcDistancia(int(mascota.posX), int(posx), int(mascota.posY),
                                                               int(posy))
                        energiaAdejar = (distanciaAdeja / 2)
                        if mascota.energia == 0:
                            return "muerto"
                        elif mascota.energia >= energiaAdejar:
                            return "si"
                        elif mascota.energia < energiaAdejar:
                            return "comida"

                    distanciaAdeja = mascota.CalcDistancia(int(mascota.posX), int(posx), int(mascota.posY), int(posy))
                    energiaAdejar = int(distanciaAdeja / 2) - 12 - int(peso)
                    if mascota.energia == 0:
                        return "muerto"
                    elif mascota.energia >= int(energiaAdejar):
                        return "si"
                    elif mascota.energia < int(energiaAdejar):
                        return "comida"

    def energiaNueva(self, nombre, posx, posy, peso):
        global listaMascotas
        indice = 0
        est = "muerto"
        for i in listaMascotas:
            mascota = i
            if mascota.nombre == nombre:
                if mascota.tipo == "Gato":
                    distanciaAdeja = mascota.CalcDistancia(int(mascota.posX), int(posx), int(mascota.posY), int(posy))
                    energiaAdejar = int(distanciaAdeja / 2) - 12 - int(peso)
                    mascota.energia = mascota.energia - (energiaAdejar)
                    mascota.posX = posx
                    mascota.posY = posy
                    print(mascota.energia)
                    if mascota.energia == 0:
                        print(mascota.energia)
                        mascota.estado = est
                        print(mascota.energia)
                        listaMascotas[indice] = mascota
                        print(mascota.energia)
                        return mascota.energia
                    else:
                        listaMascotas[indice] = mascota
                        return mascota.energia

            indice = indice + 1

    def energiaNecesitada(self, nombre, posx, posy, peso):
        global listaMascotas
        for i in listaMascotas:
            mascota = i
            if mascota.nombre == nombre:
                if mascota.tipo == "Gato":
                    distanciaAdeja = mascota.CalcDistancia(int(mascota.posX), int(posx), int(mascota.posY), int(posy))
                    energiaAdejar = int(distanciaAdeja / 2) - 12 - int(peso)
                    necesito = energiaAdejar - mascota.energia + 0
                    if necesito >= 1:
                        return necesito
                    necesito = 1
                    return necesito