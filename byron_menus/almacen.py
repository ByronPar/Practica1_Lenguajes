import os
import time
from byron_Manejadores.manejador_almacen.caracteres import Token
from byron_Manejadores.manejador_almacen.caracteres import ALMACEN
from byron_Manejadores.manejador_almacen.caracteres import TOKENS
from byron_Manejadores.manejador_almacen.caracteres import return_Token


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


def declarar(id_Cadena):
    datos = id_Cadena.split(sep=',')  # datos[0] = id     datos[1] = cadena
    TOKENS.append(Token(datos[0], len(ALMACEN), datos[1]))  # creo un token y lo almaceno
    ALMACEN.append(len(datos[1]))  # agrego el largo de la cadena al vector de caracteres
    for i in datos[1]:  # listo cada caracter en el vector
        ALMACEN.append(i)
    ALMACEN[0] = len(ALMACEN)  # cambiar el valor del vector en la posicion 1


def concatenar(cadenas):
    datos = cadenas.split(sep=',')
    token = return_Token(datos[0])
    num = token.tamanio
    cadena = token.cadena
    token = return_Token(datos[1])
    num += token.tamanio
    cadena += token.cadena
    ALMACEN.append(num)
    for i in cadena:
        ALMACEN.append(i)
    ALMACEN[0] = len(ALMACEN)  # cambiar el valor del vector en la posicion 1


def posicion_cadena(id, fecha, hora):
    token = return_Token(id)
    return token.imprimir_pos(fecha, hora)


def tamanio_cadena(id, fecha, hora):
    token = return_Token(id)
    return token.imprimir_tam(fecha, hora)


def imprimir(id, fecha, hora):
    token = return_Token(id)
    return token.imprimir(fecha, hora)


def generar_grafo(link1, link2):
    url = link1+link2
    url = url[1 : -1]  # le quito las comillas dobles a la url
    





def splitDatos(datos):
    instruccion = datos.split('\n')
    instruccionesNuevas = ""  # todas las instrucciones que mandare a mi nuevo file.mascotas_result
    for i in instruccion:
        fechaActual = time.strftime("%d/%m/%y")
        horaActual = time.strftime("%H:%M:%S")
        inst_y_dat = i.split(sep=':')
        if inst_y_dat[0] == "Declarar":

            declarar(inst_y_dat[1])

        elif inst_y_dat[0] == "Concatenar":

            concatenar(inst_y_dat[1])

        elif inst_y_dat[0] == "Posicion_cadena":

            instruccionesNuevas += posicion_cadena(inst_y_dat[1], fechaActual, horaActual)

        elif inst_y_dat[0] == "Tamanio":

            instruccionesNuevas += tamanio_cadena(inst_y_dat[1], fechaActual, horaActual)

        elif inst_y_dat[0] == "Imprimir":

            instruccionesNuevas += imprimir(inst_y_dat[1], fechaActual, horaActual)

        elif inst_y_dat[0] == "Generar_grafo":

            generar_grafo(inst_y_dat[1], inst_y_dat[2])


    newrut = "C:\\Users\\ByronJosué\\Desktop\\almacenes.almacen_result"
    arch = open(newrut, 'w')
    arch.write(instruccionesNuevas)
    arch.close()
