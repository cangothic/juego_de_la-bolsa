__author__ = 'rocka'
def pague_al_agente(jugador,agente):
    jugador.saldo-=200
    agente.dinero_recaudado+=200

def comision_de_agente(jugador,agente):
    jugador.saldo+=agente.dinero_recaudado
    agente.dinero_recaudado=0

def pague_al_banco(jugador,mercado):
    jugador.saldo-=500
    mercado.efectivo_disponible+=500



