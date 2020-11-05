from tkinter import *

ventana = Tk()
#ventana.geometry("700x500") # anulo geometry para tamano automatico

texto1 = Label(ventana, text="Hola, soy el texto numero 1")
texto1.config(
    fg="white",
    bg="Black",
    padx=50,
    pady=20,
    font=("Consolas", 30)
)
texto1.pack(side=TOP)
# ----------------------------------------------------------------
texto2 = Label(ventana, text="texto numero 2")
texto2.config(
    height=3,
    pady=100,
    bg="Orange",
    cursor="circle",
    font=("Consolas", 14)
)
texto2.pack(side=TOP, fill=X, expand=YES)
# ----------------------------------------------------------------
texto3 = Label(ventana, text="texto numero 3")
texto3.config(
    height=3,
    pady=100,
    padx=30,
    fg="White",
    bg="Green",
    cursor="spider",
    font=("Arial", 18)
)
texto3.pack(side=LEFT, fill=X, expand=YES)

# ----------------------------------------------------------------
texto4 = Label(ventana, text="texto numero 4")
texto4.config(
    pady=100,
    padx=30,
    fg="White",
    bg="Pink",
    font=("Arial", 18)
)
texto4.pack(side=LEFT, fill=X, expand=YES)
# -------------------------------------
texto5 = Label(ventana, text="texto numero 5")
texto5.config(
    pady=100,
    padx=30,
    fg="black",
    bg="yellow",
    font=("Arial", 18)
)
texto5.pack(side=LEFT, expand=YES, fill=X)
# -------------------------------------
ventana.mainloop()