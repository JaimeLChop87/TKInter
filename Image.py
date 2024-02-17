from tkinter import Tk, Label, Entry

Vppal = Tk()
Vppal.geometry("400x400")
Vppal.configure(cursor='sizing')


etiqueta = Label(text='reloj',compound='bottom',foreground='#DEAC2C', background='#4184D1', bd=5, relief='sunken')
etiqueta['bitmap']='question'
etiqueta.pack()
print(etiqueta.configure())
Vppal.mainloop() 


