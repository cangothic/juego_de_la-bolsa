__author__ = 'brian y carlos'
import random
import command
def evento(jugador,agente,query):
    funciones = {"001":command.controlador.transferencia,
                 "002":command.controlador.comision_de_agente}

    acciones = [{"posicion":6,"id":"001"},
                {"posicion":18,"id":"002"},
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
        funciones[better["id"]](jugador,agente)

def esValida(reglasEvento,query):
    for regla in reglasEvento:
        if((regla!="id") and (regla not in query or reglasEvento[regla]!= query[regla])):
            return False
    return True

def generar_query(jugador,agente):
    query={"posicion":jugador.posicion}
    evento(jugador,agente,query)