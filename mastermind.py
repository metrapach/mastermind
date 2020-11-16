#Patricia Alfaro Chaves. Mastermind. Proyecto Progra1. U Cenfotec
#Hice cada función en solitario en el IDLE, para ir probando de una a una

import random

colores=("Negro", "Blanco", "Rojo", "Amarillo", "Azul", "Verde") #tupla de colores
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
    print("\n")
    print("INSTRUCCIONES")
    print("Mastermind consiste en un juego de mesa de dos jugadores en el cual un jugador crea un código de 4 colores (codemaker) y")
    print("el otro jugador intenta adivinar este código (codebreaker) basado en pistas que el codemaker debe darle al code-breaker.")
    print("SIGNOS")
    print("[x] color y posición: correcta.")
    print("[o] color: correcto. Posición: incorrecta.")
    print("[-] hay un elemento de la adivinanza que no esta en el código secreto.")

""" def agregar_jugador():     
        jugador=[]
        nombre = input("¡Hola, codebreaker! Dime tu nombre: ")                 
        lista_jugadores[nombre]=jugador """

# def codigo_enigma(): generar de forma aleatoria una nueva lista CODEMAKER de 4 colores, basada en los 6 colores, 
# para luego compararla con la lista del jugador CODEBREAKER
def codigo_enigma(colores): 
    codemaker=[]
        for i in range (4):
            color = random.choice(colores)
            codemaker.append(color)
        return codemaker

#def jugar: muestra al jugador (CODEBREAKER) las 6 opciones, le solicita el ingreso de 4 colores e imprime su selección
def jugar():
    codebreaker=[]
    jugador=[]
    jugador = input("¡Hola, codebreaker! Dime tu nombre: ")        
    #lista_jugadores[nombre]=jugador

    print("\n")
    print("Hey,", (jugador), ". Escoge una combinación de 4 colores.")
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
    print("Profe: acá seguiría la parte del juego donde se empieza a comparar el código secreto.")

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
    print("[2] Instrucciones del juego")                   # imprimer el menú
    print("[3] Top 10 de codebreakers")
    print("[4] Borrar puntuaciones")
    print("[5] Créditos")
    print("[6] Salir")
    print("- - - - - -")
    print("\n")   

    opcion = input("Seleccione una opción del 1 al 6: ")       # Seleccion "opcion" conforme a la funcion o input asignado

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
        print("Esa opción no es válida")

