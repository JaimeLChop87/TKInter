# importar clases
from tkinter import Tk, Label, Button, Entry, END as end

# funciones de los botones
# aceptar para este caso solo desaparece la ventana simulando un acceso
def Aceptar():
    MainLogin.destroy()


def Cancelar():
    UserEntry.delete(0,end)
    ContrasenaUserEntrey.delete(0,end)


# root main
MainLogin= Tk()
MainLogin.resizable()
MainLogin.title("Login User")

# Labels/Entry
UserLabel= Label(text='USUARIO: ')
UserEntry= Entry(bd=5,highlightthickness=5, highlightcolor='red')

ContrasenaUserLabel= Label(text='CONTRASEÑA: ')
ContrasenaUserEntrey= Entry(bd=5,show='*',highlightthickness=2, highlightcolor='red')

# botones
BotonAceptar= Button(text='ACEPTAR', command=Aceptar)
BotonCancelar= Button(text='CANCELAR', command=Cancelar)

UserLabel.pack()
UserEntry.pack()
ContrasenaUserEntrey.pack()
ContrasenaUserLabel.pack()
BotonAceptar.pack()
BotonCancelar.pack()

MainLogin.mainloop()

