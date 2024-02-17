# importa modulos
from tkinter import Tk,colorchooser,Button

# define funcion 
def select_color():
    color= colorchooser.askcolor(title="Seleciona un Color")
    boton.configure(bg=color[1])
print('FOF')
# crea ventana principal
WMain= Tk()
WMain.minsize(False,False)
# crea boton de seleccion
boton= Button(text="Seleccione un color", fg='blue', bd=5, command=select_color)
boton.pack(padx=50,pady=50)
# loop
WMain.mainloop()