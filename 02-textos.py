from tkinter import *

ventana = Tk()
ventana.geometry("700x500")

texto1 = Label(ventana, text="Hola, soy el texto numero 1")
texto1.config(
    fg="white",
    bg="Black",
    padx=50,
    pady=20,
    font=("Consolas", 30)
)
texto1.pack()
# ----------------------------------------------------------------
texto2 = Label(ventana, text="Hola, soy el texto numero 2")
texto2.config(
    height=3,
    pady=100,
    bg="Orange",
    cursor="circle",
    font=("Consolas", 14)
)
texto2.pack(anchor=SW)
# ----------------------------------------------------------------
texto3 = Label(ventana, text="Hola, soy el texto numero 3")
texto3.config(
    height=3,
    pady=100,
    padx=30,
    fg="White",
    bg="Green",
    cursor="spider",
    font=("Consolas", 14)
)
texto3.pack(anchor=NE)
# -------------------------------------
ventana.mainloop()