from typing import Mapping


def potenciación(repeticiones):
    numero = int(input("Escribe un numero para saber sus potencias: "))
    potencia = int(input("Cuantas potencias del número seleccionado quieres:"))
    for i in potencia:
        resultado = numero **repeticiones
        print(resultado)
        repeticiones +=1

