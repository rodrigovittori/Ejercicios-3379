# [M4.L2] - Actividad #5: "Guía telefónica" -> "Catálogo de ñiefilms"
dicc_pelis = {"Clave" : "valor"} # Diccionario de PELIS

#dicc_pelis["Nombre original"]    = "version de ñefliks"
dicc_pelis["Raya y el dragón"]    = "Línea y el pejelagarto"
dicc_pelis["Rápido y Furioso"]    = "Veloz y molesto"
dicc_pelis["Cars"]                = "Autitos"
dicc_pelis["Toy Story"]           = "Juguetes Aventureros" # Las flipantes aventuras de Woody y sus amigos
dicc_pelis["Sonic"]               = "Sonoro: el prisas"
dicc_pelis["Mario Bros"]          = "El plomero y sus setas mágicas"
dicc_pelis["Joker"]               = "El jajas"
dicc_pelis["Digimon"]             = "Criaturas Virtuales"
dicc_pelis["Pokemon"]             = "Bestias de Bolsillo"
dicc_pelis["Star Wars"]           = "Adultos traumados pelean con peligrosos sables luminosos" 
dicc_pelis["Spiderman"]           = "El hombre que araña"

dicc_pelis["Minecraft"]           = "Creando con Cubitos"
dicc_pelis["Paddington"]          = "Osito viajero"
dicc_pelis["Barbie: Princesas"]   = "Juliana: Princesas"
dicc_pelis["Mi Villano Favorito"] = "Simples Secuaces Simpáticos"
dicc_pelis["Madagascar"] = "Locos Animales Prófugos"
dicc_pelis["Yu-Gi-Oh"] = "El adolescente tartamudo y sus dioses egipcios"
dicc_pelis["Dragon Ball"] = "Huerfanito con cola buscando las ..."

del dicc_pelis["Clave"]

letra = input('Indique la letra inicial de la peli que busca:') 
letra = letra[0]

print("Búsqueda con nombres originales:")

# Para [clave] en las claves de [diccionario], hacer:
for clave in dicc_pelis.keys():
    if clave[0] == letra:
        #print(clave, ":", dicc_pelis[clave])
        print(clave)

print("\n \n Búsqueda con nombre de Ñefliks:")
        
for valor in dicc_pelis.values():
    if valor[0] == letra:
        print(valor)