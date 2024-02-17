from tkinter import Tk, Label, NSEW


class PosicinamientoGrid():
    
    
    def __init__(self):
        self.Colores = ["#ABFFC2","#C17FDB","#4885EF","#3FD4BB","#55EB52","#D4D13F","#FFCD63","#F3D686","#D99A77","#F090AA","#B077D9","#A3B8FF"] 
        self.indcolor=0
        self.rows =  12
        self.colums= 1
        self.root=Tk()
        
        self.LabelCell()
        
        self.root.mainloop()
    
    def LabelCell(self):
        
        for row in range(self.rows):
            for colum in range(self.colums):
                self.etiqueta = Label(text=f"Etiqueta col {colum+1} fila {row+1}" ,fg=f"{self.Colores[self.indcolor-1]}", bg=f"{self.Colores[self.indcolor]}",font=("Comic Sans MS","12","bold italic"))
                self.etiqueta.grid(row=f"{row}",column=f"{colum}", padx=2,pady=2, sticky=NSEW)
                self.root.columnconfigure(colum,weight=1)
                self.root.rowconfigure(row,weight=1)
                self.indcolor+=1

Main = PosicinamientoGrid()
