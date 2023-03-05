import tkinter
from tkinter import ttk

window = tkinter.Tk()

def saludar(event) :
    print("Hola")

def saludarDobleClick(event) :
    print("Hola diste dos clicks")

boton = ttk.Button(window, text="Haz click")
boton.bind('<Button-1>', saludar)
boton.bind('<Double-1>', saludarDobleClick)
boton.pack()


window.mainloop()
