# Importação da lib tkinter
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["pady"] = 5
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["pady"] = 10
        self.container4.pack()

        self.titulo = Label(self.container1, text="Sign in")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.lbl_user = Label(self.container1, text="Usuário: ")
        self.lbl_user["font"] = ("Arial", "10", "bold")
        self.lbl_user.pack(side=LEFT)

        self.txt_user = Entry(self.container1)
        self.txt_user["width"] = 20
        self.txt_user["font"] = ("Arial", "10", "bold")
        self.txt_user.pack(side=LEFT)

        self.lbl_pass = Label(self.container2, text="Senha: ")
        self.lbl_pass["font"] = ("Arial", "10", "bold")
        self.lbl_pass.pack(side=LEFT)

        self.txt_pass = Entry(self.container2)
        self.txt_pass["width"] = 20
        self.txt_pass["font"] = ("Arial", "10", "bold")
        self.txt_pass["show"] = "*"
        self.txt_pass.pack(side=LEFT)

        self.login = Button(self.container3)
        self.login["text"] = "Login"
        self.login["font"] = ("Calibri", "8")
        self.login["width"] = 5
        self.login["command"] = self.log_sistema
        self.login.pack(side=RIGHT)
        
        self.sair = Button(self.container3)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "8")
        self.sair["width"] = 5
        self.sair["command"] = self.container3.quit
        self.sair.pack(side=LEFT)
        
        self.lbl_resultado = Label(self.container4, text="")
        self.lbl_resultado["font"] = ("Arial", "10", "bold")
        self.lbl_resultado.pack()

    def log_sistema(self):
        usuario = self.txt_user.get()
        senha = self.txt_pass.get()
        if usuario == senha:
            self.lbl_resultado["text"] = "Usuário inválido!"
        else:
            self.lbl_resultado["text"] = "Bem-vinda ao sistema, querida!"
root = Tk()
Application(root)
root.mainloop()
