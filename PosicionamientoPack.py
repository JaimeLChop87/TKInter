from tkinter import Tk,Label,TOP,BOTTOM, RIGHT,LEFT


class Posicionamiento():
    
    def __init__(self):
        self.VentPpal = Tk()
        self.VentPpal.title("PracticaPosicionamiento")
        self.VentPpal.geometry("500x500")
        self.VentPpal.resizable(True,True)
        #self.VentPpal.maxsize(800,800)
        #self.VentPpal.minsize(300,300)
        self.TextoPosicionBottom()
        self.TextoPosicionTop()
        self.TextoPosicionLeft()
        self.TextoPosicionRight()
        
        self.VentPpal.mainloop()
    
    def TextoPosicionTop(self):
        
        for HacerEtquita in range(0,3):
            
            self.Texto=  Label (text=f"Etiqueta \n Label Top {HacerEtquita+1}")   
            self.Texto.pack(side=TOP,padx=10, pady=5)        
        
    def TextoPosicionBottom(self):
        
        for HacerEtquita in range(0,3):
            
            self.Texto=  Label (text=f"Etiqueta \n Label Botton{HacerEtquita+1}")   
            self.Texto.pack(side=BOTTOM,padx=10, pady=5)
    
    def TextoPosicionLeft(self):
        
        for HacerEtquita in range(0,3):
            
            self.Texto=  Label (text=f"Etiqueta \n Label Left{HacerEtquita+1}")   
            self.Texto.pack(side=LEFT,padx=10, pady=5)        
        
    def TextoPosicionRight(self):
        
        for HacerEtquita in range(0,3):
            
            self.Texto=  Label (text=f"Etiqueta \n Label Right{HacerEtquita+1}")   
            self.Texto.pack(side=RIGHT,padx=10, pady=5) 

muestra = Posicionamiento()