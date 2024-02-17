from tkinter import Tk, Label

Incre = 1
Tempo = 100
SizeStrMax = 40
SizeStr = SizeStrMin = 8

def ChangeSizeStr  ():
    global SizeStr, SizeStrMax,SizeStrMin,Incre
    
    if SizeStr > SizeStrMax or SizeStr < SizeStrMin:
        Incre = -Incre
    SizeStr += Incre
    
    etiqueta.configure(font=("Arial",str(SizeStr),"bold"))
    etiqueta.after(Tempo,ChangeSizeStr)
    


Vpal = Tk()
Vpal.geometry("400x400")
etiqueta = Label(text="cambiamos de tamaño ", font=("Arial",str(SizeStr),"bold"))

etiqueta.pack()
ChangeSizeStr()


Vpal.mainloop()