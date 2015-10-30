__author__ = 'rocka'
import random


class Empresa():
    def __init__(self, nombre, sector, limite_inferior, limite_superior, x, y):
        self.x = x
        self.y = y
        self.nombre = nombre
        self.sector = sector
        self.inferior = limite_inferior
        self.cambio_de_mercado(self)
        self.titulos_disponibles = 7

    def vender_acción(self, usuario):
        pass

    def quiebra(self):#calcula si una empresa se quiebra o no
        aleatorio = random.random()
        if (aleatorio <= 1 / 16):
            return True
        else:
            return False

    def cambio_de_mercado(self):# cambia aleatoriamente el mercado de la ermpresa
        if (self.quiebra):
            self.valor_mercado = int(self.limite_inferior * random.uniform(0.3, 0.6))
        else:
            cantidad = (self.limite_superior - self.limite_inferior) / 50
            veces50 = random.randint(0, cantidad)
            self.valor_mercado = self.limite_inferior + veces50 * 50
