# This file holds code to program the player of the game
#
#

class Player:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"Hola, me llamo {self.name}")



print("Bienvenido a la Alfa de SpaceSurvive!!")
print()

name = input("Introduzca su nombre de jugador: ")

jugador = Player(name)

jugador.speak()