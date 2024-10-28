# [M4.L2] - Actividad #3: "Gestor de contraseñas"
# no uses este programa para almacenar contraseñas reales

# Paso Nº 1: Crear un diccionario vacío con un nombre adecuado
diccionario_wifis = {}

print("Cargamos UNA RED")

# Paso Nº 2:  pedir el nombre de un recurso/red
nueva_clave = input("Ingrese el nombre del Wi-Fi: ")
# Nota: Las claves son los registros que vamos a buscar

nuevo_valor = input("Ingrese la contraseña: ")
# Nota: Los valores son los datos que almacenamos/vinculamos a cada Clave
#       Son los que queremos que nuestro diccionario nos devuelva

# Paso Nº 4: Añade una entrada a tu diccionario
#           (utilizando el nombre del recurso como clave
#            y almacenando la contraseña como valor)

diccionario_wifis[nueva_clave] = nuevo_valor

# Paso Nº 5: Crear un sistema que permita al usuario añadir múltiples entradas.
# Pista: para lograr esta tarea, necesitarás usar bucles.

# Nota: Como NO sabemos cuántas redes wifi quiere registrar el usuario, usaremos
#       un bucle while

print("\n Entramos a un bucle de carga")

# Paso 5.1) Crear una variable de control para nuestro bucle
seguimos_cargando = True

# Paso 5.2) Escribimos el bucle de carga
while(seguimos_cargando):
    nueva_clave = input("Ingrese el nombre del Wi-Fi: ")
    nuevo_valor = input("Ingrese la contraseña: ")
    # Paso 5.3) Mostramos la clave y la cargamos a nuestro diccionario
    print("Se registró la red \"", nueva_clave, "\" con la contraseña: ", nuevo_valor)
    diccionario_wifis[nueva_clave] = nuevo_valor

    # Paso 5.4) Preguntar al usuario si desea seguir cargando redes:
    temp = input("Seguir cargando? (s/n):")
    if ('n' in temp or 'N' in temp):
        seguimos_cargando = False
        break

### FIN DEL BUCLE ###

# Paso Nº 6: Mostramos el resultado final:
print("Lista de redes: ", diccionario_wifis.keys())

# Paso Nº 7) Preguntamos de qué red se quiere obtener la contraseña:

print("\n La clave es: ", diccionario_wifis[input("Ingrese la red a buscar: ")])

# *********************************************************************************

"""
OTROS EJEMPLOS:
Juego de adivinanzas:
dicc_adivinanzas = {"¿Cuál es el animal más antiguo?" : "La cebra, ¡Porque está en blanco y negro!"}

¿Qué hace una abeja en el gimnasio? ¡Zum-ba!
¿Qué le dice un jardinero a otro? ¡Eres un rastrero!
¿Cuál es el colmo de un electricista? ¡No ser muy brillante!
¿Por qué los pájaros no usan Facebook? ¡Porque ya tienen Twitter!
¿Cómo se llama el campeón de buceo japonés? ¡Tokofondo!

"""