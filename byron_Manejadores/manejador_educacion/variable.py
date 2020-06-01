listaVariables = []


def return_variable(nombre_var):
    global listaVariables
    for variable in listaVariables:
        if variable.nombre == nombre_var:
            return variable


class Variable:
    def __init__(self, nombre, valor):
        self.__nombre = str(nombre)
        self.__valor = int(valor)

    def incrementar_var(self):
        self.valor += 1

    def mitad_var(self):
        self.valor /= 2

    def triple_var(self):
        self.valor *= 3

    def positivo_var(self):
        if self.valor < 0:
            self.valor = -(self.valor)

    def negativo_var(self):
        if self.valor > 0:
            self.valor = -(self.valor)

    @property
    def nombre(self):
        return self.__nombre

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, nuevo_valor):
        self.__valor = nuevo_valor

    @nombre.setter
    def nombre(self, nombre_var):
        self.__nombre = nombre_var
