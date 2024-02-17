# creacion cronometro estilo HH:MM:SS --> 99:59:59

# importar las clases necesarias -- > importar opcion variable control
from tkinter import Tk, Label, Button, StringVar

# variables
# valor inicial horas minutos segudos 
Hr=Min=Seg=0
# estado incial del cronometro indica si esta en marcha o no
Inicio=False

# Funciones-metodos del cronometro

def CorrerTiempo  ():
    global Hr,Min,Seg
    
    if Inicio:
        Seg+=1
        if Seg==60:
            Min+=1
            Seg=0
        if Min==60:
            Hr+=1
            Seg=0
            Min=0
        if Hr==99:
            Seg=0
            Min=0
            Hr=0
    
    # formato para mostrar los primeros digitos 0n°
    if Hr < 10: HrStr = '0'+str(Hr)
    else: HrStr= str(Hr)
    if Min < 10: MinStr= '0'+str(Min)
    else: MinStr = str(Min)
    if Seg < 10: SegStr = '0'+str(Seg)
    else: SegStr = str(Seg)
    
    VariableControl.set(HrStr+':'+MinStr+':'+SegStr)
    MainCronometro.after(1000,CorrerTiempo)

def Iniciar  ():
    global Hr,Min,Seg,Inicio
    
    if not(Inicio):
        VariableControl.set('00:00:00')
        Hr=Min=Seg=0
        Inicio=True
        MainCronometro.after(1000,CorrerTiempo)

def Detener  ():
    global Inicio
    
    Inicio=False

# Ventana principal
MainCronometro=Tk()
MainCronometro.title("El Cronometro")
MainCronometro.resizable(False,False)
MainCronometro.geometry('500x250')

# variable de control con valor inicial '00:00:00'
VariableControl=StringVar(value='00:00:00') 

# etiqueta cronometro
EtiquetaCronometro=Label(textvariable=VariableControl,bg='blue',font=("Comic Sans MS","24","bold italic"),padx=10,pady=10)
EtiquetaCronometro.pack(side='bottom', padx=10,pady=10)

# buton de inicio y boton de parar, asignar funcion mediate la opcion command
BotonIniciar=Button(command=Iniciar,text='Iniciar',font=("Comic Sans MS","12","bold italic"),fg='white',foreground='green',padx=10,pady=10)
BotonIniciar.pack(side='left',padx=10,pady=10)
BotonIniciar.flash()
BotonDetener=Button(command=Detener,text='Detener',font=("Comic Sans MS","12","bold italic"),fg='white',foreground='red',padx=10,pady=10)
BotonDetener.pack(side='right',padx=10,pady=10)


MainCronometro.mainloop()

