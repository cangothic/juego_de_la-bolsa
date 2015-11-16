#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'rocka'
from identitie.Empresa import *
from vista.Mensajes import *
#clase por implementar
from tkinter import *
class Mercado_de_valores():
    def __init__(self,pintura):
        self.efectivo_disponible=199650
        self.pitura=pintura
        self.titulos={"1":7,"3":7,"4":7,"5":7,"13":7,"15":7,"16":7,"17":7,"7":7,"8":7,"9":7,"11":7,"19":7,"20":7,"21":7,"23":7}

        self.empresas={ "1":Empresa("ChezPierre",350,1100),
                        "3":Empresa("Pluma de oro",500,1250),
                        "4":Empresa("RapiMarket ",400,1350),
                        "5":Empresa("Dakkar",600,1400),
                        "13":Empresa("Telecomunicaciones m. S.A",1000,1800),
                        "15":Empresa("Union  Mercantil",1000,1850),
                        "16":Empresa("Telesac",900,1050),
                        "17":Empresa("Transamerica",950,2000),
                        "7":Empresa("Santa Elena Textiles",750,1600),#valor temporal
                        "8":Empresa("Cena S.A ",650,1550),
                        "9":Empresa("Real tabacalera",750,1600),
                        "11":Empresa("Automark S.A",700,1700),
                        "19":Empresa("Fondos industriales u.",1300,2200),
                        "20":Empresa("seguros Sun State",900,2250),
                        "21":Empresa("Créditos del sur",1500,2500),
                        "23":Empresa("Banco interamericano",1500,2650)}

    def crear_ventana(self):
        self.ventana=Tk()
        self.ventana.resizable(0,0)
        self.ventana.geometry("1063x802+0+0")
        self.ventana.title("Mercado de valores")
        self.imagen=PhotoImage(file=self.pitura)
        self.label=Label(self.ventana,image=self.imagen)
        self.label.place(x=0,y=0)
        #izquierda
        #muestra los valores de la empresa ChezPierre 1
        if (self.empresas["1"].quebrada):
            self.ChezPierre_limite_superior= Label(self.ventana, text="//////",font=30)
            self.ChezPierre_limite_superior.place(x=240,y=120)
            self.ChezPierre_limite_inferior= Label(self.ventana, text="//////",font=30)
            self.ChezPierre_limite_inferior.place(x=320,y=120)
            self.ChezPierre_valor_mercado=Label(self.ventana, text=str(self.empresas["1"].valor_mercado),font=30)
            self.ChezPierre_valor_mercado.place(x=430,y=120)
        else:
            self.ChezPierre_limite_superior= Label(self.ventana, text=str(self.empresas["1"].limite_superior),font=30)
            self.ChezPierre_limite_superior.place(x=240,y=120)
            self.ChezPierre_limite_inferior= Label(self.ventana, text=str(self.empresas["1"].limite_inferior),font=30)
            self.ChezPierre_limite_inferior.place(x=320,y=120)
            self.ChezPierre_valor_mercado=Label(self.ventana, text=str(self.empresas["1"].valor_mercado),font=30)
            self.ChezPierre_valor_mercado.place(x=430,y=120)
        #muestra los valores de la empresa Pluma de oro 2
        if (self.empresas["3"].quebrada):
            self.Pluma_de_oro_limite_superior= Label(self.ventana, text="//////",font=30)
            self.Pluma_de_oro_limite_superior.place(x=240,y=200)
            self.Pluma_de_oro_limite_inferior= Label(self.ventana, text="//////",font=30)
            self.Pluma_de_oro_limite_inferior.place(x=320,y=200)
            self.Pluma_de_oro_valor_mercado=Label(self.ventana, text=str(self.empresas["3"].valor_mercado),font=30)
            self.Pluma_de_oro_valor_mercado.place(x=430,y=200)
        else:
            self.Pluma_de_oro_limite_superior= Label(self.ventana, text=str(self.empresas["3"].limite_superior),font=30)
            self.Pluma_de_oro_limite_superior.place(x=240,y=200)
            self.Pluma_de_oro_limite_inferior= Label(self.ventana, text=str(self.empresas["3"].limite_inferior),font=30)
            self.Pluma_de_oro_limite_inferior.place(x=320,y=200)
            self.Pluma_de_oro_valor_mercado=Label(self.ventana, text=str(self.empresas["3"].valor_mercado),font=30)
            self.Pluma_de_oro_valor_mercado.place(x=430,y=200)
        #muestra los valores de la empresa RapiMarket 3
        if (self.empresas["4"].quebrada):
            self.RapiMarket_limite_superior= Label(self.ventana, text="//////",font=30)
            self.RapiMarket_limite_superior.place(x=240,y=280)
            self.RapiMarket_limite_inferior= Label(self.ventana, text="//////",font=30)
            self.RapiMarket_limite_inferior.place(x=320,y=280)
            self.RapiMarket_valor_mercado=Label(self.ventana, text=str(self.empresas["4"].valor_mercado),font=30)
            self.RapiMarket_valor_mercado.place(x=430,y=280)
        else:
            self.RapiMarket_limite_superior= Label(self.ventana, text=str(self.empresas["4"].limite_superior),font=30)
            self.RapiMarket_limite_superior.place(x=240,y=280)
            self.RapiMarket_limite_inferior= Label(self.ventana, text=str(self.empresas["4"].limite_inferior),font=30)
            self.RapiMarket_limite_inferior.place(x=320,y=280)
            self.RapiMarket_valor_mercado=Label(self.ventana, text=str(self.empresas["4"].valor_mercado),font=30)
            self.RapiMarket_valor_mercado.place(x=430,y=280)
        #muestra los valores de la empresa Dakkar 4
        if (self.empresas["5"].quebrada):
            self.Dakkar_limite_superior= Label(self.ventana, text="//////",font=30)
            self.Dakkar_limite_superior.place(x=240,y=360)
            self.Dakkar_limite_inferior= Label(self.ventana, text="//////",font=30)
            self.Dakkar_limite_inferior.place(x=320,y=360)
            self.Dakkar_valor_mercado=Label(self.ventana, text=str(self.empresas["5"].valor_mercado),font=30)
            self.Dakkar_valor_mercado.place(x=430,y=360)
        else:
            self.Dakkar_limite_superior= Label(self.ventana, text=str(self.empresas["5"].limite_superior),font=30)
            self.Dakkar_limite_superior.place(x=240,y=360)
            self.Dakkar_limite_inferior= Label(self.ventana, text=str(self.empresas["5"].limite_inferior),font=30)
            self.Dakkar_limite_inferior.place(x=320,y=360)
            self.Dakkar_valor_mercado=Label(self.ventana, text=str(self.empresas["5"].valor_mercado),font=30)
            self.Dakkar_valor_mercado.place(x=430,y=360)
        #muestra los valores de la empresa Telecomunicaciones mundiales S.A 5
        if (self.empresas["13"].quebrada):
            self.Telecomunicaciones_mundiales_SA_limite_superior= Label(self.ventana, text="//////",font=30)
            self.Telecomunicaciones_mundiales_SA_limite_superior.place(x=240,y=480)
            self.Telecomunicaciones_mundiales_SA_limite_inferior= Label(self.ventana, text="//////",font=30)
            self.Telecomunicaciones_mundiales_SA_limite_inferior.place(x=320,y=480)
            self.Telecomunicaciones_mundiales_SA_valor_mercado=Label(self.ventana, text=str(self.empresas["13"].valor_mercado),font=30)
            self.Telecomunicaciones_mundiales_SA_valor_mercado.place(x=430,y=480)
        else:
            self.Telecomunicaciones_mundiales_SA_limite_superior= Label(self.ventana, text=str(self.empresas["13"].limite_superior),font=30)
            self.Telecomunicaciones_mundiales_SA_limite_superior.place(x=240,y=480)
            self.Telecomunicaciones_mundiales_SA_limite_inferior= Label(self.ventana, text=str(self.empresas["13"].limite_inferior),font=30)
            self.Telecomunicaciones_mundiales_SA_limite_inferior.place(x=320,y=480)
            self.Telecomunicaciones_mundiales_SA_valor_mercado=Label(self.ventana, text=str(self.empresas["13"].valor_mercado),font=30)
            self.Telecomunicaciones_mundiales_SA_valor_mercado.place(x=430,y=480)
        #muestra los valores de la empresa Telecomunicaciones Union Mercantil 6
        if (self.empresas["15"].quebrada):
            self.Union_Mercantil_limite_superior= Label(self.ventana, text="//////",font=30)
            self.Union_Mercantil_limite_superior.place(x=240,y=560)
            self.Union_Mercantil_limite__inferior= Label(self.ventana, text="//////",font=30)
            self.Union_Mercantil_limite__inferior.place(x=320,y=560)
            self.Union_Mercantil_limite_valor_mercado=Label(self.ventana, text=str(self.empresas["15"].valor_mercado),font=30)
            self.Union_Mercantil_limite_valor_mercado.place(x=430,y=560)
        else:
            self.Union_Mercantil_limite_superior= Label(self.ventana, text=str(self.empresas["15"].limite_superior),font=30)
            self.Union_Mercantil_limite_superior.place(x=240,y=560)
            self.Union_Mercantil_limite__inferior= Label(self.ventana, text=str(self.empresas["15"].limite_inferior),font=30)
            self.Union_Mercantil_limite__inferior.place(x=320,y=560)
            self.Union_Mercantil_limite_valor_mercado=Label(self.ventana, text=str(self.empresas["15"].valor_mercado),font=30)
            self.Union_Mercantil_limite_valor_mercado.place(x=430,y=560)
        #muestra los valores de la empresa Telesac 7
        if (self.empresas["16"].quebrada):
            self.Telesac_limite_superior= Label(self.ventana, text="//////",font=30)
            self.Telesac_limite_superior.place(x=240,y=640)
            self.Telesac_limite_limite_inferior= Label(self.ventana, text="//////",font=30)
            self.Telesac_limite_limite_inferior.place(x=320,y=640)
            self.Telesac_limite_valor_mercado=Label(self.ventana, text=str(self.empresas["16"].valor_mercado),font=30)
            self.Telesac_limite_valor_mercado.place(x=430,y=640)
        else:
            self.Telesac_limite_superior= Label(self.ventana, text=str(self.empresas["16"].limite_superior),font=30)
            self.Telesac_limite_superior.place(x=240,y=640)
            self.Telesac_limite_limite_inferior= Label(self.ventana, text=str(self.empresas["16"].limite_inferior),font=30)
            self.Telesac_limite_limite_inferior.place(x=320,y=640)
            self.Telesac_limite_valor_mercado=Label(self.ventana, text=str(self.empresas["16"].valor_mercado),font=30)
            self.Telesac_limite_valor_mercado.place(x=430,y=640)
        #muestra los valores de la empresa Transamerica 8
        if (self.empresas["17"].quebrada):
            self.Transamerica_limite_superior= Label(self.ventana, text="//////",font=30)
            self.Transamerica_limite_superior.place(x=240,y=720)
            self.Transamerica_limite_inferior= Label(self.ventana, text="//////",font=30)
            self.Transamerica_limite_inferior.place(x=320,y=720)
            self.Transamerica_valor_mercado=Label(self.ventana, text=str(self.empresas["17"].valor_mercado),font=30)
            self.Transamerica_valor_mercado.place(x=430,y=720)
        else:
            self.Transamerica_limite_superior= Label(self.ventana, text=str(self.empresas["17"].limite_superior),font=30)
            self.Transamerica_limite_superior.place(x=240,y=720)
            self.Transamerica_limite_inferior= Label(self.ventana, text=str(self.empresas["17"].limite_inferior),font=30)
            self.Transamerica_limite_inferior.place(x=320,y=720)
            self.Transamerica_valor_mercado=Label(self.ventana, text=str(self.empresas["17"].valor_mercado),font=30)
            self.Transamerica_valor_mercado.place(x=430,y=720)
        #derecha
        #muestra los valores de la empresa Santa Elena Textiles 1\
        if (self.empresas["7"].quebrada):
            self.Santa_Elena_Textiles_limite_superior= Label(self.ventana, text="//////",font=30)
            self.Santa_Elena_Textiles_limite_superior.place(x=740,y=120)
            self.Santa_Elena_Textiles_inferior= Label(self.ventana, text="//////",font=30)
            self.Santa_Elena_Textiles_inferior.place(x=850,y=120)
            self.Santa_Elena_Textiles_valor_mercado=Label(self.ventana, text=str(self.empresas["7"].valor_mercado),font=30)
            self.Santa_Elena_Textiles_valor_mercado.place(x=960,y=120)
        else:
            self.Santa_Elena_Textiles_limite_superior= Label(self.ventana, text=str(self.empresas["7"].limite_superior),font=30)
            self.Santa_Elena_Textiles_limite_superior.place(x=740,y=120)
            self.Santa_Elena_Textiles_inferior= Label(self.ventana, text=str(self.empresas["7"].limite_inferior),font=30)
            self.Santa_Elena_Textiles_inferior.place(x=850,y=120)
            self.Santa_Elena_Textiles_valor_mercado=Label(self.ventana, text=str(self.empresas["7"].valor_mercado),font=30)
            self.Santa_Elena_Textiles_valor_mercado.place(x=960,y=120)
        #muestra los valores de la empresa Cena S.A 2
        if (self.empresas["8"].quebrada):
            self.Cena_SA_limite_superior= Label(self.ventana, text="//////",font=30)
            self.Cena_SA_limite_superior.place(x=740,y=200)
            self.Cena_SA_inferior= Label(self.ventana, text="//////",font=30)
            self.Cena_SA_inferior.place(x=850,y=200)
            self.Cena_SA_valor_mercado=Label(self.ventana, text=str(self.empresas["8"].valor_mercado),font=30)
            self.Cena_SA_valor_mercado.place(x=960,y=200)
        else:
            self.Cena_SA_limite_superior= Label(self.ventana, text=str(self.empresas["8"].limite_superior),font=30)
            self.Cena_SA_limite_superior.place(x=740,y=200)
            self.Cena_SA_inferior= Label(self.ventana, text=str(self.empresas["8"].limite_inferior),font=30)
            self.Cena_SA_inferior.place(x=850,y=200)
            self.Cena_SA_valor_mercado=Label(self.ventana, text=str(self.empresas["8"].valor_mercado),font=30)
            self.Cena_SA_valor_mercado.place(x=960,y=200)
        #muestra los valores de la empresa Real tabacalera 3
        if (self.empresas["9"].quebrada):
            self.Real_tabacalera_limite_superior= Label(self.ventana, text="//////",font=30)
            self.Real_tabacalera_limite_superior.place(x=740,y=280)
            self.Real_tabacalera_limite_inferior= Label(self.ventana, text="//////",font=30)
            self.Real_tabacalera_limite_inferior.place(x=850,y=280)
            self.Real_tabacalera_valor_mercado=Label(self.ventana, text=str(self.empresas["9"].valor_mercado),font=30)
            self.Real_tabacalera_valor_mercado.place(x=960,y=280)
        else:
            self.Real_tabacalera_limite_superior= Label(self.ventana, text=str(self.empresas["9"].limite_superior),font=30)
            self.Real_tabacalera_limite_superior.place(x=740,y=280)
            self.Real_tabacalera_limite_inferior= Label(self.ventana, text=str(self.empresas["9"].limite_inferior),font=30)
            self.Real_tabacalera_limite_inferior.place(x=850,y=280)
            self.Real_tabacalera_valor_mercado=Label(self.ventana, text=str(self.empresas["9"].valor_mercado),font=30)
            self.Real_tabacalera_valor_mercado.place(x=960,y=280)
        #muestra los valores de la empresa Automark S.A 4
        if (self.empresas["11"].quebrada):
            self.Automark_SA_limite_superior= Label(self.ventana, text="//////",font=30)
            self.Automark_SA_limite_superior.place(x=740,y=360)
            self.Automark_SA_limite_inferior= Label(self.ventana, text="//////",font=30)
            self.Automark_SA_limite_inferior.place(x=850,y=360)
            self.Automark_SA_valor_mercado=Label(self.ventana, text=str(self.empresas["11"].valor_mercado),font=30)
            self.Automark_SA_valor_mercado.place(x=960,y=360)
        else:
            self.Automark_SA_limite_superior= Label(self.ventana, text=str(self.empresas["11"].limite_superior),font=30)
            self.Automark_SA_limite_superior.place(x=740,y=360)
            self.Automark_SA_limite_inferior= Label(self.ventana, text=str(self.empresas["11"].limite_inferior),font=30)
            self.Automark_SA_limite_inferior.place(x=850,y=360)
            self.Automark_SA_valor_mercado=Label(self.ventana, text=str(self.empresas["11"].valor_mercado),font=30)
            self.Automark_SA_valor_mercado.place(x=960,y=360)
        #muestra los valores de la empresa Fondos industriales unidos 5
        if (self.empresas["19"].quebrada):
            self.Fondos_industriales_unidos_limite_superior= Label(self.ventana, text="//////",font=30)
            self.Fondos_industriales_unidos_limite_superior.place(x=740,y=480)
            self.Fondos_industriales_unidos_limite_inferior= Label(self.ventana, text="//////",font=30)
            self.Fondos_industriales_unidos_limite_inferior.place(x=850,y=480)
            self.Fondos_industriales_unidos_valor_mercado=Label(self.ventana, text=str(self.empresas["19"].valor_mercado),font=30)
            self.Fondos_industriales_unidos_valor_mercado.place(x=960,y=480)
        else:
            self.Fondos_industriales_unidos_limite_superior= Label(self.ventana, text=str(self.empresas["19"].limite_superior),font=30)
            self.Fondos_industriales_unidos_limite_superior.place(x=740,y=480)
            self.Fondos_industriales_unidos_limite_inferior= Label(self.ventana, text=str(self.empresas["19"].limite_inferior),font=30)
            self.Fondos_industriales_unidos_limite_inferior.place(x=850,y=480)
            self.Fondos_industriales_unidos_valor_mercado=Label(self.ventana, text=str(self.empresas["19"].valor_mercado),font=30)
            self.Fondos_industriales_unidos_valor_mercado.place(x=960,y=480)
        #muestra los valores de la empresa seguros Sun State 6
        if (self.empresas["20"].quebrada):
            self.Sun_State_limite_superior= Label(self.ventana, text="//////",font=30)
            self.Sun_State_limite_superior.place(x=740,y=560)
            self.Sun_State_limite_inferior= Label(self.ventana, text="//////",font=30)
            self.Sun_State_limite_inferior.place(x=850,y=560)
            self.Sun_State_valor_mercado=Label(self.ventana, text=str(self.empresas["20"].valor_mercado),font=30)
            self.Sun_State_valor_mercado.place(x=960,y=560)
        else:
            self.Sun_State_limite_superior= Label(self.ventana, text=str(self.empresas["20"].limite_superior),font=30)
            self.Sun_State_limite_superior.place(x=740,y=560)
            self.Sun_State_limite_inferior= Label(self.ventana, text=str(self.empresas["20"].limite_inferior),font=30)
            self.Sun_State_limite_inferior.place(x=850,y=560)
            self.Sun_State_valor_mercado=Label(self.ventana, text=str(self.empresas["20"].valor_mercado),font=30)
            self.Sun_State_valor_mercado.place(x=960,y=560)
        #muestra los valores de la empresa Créditos del sur 7
        if (self.empresas["21"].quebrada):
            self.Creditos_del_sur_limite_superior= Label(self.ventana, text="//////",font=30)
            self.Creditos_del_sur_limite_superior.place(x=740,y=640)
            self.Creditos_del_sur_limite_inferior= Label(self.ventana, text="//////",font=30)
            self.Creditos_del_sur_limite_inferior.place(x=850,y=640)
            self.Creditos_del_sur_valor_mercado=Label(self.ventana, text=str(self.empresas["21"].valor_mercado),font=30)
            self.Creditos_del_sur_valor_mercado.place(x=960,y=640)
        else:
            self.Creditos_del_sur_limite_superior= Label(self.ventana, text=str(self.empresas["21"].limite_superior),font=30)
            self.Creditos_del_sur_limite_superior.place(x=740,y=640)
            self.Creditos_del_sur_limite_inferior= Label(self.ventana, text=str(self.empresas["21"].limite_inferior),font=30)
            self.Creditos_del_sur_limite_inferior.place(x=850,y=640)
            self.Creditos_del_sur_valor_mercado=Label(self.ventana, text=str(self.empresas["21"].valor_mercado),font=30)
            self.Creditos_del_sur_valor_mercado.place(x=960,y=640)
        #muestra los valores de la empresa Banco interamericano 8
        if (self.empresas["23"].quebrada):
            self.Banco_interamericano_limite_superior= Label(self.ventana, text="//////",font=30)
            self.Banco_interamericano_limite_superior.place(x=740,y=720)
            self.Banco_interamericano_limite_inferior= Label(self.ventana, text="//////",font=30)
            self.Banco_interamericano_limite_inferior.place(x=850,y=720)
            self.Banco_interamericano_valor_mercado=Label(self.ventana, text=str(self.empresas["23"].valor_mercado),font=30)
            self.Banco_interamericano_valor_mercado.place(x=960,y=720)
        else:
            self.Banco_interamericano_limite_superior= Label(self.ventana, text=str(self.empresas["23"].limite_superior),font=30)
            self.Banco_interamericano_limite_superior.place(x=740,y=720)
            self.Banco_interamericano_limite_inferior= Label(self.ventana, text=str(self.empresas["23"].limite_inferior),font=30)
            self.Banco_interamericano_limite_inferior.place(x=850,y=720)
            self.Banco_interamericano_valor_mercado=Label(self.ventana, text=str(self.empresas["23"].valor_mercado),font=30)
            self.Banco_interamericano_valor_mercado.place(x=960,y=720)

        self.ventana.mainloop()

    def cambio_de_mercado(self,jugadores):
        mensaje_cambio_de_mercado()
        for empresa in self.empresas:
            self.empresas[empresa].cambio_de_mercado()

        for empresa_quiebra in self.empresas:
            if(self.empresas[empresa_quiebra].quebrada):
                for jugador in jugadores:
                    jugador.saldo+=jugador.titulos[empresa_quiebra]*self.empresas[empresa_quiebra].valor_mercado
                    jugador.titulos[empresa_quiebra]=0
                    self.titulos[empresa_quiebra]=7