
class Entidad:
    def __init__(self, name):
        self.name = name
        self.vida = 1

        self.armadura = 0
        self.escudo = 0
        self.voluntad = 0

        self.daño_ataque = 1


    def speak(self):
        print(f"Hola, soy {self.name}")

    def check_vida(self):
        print(f"La vida actual es {self.vida}")

    def check_armadura(self):
        print(f"La armadura actual es {self.armadura}")

    def check_escudo(self):
        print(f"El escudo actual es {self.escudo}")

    def check_voluntad(self):
        print(f"La voluntad actual es {self.voluntad}")

    def check_sobrevive(self):
        if self.vida <= 0:
            print(f"Game Over, {self.name} ha sido derrotado")
        else:
            print(f"Aún te quedan {self.vida} puntos de vida, sigue aguantando")

    def daño(self, daño, tipo):
        print(f"{self.name} ha recibido {daño} puntos de daño {tipo}")

        if tipo == "fisico":
            self.vida -= daño - self.armadura
        elif tipo == "energía":
            self.vida -= daño - self.escudo
        elif tipo == "psíquico":
            self.vida -= daño - self.voluntad
        else:
            print("Ese tipo de daño no está contemplado")

    def check_all(self):
        self.speak()
        self.check_vida()
        self.check_sobrevive()
        self.daño(1, "fisico")
        self.check_sobrevive()

    def atacar(self):
        return self.daño_ataque
