from tkinter import Tk , Label # importar modulo y widgets a usar

class Aplicativo (): # creacion de clase Aplicacion
    
    def __init__(self, TextVentana): # definicion constructor 
        self.Vppal = Tk() # Llamdo metodo TK
        self.Vppal.title("Laprimera") # titulo ventana
        self.Vppal.geometry("60x800") # asiganacion geometria ventana
        self.Vppal.maxsize(400,400) # asiganacion de valores maximos y minos de la ventana
        self.Vppal.minsize(400,400) # asiganacion de valores maximos y minos de la ventana
        self.Vppal.resizable(False,False) # Permitir modificacion geometria ventana
        self.TextoPpal(TextVentana)
        self.TextoPpal.pack()
        self.Vppal.mainloop() # llamado bucle apliacacion
        
    def TextoPpal (self,TextVentana): # creacion del metodo mostrar mensaje en pantalla
        self.TextoPpal = Label(text=f"{TextVentana}")
        
        
        

Vtana = Aplicativo("Primera Ventana de TKinter")


