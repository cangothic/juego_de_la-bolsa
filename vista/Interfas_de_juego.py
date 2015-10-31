#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'rocka'
import random
import sys, pygame
from pygame.locals import *
from dto.Usuario import *
from dto.Dado import *
from vista.herramientas_graficas.Cursor import *
from vista.herramientas_graficas.Boton import *
from dto.Agente_de_bolsa import *
from dto.Tablero import *
WIDTH = 1146
HEIGHT = 815
pygame.init()
fuente = pygame.font.Font('fuentes/dejavu.ttf', 20)
def iniciar_juego(numero_jugadores):#inicia la ventana del juego
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) #crea una ventana con WIDTH pixeles de largo y HEIGHT de alto
    fondo = pygame.image.load("imagenes/tablero_de juego.png").convert() #carga la imagen de fondo
    pygame.display.set_caption("Juego Accion y bolsa") #le pone un nombre a la ventana
    ficha=random.randint(1,8)#prueba para tener una ficha aleatoria cambiar luego
    cursor=Cursor()
    boton=Boton("imagenes/botones/azul.png","imagenes/botones/azul2.png")
    jugador1=Usuario("carlos",10000,"imagenes/fichas/"+str(ficha)+".png") #crea un jugador
    dado1=Dado("imagenes/dado/1.png") #crea un dado
    dado2=Dado("imagenes/dado/1.png") #crea un dado
    agente=Agente_de_bolsa(fuente)
    tablero=[(880,350),(880,510),(880,650),(770,650),(670,650),(600,650),(500,650),(400,650),(310,650),(220,650),(90,650),(90,510),(90,350),(90,200),(90,90),(220,90),(310,90),(400,90),(500,90),(600,90),(670,90),(770,90),(880,90),(880,200)]
    posicion=0


    while True:
        for evento in pygame.event.get(): #buscar en una lista de eventos
            if evento.type==pygame.MOUSEBUTTONDOWN:
                if cursor.colliderect(boton.rect) and clic(0):
                    dado1.cambiar_cara("imagenes/dado/"+dado1.tirar_dado()+".png")
                    dado2.cambiar_cara("imagenes/dado/"+dado2.tirar_dado()+".png")
                    posicion+=dado1.valor+dado2.valor
            if evento.type == QUIT: #si hubo un evento quit cerrar la aplicación
                sys.exit(0)
        screen.blit(fondo, (0, 0)) #imprime el fondo sobre la pantalla
        screen.blit(dado1.image,(650,200)) #imprime el dado sobre la pantalla en la posición 650 200
        screen.blit(dado2.image,(720,200)) #imprime el dado sobre la pantalla en la posición 720 200}
        screen.blit(jugador1.image,tablero[posicion%24])#imprime jugador
        cursor.actualizar()
        boton.actualizar(screen,cursor)
        agente.actualizar(screen)
        pygame.display.update()
        pygame.display.flip() # actualiza ventana
