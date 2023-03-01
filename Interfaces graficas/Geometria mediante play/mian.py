import tkinter
from tkinter import ttk
window = tkinter.Tk()

label1 = ttk.Label(window, text="Posicionamiento absoluto", background='blue', foreground='white')
label1.place(x=10, y=50)

label2 = ttk.Label(window, text="Yelow", background='yellow', foreground='black')
label2.place(x=0.10, y=0.50)

window.mainloop()
