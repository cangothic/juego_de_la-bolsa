__author__ = 'rocka'
def transferencia(jugador,agente):
    if(jugador.saldo > 200):
        jugador.saldo-=200
        agente.dinero_recaudado+=200

def comision_de_agente(jugador,agente):
    jugador.saldo+=agente.dinero_recaudado
    agente.dinero_recaudado=0

