import os
import time


def archivo():
    ruta = input("\n Ingrese la dirección donde se encuentre su Archivo .almacen     ")
    extension = "almacen"
    if ruta[len(ruta) - 7:len(ruta)] == extension:  # VERIFICO QUE SEA UNA Ruta con la extension adecuada
        if os.path.isfile(ruta):  # Verificar que el archivo exista
            f = open(ruta, 'r')
            contenido = f.read()  # leo el contenido de mi archivo
            splitDatos(contenido)  # print(contenido)
            f.close()
            os.system("cls")
            print("\nEl  archivo fue registrado correctamente")
        else:
            os.system("cls")
            print("\nEl  archivo no existe ingrese una dirección valida")
    else:
        os.system("cls")
        print("\n Debe Ingresar Un archivo con la extension solicitada,    VUELVA A INTENTARLO")

def declarar():

def splitDatos(datos):
    instruccion = datos.split('\n')
    instruccionesNuevas = ""  # todas las instrucciones que mandare a mi nuevo file.mascotas_result
    for i in instruccion:
        fechaActual = time.strftime("%d/%m/%y")
        horaActual = time.strftime("%H:%M:%S")
        inst_y_dat = i.split(sep=':')
        if inst_y_dat[0] == "Declarar":

            instruccionesNuevas += declarar(inst_y_dat[1], fechaActual, horaActual)

        elif inst_y_dat[0] == "Puede_Entregar_Mensaje":

            instruccionesNuevas += puede_entregar_mensaje(inst_y_dat[1], fechaActual, horaActual)

        elif inst_y_dat[0] == "Enviar_Mensaje":

            instruccionesNuevas += enviar_mensaje(inst_y_dat[1], fechaActual, horaActual)

        elif inst_y_dat[0] == "Crear_Gato":

            instruccionesNuevas += crear_Gato(inst_y_dat[1], fechaActual, horaActual)

        elif inst_y_dat[0] == "Conviene_Comer_Raton":

            instruccionesNuevas += conviene_comer_raton(inst_y_dat[1], fechaActual, horaActual)

        elif inst_y_dat[0] == "Enviar_Comer_Raton":

            instruccionesNuevas += enviar_comer_raton(inst_y_dat[1], fechaActual, horaActual)

        elif inst_y_dat[0] == "Dar_de_Comer":

            instruccionesNuevas += enviar_comer(inst_y_dat[1], fechaActual, horaActual)

        elif inst_y_dat[0] == "Resumen_Mascota":

            instruccionesNuevas += resumen_mascota(inst_y_dat[1], fechaActual, horaActual)

    newrut = "C:\\Users\\ByronJosué\\Desktop\\almacenes.almacen_result"
    arch = open(newrut, 'w')
    arch.write(instruccionesNuevas)
    arch.close()