from tkinter import Tk, Label, Entry
from random import randint

texto = "celebre"
periodo = 400


def modificarFoco(campo_actual):
    
    estado= "EN CURSO"
    textoCampoActual = campo_actual.get()
    if texto[0:len(textoCampoActual)] != textoCampoActual:
        estado = "OK"
        

    
def Campos():
        
    for camp in range(4):
        campo = Entry(font=("Arial",24,"bold"),highlightcolor="green",bd=5,highlightthickness=2)
        campo.pack(padx=10,pady=10)     
        print (camp)  
        if camp == 0:
            campo.focus_get()

Vppal = Tk()
Vppal.title("FocusFocus")
Vppal.resizable(False,False)

Campos()




Vppal.mainloop()
