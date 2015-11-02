#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'rocka'
import random
import sys, pygame
import command
from pygame.locals import *
from dto.Jugador import *
from dto.Dado import *
from vista.herramientas_graficas.Cursor import *
from vista.herramientas_graficas.Boton import *
from dto.Agente_de_bolsa import *
from command.Generador_de_eventos import *

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
    #crear jugadores
    jugador1=Jugador("jugador1",10000,"imagenes/fichas/1.png")
    jugador2=Jugador("jugador2",10000,"imagenes/fichas/2.png")
    jugador3=Jugador("jugador3",10000,"imagenes/fichas/3.png")
    jugador4=Jugador("jugador4",10000,"imagenes/fichas/4.png")
    jugador5=Jugador("jugador5",10000,"imagenes/fichas/5.png")
    jugador6=Jugador("jugador6",10000,"imagenes/fichas/6.png")
    jugador7=Jugador("jugador7",10000,"imagenes/fichas/7.png")
    jugador8=Jugador("jugador8",10000,"imagenes/fichas/8.png")
    jugadores=[jugador1,jugador2,jugador3,jugador4,jugador5,jugador6,jugador7,jugador8]
    dado1=Dado("imagenes/dado/1.png") #crea un dado
    dado2=Dado("imagenes/dado/1.png") #crea un dado
    agente=Agente_de_bolsa(fuente)
    #tablero en un arreglo con la posicion de cada casilla
    tablero=[(880,350),(880,510),(880,650),(770,650),(670,650),(600,650),(500,650),(400,650),(310,650),(220,650),(90,650),(90,510),(90,350),(90,200),(90,90),(220,90),(310,90),(400,90),(500,90),(600,90),(670,90),(770,90),(880,90),(880,200)]
    #la variable turno es la que maneja que jugador esta en curso
    turno=0
    #se pinta el juego
    while True:
        for evento in pygame.event.get(): #buscar en una lista de eventos
            if evento.type==pygame.MOUSEBUTTONDOWN:
                if cursor.colliderect(boton.rect) and clic(0):
                    #se cambian la imagen de lo dados aleatoriamente conservando el valor en el cual callo
                    dado1.cambiar_cara("imagenes/dado/"+dado1.tirar_dado()+".png")
                    dado2.cambiar_cara("imagenes/dado/"+dado2.tirar_dado()+".png")
                    jugadores[turno].posicion=(jugadores[turno].posicion+dado1.valor+dado2.valor)%24
                    generar_query(jugadores[turno],agente) #genera una consulta e investiga que se puede hacer
                    if not ((dado1.valor == dado2.valor) or (dado1.valor == 5 and dado2.valor==6) or (dado1.valor == 6 and dado2.valor==5)):
                        turno=(turno+1)%8
            if evento.type == QUIT: #si hubo un evento quit cerrar la aplicación
                sys.exit(0)
        screen.blit(fondo, (0, 0)) #imprime el fondo sobre la pantalla
        screen.blit(dado1.image,(650,200)) #imprime el dado sobre la pantalla en la posición 650 200
        screen.blit(dado2.image,(720,200)) #imprime el dado sobre la pantalla en la posición 720 200
        #imprimir jugadores
        for jugando in jugadores:
            screen.blit(jugando.image,tablero[jugando.posicion])
        cursor.actualizar()
        boton.actualizar(screen,cursor) #actualiza la imagen del boton con la posicion del cursor
        agente.actualizar(screen,jugadores[turno].nombre)#imprime el monto del agente y la informacion del jugador en curso
        screen.blit(jugadores[turno].image,(602,377))#imprime la imagen del jugador en curso para que el sepa con que ficha esta jugando
        pygame.display.update()
        pygame.display.flip() # actualiza ventana
