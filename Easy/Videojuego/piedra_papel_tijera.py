import random

is_game = True

defconversacion(mensaje):
  if mensaje == 'piedra':
    return1
  elif mensaje == 'papel':
    return2
  elif mensaje == 'tijera':
    return3
  else:
    return0

defquien_gano(oponente, ususario):
  if oponente == 1and usuario == 2:
    return'YASSSSS GANASTEEEEE 🎉🎉'
  elif oponente == 2and usuario == 1:
    return'NOOOO PANAAAA PERDISTEEEE'
  elif oponente == 1and usuario == 3:
    return'NOOOO PANAAAA PERDISTEEEE'
  elif oponente == 3and usuario == 1:
    return'YASSSSS GANASTEEEEE 🎉🎉'
  elif oponente == 2and usuario == 3:
    return'YASSSSS GANASTEEEEE 🎉🎉'
  elif oponente == 3and usuario == 1:
    return'NOOOO PANAAAA PERDISTEEEE'
  elif oponente == usuario:
    return'lol fue un empate equisde'
  elif oponente == 0or usuario == 0:
    return'Error watafak ???????'
  else:
    return'Error???????'

defseguir_jugando(respuesta):
  if respuesta == 'si':
    returnTrue
  else:
    returnFalse


bienvenida = """ 
B I E N V E N I D O S

            T O D O S . . . 


    AQUÍ SE DESAFÍA...

                  AQUÍ HAY SANGRE...

        LA MUERTE ES INEVITABLE...


      ESTÁS PREPARADO ?

                ENTONCES...


          B I E N V E N I D O... 
                  A . . . 

██████╗ ██╗███████╗██████╗ ██████╗  █████╗ 
██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔══██╗
██████╔╝██║█████╗  ██║  ██║██████╔╝███████║
██╔═══╝ ██║██╔══╝  ██║  ██║██╔══██╗██╔══██║
██║     ██║███████╗██████╔╝██║  ██║██║  ██║
╚═╝     ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝

  ██████╗  █████╗ ██████╗ ███████╗██╗     
  ██╔══██╗██╔══██╗██╔══██╗██╔════╝██║     
  ██████╔╝███████║██████╔╝█████╗  ██║     
  ██╔═══╝ ██╔══██║██╔═══╝ ██╔══╝  ██║     
  ██║     ██║  ██║██║     ███████╗███████╗
  ╚═╝     ╚═╝  ╚═╝╚═╝     ╚══════╝╚══════╝

                   ██████╗ 
                  ██╔═══██╗
                  ██║   ██║
                  ██║   ██║
                  ╚██████╔╝

████████╗██╗     ██╗███████╗██████╗  █████╗ 
╚══██╔══╝██║     ██║██╔════╝██╔══██╗██╔══██╗
   ██║   ██║     ██║█████╗  ██████╔╝███████║
   ██║   ██║██   ██║██╔══╝  ██╔══██╗██╔══██║
   ██║   ██║╚█████╔╝███████╗██║  ██║██║  ██║
   ╚═╝   ╚═╝ ╚════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
________________________________________________

            -= PRESIONE START =-

"""

print(bienvenida)

while is_game:
  oponente = random.randint(1,3)
  usuario = conversacion(input('Piedra, papel o tije...'))

  print(quien_gano(oponente, usuario))
  is_game = seguir_jugando(input('Quieres seguir jugando? '))  