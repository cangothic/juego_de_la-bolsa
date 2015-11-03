__author__ = 'rocka'
from dto.Empresa import *
#clase por implementar
from tkinter import *
class Mercado_de_valores():
    def __init__(self,pintura):
        self.pitura=pintura

    def crear_ventana(self):
        self.ventana=Tk()
        self.ventana.geometry("1063x802+0+0")
        self.ventana.title("Mercado de valores")
        self.imagen=PhotoImage(file=self.pitura)
        self.label=Label(self.ventana,image=self.imagen)
        self.label.pack()
        self.ventana.mainloop()