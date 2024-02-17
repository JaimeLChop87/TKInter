# creacion de reloj digital
from tkinter import Tk,Label, StringVar
import time

# funcion mostrar reloj actualizado
def ActualizarHora ():
    hora = time.strftime('%H:%M:%S')
    variableControl.set(hora)
    MainRelog.after(1000,ActualizarHora)
    

# ventana ppal
MainRelog =  Tk()
MainRelog.resizable(False,False)
# variable control
variableControl = StringVar()


# creacion etiqueta
# configuracion de etiqueta, asiganacion de variable control
Reloj = Label(textvariable=variableControl,fg="red",font=("Comic Sans MS","24","bold italic"),padx='200',pady='100')
# empaquetamiento etiqueta
Reloj.pack()

ActualizarHora ()


MainRelog.mainloop()
