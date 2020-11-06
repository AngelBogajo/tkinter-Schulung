from tkinter import *

ventana = Tk()
ventana.geometry("700x400")
ventana.config(
    bd=30
)


def getdato():
    resultado.set(dato.get())
    if len(resultado.get()) >= 1:
        text_obtenido.config(
            bg="yellow",
            fg="black"
        )


dato = StringVar()
resultado = StringVar()

Label(ventana, text="escribe un texto: ").pack(anchor=NW)

Entry(ventana, textvariable=dato).pack(anchor=NW)

Label(ventana, text="ensenar el texto: ").pack(anchor=NW)

text_obtenido = Label(ventana, textvariable=resultado)
text_obtenido.pack(anchor=NW)

Button(ventana, text="Mostrar", command=getdato).pack(anchor=NW)

ventana.mainloop()
