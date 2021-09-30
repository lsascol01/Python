import random

def run():
    mensaje= """
    
    TENDRAS SOLO 10 VIDAS PARA COMPLETAR EL JUEGO
    
    Selecciona un numero entre el 1 y el 100: 

    """
    numero_aleatorio = random.randint(1,100)
    seleccion=int(input(mensaje))
    vidas= int(input("Cuantas vidas quieres? "))
    while seleccion != numero_aleatorio:
            vidas -=1 
            vidas_restantes=print("Tienes "+ str(vidas) +" vidas")
            if seleccion > numero_aleatorio and vidas != 0:
                print ("Intenta un número más bajo")
            elif seleccion < numero_aleatorio and vidas != 0:
                print ("Intenta un número más alto")
            elif seleccion== numero_aleatorio and vidas != 0:
                print("Ganaste")
            else:
                print("Perdiste")
                break
            seleccion = int(input("Elige otro numero: "))



if __name__ == "__main__":
    run()




# def run():
#     numerorandom = random.randint(1, 100)
#     numeroelegido = int(input("Introduce un numero: "))
#     vidas = 5
#     while numerorandom != numeroelegido :
#         if numerorandom < numeroelegido : 
#             print("Elige un numero mas pequeño.")
#             vidas -= 1
#         elif numerorandom > numeroelegido : 
#             print("Elige un numero mas grande.")
#             vidas -= 1
#         if vidas == 0 :
#             print("GAME OVER")
#             break
#         print("Tienes", vidas, "vidas")
#         numeroelegido = int(input("Introduce numero: "))
#     if numerorandom == numeroelegido : 
#         print("FELICIDADES GANASTE")

# import random

# def main():
#     numero_aleatorio = random.randint(1, 100)
#     numero_elegido = int(input('Elige un número del 1 al 100: '))
#     while numero_elegido != numero_aleatorio:
#         if numero_elegido < numero_aleatorio:
#             print('Busca un número más grande')
#         else:
#         numero_elegido = int(input('Elige un nuevo número: '))
#     print('¡Ganaste!')


# def main():

#     bienvenida = """
#     Bienvenido a "Adivina el número que tu compu esté pensando" :)
#     """

#     mayor = """
#     Intenta con un número más grande.

#     ¡Pero con cuidado! 

#     Solo te restan """

#     menor = """
#     Intenta con un número más pequeño.

#     ¡Pero con cuidado!

#     Solo te restan """

#     salto = """
    
#     """

#     mensaje_perdedor = """
#     Perdiste :(

#     Pero puedes volver a intentarlo...

#     ¡¡Seguro a la próxima lo lograrás!!
#     """

#     print(bienvenida)
#     numero_aleatorio = random.randint(1, 100)
#     vidas = int(input('Ingrese el número de vidas que quieres tener: '))
#     numero_elegido = int(input(salto + '¡Muy bien!' + salto + 'Ahora elige un número del 1 al 100: '))


#     while numero_elegido != numero_aleatorio:
#         vidas -= 1
#         if vidas == 0:
#             print(mensaje_perdedor)
#             break
#         if numero_elegido < numero_aleatorio:
#             print(mayor + str(vidas) + ' vidas' + salto)
#         else:
#             print(menor + str(vidas) + ' vidas' + salto)
#         numero_elegido = int(input('Elige un nuevo número: '))
#     if numero_elegido == numero_aleatorio:
#         print(salto + '¡Ganaste!')
    

# if __name__ == '__main__':
#     main()