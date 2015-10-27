#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'rocka'

import sys, pygame
from pygame.locals import *

WIDTH = 1046
HEIGHT = 815

def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except (pygame.error):
                raise (SystemExit)
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image

def iniciar_juego():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    fondo = pygame.image.load("imagenes/tablero_de juego.png").convert()
    pygame.display.set_caption("Juego Accion y bolsa")
    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        screen.blit(fondo, (0, 0))
        pygame.display.flip()
    return 0