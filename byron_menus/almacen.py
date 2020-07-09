import os
import time
from byron_Manejadores.manejador_almacen.caracteres import Token
from byron_Manejadores.manejador_almacen.caracteres import ALMACEN
from byron_Manejadores.manejador_almacen.caracteres import TOKENS
from  byron_Manejadores.manejador_almacen.caracteres import return_Token

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
    datos = id_Cadena.split(sep=',') #datos[0] = id     datos[1] = cadena
    TOKENS.append(Token(datos[0],len(ALMACEN),datos[1]))    # creo un token y lo almaceno
    ALMACEN.append(len(datos[1])) # agrego el largo de la cadena al vector de caracteres
    for i in datos[1]:      #listo cada caracter en el vector
        ALMACEN.append(i)

def concatenar(cadenas):
    datos = cadenas.split(sep=',')
    Token1 = return_Token(datos[0])
    token2 = return_Token(datos[1])
    ALMACEN.append(Token1.tamanio + token2.tamanio)

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