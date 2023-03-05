import tkinter
from tkinter import ttk

import random

window = tkinter.Tk()

colors = ["blue", "red", "yellow", "green", "black"]

label1 = ttk.Label(window, text="Posicionamiento absoluto", background='blue', foreground='white')
label1.place(x=10, y=50)

for x in range(0, 10) :
    color = random.randint(0, len(colors)-1)
    color2 = random.randint(0, len(colors)-1)
    label = tkinter.Label(window, text="etiqueta!", bg=colors[color], fg=colors[color2])
    label.place(x=random.randint(0,100), y=random.randint(0,100))

label2 = ttk.Label(window, text="Yelow", background='yellow', foreground='black')
label2.place(x=0.10, y=0.50)

window.mainloop()
