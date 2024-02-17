from tkinter import Tk, Entry, Label,NSEW,W

def EncabezadoPPal (CantMeses):
    TextoEncabezado = Label(text= "Gastos mensuales personales" ,fg=Colores[4] ,font=("Comic Sans MS","14","bold"), anchor=W)
    TextoEncabezado.grid(row=0,column=0,columnspan=CantMeses,sticky=NSEW)

def Entrada(CantMeses):
    for TipoApto in range(CantMeses):
        TextTipoApto = Label(text=f"Mes{TipoApto+1}",bg=Colores[1],fg=Colores[3],font=("Comic Sans MS","8","bold italic")) 
        TextTipoApto.grid(row=1,column=TipoApto+1,sticky=NSEW)
        
    for Piso in range(Pisos):
        TexPiso = Label(text=f"Detalle de Actividad {Piso+1}", bg=Colores[1],fg=Colores[3],font=("Comic Sans MS","8","bold italic"))
        TexPiso.grid(row=Piso+2,column=0,sticky=NSEW)
        for TipoApto in range(CantMeses):
            CampoIngreso=Entry(bg=Colores[2],fg=Colores[4],font=("Comic Sans MS","8","italic"),highlightcolor=Colores[3],highlightthickness=1.5)
            CampoIngreso.grid(row=Piso+2,column=TipoApto+1, padx=1,pady=1)
            


Colores = ["#668CD9","#949AA6","#CCD0D9","#1B78F2","#2D3540","#000000","#FFFFFF"]
CantMeses = 12
MainWindow = Tk()
MainWindow.title("Foco")
MainWindow.geometry("1200x400")
MainWindow.configure(background=Colores[1])

#for apto in range(CantMeses):
#    MainWindow.columnconfigure(apto ,weight=1)



Pisos = 12
EncabezadoPPal(CantMeses+1)
Entrada(Pisos)




MainWindow.mainloop()
