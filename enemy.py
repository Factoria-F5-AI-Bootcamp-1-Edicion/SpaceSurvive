class Enemigo:
    def __init__(self, nombre):

        self.nombre = nombre

        self.vida = 0
        self.armadura = 0
        self.daño_ataque = 1

        self.experiencia_morir = 1


    def atacar(self):
        pass

    def defenderse(self):
        pass

    def huir(self):
        pass

    def morir(self):
        pass