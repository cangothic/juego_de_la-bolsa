__author__ = 'rocka'
import random
def calcular_porcentage(numero,inferior,superior):
    valor = int(numero * random.uniform(inferior,superior))
    mayor=numero*superior
    if(valor%50!=0):
        valor=valor+50-(valor%50)
        if(valor>mayor):
            valor-=50
    return valor