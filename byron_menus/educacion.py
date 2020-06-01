import os
import time
from byron_Manejadores.manejador_educacion.variable import Variable, listaVariables, return_variable
from byron_Manejadores.manejador_educacion.calculadora import calcular_valor, calculo_posfija, calculo_potencia


def archivo():  # Cargo mi archivo .edu y genero mis datos con programación funcional
    ruta = input("\n Ingrese la dirección donde se encuentre su Archivo .edu     ")
    extension = "edu"
    # print(ruta[len(ruta)-7:len(ruta)])
    if ruta[len(ruta) - 3:len(ruta)] == extension:  # VERIFICO QUE SEA UNA Ruta con la extension adecuda
        if os.path.isfile(ruta):  # Verificar que el archivo exista
            f = open(ruta, 'r')
            contenido = f.read()  # leo el contenido de mi archivo
            splitDatos(contenido)  # print(contenido)
            f.close()
            os.system("cls")
            print("\nEl  archivo fue registrado correctamente")
        # AQUI RETORNARE MI LINK CON MI ARCHIVO CREADO
        else:
            os.system("cls")
            print("\nEl  archivo no existe ingrese una dirección valida")
    else:
        os.system("cls")
        print("\n Debe Ingresar Un archivo con la extension solicitada,    VUELVA A INTENTARLO")


def crear_Variable(datos_var):
    atributos = datos_var.split(sep=',')
    datos = atributos[1].split(sep=' ')
    valor = calcular_valor(datos)
    listaVariables.append(Variable(atributos[0], valor))


def postfija(expresion, fecha, hora):
    datos = expresion.split(sep=' ')
    post = calculo_posfija(datos)
    escritura = f'\n[{fecha}   {hora}]   Postfija: {post}'
    return escritura


def incrementar_var(datos_var):
    variable = return_variable(datos_var)
    variable.incrementar_var()


def mitad_var(datos_var):
    variable = return_variable(datos_var)
    variable.mitad_var()


def triple_var(datos_var):
    variable = return_variable(datos_var)
    variable.triple_var()


def positivo_var(datos_var):
    variable = return_variable(datos_var)
    variable.positivo_var()


def negativo_var(datos_var):
    variable = return_variable(datos_var)
    variable.negativo_var()


def potencia(datos_var, fecha, hora):
    atributos = datos_var.split(sep=',')
    datos1 = atributos[0].split(sep=' ')
    datos2 = atributos[1].split(sep=' ')
    valor = calculo_potencia(datos1, datos2)
    escritura = f'\n[{fecha}   {hora}]   Potencia: {valor}'
    return escritura


def valor_variable(name_var, fecha, hora):
    variable = return_variable(name_var)
    escritura = f'\n[{fecha}   {hora}]   {name_var}: {variable.valor}'
    return escritura


def splitDatos(datos):
    instruccion = datos.split('\n')
    instruccionesNuevas = ""  # todas las instrucciones que mandare a mi nuevo file.mascotas_result
    for i in instruccion:
        fechaActual = time.strftime("%d/%m/%y")
        horaActual = time.strftime("%H:%M:%S")
        inst_y_dat = i.split(sep=':')
        if inst_y_dat[0] == "Variable":

            crear_Variable(inst_y_dat[1])

        elif inst_y_dat[0] == "Postfija":

            instruccionesNuevas += postfija(inst_y_dat[1], fechaActual, horaActual)

        elif inst_y_dat[0] == "Incrementar":

            incrementar_var(inst_y_dat[1])

        elif inst_y_dat[0] == "Mitad":

            mitad_var(inst_y_dat[1])

        elif inst_y_dat[0] == "Triple":

            triple_var(inst_y_dat[1])

        elif inst_y_dat[0] == "Positivo":

            positivo_var(inst_y_dat[1])

        elif inst_y_dat[0] == "Negativo":

            negativo_var(inst_y_dat[1])

        elif inst_y_dat[0] == "Potencia":

            instruccionesNuevas += potencia(inst_y_dat[1], fechaActual, horaActual)

        elif inst_y_dat[0] == "Imprimir":

            instruccionesNuevas += valor_variable(inst_y_dat[1], fechaActual, horaActual)

        elif inst_y_dat[0] == "Imprimir_Mensaje":

            instruccionesNuevas += f'\n[{fechaActual}   {horaActual}]  {inst_y_dat[1]}'

    newrut = "C:\\Users\\ByronJosué\\Desktop\\calculadora.mascotas_result"
    arch = open(newrut, 'w')
    arch.write(instruccionesNuevas)
    arch.close()