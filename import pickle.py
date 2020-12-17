from io import open
import pickle

# Creamos una clase de prueba
class Persona:

    def __init__(self,nombre):
        self.jugador = jugador

    def __str__(self):
        return self.jugador

# Creamos la lista con los objetos
jugadores = ["Héctor","Mario","Marta", "Patri"]
lista_jugadores = []

for n in jugadores:
    p = Persona(n)
    lista_jugadores.append(p)

# Escribimos la lista en el fichero con pickle
import pickle
f = open('lista_jugadores.pckl','wb')
pickle.dump(lista_jugadores, f)
f.close()

# Leemos la lista del fichero con pickle
f = open('lista_jugadores.pckl','rb')
lista_jugadores = pickle.load(f)
f.close()

for p in lista_jugadores:
    print(p)