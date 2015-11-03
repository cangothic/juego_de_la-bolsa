__author__ = 'brian y carlos'
import random
from mannanger.Algoritmos_de_manejo_de_dinero import *
def cambio_de_pizarra():
    print("cambio la pizarra")
def evento(jugador,agente,mercado,query):
    funciones = {"001":transferencia,
                 "002":comision_de_agente,
                 "003":cambio_de_pizarra}

    acciones = [{"posicion":6,"id":"001"},
                {"posicion":18,"id":"002"},
                {"posicion":2,"id":"003"},
                {"posicion":10,"id":"003"},
                {"posicion":14,"id":"003"},
                {"posicion":22,"id":"003"},
                ]
    validos = []
    tamano = 0
    for event in acciones:
        if(esValida(event,query) and len(event)>tamano):
            validos.append(event)
    if len(validos)>0:
        tamano = len(validos[0])
        better = validos[0]
        for event in validos:
            if len(event)>tamano:
                tamano = len(event)
                better = event
            if len(event)==tamano:
                if(random.randint(0,2)==1):
                    better = event
        if jugador.posicion == 6 or jugador.posicion==18:
            funciones[better["id"]](jugador,agente)
        if jugador.posicion == 2 or jugador.posicion==10 or jugador.posicion == 14 or jugador.posicion== 22:
            funciones[better["id"]]()

def esValida(reglasEvento,query):
    for regla in reglasEvento:
        if((regla!="id") and (regla not in query or reglasEvento[regla]!= query[regla])):
            return False
    return True

def generar_query(jugador,agente,mercado):
    query={"posicion":jugador.posicion}
    evento(jugador,agente,mercado,query)