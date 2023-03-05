import tkinter
from tkinter import StringVar, ttk
import random

window = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

lista = ["Windows", "Macos", "Ms2", "AmigaOs", "Be0s"]
listaItems= StringVar(value=lista)
listBox = tkinter.Listbox(window, height=20, listvariable=listaItems)
listBox.grid(column=0, row=0, sticky=tkinter.W)


selected = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text="si", value=1, variable=selected)
r2 = ttk.Radiobutton(window, text="no", value=2, variable=selected)
r3 = ttk.Radiobutton(window, text="quiza", value=3, variable=selected)

r1.grid(column=0, row=1, pady=5, padx=5)
r2.grid(column=0, row=2, pady=5, padx=5)
r3.grid(column=0, row=3, pady=5, padx=5)

# Frames
frame = ttk.Frame(window)
frame['relief'] = 'sunken'
frame.grid(column=0, row=0, sticky=tkinter.W)

label = ttk.Label(frame, text='tete')
label.grid(column=0, row=0, sticky=tkinter.W, padx=60, pady=50)

window.mainloop()
