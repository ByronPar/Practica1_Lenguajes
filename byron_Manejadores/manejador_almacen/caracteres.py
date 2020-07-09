

ALMACEN = [1]
TOKENS = []
def return_Token(id):
    for Token in TOKENS:
        if Token.id == id:
            return Token


class Token:
    def __init__(self, id, posicion, cadena):
        self.__id = id
        self.__posicion = posicion
        self.__tamanio = len(cadena)

    @property
    def id(self):
        return self.__id

    @property
    def posicion(self):
        return self.__posicion

    @property
    def tamanio(self):
        return self.__tamanio

    @id.setter
    def id(self, nuevo_id):
        self.__id = nuevo_id

    @posicion.setter
    def posicion(self, pos_):
        self.__posicion = pos_

    @tamanio.setter
    def tamanio(self, tam):
        self.__tamanio = tam
