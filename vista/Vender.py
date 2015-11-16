#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'rocka'
miVersion = "venta de propiedades"
from tkinter import *
from tkinter.ttk import *
from mannanger.Algoritmos_de_manejo_de_titulos import *
class Empresas():
	def __init__(self, id, empresa):
		self.id = id
		self.empresa = empresa
	def __str__(self):
		return self.empresa

class Aplicacion(Frame):
	def __init__(self, master,arreglo,seleccionado,jugador,mercado_de_valores):
            Frame.__init__(self, master=None)
            self.master.title(miVersion)
            self.idEmpresa = StringVar()
            # Cemporadas
            Label(self.master, text="empresas",font=("",40)).grid(row=1, sticky=W)
            self.cbotemporadas = Combobox(self.master, textvariable=self.idEmpresa, state="readonly",font=("",40) )
            self.cbotemporadas.grid(row=2, sticky=E)
            self.cbotemporadas.bind("<<ComboboxSelected>>")
            self.botonEnviar=Button(self.master, text="vender",command=lambda:vender(self.master,jugador,mercado_de_valores,self.valores[self.idEmpresa.get()]),font=("",40))
            self.botonEnviar.grid(row=3,sticky=W)
            self.valores = self._cargaFromObject(arreglo, self.cbotemporadas, "empresa", "id", seleccionado, self.idEmpresa)
            self.valores['']=''

	def _cargaFromObject(self, coleccion, objeto, campodesc, campoid, val2select, variable):
		misc , misv = [] , []
		for vv in coleccion:
			misv.append(getattr(vv,campodesc))
			misc.append(getattr(vv,campoid))
			if getattr(vv,campoid) == val2select: variable.set(getattr(vv,campodesc))  # Selección de Quiniela
		objeto["values"] = misv
		return dict(zip(misv, misc))	# Crea diccionario

def creavalores(arreglo,jugador,mercado_de_valores,sector):
    titulaciones= jugador.titulos
    if(sector):
        for titulo in titulaciones:
            if(jugador.posicion in range(1,6) and jugador.titulos[titulo]>0):
                if(int(titulo) in range(1,6)):
                    empresa=Empresas(titulo,mercado_de_valores.empresas[titulo].nombre)
                    arreglo.append(empresa)
            if(jugador.posicion in range(7,12) and jugador.titulos[titulo]>0):
                if(int(titulo) in range(7,12)):
                    empresa=Empresas(titulo,mercado_de_valores.empresas[titulo].nombre)
                    arreglo.append(empresa)
            if(jugador.posicion in range(13,18) and jugador.titulos[titulo]>0):
                if(int(titulo) in range(13,18)):
                    empresa=Empresas(titulo,mercado_de_valores.empresas[titulo].nombre)
                    arreglo.append(empresa)
            if(jugador.posicion in range(19,24) and jugador.titulos[titulo]>0):
                if(int(titulo) in range(19,24)):
                    empresa=Empresas(titulo,mercado_de_valores.empresas[titulo].nombre)
                    arreglo.append(empresa)
    else:
        for titulo in titulaciones:
            empresa=Empresas(titulo,mercado_de_valores.empresas[titulo].nombre)
            arreglo.append(empresa)
def vendervista(jugador,mercado_de_valores,sector):
    arreglo2 = []
    seleccionado = 1
    creavalores(arreglo2,jugador,mercado_de_valores,sector)
    root = Tk()
    root.resizable(0,0)
    a = Aplicacion(root,arreglo2,seleccionado,jugador,mercado_de_valores)
    root.mainloop()