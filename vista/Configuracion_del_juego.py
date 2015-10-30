#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'rocka'
from tkinter import *
from vista.Interfas_de_juego import *
class Configuracion_deljuego():#esta clase es para configurar el inicicio del juego para esta ventana se aplica la libreria tkinter que viene incluida con python
    def obtener_texbox(self):#obtiene el texto digitado en el recuadro
        print(self.numero_de_jugadores.get())

    def __init__(self):#inicia la ventana
        self.ventana=Tk()
        self.ventana.geometry("300x300")
        self.etiqueta_numero_de_jugadores = Label(self.ventana, text="digite el numero de personas que quieren jugar", fg="cyan", bg="blue")#dibuja un label
        self.etiqueta_numero_de_jugadores.pack() #posiciona el label
        self.numero_de_jugadores = Entry(self.ventana) #crea un cuadro de texto
        self.numero_de_jugadores.pack() #posiciona el cuadro de texto
        self.boton_enviar=Button(self.ventana,text="enviar",width=10, command=self.obtener_texbox)#crea un boton
        self.boton_enviar.pack()#posiciona el boton
        self.ventana.mainloop()# actualiza la ventana

