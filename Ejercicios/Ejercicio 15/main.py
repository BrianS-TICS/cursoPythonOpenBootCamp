import tkinter as tk
from tkinter import StringVar, ttk
import sys

window = tk.Tk()

username_label = ttk.Label(window, text="= Colores =")
username_label.pack()
lista = tk.Listbox(window, width=50)

lista.insert(1, "Blue")
lista.insert(2, "Yellow")
lista.insert(3, "Black")

lista.pack()

window.mainloop()