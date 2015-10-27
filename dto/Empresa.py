__author__ = 'rocka'
import random
class Empresa():
    def __init__(self,nombre,sector,limite_inferior,limite_superior):
        self.nombre=nombre
        self.sector=sector
        self.inferior=limite_inferior
        self.superior=limite_superior
        self.valor_mercado=random.randomint(limite_inferior,limite_superior)
        self.titulos_disponibles=7

    def vender_acción(self,usuario):
        pass

    def quiebra(self):
        aleatorio=random.random()
        if(aleatorio <= 0.5):
            return True
        else:
            return False

    def cambio_de_mercado(self):
         if(self.quiebra):
             self.valor_mercado=self.limite_inferior*random.uniform(0.3,0.6)
         else:
             self.valor_mercado=random.randomint(self.limite_inferior,self.limite_superior)