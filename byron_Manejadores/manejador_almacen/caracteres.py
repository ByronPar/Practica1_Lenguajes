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
        self.__cadena = cadena

    def imprimir(self, fecha, hora):
        cadena = ""
        pos = self.posicion
        for i in self.cadena:
            pos += 1
            cadena += f'\n[{fecha}  {hora}]  {self.id} , {pos} , {i}'
        return cadena

    def imprimir_tam(self, fecha, hora):
        return f'\n[{fecha}  {hora}]  {self.id} , Tam: {self.tamanio}'

    def imprimir_pos(self, fecha, hora):
        return f'\n[{fecha}  {hora}]  {self.id} , Pos: {self.posicion}'

    @property
    def id(self):
        return self.__id

    @property
    def cadena(self):
        return self.__cadena

    @property
    def posicion(self):
        return self.__posicion

    @property
    def tamanio(self):
        return self.__tamanio

    @cadena.setter
    def cadena(self, new_cadena):
        self.__cadena = new_cadena

    @id.setter
    def id(self, nuevo_id):
        self.__id = nuevo_id

    @posicion.setter
    def posicion(self, pos_):
        self.__posicion = pos_

    @tamanio.setter
    def tamanio(self, tam):
        self.__tamanio = tam
