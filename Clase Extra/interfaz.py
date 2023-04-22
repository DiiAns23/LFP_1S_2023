from fileinput import filename
from tkinter.filedialog import askopenfilename
from tkinter.tix import Tree
from tkinter import Tk
from tkinter import *
from tkinter import ttk
from analizador_lexico import instruccion, operar_ , getErrores

class Pantalla_Principal():
    
    def __init__(self):
        self.PP = Tk()
        self.PP.title("Pantalla Principal Proyecto 1")
        self.centrar(self.PP, 1000, 500)
        self.PP.configure(bg="#102027")
        self.pantalla_1()
            

    def centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        anchura_pantalla = r.winfo_screenwidth()
        x = (anchura_pantalla // 2) - (ancho//2)
        y = (altura_pantalla//2) - (alto//2)
        r.geometry(f"+{x}+{y}")

    def pantalla_1(self):
        self.Frame = Frame(height=500, width=800)
        self.Frame.config(bg="#37474f")
        self.Frame.pack(padx=25, pady=25)
        self.text = ''
        Button(self.Frame,command=self.abrir_archivo,text="Abrir Archivo", font=("Times New Roman", 20), fg="#ffffff", bg = "#ff6f00", width=10).place(x=310, y=50)

        Button(self.Frame,command=self.ejecutar,text="Ejecutar", font=("Times New Roman", 20), fg="#ffffff", bg = "#ff6f00", width=10).place(x=310, y=150)

        Button(self.Frame,command=self.getErrores,text="Errores", font=("Times New Roman", 20), fg="#ffffff", bg = "#ff6f00", width=10).place(x=310, y=250)

        # Button(self.Frame,command=self.getErrores,text="Grafo", font=("Times New Roman", 20), fg="#ffffff", bg = "#ff6f00", width=10).place(x=310, y=250)

        Text(self.Frame,font=("Times New Roman",15),fg="black", width=60, height=5).place(x=100,y=350)

        self.Frame.mainloop()

    def abrir_archivo(self):
        x = ""
        Tk().withdraw()
        try:
            filename = askopenfilename(title='Selecciona un archivo',
                                            filetypes=[('Archivos', f'*.json')])
            # print(filename)
            with open(filename, encoding='utf-8') as infile:
                x = infile.read()
            # print(str(x))
        except:
            print('Error, no se ha seleccionado ningun archivo')
            return
        
        self.texto = x
        print(self.texto)

    def ejecutar(self):
        instruccion(self.texto)
        respuestas = operar_()
        for respuesta in respuestas:
            print(respuesta.operar(None))
    
    def getErrores(self):
        lista_errores = getErrores()
        contador = 1
        print('{')
        while lista_errores:
            error = lista_errores.pop(0)
            print(error.operar(contador), ',')
            contador += 1
        print('}')

r = Pantalla_Principal()
