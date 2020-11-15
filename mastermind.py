#Patricia Alfaro Chaves. Mastermind. Proyecto Progra1. U Cenfotec#

import random

colores=("Negro", "Blanco", "Rojo", "Amarillo", "Azul", "Verde")
pista=["x", "o", "-"]
lista_jugadores={}
jugador=[]

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

#generar de forma aleatoria una nueva lista CODEMAKER de 4 colores, basada en los 6 colores, 
# para luego compararla con la lista del jugador CODEBREAKER
def codigo_enigma(): 
    codemaker=[]
    for i in range (4):
        color = random.choice(colores)
        codemaker.append(color)
        print (codemaker)

def jugar():
    codebreaker=[]
    print("Escoge una combinacion de 4 colores.")
    print("Opciones: negro, blanco, rojo, amarillo, azul y verde")
    color1= input("Color 1: ")                  
    codebreaker.append(color1)
    color2 = input("Color 2: ")   
    codebreaker.append(color2)
    color3= input("Color 3: ")            
    codebreaker.append(color3)
    color4= input("Color 4: ")            
    codebreaker.append(color4)
    print("Tu combinación es: ", (codebreaker))

def codemakerVRcodebreaker():
    


isRunning = True 

while isRunning:
    print("\n")   
    print("-- MASTERMIND --")
    print("[1] Iniciar el juego")
    print("[2] Ver instrucciones del juego")                   # Print Menu
    print("[3] Ver las mejores 10 puntuaciones")
    print("[4] Borrar puntuaciones")
    print("[5] Creditos")
    print("[6] Salir")
    print("- - - - - -")
    print("\n")   

    opcion = input("Seleccione una opción del 1 al 6: ")       # Set "sel" to the output of input()

    if opcion == "1":
        jugar ()
        
    elif opcion == "2":
        instrucciones ()
    
    elif opcion == "3":
        print("Gracias por jugar!")
        break

    else:
        print("Esa opcion no es válida")

