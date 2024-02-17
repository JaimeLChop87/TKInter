from tkinter import Tk,Label, Button, Listbox, StringVar


# funcion traducir

def Traducir():
    seleccion= ListaEntradas.curselection() 
    if seleccion !=():
        idiomaseleccion= ListaEntradas.get(seleccion)
        if idiomaseleccion == 'Ingles': traduccion='Hello'
        elif idiomaseleccion == 'Frances': traduccion='Salut'
        elif idiomaseleccion == 'Italiano': traduccion='Ciao'
        elif idiomaseleccion == 'Aleman': traduccion='Hallo'
        PalabraTraducida.configure(text=traduccion)


# ventana principal
TraductorMain= Tk()
TraductorMain.resizable(False,False)


# declaracion de la variable de control
VarControlIndioma= StringVar(value='Ingles Frances Italiano Aleman')

# widgets
PalabraTraducir=Label(text='hola',font=('Arial',12,'bold italic'))
BotonTradudir=Button(text='<-->',command=Traducir)
PalabraTraducida=Label(text='?¿',font=('Arial',13,'bold italic'))
ListaEntradas= Listbox(listvariable=VarControlIndioma,height=4,bd=3)

#posicionamiento

PalabraTraducir.grid(row=0,column=0,padx=5,pady=5)
BotonTradudir.grid(row=0,column=1,padx=5,pady=5)
PalabraTraducida.grid(row=0,column=2,padx=5,pady=5)
ListaEntradas.grid(row=1,column=1,padx=5,pady=5)



TraductorMain.mainloop()