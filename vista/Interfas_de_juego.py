#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'rocka'
import time
import threading
import random
import sys, pygame
import command
from pygame.locals import *
from identitie.Jugador import *
from identitie.Dado import *
from vista.herramientas_graficas.Cursor import *
from vista.herramientas_graficas.Boton import *
from identitie.Agente_de_bolsa import *
from command.Generador_de_eventos import *
from identitie.Mercado_de_valores import *
from vista.Negociar import *
from vista.Vender import *
from vista.Score import *
global segundos
segundos=0
WIDTH = 1146
HEIGHT = 815
pygame.init()
fuente = pygame.font.Font('fuentes/dejavu.ttf', 20)
fuente2 = pygame.font.Font('fuentes/dejavu.ttf', 40)
sonido_dados=pygame.mixer.Sound('sonidos/dados.wav')
'''def crono():
    global segundos
    segundos=int(segundos)
    segundos+=1
    time.sleep(1)
    return crono()'''

def iniciar_juego(numero_jugadores,nombre_de_jugadores,minutos):#inicia la ventana del juego

    screen = pygame.display.set_mode((WIDTH, HEIGHT)) #crea una ventana con WIDTH pixeles de largo y HEIGHT de alto
    fondo = pygame.image.load("imagenes/tablero_de juego.png").convert() #carga la imagen de fondo
    pygame.display.set_caption("Juego Accion y bolsa") #le pone un nombre a la ventana
    mercado=Mercado_de_valores("imagenes/mercado_de_valores.png")
    cursor=Cursor()
    boton_lanzar_dado=Boton("imagenes/botones/lanzar.png","imagenes/botones/lanzar2.png")
    boton_cartera=Boton("imagenes/botones/cartera.png","imagenes/botones/cartera2.png")
    boton_mercado=Boton("imagenes/botones/mercado.png","imagenes/botones/mercado2.png")
    boton4=Boton("imagenes/botones/negocear.png","imagenes/botones/negocear2.png")
    boton5=Boton("imagenes/botones/vender.png","imagenes/botones/vender2.png")
    #crear jugadores
    jugadores=[]

    for i in range(numero_jugadores):
        jugadores.append(Jugador(nombre_de_jugadores[i],10000,"imagenes/fichas/"+str(i+1)+".png"))
    random.shuffle(jugadores)
    dado1=Dado("imagenes/dado/1.png") #crea un dado
    dado2=Dado("imagenes/dado/1.png") #crea un dado
    agente=Agente_de_bolsa(fuente)
    #tablero en un arreglo con la posicion de cada casilla
    tablero=[(880,350),(880,510),(880,650),(770,650),(670,650),(600,650),(500,650),(400,650),(310,650),(220,650),(90,650),(90,510),(90,350),(90,200),(90,90),(220,90),(310,90),(400,90),(500,90),(600,90),(670,90),(770,90),(880,90),(880,200)]
    #la variable turno es la que maneja que jugador esta en curso
    turno=0
    segundos=0
    '''hilo=threading.Thread(target=crono,args=())
    hilo.start()'''
    pygame.FULLSCREEN
    #se pinta el juego
    while True:
        for evento in pygame.event.get(): #buscar en una lista de eventos
            if evento.type==pygame.MOUSEBUTTONDOWN:
                if cursor.colliderect(boton_lanzar_dado.rect) and clic(0):
                    #se cambian la imagen de lo dados aleatoriamente conservando el valor en el cual callo
                    dado1.cambiar_cara("imagenes/dado/"+dado1.tirar_dado()+".png")
                    dado2.cambiar_cara("imagenes/dado/"+dado2.tirar_dado()+".png")
                    jugadores[turno].posicion=(jugadores[turno].posicion+dado1.valor+dado2.valor)%len(tablero)
                    screen.fill((255,35,1))
                    sonido_dados.play(0)
                    screen.blit(fondo, (0, 0)) #imprime el fondo sobre la pantalla
                    screen.blit(dado1.image,(650,200)) #imprime el dado sobre la pantalla en la posición 650 200
                    screen.blit(dado2.image,(720,200)) #imprime el dado sobre la pantalla en la posición 720 200
                    #imprimir jugadores
                    for jugando in jugadores:
                        screen.blit(jugando.image,tablero[jugando.posicion])
                    cursor.actualizar()
                    boton_lanzar_dado.actualizar(screen,cursor,(680,300)) #actualiza la imagen del boton con la posicion del cursor
                    boton_cartera.actualizar(screen,cursor,(1060,10))
                    boton_mercado.actualizar(screen,cursor,(1060,200))
                    boton4.actualizar(screen,cursor,(1060,390))
                    boton5.actualizar(screen,cursor,(1060,580))
                    agente.actualizar(screen,jugadores[turno])#imprime el monto del agente y la informacion del jugador en curso
                    screen.blit(jugadores[turno].image,(602,370))#imprime la imagen del jugador en curso para que el sepa con que ficha esta jugando
                    pygame.display.update()
                    pygame.display.flip() # actualiza ventana

                    generar_query(jugadores,turno,agente,mercado) #genera una consulta e investiga que se puede hacer
                    if not ((dado1.valor == dado2.valor) or (dado1.valor == 5 and dado2.valor==6) or (dado1.valor == 6 and dado2.valor==5)):
                        turno=(turno+1)%len(jugadores)
                if cursor.colliderect(boton_mercado.rect) and clic(0):
                    mercado.crear_ventana()
                if cursor.colliderect(boton_cartera.rect) and clic(0):
                    jugadores[turno].abrir_cartera("imagenes\cartera.png",mercado)
                if cursor.colliderect(boton4.rect) and clic(0):
                    negocearvista(jugadores,turno,mercado)
                if cursor.colliderect(boton5.rect) and clic(0):
                    vendervista(jugadores[turno],mercado,True)

            if evento.type == QUIT: #si hubo un evento quit cerrar la aplicación
                sys.exit(0)
        if segundos/60>minutos:
            calcula_score(jugadores,mercado)
            sys.exit()
        screen.fill((255,35,1))
        screen.blit(fondo, (0, 0)) #imprime el fondo sobre la pantalla
        screen.blit(dado1.image,(650,200)) #imprime el dado sobre la pantalla en la posición 650 200
        screen.blit(dado2.image,(720,200)) #imprime el dado sobre la pantalla en la posición 720 200
        segundos=int(pygame.time.get_ticks()/1000)
        cronometro=fuente2.render(str(int(segundos/3600)%12)+":"+str((int(segundos/60))%60)+":"+str(segundos%60),0,(0,0,0))
        screen.blit(cronometro,(450,527))
        #imprimir jugadores
        for jugando in jugadores:
            screen.blit(jugando.image,tablero[jugando.posicion])
        cursor.actualizar()
        boton_lanzar_dado.actualizar(screen,cursor,(680,300)) #actualiza la imagen del boton con la posicion del cursor
        boton_cartera.actualizar(screen,cursor,(1060,10))
        boton_mercado.actualizar(screen,cursor,(1060,200))
        boton4.actualizar(screen,cursor,(1060,390))
        boton5.actualizar(screen,cursor,(1060,580))
        agente.actualizar(screen,jugadores[turno])#imprime el monto del agente y la informacion del jugador en curso
        screen.blit(jugadores[turno].image,(602,370))#imprime la imagen del jugador en curso para que el sepa con que ficha esta jugando
        pygame.display.update()
        pygame.display.flip() # actualiza ventana
