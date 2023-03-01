import tkinter
window = tkinter.Tk()

label_saludo = tkinter.Label(window, text="Hola!", bg='blue', fg='white')
label_saludo.pack(ipadx=50, ipady=50, fill='both', side='left')


label_despedida = tkinter.Label(window, text="Adios!", bg='red', fg='white')
label_despedida.pack(ipadx=50, ipady=100, fill='both', expand=True)

window.mainloop()
