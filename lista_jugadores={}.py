jugador=[] #llave
puntajes={"Leo":1, "Patri":2}
#valor

def agregar_jugador():     
        #jugador=[]
        nombre = input("¡Hola, codebreaker! Dime tu nombre: ")                 
        
        if nombre in puntajes:  # Encontró al jugador
            print ("Jugador existe")
        else:
            puntajes[nombre]=0
        print (puntajes)
        
        return nombre
        #verificar si nombre de jugador existe
        #return jugador

def puntuaciones(nombre):
    if nombre in puntajes:  # Encontró al jugador
        puntajes[nombre] = puntajes[nombre]+1
    else:
        puntajes[nombre] = 1
    print("La lista de puntajes actual es", (puntajes))

nombre_jugador = agregar_jugador()
puntuaciones(nombre_jugador)