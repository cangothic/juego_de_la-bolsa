__author__ = 'rocka'
from vista.Interfas_de_juego import *
from vista.Configuracion_del_juego import *
#resibe peticiones y llama a lo que nesecite
def recibir_peticiones(peticion):
    if(peticion=="comenzar"):
        pregunta=Configuracion_deljuego()

    if(peticion=="juego"):
        iniciar_juego(0)