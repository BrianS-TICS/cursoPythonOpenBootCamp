import tkinter as tk
from tkinter import StringVar, ttk
import sys

window = tk.Tk()

def ClickToRestart() :
    selected.set(None) 
    
def seleccionar(self) :
    print()

selected = tk.StringVar()
r1 = ttk.Radiobutton(window, text="Camisa simple", value="Camisa simple", variable=selected, command=seleccionar)

r1.pack()
r2 = ttk.Radiobutton(window, text="Camisa de vestir", value="Camisa de vestir", variable=selected, command=seleccionar)

r2.pack()
r3 = ttk.Radiobutton(window, text="Traje", value="Traje", variable=selected, command=seleccionar)
r3.pack()

btnRestart = ttk.Button(window, text="Reiniciar")
btnRestart.bind('<Button-1>', ClickToRestart)
btnRestart.pack()

window.mainloop()