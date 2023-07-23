import tkinter
from tkinter import ttk
from tkinter import Radiobutton
from tkinter import StringVar,IntVar
import pprint
from tkinter import filedialog

if __name__ == '__main__':

    window = tkinter.Tk()
    window.config(bg='black')
    window.resizable(1,1)
    window.title("VENTANA DEMO 1")

    #Configuración Frame
    frame1 = tkinter.Frame(window)
    frame1.config(bg='lightblue',width=480,height=320,relief="sunken")
    frame1.pack(padx=10,pady=10,fill="both",expand=1)

    #Configuracion de titulo

    title = ttk.Label(frame1,text="SELECCIONE VELOCIDAD DE TRANSMISIÓN (bps)")
    title.config(background='lightblue',
                 justify='center',
                 font=("Helvetica",20),borderwidth=100)
    title.grid(row=0,column=2,pady=2)

    #Configuracion checklist



    list_option = { "1200" : 1200,
                    "4800": 4800,
                    "9600": 9600,
                    "19200": 19200,
                    "11520 ": 115200}

    count = 2
    bps = IntVar()

    def valor():
        global bps
        a = bps.get()
        print(f"Hola {a}")


    for (key,val) in list_option.items():

        radio = Radiobutton(frame1, text=key , variable=bps , value= val,command=valor)
        radio.config(justify='center',font=("Helvetica",20),bg='lightblue')
        radio.grid(row=count,column=2)
        count = count+1


    window.mainloop()


