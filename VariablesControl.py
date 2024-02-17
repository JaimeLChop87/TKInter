from tkinter import Tk, Label, StringVar

texto = "Aviso de prueba..."
intervalo = 150

textoAuxiliar = texto + " " * len(texto)

def Desplazar():
    
    global texto, textoAuxiliar
    
    ultimoCaracter = textoAuxiliar[len(textoAuxiliar)-1]
    textoAuxiliar = textoAuxiliar[:-1]
    textoAuxiliar = ultimoCaracter + textoAuxiliar
    variableControl.set(textoAuxiliar[0:len(texto)])
    mainW.after(intervalo,Desplazar)

mainW = Tk()
mainW.title("se desplaza")

variableControl = StringVar()


etiqueta = Label(textvariable= variableControl, width= len(texto), padx=10,pady=10,fg="green",font=("Arial",'22','bold'))
etiqueta.pack()

Desplazar()
mainW.mainloop()
