__author__ = 'rocka'
class Algoritmos_de_manejo_de_dienero:
    def __int__(self):
        object.__init__()

    def transferencia(self,jugador,agente):
        if(jugador.saldo > 200):
            jugador.saldo-=200
            agente.dinero_recaudado+=200

    def comision_de_agente(self,jugador,agente):
        jugador.saldo+=agente.dinero_recaudado
        agente.dinero_recaudado=0

