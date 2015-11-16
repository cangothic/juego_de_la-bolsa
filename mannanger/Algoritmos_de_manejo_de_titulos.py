__author__ = 'rocka'
import random
from mannanger.Algoritmos_de_probabilidad import *
from tkinter import *
from vista.Mensajes import *
from mannanger.Algoritmos_para_validaciones import *
def comprar(ventana,jugador,mercado,cantidad):
    ventana.destroy()
    empresa=mercado.empresas[str(jugador.posicion)]
    valor_de_venta=empresa.valor_mercado*cantidad
    if(mercado.titulos[str(jugador.posicion)]>=cantidad):
        if(jugador.saldo>=valor_de_venta):
            jugador.saldo-=valor_de_venta
            mercado.titulos[str(jugador.posicion)]-=cantidad
            jugador.titulos[str(jugador.posicion)]+=cantidad
            mensaje_confirmacion()
        else:
            ventana_mensaje_de_confirmacion=Tk()
            mensaje=Label(ventana_mensaje_de_confirmacion, text="No tiene dinero suficiente",font=("",40)).pack()
            ventana_mensaje_de_confirmacion.mainloop()
    else:
        ventana_mensaje_de_confirmacion=Tk()
        mensaje=Label(ventana_mensaje_de_confirmacion, text="Lo sentimos no nos quedan existencias",font=("",40)).pack()
        ventana_mensaje_de_confirmacion.mainloop()
def validar_venta(ventana,jugador,mercado_de_valores,clave,entrada):
    if(es_un_numero(entrada)):
        numero=float(entrada)
        if(es_entero(numero) and numero>0):
            cantidad=int(entrada)
            if(jugador.titulos[clave]>=cantidad):
                jugador.titulos[clave]-=cantidad
                jugador.saldo+=cantidad*mercado_de_valores.empresas[clave].valor_mercado
                mercado_de_valores.titulos[clave]+=cantidad
                ventana_mensaje=Toplevel(ventana)
                ventana.destroy()
            else:
                ventana_mensaje=Toplevel(ventana)
                mensaje=Label(ventana_mensaje, text="No tienes titulaciones suficientes",font=("",40)).pack()
        else:
            ventana_mensaje=Toplevel(ventana)
            mensaje=Label(ventana_mensaje, text="la cantidad de titulaciones es un numero entero positivo",font=("",40)).pack()

    else:
        ventana_mensaje=Toplevel(ventana)
        mensaje=Label(ventana_mensaje, text="la cantidad de titulaciones es un valor numerico",font=("",40)).pack()

def vender(recibida,jugador,mercado_de_valores,clave):
    if clave !='':
        recibida.destroy()
        cantidad=1
        empresa=mercado_de_valores.empresas[clave]
        ventana=Tk()
        ventana.resizable(0,0)
        Label(ventana, text=empresa.nombre,font=("",20)).pack()
        Label(ventana, text="Valor: "+str(empresa.valor_mercado),font=("",20)).pack()
        Label(ventana, text="Titulos que posee: "+str(jugador.titulos[clave]),font=("",20)).pack()
        Label(ventana, text="Ingrese la cantidad de titulos: ",font=("",20)).pack()
        pedir_cantidad=Entry(ventana,width=55)
        pedir_cantidad.pack()
        boton=Button(ventana, text="enviar",command=lambda:validar_venta(ventana,jugador,mercado_de_valores,clave,pedir_cantidad.get()))
        boton.pack()

def validar_negociacion(ventana,jugador,negociante,mercado_de_valores,clave,comision,entrada):
    if(es_un_numero(entrada)):
        numero=float(entrada)
        if(es_entero(numero) and numero>0):
            cantidad=int(entrada)
            if(jugador.titulos[clave]>=cantidad):
                jugador.titulos[clave]-=cantidad
                jugador.saldo+=cantidad*mercado_de_valores.empresas[clave].valor_mercado
                jugador.saldo-=comision*cantidad
                negociante.saldo+=comision*cantidad
                mercado_de_valores.titulos[clave]+=cantidad
                ventana_mensaje=Toplevel(ventana)
                ventana.destroy()
            else:
                ventana_mensaje=Toplevel(ventana)
                mensaje=Label(ventana_mensaje, text="No tienes titulaciones suficientes",font=("",40)).pack()
        else:
            ventana_mensaje=Toplevel(ventana)
            mensaje=Label(ventana_mensaje, text="la cantidad de titulaciones es un numero entero positivo",font=("",40)).pack()

    else:
        ventana_mensaje=Toplevel(ventana)
        mensaje=Label(ventana_mensaje, text="la cantidad de titulaciones es un valor numerico",font=("",40)).pack()
def negociar(recibida,jugador,negociante,mercado_de_valores,clave):
    if clave !='':
        recibida.destroy()
        comision=calcular_porcentage(mercado_de_valores.empresas[clave].limite_inferior,0.3,0.6)
        empresa=mercado_de_valores.empresas[clave]
        ventana=Tk()
        ventana.resizable(0,0)
        Label(ventana, text="Comision: "+str(comision),font=("",20)).pack()
        Label(ventana, text=empresa.nombre,font=("",20)).pack()
        Label(ventana, text="Valor: "+str(empresa.valor_mercado),font=("",20)).pack()
        Label(ventana, text="Titulos que posee: "+str(jugador.titulos[clave]),font=("",20)).pack()
        Label(ventana, text="Ingrese la cantidad de titulos: ",font=("",20)).pack()
        pedir_cantidad=Entry(ventana,width=55)
        pedir_cantidad.pack()
        boton=Button(ventana, text="enviar",command=lambda:validar_negociacion(ventana,jugador,negociante,mercado_de_valores,clave,comision,pedir_cantidad.get()))
        boton.pack()

def recoger_titulaciones(jugadores,mercado_de_valores):
    for empresa in mercado_de_valores.titulos:
        for jugador in jugadores:
            jugador.saldo+=jugador.titulos[empresa]*mercado_de_valores.empresas[empresa].valor_mercado
            mercado_de_valores.efectivo_disponible-=jugador.titulos[empresa]*mercado_de_valores.empresas[empresa].valor_mercado
            jugador.titulos[empresa]=0
            mercado_de_valores.titulos[empresa]=7


