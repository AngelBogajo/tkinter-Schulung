from tkinter import *

ventana = Tk()
ventana.geometry("700x400")
ventana.title("Formular mit Eingabenfeldern")

# encabezado
encabezado = Label(ventana, text="TKINTER FORMULAR - Angel J. Bogajo")
encabezado.config(
    fg="white",
    bg="Darkgrey",
    font=("Open sans", 18),
    padx=10,
    pady=10
)
# columnspan para que las cajas despues esten mas juntas
encabezado.grid(row=0, column=0, columnspan=12, sticky=W)

# Text Label(Name)
campo_texto_label = Label(ventana, text="Vorname")
campo_texto_label.grid(row=1, column=0, padx=5, pady=5)

# Text Entry(Name)
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="left", state="normal")# state normal or disabled para desabilitarlo

#------------------------------------------------

# Text Label(Nachname)
campo_texto_label = Label(ventana, text="Nachname")
campo_texto_label.grid(row=2, column=0, padx=5, pady=5)

# Text Entry(nachname)
campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="left", state="normal")

#-------------------------------------------------------

# Text Label(TEXT Beschreibung)
text_beschreibung_label = Label(ventana, text="Beschreibung")
text_beschreibung_label.grid(row=3, column=0, padx=5, pady=5, sticky=N)

# Text Beschreibung Entry
text_beschreibung = Text(ventana)
text_beschreibung.grid(row=3, column=1)
text_beschreibung.config(
    width=26,
    height=5,
    padx=5,
    pady=5,
    font=("Arial", 12)
)

#------------------------------------------

# Button
Label(ventana).grid(row=4, columnspan=10)

knopf = Button(ventana, text="Senden")
knopf.grid(row=5, column=1, sticky=W)
knopf.config(padx=8, pady=3, bg="black", fg="yellow")

ventana.mainloop()