#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'rocka'
from dto.Empresa import *
#clase por implementar
from tkinter import *
class Mercado_de_valores():
    def __init__(self,pintura):
        self.pitura=pintura
        self.empresas={ "1":Empresa("ChezPierre",350,1100),
                        "3":Empresa("Pluma de oro",500,1250),
                        "4":Empresa("RapiMarket ",400,1350),
                        "5":Empresa("Dakkar ",350,1100),
                        "13":Empresa("Telecomunicaciones mundiales S.A ",350,1100),
                        "15":Empresa("Unión  Mercantil ",350,1100),
                        "16":Empresa("Telesac",350,1100),
                        "17":Empresa("Transamerica",350,1100),
                        "7":Empresa("Sanata Elena Textiles ",350,1100),
                        "8":Empresa("Cena S.A ",350,1100),
                        "9":Empresa("Real tabacalera ",350,1100),
                        "11":Empresa("Automark S.A ",350,1100),
                        "19":Empresa("Fondos industriales unidos",350,1100),
                        "20":Empresa("seguros sun state ",350,1100),
                        "21":Empresa("Créditos del sur ",350,1100),
                        "26":Empresa("Banco interamericano ",350,1100)}

    def crear_ventana(self):
        self.ventana=Tk()
        self.ventana.geometry("1063x802+0+0")
        self.ventana.title("Mercado de valores")
        self.imagen=PhotoImage(file=self.pitura)
        self.label=Label(self.ventana,image=self.imagen)
        self.label.pack()
        self.ventana.mainloop()

    def cambio_de_mercado(self):
        for empresa in self.empresas:
            self.empresas[empresa].cambio_de_mercado()