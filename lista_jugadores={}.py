lista_jugadores={}
jugador=[]

def puntuaciones(puntajes,jugador):
    jugador = str (jugador).upper()

    if jugador in puntajes:  # Encontró al jugador
        puntajes[jugador] = puntajes[jugador]+1
    else:
        puntajes[jugador] = 1

    print(puntajes)