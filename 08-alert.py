from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.config(bd=70)


def alerta():
    messagebox.showinfo("CUIDADIN!!", "Estoy aprendiendo pero mucho, ehh!!")
    messagebox.showwarning("Cuidado", "Pollo!!")
    messagebox.showerror("Uppss!!", "Error")


boton = Button(ventana, text="Mostrar alerta", command=alerta).pack()


# ---------------------------------------------------------------------


def salir(nombre):
    resultado = messagebox.askquestion("Salir", "Quieres salir?", )
    if resultado == "yes":
        messagebox.showinfo("Ciao!", f" Adios {nombre}")
        ventana.destroy()

# funcion lambda para que no se carge directamente los parametros de la funcion salir
# sin la funcion lambda se ejecutaria directamente al arrancar el programa la funcion salir


boton1 = Button(ventana, text="Mostrar Mensaje", command=lambda: salir("Angel J. Bogajo")).pack()

ventana.mainloop()
