#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'rocka'
miVersion = "venta de propiedades"
from tkinter import *
from tkinter.ttk import *
from mannanger.Algoritmos_de_manejo_de_titulos import *
from vista.EmpresasNegociar import *
class Negociante():
	def __init__(self, id, negociante):
		self.id = id
		self.negociante = negociante
	def __str__(self):
		return self.negociante

class Aplicacion(Frame):
	def __init__(self, master,arreglo,seleccionado,jugadores,enturno,mercado_de_valores):
            Frame.__init__(self, master=None)
            self.master.title(miVersion)
            self.idNegociante = StringVar()
            # Cemporadas
            Label(self.master, text="jugadores en curso",font=("",40)).grid(row=1, sticky=W)
            self.cbotemporadas = Combobox(self.master, textvariable=self.idNegociante, state="readonly",font=("",40) )
            self.cbotemporadas.grid(row=2, sticky=E)
            self.cbotemporadas.bind("<<ComboboxSelected>>")
            self.botonEnviar=Button(self.master, text="negociar",command=lambda:EmpresasNegociarvista(self.master,jugadores[enturno],jugadores[self.valores[self.idNegociante.get()]],mercado_de_valores),font=("",40))
            self.botonEnviar.grid(row=3,sticky=W)
            self.valores = self._cargaFromObject(arreglo, self.cbotemporadas, "negociante", "id", seleccionado, self.idNegociante)
            self.valores['']=''
	def _cargaFromObject(self, coleccion, objeto, campodesc, campoid, val2select, variable):
		misc , misv = [] , []
		for vv in coleccion:
			misv.append(getattr(vv,campodesc))
			misc.append(getattr(vv,campoid))
			if getattr(vv,campoid) == val2select: variable.set(getattr(vv,campodesc))  # Selección de Quiniela
		objeto["values"] = misv
		return dict(zip(misv, misc))	# Crea diccionario

def creavalores(arreglo,jugadores,enturno):
        for jugador in jugadores:
            if jugador != jugadores[enturno]:
                negociante=Negociante(jugadores.index(jugador),jugador.nombre)
                arreglo.append(negociante)

def negocearvista(jugadores,enturno,mercado_de_valores):
    arreglo2 = []
    seleccionado = 1
    creavalores(arreglo2,jugadores,enturno)
    root = Tk()
    root.resizable(0,0)
    a = Aplicacion(root,arreglo2,seleccionado,jugadores,enturno,mercado_de_valores)
    root.mainloop()