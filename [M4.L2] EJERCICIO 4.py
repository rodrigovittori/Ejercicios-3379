# [M4.L2] - Actividad #4: "Métodos de diccionario"
dicc_pelis = {"Clave" : "valor"} # Diccionario de PELIS

#dicc_pelis["Nombre original"] = "version de ñefliks"
dicc_pelis["Raya y el dragon"] = "Línea y el pejelagarto"
dicc_pelis["Cars"] = "Autitos"
dicc_pelis["Toy Story"] = "Juguetes Aventureros" # Las flipantes aventuras de Woody y sus amigos
dicc_pelis["Sonic"] = "Sonoro: el prisas"
dicc_pelis["Mario Bros"] = "El plomero y sus setas mágicas"
dicc_pelis["Digimon"] = "Criaturas Virtuales"
dicc_pelis["Pokemon"] = "Bestias de Bolsillo"
dicc_pelis["Star Wars"] = "Adultos traumados pelean con peligrosos sables luminosos"
dicc_pelis["Spiderman"] = "El hombre que araña"

del dicc_pelis["Clave"] # Eliminar valor

print("DICCIONARIO COMPLETO: ", dicc_pelis)

print("\n CLAVES DEL DICCIONARIO: ", dicc_pelis.keys())
print("\n VALORES DEL DICCIONARIO: ", dicc_pelis.values())

# Buscar valor
peli_a_buscar = "Pokemon"
if peli_a_buscar in dicc_pelis:
    print("\n La peli ", peli_a_buscar, " SI ESTÁ en nuestra colección, pero se encuentra registrada como: ", dicc_pelis[peli_a_buscar] )
else:
    print("\n La peli ", peli_a_buscar, " NO ESTÁ en nuestra colección" )

dicc_pelis.clear() # Vaciar un diccionario

print("\n Diccionario (despues del clear): \n", dicc_pelis)