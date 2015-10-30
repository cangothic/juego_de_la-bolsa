#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'rocka'
from vista.menu.Cursor import *
from vista.menu.Opcion import *
import sys
import pygame
from pygame.locals import  *
class Menu :
    #cambiar esta clase por bontones donde se haga clic

    def __init__(self, opciones): #crea el menu con sus opciones
        self.opciones = []
        fuente = pygame.font.Font('fuentes/dejavu.ttf', 20)# fuente de las opciones
        x = 105
        y = 105
        paridad = 1

        self.cursor = Cursor(x - 30, y, 30)

        for titulo, funcion in opciones:
            self.opciones.append(Opcion(fuente, titulo, x, y, paridad, funcion))
            y += 30
            if paridad == 1:
                paridad = -1
            else:
                paridad = 1

        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self):
        """Altera el valor de 'self.seleccionado' con los direccionales."""

        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:
                # Invoca a la funciÃ³n asociada a la opciÃ³n.
                self.opciones[self.seleccionado].activar()

        # procura que el cursor estÃ© entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1

        self.cursor.seleccionar(self.seleccionado)

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]

        self.cursor.actualizar()

        for o in self.opciones:
            o.actualizar()

    def imprimir(self, screen):
        """Imprime sobre 'screen' el texto de cada opciÃ³n del menÃº."""

        self.cursor.imprimir(screen)

        for opcion in self.opciones:
            opcion.imprimir(screen)