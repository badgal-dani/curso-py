# Importação da lib tkinter
from tkinter import *
import eq_quadratica as eq

class Application:
    def __init__(self, master=None):
        self.container1 = Frame(master)
        # self.container1["background"] = 'red'  # Coloca cor no container
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["pady"] = 10
        self.container2.pack()
        
        self.container3 = Frame(master)
        self.container3["pady"] = 5
        self.container3.pack()

        self.titulo = Label(self.container1, text="CALCULADORA EQUAÇÃO 2-GRAU")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.lbl_a = Label(self.container1, text="a: ")
        self.lbl_a["font"] = ("Arial", "10", "bold")
        self.lbl_a.pack(side=LEFT)

        self.txt_a = Entry(self.container1)
        self.txt_a["width"] = 10
        self.txt_a["font"] = ("Arial", "10", "bold")
        self.txt_a.pack(side=LEFT)

        self.lbl_b = Label(self.container1, text="b: ")
        self.lbl_b["font"] = ("Arial", "10", "bold")
        self.lbl_b.pack(side=LEFT)

        self.txt_b = Entry(self.container1)
        self.txt_b["width"] = 10
        self.txt_b["font"] = ("Arial", "10", "bold")
        self.txt_b.pack(side=LEFT)
        
        self.lbl_c = Label(self.container1, text="c: ")
        self.lbl_c["font"] = ("Arial", "10", "bold")
        self.lbl_c.pack(side=LEFT)

        self.txt_c = Entry(self.container1)
        self.txt_c["width"] = 10
        self.txt_c["font"] = ("Arial", "10", "bold")
        self.txt_c.pack(side=LEFT)
        
        self.btn_calcular = Button(self.container2)
        self.btn_calcular["text"] = "Calcular"
        self.btn_calcular["font"] = ("Calibri", "12")
        self.btn_calcular["width"] = 7
        self.btn_calcular["command"] = self.calcular
        self.btn_calcular.pack(side=LEFT)

        self.lbl_raizes = Label(self.container3, text="Resposta: ")
        self.lbl_raizes["font"] = ("Arial", "10", "bold")
        self.lbl_raizes.pack()
        
        
    def calcular(self):
        a = float(self.txt_a.get())
        b = float(self.txt_b.get())
        c = float(self.txt_c.get())
        
        raizes = eq.raiz_quad(a, b, c)
        self.lbl_raizes["text"] = f"{raizes}"

root = Tk()
Application(root)
root.mainloop()
