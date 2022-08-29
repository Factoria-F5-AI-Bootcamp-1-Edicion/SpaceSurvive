
from entity import Entidad

class Enemigo(Entidad):
    def __init__(self, name):
        super().__init__(name)
        self.experiencia_morir = 1


enemigo = Enemigo("Aberración")
enemigo.speak()