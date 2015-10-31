#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'rocka'
from mannanger.Imagen import * #importa algoritmo de carga
#dimenciones del dado
WIDTH=100
HEIGHT=100
#clase que genera un lado
class Dado(pygame.sprite.Sprite):
    def __init__(self,imagen_dado): #inicia el dado
        #logica de dado
        self.valor=random.randint(1,6)
        #logica de la imagen
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(imagen_dado,True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2

    def tirar_dado(self): #cambia el varor del dado un entero de 1 a 6
        self.valor=random.randint(1,6)
        return str(self.valor)

    def cambiar_cara(self,nuevaimagen): # cambiar inmagen del dado
        self.image = load_image(nuevaimagen, True)
