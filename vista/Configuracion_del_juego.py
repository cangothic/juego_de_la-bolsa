#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'rocka'
from tkinter import *
from vista.Interfas_de_juego import *
from mannanger.Algoritmos_para_validaciones import *
def validar_palabra_ingreso(ingreso):
    if len(ingreso) <=8 and ingreso != "":
        return True
    return False

def validar_arreglo_ingreso(ventana,text_boxs,nombre_de_jugadores):
    for nombre in text_boxs:
        nombre_de_jugadores.append(nombre.get())
    for nombre in nombre_de_jugadores:
        if not(validar_palabra_ingreso(nombre)):
            return False
    return True

def enviar(ventana,text_box,cantidad_de_jugadores,nombre_de_jugadores,minutos):
    nombre_de_jugadores.clear()
    if(validar_arreglo_ingreso(ventana,text_box,nombre_de_jugadores)):
        ventana.destroy()
        iniciar_juego(cantidad_de_jugadores,nombre_de_jugadores,minutos)
    else:
        ventana_mensaje=Toplevel(ventana)
        mensaje=Label(ventana_mensaje, text="Datos incorrectos los jugadores no pueden tener mas de 8 caracteres ni ser vacios",font=("",40)).pack()


def pedir_nombre_de_jugadores(cantidad_de_jugadores,minutos):
    nombre_de_jugadores=[]
    text_boxs=[]
    ventana=Tk()
    ventana.geometry("528x905+0+0")
    ventana.resizable(0,0)
    imagen=PhotoImage(file="imagenes/identificacion.png")
    mensaje=Label(ventana, image=imagen).place(x=0,y=0)
    for i in range(cantidad_de_jugadores):
        text_boxs.append(Entry(ventana))
    desplazamiento=200
    distancia=25
    final=2*distancia*(cantidad_de_jugadores)+desplazamiento
    for i in range(cantidad_de_jugadores):
        Label(ventana, text="nombre del jugador "+str(i+1)+":").place(x=200,y=distancia*2*i+desplazamiento)
        text_boxs[i].place(x=200,y=distancia*(2*i+1)+desplazamiento)
    boton=Button(ventana, text="enviar",command=lambda:enviar(ventana,text_boxs,cantidad_de_jugadores,nombre_de_jugadores,minutos))
    boton.place(x=200,y=final)
    ventana.mainloop()

def iniciar(ventana,numero_de_jugadores,minuto):#obtiene el texto digitado en el recuadro
    minutos=minuto.get()
    cadena=numero_de_jugadores.get()
    if(es_un_numero(cadena)):
        numero=float(cadena)
        if(es_entero(numero)):
            entero=int(numero)
            if(entero in range(2,9)):
                if(es_un_numero(minutos)):
                    ventana.destroy()
                    pedir_nombre_de_jugadores(entero,float(minutos))
                else:
                    ventana_mensaje=Toplevel(ventana)
                    mensaje=Label(ventana_mensaje, text="EL numero de minutos debe ser un valor numerico",font=("",40)).pack()
            else:
                ventana_mensaje=Toplevel(ventana)
                mensaje=Label(ventana_mensaje, text="EL numero jugadores debe esta entre 2 y 8",font=("",40)).pack()
        else:
            ventana_mensaje=Toplevel(ventana)
            mensaje=Label(ventana_mensaje, text="EL numero jugadores debe ser un numero entero",font=("",40)).pack()
    else:
        ventana_mensaje=Toplevel(ventana)
        mensaje=Label(ventana_mensaje, text="EL numero jugadores debe ser un valor numerico",font=("",40)).pack()


def Configuracion_deljuego():#inicia la ventana
    ventana=Tk()
    ventana.geometry("545x620")
    ventana.resizable(0,0)
    imagen=PhotoImage(file="imagenes/numero_de_jugadores.png")
    mensaje=Label(ventana, image=imagen).place(x=0,y=0)
    numero_de_jugadores = Entry(ventana,width=55) #crea un cuadro de texto
    numero_de_jugadores.place(x=100,y=200) #posiciona el cuadro de texto
    mensaje=Label(ventana, text="Ingrese el numero de minutos que desea jugar",font=("",15)).place(x=70,y=300)
    minutos=Entry(ventana,width=60)
    minutos.place(x=90,y=350)
    boton_enviar=Button(ventana,text="enviar",width=10, command=lambda:iniciar(ventana,numero_de_jugadores,minutos))#crea un boton
    boton_enviar.place(x=200,y=400)#posiciona el boton
    ventana.mainloop()# actualiza la ventana