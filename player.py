# This file holds code to program the player of the game
#
#

from entity import Entidad

class Player(Entidad):

    def __init__(self, name, tipo):
        super().__init__(name)

        self.inventario = {
            "Objeto_1": 0,
            "Objeto_2": 4
        }

        self.nivel = 0
        self.experiencia = 0

        self.hold = 0
        self.anterior_criterio_subida = 10
        self.criterio_subida_nivel = 10


    def check_nivel(self):
        print(f"El nivel actual es {self.nivel}")

    def check_xp(self):
        print(f"La experiencia actual es {self.experiencia}")

    def check_inventario(self):
        if self.inventario == {}:
            print("El inventario está vacío :(")

        else:
            for objeto, cantidad in self.inventario.items():
                print(f"Tengo del objeto {objeto}, {cantidad} unidades")


    def gain_exp(self, exp):
        self.experiencia += exp
        if self.experiencia >= self.criterio_subida_nivel:
            self.lvl_up()

    def lvl_up(self):
        """
        Esta clase aumenta el nivel de nuestro personaje y además actualiza el criterio para el siguiente nivel
        :return:
        """
        self.nivel += 1

        self.hold = self.criterio_subida_nivel
        self.criterio_subida_nivel = self.criterio_subida_nivel + self.anterior_criterio_subida
        self.anterior_criterio_subida = self.hold



#print("Bienvenido a la Alfa de SpaceSurvive!!")
#print()

#name = input("Introduzca su nombre de jugador: ")

jugador = Player("Prueba")

jugador.speak()