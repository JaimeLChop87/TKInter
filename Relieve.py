from tkinter import Tk,Label, Entry



TiposRelieves = ["FLAT", "GROOVE", "RIDGE", "SUNKEN", "RAISED"]

WindowsMain= Tk()
WindowsMain.geometry("450x450")
WindowsMain.title("Relieve")
WindowsMain.resizable(False,False)
WindowsMain.configure(bg='#3B523D')
#WindowsMain.attributes('-alpha',0.7)


Etiqueta1 = Label(text=f"Ver Relieve {TiposRelieves[0]}")
Entrada1 = Entry(bd=5, relief="flat")
Etiqueta1.pack(padx=5,pady=5)
Entrada1.pack(padx=5,pady=5)

Etiqueta2 = Label(text=f"Ver Relieve {TiposRelieves[1]}")
Entrada2 = Entry(bd=5, relief="groove")
Etiqueta2.pack(padx=5,pady=5)
Entrada2.pack(padx=5,pady=5)

Etiqueta3 = Label(text=f"Ver Relieve {TiposRelieves[2]}")
Entrada3 = Entry(bd=5, relief="ridge")
Etiqueta3.pack(padx=5,pady=5)
Entrada3.pack(padx=5,pady=5)

Etiqueta4 = Label(text=f"Ver Relieve {TiposRelieves[3]}")
Entrada4 = Entry(bd=5, relief="sunken")
Etiqueta4.pack(padx=5,pady=5)
Entrada4.pack(padx=5,pady=5)

Etiqueta5 = Label(text=f"Ver Relieve {TiposRelieves[4]}")
Entrada5 = Entry(bd=5, relief="raised")
Etiqueta5.pack(padx=5,pady=5)
Entrada5.pack(padx=5,pady=5)





WindowsMain.mainloop()