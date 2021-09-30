def run(opcion,u):

    if opcion == 1:
        enumeración_exhaustiva(u)
    elif opcion == 2:
        aproximación_fuerza_bruta(u)
    elif opcion == 3:
        busqueda_binaria(u)
    else:
        print("ERROR INTENTE DENUEVO")
        print(" ")
        opcion=int(input(menu))


def enumeración_exhaustiva(objetivo):
    epsilon = 0.01
    paso = epsilon**2 
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) > epsilon and respuesta <= objetivo:
        respuesta += paso

    if abs(respuesta**2 - objetivo) > epsilon:
        print(f'No se encontro la raiz cuadrada {objetivo}')
    else:
        print(f'La raiz cudrada de {objetivo} es {respuesta}')




def busqueda_binaria(objetivo):
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo)/2


    while abs(respuesta**2 - objetivo) >= epsilon:

        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        
        respuesta = (alto + bajo)/2


    print(f'La raiz cuadrada de {objetivo} es {respuesta}')




def aproximación_fuerza_bruta(objetivo):
    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta += 1

    print(respuesta)
    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz exacta')






if __name__ == "__main__":
    menu= """ 
    Bienvenido al programa para calcular raices posees 3 opciones:
    Opción 1 Enumeración exhaustiva
    Opción 2 Aproximación fuerza bruta
    Opción 3 Busqueda binaria
    
    """
    opcion_usuario = int(input(menu))
    objetivo = int(input('Escoge un numero: '))
    run(opcion_usuario, objetivo)
