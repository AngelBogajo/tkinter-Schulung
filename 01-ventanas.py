# tkinter -> modulo para hacer interfaces graficas

from tkinter import *


class Programm:

    def __init__(self):
        self.title = "INTERFACE GRAFICA CON ANGEL J. BOGAJO"
        self.icon = "./imagenes/bilder.ico"
        self.size = "750x450"
        self.resizable = False


    def cargar(self):

        # crear la ventana raiz
        ventana = Tk()
        self.ventana = ventana

        # Titulo
        ventana.title(self.title)

        # icono de la ventana
        ventana.iconbitmap(self.icon)

        # cambiar el tamano de la ventana
        ventana.geometry(self.size)

        # hacer fija la dimensiones de la ventana
        if ventana.resizable:
            ventana.resizable(1, 1)
        else:
            ventana.resizable(0, 0)


    def addTexto(self):
        texto = Label(self.ventana, text="Hola, soy un texto desde el metodo addTexto")
        texto.pack()

# Variacion
    #def addTexto(self, Dato):
        #texto = Label(self.ventana, text="Dato")
        #texto.pack()

    def mostrar(self):
        self.ventana.mainloop()


# Instanciar mi programa
programm = Programm() # llamar a la clase con el constructor y a continuación a los métodos
programm.cargar()
programm.addTexto()
#programm.addTexto("Hi, How are you? ")
programm.mostrar()