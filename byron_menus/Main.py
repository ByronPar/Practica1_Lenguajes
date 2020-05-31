import msvcrt
import os
import sys
from datetime import time

from Educacion import Educacion
from Entretenimiento import Entretenimiento


def mostrar_menuOpciones():

    print("""
#########################      Menu Principal      #########################

                    1)   Menu Entretenimiento
                    2)   Menu Educación
                    3)   Salir
""")


def mostrar_menu():
    print("""
########################      DATOS DEL ESTUDIANTE      ########################


       Lenguajes formales y de Programación

       Sección :  A+
                                                                 Practica No.1
       Byron Josué Par Rancho  

       Carnet : 201701078


########################                                 ########################



""")


class Menu:
    def __init__(self):
        self.Educacion = Educacion()
        self.Entretenimiento = Entretenimiento()
        self.elecciones = {  # mi diccionario menu
            "1": self.entretenimiento,
            "2": self.educacion,
            "3": self.quit
        }

    def run(self):  # Para Correr mi menu
        while True:
            mostrar_menuOpciones()
            eleccion = input("\n   Seleccione una opción: ")
            accion = self.elecciones.get(eleccion)
            if accion:
                accion()
                break
            else:
                print("\n{0} no es una elección válida".format(eleccion))

    def entretenimiento(self):
        msj = "hola"
        os.system("cls")
        self.Entretenimiento.run(msj)

    def educacion(self):
        msj = "hola"
        os.system("cls")
        self.Educacion.run(msj)

    def quit(self):
        os.system("cls")
        print("\n FIN DE LA APLICACIÓN  ")
        sys.exit(0)


if __name__ == "__main__":
    mostrar_menu()
    input("\n     --->   Presione Enter Para Continuar")
    Menu().run()
