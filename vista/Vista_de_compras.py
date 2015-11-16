__author__ = 'rocka'
from tkinter import *
from mannanger.Algoritmos_de_manejo_de_titulos import *
from identitie.Mercado_de_valores import *
from identitie.Jugador import *
def comprar_titulos(jugador,mercado,quiebra):
    ventana_de_compra=Tk()
    if(quiebra):
        ventana_de_compra.geometry("459x180+0+0")
        ventana_de_compra.resizable(0,0)
        imagen=PhotoImage(file="imagenes/compras/compra_empresa_quiebra.png")
        mensaje=Label(ventana_de_compra, image=imagen).pack()
    else:
        ventana_de_compra.geometry("628x544+0+0")
        ventana_de_compra.resizable(0,0)
        imagen=PhotoImage(file="imagenes/compras/comprar.png")
        mensaje=Label(ventana_de_compra, image=imagen).pack()
        jugador_que_compra=jugador
        empresa=mercado.empresas[str(jugador.posicion)]
        label_empresa=Label(ventana_de_compra, text=empresa.nombre,font=30)
        label_empresa.place(x=120,y=110)
        label_disponibilidad=Label(ventana_de_compra, text="disponibilidad :"+str(mercado.titulos[str(jugador_que_compra.posicion)]),font=30)
        label_disponibilidad.place(x=120,y=140)
        label_limite_inferior=label_empresa=Label(ventana_de_compra, text="limite inferior = "+str(empresa.limite_inferior),font=30)
        label_limite_inferior.place(x=120,y=170)
        label_limite_superior=label_empresa=Label(ventana_de_compra, text="limite superior = "+str(empresa.limite_superior),font=30)
        label_limite_superior.place(x=120,y=200)
        label_valor_mercado=label_empresa=Label(ventana_de_compra, text="valor mercado = "+str(empresa.valor_mercado),font=30)
        label_valor_mercado.place(x=120,y=230)
        imagen_boton1=PhotoImage(file="imagenes/compras/boton1.png")
        btcompra1=Button(ventana_de_compra,command=lambda:comprar(ventana_de_compra,jugador,mercado,1),image=imagen_boton1,bg="green")
        btcompra1.place(x=400,y=360)
        imagen_boton2=PhotoImage(file="imagenes/compras/boton2.png")
        btcompra2=Button(ventana_de_compra,command=lambda:comprar(ventana_de_compra,jugador,mercado,2),image=imagen_boton2,bg="green")
        btcompra2.place(x=400,y=410)
        imagen_boton3=PhotoImage(file="imagenes/compras/boton3.png")
        btcompra3=Button(ventana_de_compra,command=lambda:comprar(ventana_de_compra,jugador,mercado,3),image=imagen_boton3,bg="green")
        btcompra3.place(x=400,y=460)
    ventana_de_compra.mainloop()