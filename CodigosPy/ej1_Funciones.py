import tkinter
import tkinter as tk
import math
from functools import partial
from tkinter import ttk
from tkinter import*


root = tk.Tk();
root.config(width=300, height=200)
root.title("Areas de figuras")


def calculoArea(**kwargs):

    ventana_secundaria = tkinter.Toplevel(root)
    ventana_secundaria.title("Ventana secundaria")
    ventana_secundaria.config(width=300, height=200)
    ventana_secundaria.focus()
    ventana_secundaria.grab_set()
    root.iconify()
    if 'titulo' in kwargs and kwargs['titulo'] == "AREA TRIANGULO":
        entry_base = ttk.Entry(ventana_secundaria, state="write only")
        entry_base.place(x=110, y=50)
        entry_altura = ttk.Entry(ventana_secundaria, state="write only")
        entry_altura.place(x=110, y=80)
        lbase = Label(ventana_secundaria,text = kwargs['base']).place(x = 40,y = 50)
        laltura = Label(ventana_secundaria,text = kwargs['altura']).place(x = 40,y = 80)
    else:
        entry_radio = ttk.Entry(ventana_secundaria, state="write only")
        entry_radio.place(x=110, y=50)
        lradio = Label(ventana_secundaria,text = kwargs['radio']).place(x = 40,y = 50)

    entry_salida = ttk.Entry(ventana_secundaria, state=tk.DISABLED)
    entry_salida.place(x=110, y=110)
    ltitulo = Label(ventana_secundaria,text = kwargs['titulo']).place(x = 120,y = 20)
    lsalida = Label(ventana_secundaria,text = "Area").place(x = 40,y = 110)

    def areaCirculo():

        try:
            radio = float(entry_radio.get())
            entry_salida.config(state=tk.NORMAL)
            entry_salida.insert(0,math.pi * radio **2)
            entry_salida.config(state=tk.DISABLED)
        except:
            entry_salida.config(state=tk.NORMAL)
            entry_salida.insert(0,"Valores Invalidos")
            entry_salida.config(state=tk.DISABLED)

    def areaTriangulo():

        try:
            base = float(entry_base.get());
            altura = float(entry_altura.get());
            entry_salida.config(state=tk.NORMAL)
            entry_salida.insert(0, base * altura / 2)
            entry_salida.config(state=tk.DISABLED)
        except:
            entry_salida.config(state=tk.NORMAL)
            entry_salida.insert(0,"Valores Invalidos")
            entry_salida.config(state=tk.DISABLED)

    def limpiar():

        if kwargs['titulo'] == "AREA TRIANGULO":
            entry_altura.delete("0",last="end")
            entry_base.delete("0",last="end")
        else:
            entry_radio.delete("0",last="end")
        entry_salida.config(state=tk.NORMAL)
        entry_salida.delete("0",last="end")
        entry_salida.config(state=tk.DISABLED)

    if 'titulo' in kwargs and kwargs['titulo'] == "AREA TRIANGULO":
         calcular = ttk.Button(ventana_secundaria, text="CALCULAR", command=areaTriangulo)
    else:
        calcular = ttk.Button(ventana_secundaria, text="CALCULAR", command=areaCirculo)
    calcular.place(x=110, y=140)

    delete = ttk.Button(ventana_secundaria, text="LIMPIAR", command=limpiar)
    delete.place(x=190, y=140)

    ventana_secundaria.mainloop()


boton_aTriangulo = ttk.Button(text="Area Triangulo", command=partial(calculoArea,titulo="AREA TRIANGULO",
                                                                     base="Base",altura="Altura"))
boton_aTriangulo.place(x=50, y=50)

boton_aCirculo = ttk.Button(text="Area Circulo", command=partial(calculoArea,titulo = "AREA CIRCULO",
                                                                  radio= "Radio"))
boton_aCirculo.place(x=200, y=50)

root.mainloop()
