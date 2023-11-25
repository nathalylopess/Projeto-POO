from tkinter import *

class App:
   def __init__(self):
        
        self.janela = Tk()
        self.janela.title('Sistema de Cadastro de Eventos')
        self.janela.geometry('710x400')
        self.janela.eval('tk::PlaceWindow . center')
        self.janela.resizable(width = False, height = False)

        self.frame_logo = Frame(self.janela, bg='red', height=400, width=355)
        self.frame_logo.place(x=0, y=0)

        self.frame_conteudo = Frame(self.janela, bg='blue', height=400, width=355)
        self.frame_conteudo.place(x=355, y=0)

        self.labelteste = Label(self.frame_conteudo, text='oi', bg='white', height=2, width=10)
        self.labelteste.place(x=355, y=1)

        self.butao_entrar = Button(self.frame_conteudo, text='Entrar', fg='black', height=2, width=15, bg='purple')
        self.butao_entrar.place(x=355, y=1)

#       self.frame_cadastroinicial = Frame(self.label_conteudo, bg='yellow', height=120, width=50)
#       self.frame_cadastroinicial.pack()


        self.janela.mainloop()

aplicacao=App()