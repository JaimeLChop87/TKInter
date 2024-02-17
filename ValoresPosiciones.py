from tkinter import Tk, Label


# definir funciones

def MostrarPosicion():
    
    x,y = MainWin.winfo_pointerxy()
    window_x = MainWin.winfo_x()
    window_y = MainWin.winfo_y()
    Mouse_x = x
    Etiqueta.configure(text=f'{window_x}',)
    MainWin.after(10,MostrarPosicion)
    
    
MainWin = Tk()

Etiqueta = Label()
Etiqueta.pack()

MostrarPosicion()
MainWin.mainloop()