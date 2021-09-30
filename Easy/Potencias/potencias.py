
def potenciación(repeticiones):
    if repeticiones > 0:
        cont= repeticiones
        proceso_potenciacion = (numero**cont)
        resultado = proceso_potenciacion
        print(resultado)
        potenciación(repeticiones-1)
    else:
        print("Ya")


if __name__ == "__main__":
    numero = int(input("Escribe un numero para saber sus potencias: "))
    potencia = int(input("Cuantas potencias del número seleccionado quieres:"))
    repts = potencia
    potenciación(repts)
