__author__ = 'rocka'
import pygame
from pygame.locals import *
from mannanger.Imagen import *
class Agente_de_bolsa:
    def __init__(self,fuente):
        self.fuente=fuente
        self.dinero_recaudado=0
        pygame.sprite.Sprite.__init__(self)
        self.image = self.fuente.render("Dinero recaudado: ", 1, (0, 0, 0))
        self.image2 = fuente.render(str(self.dinero_recaudado), 1, (0, 0, 0))
        self.rect = (402,327)

    def actualizar(self,pantalla,jugador):
        self.image2 = self.fuente.render(str(self.dinero_recaudado), 1, (0, 0, 0))
        self.jugador=self.fuente.render(jugador.nombre+" posicion: "+str(jugador.posicion), 1, (0, 0, 0))
        pantalla.blit(self.image,(402,327))
        pantalla.blit(self.image2,(402,377))
        pantalla.blit(self.jugador,(402,427))