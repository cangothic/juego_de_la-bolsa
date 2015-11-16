from tkinter import *
from mannanger.Algoritmos_de_manejo_de_titulos import *
__author__ = 'rocka'
def calcula_score(jugadores,mercado):
    recoger_titulaciones(jugadores,mercado)
    ventana=Tk()
    ventana.geometry("528x905+0+0")
    imagen=PhotoImage(file="imagenes/score.png")
    mensaje=Label(ventana, image=imagen).place(x=0,y=0)
    distancia=20
    desplazamiento=300
    for i in range(0,len(jugadores)):
        Label(ventana, text=jugadores[i].nombre+":      saldo:"+str(jugadores[i].saldo)).place(x=200,y=distancia*i+desplazamiento)
    ventana.mainloop()


