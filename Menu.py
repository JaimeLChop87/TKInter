# importar clases
from tkinter import Tk,Label, Menu, PhotoImage

# funciones de la aplicacion
def salir():
    Wmain.destroy()

# ventana principal 
Wmain = Tk()

# barra menu la cual contendra las opcines principales 'archivo edicion ayuda
barraMenu= Menu(Wmain)
Wmain.config(menu=barraMenu)

# creacion MenuArchivo, contendra las opciones de nuevo, abrir, guardar, guardar como y salir
menuArchivo= Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label='Archivo',menu=menuArchivo)

menuArchivo.add_command(label='Nuevo')

#creacion Submenu Abrir
menuAbrir=Menu(menuArchivo,tearoff=0)
menuAbrir.add_command(label='Reciente')
menuAbrir.add_command(label='Historial')

# creacion opcipones del menuArchivo
menuArchivo.add_cascade(label='Abrir',menu=menuAbrir)
menuArchivo.add_command(label='Guardar')
menuArchivo.add_command(label='Guardar Como')
menuArchivo.add_separator()
menuArchivo.add_command(label='Salir', command=salir)
Img= PhotoImage()

#Asiganacion Submenu Abrir




# creacion MenuEdicion,Deshacer, Reahacer, Copiar, Pegar, Borrar, Seleccionar todo
menuEdicion= Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label='Edicion',menu=menuEdicion)

# creacion opcipones del menuEdicion
menuEdicion.add_command(label='Deshacer')
menuEdicion.add_command(label='Rehacer')
menuEdicion.add_separator()
menuEdicion.add_command(label='Copiar')
menuEdicion.add_command(label='Pegar')
menuEdicion.add_command(label='Borrar')
menuEdicion.add_separator()
menuEdicion.add_cascade(label='Seleccionar Todo')

# creacion MenuAyuda,Manual de ayuda, preguntas frecuentes, acerca de...

menuAyuda= Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label='Ayuda',menu=menuAyuda)
# creaciond e opciones para la ayuda
menuAyuda.add_command(label='Manual Usuario')
menuAyuda.add_command(label='preguntas frecuentes')
menuAyuda.add_command(label='Acerca de...')




Wmain.mainloop()

