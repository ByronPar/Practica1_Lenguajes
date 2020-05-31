from cmath import sqrt
import time

listaMascotas = []  # VARIABLE GLOBAL PARA ALMACENAR MIS MSACOTAS



def resumenGlobal():
    fechaActual = time.strftime("%d/%m/%y")
    horaActual = time.strftime("%H:%M:%S")
    global listaMascotas
    cadena = ""
    for mascota in listaMascotas:
        cadena = cadena + "\n[" + fechaActual + "  " + horaActual + "]  " + mascota.nombre + " , " + "Energia: " + str(
            mascota.energia) + " , X: " + str(mascota.posx) + " , Y: " + str(
            mascota.posy) + " , Tipo: " + mascota.tipo + " , Estado: " + mascota.estado
    return cadena


def return_Mascota(nombre_Mascota):
    global listaMascotas
    for mascota in listaMascotas:
        if mascota.nombre == nombre_Mascota:
            return mascota


def CalcDistancia(p1X, p2X, p1Y, p2Y):  # CALCULO DE LA DISTANCIA RRECORRIDA
    complejo = sqrt((p1X - p2X) ** 2 + (p1Y - p2Y) ** 2)
    return int(round(complejo.real))


class Mascota:
    def __init__(self, nombre, tipo):
        self.__nombre = nombre
        self.__energia = 1
        self.__estado = "vivo"
        self.__posx = 0.0
        self.__posy = 0.0
        self.__tipo = tipo

    def darComida(self, peso):
        if self.__tipo == "gato":
            self.__energia = self.__energia + 12 + int(peso)
        else:  # SIGNIFICA QUE LA MASCOTA ES DE TIPO PAJARO
            self.__energia = self.__energia + (int(peso) * 4)

    def resumenMascota(self):
        cadena = self.__nombre + " , " + "Energia: " + str(self.__energia) + " , X: " + str(
            self.__posx) + " , Y: " + str(
            self.__posy) + " , Tipo: " + self.__tipo + " , Estado: " + self.__estado
        return cadena

    def energiaAdejar(self, posx, posy, peso=0):
        if self.__tipo == 'pajaro':  # energia a dejar para un pajaro
            distanciaAdeja = CalcDistancia(int(self.__posx), int(posx), int(self.__posy), int(posy))
            energiaAdejar = 10 + int(distanciaAdeja)
            return energiaAdejar
        else:  # energia a dejar para un gato
            distanciaAdeja = CalcDistancia(int(self.__posx), int(posx), int(self.__posy), int(posy))
            energiaAdejar = int(distanciaAdeja / 2) - 12 - int(peso)
            return energiaAdejar

    def energiaNecesitada(self, posx, posy, peso=0):
        if self.__tipo == 'pajaro':  # energia necesitada para un pajaro
            necesito = self.energiaAdejar(posx, posy) - self.__energia
            return necesito
        else:  # energia necesitada para un gato
            necesito = self.energiaAdejar(posx, posy, peso) - self.__energia
            return necesito

    @property
    def nombre(self):
        return self.__nombre

    @property
    def estado(self):
        return self.__estado

    @property
    def energia(self):
        return self.__energia

    @property
    def posx(self):
        return self.__posx

    @property
    def posy(self):
        return self.__posy

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, nuevo_tipo):
        self.__tipo = nuevo_tipo

    @nombre.setter
    def nombre(self, nombre_Masc):
        self.__nombre = nombre_Masc

    @energia.setter
    def energia(self, nueva_energia):
        self.__energia = nueva_energia

    @estado.setter
    def estado(self, nuevo_estado):
        self.__estado = nuevo_estado

    @posx.setter
    def posx(self, n_posX):
        self.__posx = n_posX

    @posy.setter
    def posy(self, n_posY):
        self.__posy = n_posY
