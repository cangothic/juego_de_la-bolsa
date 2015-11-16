#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'rocka'
import pygame,sys
from mannanger.Imagen import *
from tkinter import *

WIDTH=225
HEIGHT=250
# clase principal de jugadores del juego
class Jugador(pygame.sprite.Sprite):
    def __init__(self,nombre,saldo,imagen):
        #logica de jugador
        self.nombre = nombre
        self.posicion=0
        self.saldo = saldo
        self.titulos = {"1":0,"3":0,"4":0,"5":0,"13":0,"15":0,"16":0,"17":0,"7":0,"8":0,"9":0,"11":0,"19":0,"20":0,"21":0,"23":0}
        #logica de la ficha
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(imagen, True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2

    def abrir_cartera(self,pintura,mercado):
        self.pintura=pintura
        self.ventana=Tk()
        self.ventana.resizable(0,0)
        self.ventana.geometry("778x713+0+0")
        self.ventana.title("cartera")
        self.imagen=PhotoImage(file=self.pintura)
        self.label=Label(self.ventana,image=self.imagen)
        self.label.place(x=0,y=0)
        self.etiqueta_nombre= Label(self.ventana, text=self.nombre,font=30)
        self.etiqueta_nombre.place(x=350,y=0)
        self.etiqueta_saldo = Label(self.ventana, text=str(self.saldo),font=30)
        self.etiqueta_saldo.place(x=370,y=170)
        i=80
        for titulo,cantidad in self.titulos.items():
            Label(self.ventana, text=mercado.empresas[titulo].nombre+": "+str(cantidad),font=("",7)).place(x=500,y=i)
            i+=20

        self.ventana.mainloop()


