# [M4.L2] - Actividad #6: "Duelo"
import random
import time

# Paso Nº 1) Crear nuestros personajes

# Estructura: personaje = { "Nombre": str(), "Vida": int, "Ataque": int() }

personaje1 = {"Nombre": "Iron Man"   , "Vida" : 20, "Ataque" : 10}
personaje2 = {"Nombre": "Hulk"       , "Vida" : 20, "Ataque" : 10}

ronda_actual = 1

while(not ((personaje1["Vida"] <= 0) or (personaje2["Vida"] <= 0))): # Mientras ninguno de los dos tenga su salud en 0 o negativo
    # DUELO
    print("\n ############################### \n \n RONDA # ", ronda_actual)
    
    personaje1["Ataque"] = random.randint(0,12)
    personaje2["Ataque"] = random.randint(0,12)
    
    # P1 ATK P2
    print(personaje1["Nombre"], " ataca a ", personaje2["Nombre"])
    personaje2["Vida"] -= personaje1["Ataque"] # Restamos vida al J2 segun el atk del J1
    print(personaje1["Nombre"], "ha hecho ", personaje1["Ataque"], "puntos de daño")
    time.sleep(2)
    
    # P2 ATK P1
    print(personaje2["Nombre"], " ataca a ", personaje1["Nombre"])
    personaje1["Vida"] -= personaje2["Ataque"] # Restamos vida al J1 segun el atk del J2
    print(personaje2["Nombre"], "ha hecho ", personaje2["Ataque"], "puntos de daño")
    time.sleep(2)
    
    print("\n ############################### \n")
    print("FIN DE RONDA # ", ronda_actual, ":", personaje1['Nombre'], ":", personaje1['Vida'], '| ', personaje2['Nombre'], ":", personaje2['Vida'])
    ronda_actual += 1

##################################
# Si estoy acá, la pelea terminó #
##################################

ganador = ""

if (personaje1["Vida"] <= 0 and personaje2["Vida"] <= 0):
    # Ambos murieron
    print("Ambos caen al suelo, ¡Ha sido un empate!")

else:
    if (personaje1["Vida"] > 0):
        ganador = personaje1["Nombre"]
    else:
        ganador = personaje2["Nombre"]

    print("\n \n ¡", ganador, "ha ganado el duelo!"