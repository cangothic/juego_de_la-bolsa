__author__ = 'brian y carlos'
import random

from vista.Vista_de_compras import *
from mannanger.Algoritmos_de_manejo_de_dinero import *


def evento(jugadores,turno,agente,mercado,query):
    jugador=jugadores[turno]
    funciones = {"001":lambda:pague_al_agente(jugador,agente),
                 "002":lambda:comision_de_agente(jugador,agente),
                 "003":lambda:mercado.cambio_de_mercado(jugadores),
                 "004":lambda:comprar_titulos(jugador,mercado,False),
                 "005":lambda:comprar_titulos(jugador,mercado,True),
                 "006":lambda:pague_al_banco(jugador,mercado),
                 "007":lambda:jugadores.remove(jugador),
                 "008":lambda:jugadores.remove(jugador)}

    acciones = [{"posicion":6,"menor 200":False,"id":"001"},
                {"posicion":18,"id":"002"},
                {"posicion":2,"id":"003"},
                {"posicion":10,"id":"003"},
                {"posicion":14,"id":"003"},
                {"posicion":22,"id":"003"},
                {"es empresa":True,"esta quebrada":False,"id":"004"},
                {"es empresa":True,"esta quebrada":True,"id":"005"},
                {"posicion":12,"menor 500":False,"id":"006"},
                {"posicion":12,"menor 500":True,"id":"007"},
                {"posicion":6,"menor 200":True,"id":"008"}
                ]
    validos = []
    tamano = 0
    for event in acciones:
        if(esValida(event,query) and len(event)>tamano):
            validos.append(event)
    if len(validos)>0:
        tamano = len(validos[0])
        mejor_regla = validos[0]
        for event in validos:
            if len(event)>tamano:
                tamano = len(event)
                mejor_regla = event
            if len(event)==tamano:
                if(random.randint(0,2)==1):
                    mejor_regla = event
        funciones[mejor_regla["id"]]()


def esValida(reglasEvento,query):
    for regla in reglasEvento:
        if((regla!="id") and (regla not in query or reglasEvento[regla]!= query[regla])):
            return False
    return True

def generar_query(jugadores,turno,agente,mercado):
    jugador=jugadores[turno]
    query={"posicion":jugador.posicion,
           "menor 200":jugador.saldo<200,
           "es empresa":(jugador.posicion==1) or
                        (jugador.posicion >=3 and jugador.posicion <=5) or
                        (jugador.posicion >=7 and jugador.posicion <=9) or
                        (jugador.posicion==11) or
                        (jugador.posicion==13) or
                        (jugador.posicion >=15 and jugador.posicion <=17) or
                        (jugador.posicion >=19 and jugador.posicion <=21) or
                        (jugador.posicion==23),
           "menor 500":jugador.saldo<500
           }
    if(jugador.posicion==1) or (jugador.posicion >=3 and jugador.posicion <=5) or (jugador.posicion >=7 and jugador.posicion <=9) or (jugador.posicion==11) or (jugador.posicion==13) or (jugador.posicion >=15 and jugador.posicion <=17) or (jugador.posicion >=19 and jugador.posicion <=21) or (jugador.posicion==23):
        query["esta quebrada"]=mercado.empresas[str(jugador.posicion)].quebrada
    evento(jugadores,turno,agente,mercado,query)