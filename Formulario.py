# imprtar clase TK
from tkinter import Tk, Label, Button, Entry, Spinbox,W,E,EW

def Aceptar():
    Selecciones=''
    nombre= NombreEntry.get()
    direccion= DireccionEntry.get()
    edad= EdadSpinbox.get()
    if nombre:Selecciones= 'Nombre: '+nombre+'\n'
    if direccion:Selecciones += 'Direccion: '+direccion+'\n'
    Selecciones += 'Edad: '+edad
    
    SeleccionLabel.config(text=Selecciones)
    
def Cancelar():
    NombreEntry.delete(0,'end')
    DireccionEntry.delete(0,'end')
    EdadSpinbox.delete(0,'end')
    EdadSpinbox.insert(0,18)
    SeleccionLabel.config(text='')

# variables del porgrama
edad_min=18
edad_max=105

# ventana principal
FormularioMain= Tk()
FormularioMain.title('Formulario Usuario')
FormularioMain.resizable(True,False)
FormularioMain.minsize(300,150)

# nombre
NombreLabel= Label(text='Nombre:')
NombreEntry= Entry(bd=2,highlightcolor='red', highlightthickness=2)

# Direccion
DireccionLabel= Label(text='Direccion:')
DireccionEntry= Entry(bd=2,highlightcolor='red', highlightthickness=2)

# edad
EdadLabel= Label(text='Edad:')
EdadSpinbox= Spinbox(from_=edad_min,to=edad_max, width=3, bd=5,highlightcolor='red',highlightthickness=2)

# Botones
# pendiente anexar funciones
ButtonCancelar=Button(text='CANCELAR',command=Cancelar)
ButtonAceptar=Button(text='ACEPTAR',command=Aceptar)

# etiqueta de datos introducidos
SeleccionLabel=Label(padx=2,pady=2, justify='left') 

# posicionamiento
NombreLabel.grid(row=0,column=0,padx=2,pady=2, sticky=W)
NombreEntry.grid(row=0,column=1,padx=2,pady=2, sticky=EW)
DireccionLabel.grid(row=2,column=0,padx=2,pady=2, sticky=W)
DireccionEntry.grid(row=2,column=1,padx=2,pady=2, sticky=EW)
EdadSpinbox.grid(row=3,column=1,padx=2,pady=2, sticky=W)
ButtonCancelar.grid(row=4,column=0,padx=2,pady=2, sticky=W)
ButtonAceptar.grid(row=4,column=1,padx=2,pady=2, sticky=E)

SeleccionLabel.grid(row=5,column=0, columnspan=2, sticky=EW)

FormularioMain.columnconfigure(1,weight=1)

FormularioMain.mainloop()
