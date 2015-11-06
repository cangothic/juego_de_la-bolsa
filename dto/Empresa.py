__author__ = 'rocka'
import random

class Empresa():
    def __init__(self, nombre,limite_inferior, limite_superior):
        self.nombre = nombre
        self.limite_inferior = limite_inferior
        self.limite_superior= limite_superior
        self.cambio_de_mercado()
        self.titulos_disponibles = 7

    def quiebra(self):#calcula si una empresa se quiebra o no
        aleatorio = random.random()
        if (aleatorio <= 1 / 16):
            return True
        else:
            return False

    def cambio_de_mercado(self):# cambia aleatoriamente el mercado de la ermpresa
        self.quebrado=self.quiebra()
        if (self.quebrado): #calcula el precio de la empresa quebrada de 50 en 50
            valor = int(self.limite_inferior * random.uniform(0.3, 0.6))
            sesenta=self.limite_inferior*0.6
            if(valor%50!=0):
                valor=valor+50-(valor%50)
                if(valor>sesenta):
                    valor-=50
            self.valor_mercado=valor
        else:
            cantidad = (self.limite_superior - self.limite_inferior) / 50
            veces50 = random.randint(0, cantidad)
            self.valor_mercado = self.limite_inferior + veces50 * 50
