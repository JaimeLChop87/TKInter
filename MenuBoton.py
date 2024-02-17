# impórtar las clases/modulos a usar
from tkinter import Tk, Label, Entry, Spinbox, Button, OptionMenu, StringVar,Menu, Menubutton,W,RIGHT

# funciones app
def Aceptar():
    Selecciones=''
    nombre= ENombre.get()
    direccion= EDireccion.get()
    municipio= VMunicipio.get()
    edad= EEdad.get()
    sexo=ESexo.get()
    if nombre: Selecciones= 'Nombre: '+nombre+'\n'
    if direccion: Selecciones += 'Direccion: '+direccion+'\n'
    if municipio != "Seleccionar Municipio":
        Selecciones += 'Municipio: '+municipio+'\n'
    if edad: Selecciones += "Edad: "+edad+'\n'
    if sexo != 'Pulse boton para seleccionar sexo':
        Selecciones += 'Sexo: '+sexo+'\n'
    LSeleccion.config(text=Selecciones)
    
def Cancelar():
    Mformulario.destroy()

def EsHombre():
    VSexo.set('Hombre')

def EsMujer():
    VSexo.set('Mujer')

# Ventana ppal
Mformulario= Tk()
Mformulario.title('Formulario 2.0')
Mformulario.resizable(True,False)
Mformulario.geometry('300x350')

# labels/etiquetas
LNombre= Label(Mformulario,text='Nombre: ',font=("Times New Roman", "10"),justify='right',anchor=W)
LNombre.grid(row=0,column=0,padx=5,pady=5)
LDireccion= Label(Mformulario,text='Dirección: ',font=("Times New Roman", "10"),justify='left',anchor=W)
LDireccion.grid(row=1,column=0,padx=5,pady=5)
LMunicipio= Label(Mformulario,text='Municipio: ',font=("Times New Roman", "10"),justify='left',anchor=W)
LMunicipio.grid(row=2,column=0,padx=5,pady=5)
LEdad= Label(Mformulario,text='Edad: ',font=("Times New Roman", "10"),justify='left',anchor=W)
LEdad.grid(row=3,column=0,padx=5,pady=5)
LSexo= Label(Mformulario,text='Sexo: ',font=("Times New Roman", "10"),justify='left',anchor=W)
LSexo.grid(row=4,column=0,padx=5,pady=5)
LSeleccion= Label(text='',padx=5, pady=5, justify='right',anchor=W)
LSeleccion.grid(row=5,column=0,padx=5,pady=5)

# Entradas/Dgitadas
ENombre=Entry(Mformulario, bd=5, highlightcolor='green',highlightthickness=2)
ENombre.grid(row=0,column=1,padx=5,pady=5,sticky=W)
EDireccion=Entry(Mformulario, bd=5, highlightcolor='green',highlightthickness=2)
EDireccion.grid(row=1,column=1,padx=5,pady=5,sticky=W)

#EntradaOptionMenu
#declaracion de la variable control para asignar lo seleccionado por el usuario
Municipios=['Envigado' ,'Bello','Medellin' ,'Copacabana','Itagui','Rionegro','Girardota','Barbosa','Caldas','Estrella']
VMunicipio= StringVar()
EMunicipio= OptionMenu(Mformulario, VMunicipio,*Municipios)
VMunicipio.set("Seleccionar Municipio")
EMunicipio.grid(row=2,column=1,padx=5,pady=5)

#EntradaSpinbox
EEdad= Spinbox(Mformulario, from_=18,to=115,wrap=True,width=5, highlightcolor='green',highlightthickness=2)
EEdad.grid(row=3,column=1,padx=5,pady=5,sticky=W)

#EntradaBoton
VSexo= StringVar()
ESexo= Entry(Mformulario,bd=5,state='disabled',textvariable=VSexo)
VSexo.set('Pulse boton para seleccionar sexo')

MSexo= Menubutton(Mformulario,text="Sexo", relief='raised')
MSexo.menu= Menu(MSexo,tearoff=0)
MSexo.menu.add_command(label='Hombre',command=EsHombre)
MSexo.menu.add_command(label='Mujer',command=EsMujer)
MSexo['menu']=MSexo.menu
ESexo.grid(row=4,column=1,padx=5,pady=5,sticky=W)
MSexo.grid(row=4,column=2,padx=5,pady=5,sticky=W)


#botones
BAceptar= Button(text='Aceptar',command=Aceptar)
BAceptar.grid(row=7,column=0,padx=5,pady=5)

BCancelar= Button(text='Cancelar',command=Cancelar)
BCancelar.grid(row=7,column=1,padx=5,pady=5)


# loopPpal
Mformulario.mainloop()