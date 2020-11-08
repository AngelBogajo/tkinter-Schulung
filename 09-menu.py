# Beispiel -> Wie Menu & submenu erstellen soll

from tkinter import *

window = Tk()
window.geometry("500x500")

mein_menu = Menu(window)
window.config(menu=mein_menu)

# Submenu file
file = Menu(mein_menu, tearoff=0)
file.add_command(label="New Projekt")
file.add_command(label="Open")
file.add_separator()
file.add_command(label="Save All")
file.add_command(label="Settings")

# Hauptmenü
mein_menu.add_cascade(label="File", menu=file)
mein_menu.add_command(label="Edit")
mein_menu.add_command(label="Code")
mein_menu.add_command(label="Help")
mein_menu.add_command(label="Exit", command=window.quit)


window.mainloop()