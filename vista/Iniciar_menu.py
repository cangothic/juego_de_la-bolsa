#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'rocka'
import sys
from command.controlador import *
from vista.menu.Menu import *
#procedimientos que deben invocarse por cada opción del menu
def comenzar_nuevo_juego():
    recibir_peticiones("comenzar")

def creditos():
    recibir_peticiones("creditos")

def salir_del_programa():
    sys.exit()
#fin de procedimientos

#codigo para mostrar el menu este hoja de texto importa menu
if __name__ == '__main__':
    #opciones y sus funciones a realizar
    opciones = [
        ("Jugar", comenzar_nuevo_juego),
        ("Creditos", creditos),
        ("Salir", salir_del_programa)
        ]

    pygame.font.init()
    screen = pygame.display.set_mode((320, 240))#crea una venta con 320 de ancho y 240 de alto
    fondo = pygame.image.load("imagenes/fondo.png").convert() #carga la imagen de fondo
    menu = Menu(opciones) #crea un objeto de la clase menu iniciandolo con las opciones

    while True:#ciclo para la ventana
        for evento in pygame.event.get():#buscar en una lista de eventos
            if evento.type == QUIT: #si hubo un evento quit cerrar la aplicación
                sys.exit(0)

        screen.blit(fondo, (0, 0)) #imprimir fondo
        menu.actualizar()  # actualizar menu
        menu.imprimir(screen) #imprimir menu en la ventana screen
        pygame.display.flip() # actualizar ventana
        pygame.time.delay(10)# retarda la actualizacion de la ventana