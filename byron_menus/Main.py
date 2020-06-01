import os
import sys

from byron_menus import educacion
from byron_menus import Entretenimiento


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


def mostrar_menu_Entrenimiento():
    print("""
########################      Menu Entretenimiento      ########################

                1)   Cargar Archivo  .mascotas
                2)   Regresar al Menu Principal
""")


def mostrar_menu_educacion():
    print("""
    ########################      Menu Educación      ########################

                        1)   Cargar Archivo .edu
                        2)   Cargar Archivo .almacen
                        3)   Regresar al Menu Principal
    """)


def regresar():  # Regreso a mi menu principal
    os.system("cls")
    Menu().run()


def quit():
    os.system("cls")
    print("\n FIN DE LA APLICACIÓN  ")
    sys.exit(0)


class Menu:
    def __init__(self):
        self.elecciones = {  # mi diccionario menu
            "1": self.entretenimiento,
            "2": self.educacion,
            "3": quit
        }
        self.elecciones_Entrenimiento = {  # mi diccionario menu
            "1": self.archivo_entretenimiento,
            "2": regresar
        }

        self.elecciones_Educacion = {  # mi diccionario menu
            "1": self.archivo_Educacion,
            #"2": self.archivo_Almacen,
            "3": regresar
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
                os.system("cls")
                print("\n{0} no es una elección válida".format(eleccion))

    def entretenimiento(self):
        while True:
            mostrar_menu_Entrenimiento()
            eleccion = input("\n   Seleccione una opción: ")
            accion = self.elecciones_Entrenimiento.get(eleccion)
            if accion:
                accion()
                break
            else:
                os.system("cls")
                print("\n{0} no es una elección válida".format(eleccion))

    def archivo_entretenimiento(self):
        Entretenimiento.archivo()
        self.entretenimiento()

    def educacion(self):
        while True:
            mostrar_menu_educacion()
            eleccion = input("\n   Seleccione una opción: ")
            accion = self.elecciones_Educacion.get(eleccion)
            if accion:
                accion()
                break
            else:
                os.system("cls")
                print("\n{0} no es una elección válida".format(eleccion))

    def archivo_Educacion(self):
        educacion.archivo()
        self.educacion()


if __name__ == "__main__":
    mostrar_menu()
    input("\n     --->   Presione Enter Para Continuar")
    os.system("cls")
    Menu().run()
