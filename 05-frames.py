from tkinter import *

ventana = Tk()
ventana.title = "Frames mit Tkinter"
ventana.geometry("700x450")
#----------------------------------------------------------
# Frames padre

frame_vater_top = Frame(ventana, width="200", height="200")
# el bg simplemente para saber que esta ahi y poder verlo
frame_vater_top.config(bg="lightblue")
frame_vater_top.pack(side=TOP, anchor=N, fill=X, expand=YES)

frame_vater_bottom = Frame(ventana, width="200", height="200")
frame_vater_bottom.config(bg="lightblue")
frame_vater_bottom.pack(side=BOTTOM, anchor=S, fill=X, expand=YES)

#-----------------------------------------------------------
# anidando los otros marcos dentro del padre

frame1 = Frame(frame_vater_top, width="200", height="200")
frame1.config(bg="red", bd="8", relief="solid")
frame1.pack(side=LEFT, anchor=NW)

# ----- anadiendo un label dentro del Frame rojo
frame1.pack_propagate(False)
Label(frame1, text="Color Rojo").pack(side=LEFT, anchor=CENTER, fill=X, expand=YES)

frame2 = Frame(frame_vater_bottom, width="200", height="200")
frame2.config(bg="green", bd="8", relief="solid")
frame2.pack(side=LEFT, anchor=SW)

# ----- anadiendo un label dentro del Frame verde
frame2.pack_propagate(False)
Label(frame2, text="Color Verde").pack(side=LEFT, anchor=CENTER, fill=X, expand=YES)

frame3 = Frame(frame_vater_top, width="200", height="200")
frame3.config(bg="yellow", bd="8", relief="solid")
frame3.pack(side=RIGHT, anchor=NE)

# ----- anadiendo un label dentro del Frame Amarillo
frame3.pack_propagate(False)
Label(frame3, text="Color Amarillo").pack(side=LEFT, anchor=CENTER, fill=X, expand=YES)

frame4= Frame(frame_vater_bottom, width="200", height="200")
frame4.config(bg="blue", bd="8", relief="solid")
frame4.pack(side=RIGHT, anchor=SE)

# ----- Variacion -> anadiendo un label dentro del Frame Azul
frame4.pack_propagate(False)

# variacion con una variable para poder configurar el texto
texto = Label(frame4, text="Color Azul")
texto.config(bg="blue", fg="white", font=("Arial", 20))
texto.pack(anchor=CENTER, fill=Y, expand=YES)


ventana.mainloop()