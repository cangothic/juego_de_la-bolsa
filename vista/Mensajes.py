__author__ = 'rocka'
from tkinter import *
def mensaje_confirmacion():
    ventana=Tk()
    ventana.geometry("738x438+0+0")
    ventana.resizable(0,0)
    imagen=PhotoImage(file="imagenes/compras/exito.png")
    mensaje=Label(ventana, image=imagen).place(x=0,y=0)
    ventana.mainloop()

def mensaje_cambio_de_mercado():
    ventana=Tk()
    ventana.geometry("450x446+0+0")
    ventana.resizable(0,0)
    imagen=PhotoImage(file="imagenes/cambio_de_mercado.png")
    mensaje=Label(ventana, image=imagen).place(x=0,y=0)
    ventana.mainloop()