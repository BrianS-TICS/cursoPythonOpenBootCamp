import tkinter
from tkinter import ttk
window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

# Username
username_label = ttk.Label(window, text="Username:")
username_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

username_entry = ttk.Entry(window)
username_entry.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)

# Password
password_label = ttk.Label(window, text="Password:")
password_label.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

password_entry = ttk.Entry(window, show="*")
password_entry.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5)

# Boton
login_button = ttk.Button(window, text="Acceder")
login_button.grid(column=1, sticky=tkinter.E, row=3, pady=5, padx=5)
window.mainloop()
