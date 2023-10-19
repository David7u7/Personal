#PPT
#haremos un piedra papel o tijera
import random #con esto tomaremos las opciones de la compu


print("--------Bienvenido-------")
print(" -Estas son las opciones- ")
print("""Piedra
Papel
Tijera""")

#"declaracion de variables"
cconsola = 0
cjugador = 0
counter = 0
ganador = ""

while counter < 5: #maximo de partidas
    options = ("piedra", "papel", "tijera")
    pc = random.choice(options)  #eleccion de la pc
    jugador = input("-Elige una opcion:  ") #solicito la opcion del jugador
    jugador = jugador.lower() 

    
    if (jugador == "piedra" and pc == "papel") or (jugador == "papel" and pc == "tijera") or (jugador == "tijera" and pc == "piedra"):
        ganador = "consola"
        print("-La consola eligio: ", pc)
        cconsola += 1
    elif (jugador == "papel" and pc == "piedra") or (jugador == "tijera" and pc == "papel") or (jugador == "piedra" and pc == "tijera"):
        print("-La consola eligio: ", pc)
        ganador = "usuario"
        cjugador += 1
    elif (jugador == "papel" and pc == "papel") or (jugador == "tijera" and pc == "tijera") or (jugador == "piedra" and pc == "piedra"):
        print("-La consola eligio: ", pc)
    else:
        print("Ingresa una opcion valida")

#determinacion del ganador y mostrarlo en pantalla
    if ganador == "consola":
        print("------------Gana la consola-----------  ")
    elif ganador == "usuario":
        print("------------Gana el usuario-----------")
    else: 
        print("---------Es un Empate---------")


    #conteo de rondas y de marcador 
    print("El marcador es: ")
    print("Consola: ", str(cconsola), " <=> ", "Usuario:  ",  str(cjugador))
    counter += 1 
    print("++++++++++  Ronda: ", counter, "  +++++++++++")


#saliendo del bucle con esto se mostrara quien gano 
if cconsola > cjugador:
    print("FELICIDADES, ha ganado la consola")
elif cconsola == cjugador:
    print("----------Es un Empateeee---------")
else:
    print("FELICIDADES, ha ganado el usuario ")
