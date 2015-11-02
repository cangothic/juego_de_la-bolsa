__author__ = 'rocka'
from vista.Interfas_de_juego import *
from vista.Configuracion_del_juego import *
from  mannanger.Algoritmos_de_manejo_de_dinero import *
#recibe peticiones y llama a lo que nesecite
def recibir_peticiones(peticion):
    if(peticion=="comenzar"):
        pregunta=Configuracion_deljuego()
    if(peticion=="juego"):
        iniciar_juego(0)
def transferencia(jugador,agente):
    manejo=Algoritmos_de_manejo_de_dienero()
    manejo.transferencia(jugador,agente)

def comision_de_agente(jugador,agente):
    manejo=Algoritmos_de_manejo_de_dienero()
    manejo.comision_de_agente(jugador,agente)
