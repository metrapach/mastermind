#Patricia Alfaro Chaves. Mastermind. Proyecto Progra1. U Cenfotec#
#Hace cada funcion en solitario en el IDLE, para ir probando una a una#

import random

colores=("Negro", "Blanco", "Rojo", "Amarillo", "Azul", "Verde")
pista=["x", "o", "-"]
lista_jugadores={}
jugador=[]
rondas=0 
intentos=12 #puede jugar hasta 12 intentos
puntajes={} #ir sumando el top10

"""
*"x" color y posición: correcta.
* "o" color: correcto. Posición: incorrecta.
* "-" hay un elemento de la adivinanza que no esta en el código secreto. """

def instrucciones():
    print("Instrucciones:")
    print("Mastermind consiste en un juego de mesa de dos jugadores en el cual un jugador crea un código de 4 colores (codemaker) y")
    print("el otro jugador intenta adivinar este código (codebreaker) basado en pistas que el codemaker debe darle al code-breaker.")
    print("Indicaciones:")
    print("[x] color y posición: correcta.")
    print("[o] color: correcto. Posición: incorrecta.")
    print("[-] hay un elemento de la adivinanza que no esta en el código secreto.")

def agregar_jugador():     
        jugador=[]
        nombre = input("¡Hola, codebreaker! Dime tu nombre: ")                 
        lista_jugadores[nombre]=jugador

# def codigo_enigma(): generar de forma aleatoria una nueva lista CODEMAKER de 4 colores, basada en los 6 colores, 
# para luego compararla con la lista del jugador CODEBREAKER
def codigo_enigma(): 
    codemaker=[]
    for i in range (4):
        color = random.choice(colores)
        codemaker.append(color)
        print (codemaker)

#def jugar: muestra al jugar las 6 opciones, solicita el ingreso de 4 colores e imprime
def jugar():
    codebreaker=[]
    jugador=[]
    jugador = input("¡Hola, codebreaker! Dime tu nombre: ")        
    #lista_jugadores[nombre]=jugador

    print("Hey,", (jugador), ". Escoge una combinacion de 4 colores.")
    print("Opciones: negro, blanco, rojo, amarillo, azul y verde")
    color1= input("Color 1: ")                  
    codebreaker.append(color1)
    color2 = input("Color 2: ")   
    codebreaker.append(color2)
    color3= input("Color 3: ")            
    codebreaker.append(color3)
    color4= input("Color 4: ")            
    codebreaker.append(color4)
    print("¡Suerte! Tu combinación es: ", (codebreaker))

#def codemakerVRcodebreaker():

def puntuaciones(jugador):
    global puntajes

    jugador = str (jugador).upper()

    if puntajes:  # el diccionario tiene datos
        if jugador in puntajes:  # Encontró al jugador
            puntajes[jugador] = sum(puntajes.values(),1)
    else:
        puntajes[jugador] = 1

    print(puntajes)

isRunning = True 

while isRunning:
    print("\n")   
    print("-- MASTERMIND --")
    print("[1] Iniciar el juego")
    print("[2] Ver instrucciones del juego")                   # Print Menu
    print("[3] Ver las mejores 10 puntuaciones")
    print("[4] Borrar puntuaciones")
    print("[5] Créditos")
    print("[6] Salir")
    print("- - - - - -")
    print("\n")   

    opcion = input("Seleccione una opción del 1 al 6: ")       # Set "sel" to the output of input()

    if opcion == "1":
        jugar ()
        
    elif opcion == "2":
        instrucciones ()
    
    elif opcion == "3":
        print("Faltan datos para que corra la función")
    
    elif opcion == "4":
        print("Falta definir función")

    elif opcion == "5":
        print("Falta definir función")

    elif opcion == "6":
        isRunning = False

    else:
        print("Esa opcion no es válida")

