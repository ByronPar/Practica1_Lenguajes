import os
import time

from byron_Manejadores.manejador_mascotas.pajaro import Pajaro
from byron_Manejadores.manejador_mascotas.gato import Gato
from byron_Manejadores.manejador_mascotas.mascota import listaMascotas, return_Mascota, resumenGlobal


def crear_Pajaro(name_paj, fecha, hora):
    listaMascotas.append(Pajaro(name_paj))
    escritura = "\n[" + fecha + "  " + hora + "]  " + "Se Creo el pájaro " + name_paj
    return escritura


def puede_entregar_mensaje(datos_paj, fecha, hora):
    atributos = datos_paj.split(sep=',')
    pajaro = return_Mascota(atributos[0])
    escritura = "\n[" + fecha + "  " + hora + "]  " + pajaro.puedeEntregarMensaje(atributos[1], atributos[2])
    return escritura


def enviar_mensaje(datos_paj, fecha, hora):
    atributos = datos_paj.split(sep=',')
    pajaro = return_Mascota(atributos[0])
    escritura = "\n[" + fecha + "  " + hora + "]  " + pajaro.enviarMensaje(atributos[1], atributos[2])
    return escritura


def crear_Gato(name_cat, fecha, hora):
    listaMascotas.append(Gato(name_cat))
    escritura = "\n[" + fecha + "  " + hora + "]  " + "Se Creo el gato " + name_cat
    return escritura


def conviene_comer_raton(datos_cat, fecha, hora):
    atributos = datos_cat.split(sep=',')
    gato = return_Mascota(atributos[0])
    escritura = "\n[" + fecha + "  " + hora + "]  " + gato.conviene_Comer(atributos[1], atributos[2], atributos[3])
    return escritura


def enviar_comer_raton(datos_cat, fecha, hora):
    atributos = datos_cat.split(sep=',')
    gato = return_Mascota(atributos[0])
    escritura = "\n[" + fecha + "  " + hora + "]  " + gato.comer_raton(atributos[1], atributos[2], atributos[3])
    return escritura


def enviar_comer(datos_Animal, fecha, hora):
    atributos = datos_Animal.split(sep=',')
    mascota = return_Mascota(atributos[0])
    escritura = "\n[" + fecha + "  " + hora + "]  " + mascota.dar_Comida(atributos[1])
    return escritura


def resumen_mascota(name_mascota, fecha, hora):
    mascota = return_Mascota(name_mascota)
    escritura = "\n[" + fecha + "  " + hora + "]  " + mascota.resumen_Mascota()
    return escritura


def archivo():  # cargo mis  archivos y genero mis datos
    ruta = input("\n Ingrese la dirección donde se encuentre su Archivo .mascotas     ")
    extension = "mascotas"
    if ruta[len(ruta) - 8:len(ruta)] == extension:  # VERIFICO QUE SEA UNA Ruta con la extension adecuda
        if os.path.isfile(ruta):  # Verificar que el archivo exista
            f = open(ruta, 'r')  # ABRO EL ARCHIVO
            contenido = f.read()  # leo el contenido de mi archivo
            splitDatos(contenido)  # print(contenido)
            f.close()  # cierro el archivo
            os.system("cls")
            print("\nEl  archivo fue registrado correctamente")
        else:
            os.system("cls")
            print("\nEl  archivo no existe ingrese una dirección valida")
    else:
        os.system("cls")
        print("\n Debe Ingresar Un archivo con la extension solicitada,    VUELVA A INTENTARLO")


def splitDatos(datos):  # METODO PARA SEPARAR MIS INSTRUCCIONES
    instruccion = datos.split('\n')
    instruccionesNuevas = ""  # todas las instrucciones que mandare a mi nuevo file.mascotas_result
    for i in instruccion:
        fechaActual = time.strftime("%d/%m/%y")
        horaActual = time.strftime("%H:%M:%S")
        inst_y_dat = i.split(sep=':')
        if inst_y_dat[0] == "Crear_Pajaro":

            instruccionesNuevas = instruccionesNuevas + crear_Pajaro(inst_y_dat[1], fechaActual, horaActual)

        elif inst_y_dat[0] == "Puede_Entregar_Mensaje":

            instruccionesNuevas = instruccionesNuevas + puede_entregar_mensaje(inst_y_dat[1], fechaActual, horaActual)

        elif inst_y_dat[0] == "Enviar_Mensaje":

            instruccionesNuevas = instruccionesNuevas + enviar_mensaje(inst_y_dat[1], fechaActual, horaActual)

        elif inst_y_dat[0] == "Crear_Gato":

            instruccionesNuevas = instruccionesNuevas + crear_Gato(inst_y_dat[1], fechaActual, horaActual)

        elif inst_y_dat[0] == "Conviene_Comer_Raton":

            instruccionesNuevas = instruccionesNuevas + conviene_comer_raton(inst_y_dat[1], fechaActual, horaActual)

        elif inst_y_dat[0] == "Enviar_Comer_Raton":

            instruccionesNuevas = instruccionesNuevas + enviar_comer_raton(inst_y_dat[1], fechaActual, horaActual)

        elif inst_y_dat[0] == "Dar_de_Comer":

            instruccionesNuevas = instruccionesNuevas + enviar_comer(inst_y_dat[1], fechaActual, horaActual)

        elif inst_y_dat[0] == "Resumen_Mascota":

            instruccionesNuevas = instruccionesNuevas + resumen_mascota(inst_y_dat[1], fechaActual, horaActual)

        elif inst_y_dat[0] == "Resumen_Global":
            instruccionesNuevas = instruccionesNuevas + "\n--------------------------------    RESUMEN GLOBAL  -----------------------------"
            instruccionesNuevas = instruccionesNuevas + resumenGlobal()
            instruccionesNuevas = instruccionesNuevas + "\n---------------------------------------------------------------------------------"
    newrut = "C:\\Users\\ByronJosué\\Desktop\\ResumenMascotas.mascotas_result"
    arch = open(newrut, 'w')
    arch.write(instruccionesNuevas)
    arch.close()
