def calcular_valor(expresion):
    postfija2 = calculo_posfija(expresion)
    postfija = postfija2.split(sep=' ')
    pila = []
    for i in postfija:
        if i != '':
            if i != ' ':
                if i.isdigit():
                    pila.append(i)
                else:
                    operador2 = int(pila.pop())
                    operador1 = int(pila.pop())
                    if i == '+':
                        pila.append(operador1 + operador2)
                    elif i == '-':
                        pila.append(operador1 - operador2)
                    elif i == '*':
                        pila.append(operador1 * operador2)
                    elif i == '/':
                        pila.append(operador1 / operador2)

    return int(pila[0])


def calculo_posfija(expresion):
    pila = []
    postfija = ""
    prioridadPila = 0
    for i in expresion:
        if not i.isdigit():  # significa que no es un digito
            if pila:  # si la pila no esta vacia hare esto
                if i == ')':  # si el elemento analizar es este  entonces
                    while pila[- 1] != '(':  # se hara pop a la pila hasta encontrar este elemento
                        postfija += str(pila.pop())  # lo que se se saque se añadira al string
                        postfija += ' '
                    pila.pop()  # de ultimo se sacara el elemento ( y si la pila no esta vacia tomare el valor de prioridad
                    if pila:
                        prioridadPila = prioridad_pila(pila[- 1])
                elif prioridad_exp(i) > prioridadPila:  # si cumple esto, facil , solo lo agregare a la pila
                    pila.append(i)
                    prioridadPila = prioridad_pila(i)  # modifico la prioridad en la pila
                else:
                    while prioridad_exp(i) < prioridadPila and pila == True and pila[-1] != '(':
                        postfija += str(pila.pop())
                        postfija += ' '
                        if pila:
                            prioridadPila = prioridad_pila(pila[-1])
                    pila.append(i)
                    prioridadPila = prioridad_pila(i)
            else:  # si la pila esta vacia , agrego el operador
                pila.append(i)
                prioridadPila = prioridad_pila(i)
        else:  # significa que es un digito y lo agrego a la cadena
            postfija += str(i)
            postfija += ' '
    while pila:
        postfija += str(pila.pop())
        postfija += ' '
    return postfija


def prioridad_pila(i):
    if i == '/' or i == '*':
        return 2
    elif i == '+' or i == '-':
        return 1
    elif i == '(':
        return 0


def prioridad_exp(i):
    if i == '/' or i == '*':
        return 2
    elif i == '+' or i == '-':
        return 1
    elif i == '(':
        return 5


def calculo_potencia(exp1, exp2):
    val1 = calcular_valor(exp1)
    val2 = calcular_valor(exp2)
    return pow(val1, val2)
