#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'rocka'
import pygame,sys
from mannanger.Imagen import *

WIDTH=225
HEIGHT=250
# clase principal de jugadores del juego
class Jugador(pygame.sprite.Sprite):
    def __init__(self,nombre,saldo,imagen):
        #logica de jugador
        self.nombre = nombre
        self.posicion=0
        self.saldo = saldo
        self.titulos = {}
        #logica de la ficha
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(imagen, True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2

    def abrir_cartera(self):
        pass


