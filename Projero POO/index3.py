import tkinter as tk, time, sqlite3
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import traceback
from PIL import ImageTk, Image
import sqlite3


class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("Sistema de Cadastro de Eventos ")
        self.width = 850
        self.height = 493
        self.screenwidth = self.root.winfo_screenwidth()
        self.screenheight = self.root.winfo_screenheight()
        self.alignstr = '%dx%d+%d+%d' % (self.width, self.height, (self.screenwidth - self.width) / 2, (self.screenheight - self.height) / 2)
        self.root.geometry(self.alignstr)
        self.root.resizable(width=False, height=False)

        self.deu_certo_ou_nao = 1

        self.label_logo = tk.Label(
            self.root, 
            bg="#F0F0F0", 
            fg="#393d49", 
            justify="center"
        )
        self.label_logo.place(x=0, y=0, width=355, height=495)

        self.imagemCarregada = PhotoImage(file='imagem.png').subsample(20)
        self.imagem1 = Label(self.label_logo, image=self.imagemCarregada)
        self.imagem1.pack()

        self.label_conteudo = tk.Label(
            self.root, 
            justify='center', 
            bg="#D7842A", 
            borderwidth='0px', 
            fg="#333333",
        )
        self.label_conteudo.place(x=350, y=0, width=500, height=494)

    
        self.imagemCarregada = PhotoImage(file='imagem.png')
        self.imagem1 = Label(self.label_logo,image=self.imagemCarregada)
        self.imagem1.pack()


        self.label_conteudo = tk.Label(
               self.root, 
               justify='center', 
               bg = "#D7842A", 
               borderwidth='0px', 
               fg = "#333333",
          )
        self.label_conteudo.place(x=350,y=0,width=500,height=494)

        self.msg_title = tk.Message(
               self.root,
               anchor ='center',
               justify = 'center',
               fg = '#333333',
               text = "CADASTRO DE EVENTOS",
               relief = "raised", 
               bg = "#D7842A",
               borderwidth='0px',
               width='130px'
               )
        self.msg_title.place(x=350,y=0,width=500,height=43)

        self.msg_seusdados = tk.Message(
               self.root,
               fg ="#333333",
               justify ='center',
               text = "Seus dados",
               bg = "#D7842A",
               borderwidth='0px',
               width='130px'
               )
        self.msg_seusdados.place(x=350,y=50,width=104,height=30)


        self.msg_nome = tk.Message(
               self.root,
               fg = "#333333",
               justify = "left",
               text =  "Nome:",
               bg = "#D7842A",
               borderwidth='0px',
               width='130px')
        self.msg_nome.place(x=360,y=90,width=80,height=25)
          
        self.texto_aux_nome = StringVar()
        self.label_nome = tk.Entry(
               self.root,
               bg = '#ffffff',
               borderwidth = '1px',
               justify = 'center',
               fg = "#333333",
               textvariable = self.texto_aux_nome
          )
        self.label_nome.place(x=440,y=90,width=351,height=25)
          

        self.msg_email =tk.Message(
               self.root,
               justify ="left",
               text = "E-mail:",
               fg = "#333333",
               bg = "#D7842A",
               borderwidth='0px',
               width='130px')
        self.msg_email.place(x=360,y=120,width=80,height=25)

        self.texto_aux_email = StringVar()
        self.label_email = tk.Entry(
               self.root,
               borderwidth = '1px',
               fg = "black",
               justify='center',
               bg = "#ffffff",
               textvariable = self.texto_aux_email)
        self.label_email.place(x=440,y=120,width=351,height=25)

        self.msg_dadosevento =tk.Message(
               self.root,
               fg = "#333333",
               justify='left',
               text = "Dados do Evento",
               bg = "#D7842A",
               borderwidth='0px',
               width='130px'
               )
        self.msg_dadosevento.place(x=350,y=170,width=144,height=32)

        self.msg_nomedoevento = tk.Message(
               self.root,
               justify='left',
               text='Nome do Evento:',
               fg="#333333",
               bg = "#D7842A",
               borderwidth='0px',
               width='130px')
        self.msg_nomedoevento.place(x=360,y=210,width=100,height=30)

        self.texto_aux_nome_evento = StringVar()
        self.label_nome_evento = tk.Entry(
               self.root,
               borderwidth='1px',
               bg="#ffffff",
               justify='center',
               fg="#333333",
               textvariable= self.texto_aux_nome_evento)
        self.label_nome_evento.place(x=470,y=210,width=321,height=25)

        self.msg_datadoevento = tk.Message(
               self.root,
               justify='left',
               fg="#333333",
               text= 'Data do Evento',
               bg = "#D7842A",
               borderwidth='0px',
               width='130px')
        self.msg_datadoevento.place(x=360,y=240,width=100,height=30)

        self.texto_aux_data = StringVar()
        self.label_entry_data = tk.Entry(
               self.root,
               bg="#ffffff",
               borderwidth='1px',
               fg= "black",
               justify='center',
               textvariable= self.texto_aux_data)
        self.label_entry_data.place(x=470,y=240,width=321,height=25)

        self.msg_temadoevento = tk.Message(
               self.root,
               justify='left',
               fg="#333333",
               text="Tema do Evento",
               bg = "#D7842A",
               borderwidth='0px',
               width='130px')
        self.msg_temadoevento.place(x=360,y=270,width=100,height=25)

        self.texto_aux_tema = StringVar()
        self.label_entry_tema = tk.Entry(
             self.root,
             bg="#ffffff",
             borderwidth='1px',
             fg= "black",
             justify='center',
             textvariable=self.texto_aux_tema)
        self.label_entry_tema.place(x=470,y=270,width=321,height=25)

        self.msg_localdoevento = tk.Message(
               self.root,
               justify='left',
               fg="#333333",
               text="Local do Evento",
               bg = "#D7842A",
               borderwidth='0px',
               width='130px')
        self.msg_localdoevento.place(x=360,y=300,width=100,height=25)

        self.texto_aux_local = StringVar()
        self.label_entry_local=tk.Entry(
               self.root,
               bg="#ffffff",
               borderwidth='1px',
               fg= "black",
               justify='center',
               textvariable=self.texto_aux_local)
        self.label_entry_local.place(x=470,y=300,width=321,height=25)

        self.button_inserir = tk.Button(
               self.root,
               justify= 'center',
               command=self.inserir,
               text='Inserir',
               fg = "#000000",
               relief='raised',
               )
        self.button_inserir.place(x=410,y=400,width=100,height=25)

        self.button_exclusao =tk.Button(
               self.root,
               justify= 'center',
               command=self.exclusao,
               text='Excluir',
               fg = "#000000",
               relief='raised',)
        self.button_exclusao.place(x=550,y=400,width=100,height=25)

        self.button_consulta = tk.Button(
               self.root,
               fg= "#000000",
               justify='center',
               text = "Consultar",
               relief='raised',
               command=self.consulta)
        self.button_consulta.place(x=690,y=400,width=100,height=25)

        self.dicionario = {}
        self.conectar_banco()  # Abre a conexão ao criar a instância da classe
        self.root.mainloop()

    def conectar_banco(self):
        self.con = sqlite3.connect('banco.db')
        self.sql = self.con.cursor()

        self.sql.execute('''
            SELECT name FROM sqlite_master WHERE type='table' AND name='tabela'
        ''')
        self.tabela_existe = self.sql.fetchone()

        # Cria a tabela se ela não existir
        if not self.tabela_existe:
            self.sql.execute('CREATE TABLE tabela (Nome,Email,NomedoEvento,DatadoEvento,TemadoEvento,LocaldoEvento)')

    def Conferir(self):
        try:
            while True:
                if self.deu_certo_ou_nao != 0:
                    #self.deu_certo_ou_nao = 1
                    self.inserir()

                elif self.deu_certo_ou_nao == 0:
                    self.sql.execute('INSERT INTO tabela (Nome) VALUES (?)', (self.label_nome.get(),))
                    self.sql.execute('INSERT INTO tabela (Email) VALUES (?)', (self.label_email.get(),))
                    self.sql.execute('INSERT INTO tabela (NomedoEvento) VALUES (?)', (self.label_nome_evento.get(),))
                    self.sql.execute('INSERT INTO tabela (DatadoEvento) VALUES (?)', (self.label_entry_data.get(),))
                    self.sql.execute('INSERT INTO tabela (TemadoEvento) VALUES (?)', (self.label_entry_tema.get(),))
                    self.sql.execute('INSERT INTO tabela (LocaldoEvento) VALUES (?)', (self.label_entry_local.get(),))

                    self.con.commit()

                    self.label_nome.delete(0,END)
                    self.label_email.delete(0,END)
                    self.label_nome_evento.delete(0,END)
                    self.label_entry_data.delete(0,END)
                    self.label_entry_tema.delete(0,END)
                    self.label_entry_local.delete(0,END)

                    
                    break

        except Exception as e:
            print(f"Erro durante a execução de Conferir: {e}")
            traceback.print_exc()

    def inserir(self):
        #VALIDANDO OS ENTRY 
        #-----------------------------------------------------------------------------------------------------------------
        #Validando o entry do nome do usuário
        # Limpando as mensagens de sucesso ou erro
        

        self.conectar_banco()

        self.sql.execute('''
        SELECT name FROM sqlite_master WHERE type='table' AND name='tabela'
        ''')
        self.tabela_existe = self.sql.fetchone()

        # Criar tabela se não existir
        if not self.tabela_existe:
            self.sql.execute('CREATE TABLE tabela (Nome,Email,NomedoEvento,DatadoEvento,TemadoEvento,Localdoevento)')
                         
        
        try:
            self.lista = []
            for i in self.label_nome.get():
                self.lista.append(i)

            for i in range(0,len(self.lista)):
                if self.lista[i].isalpha() != True:
                    raise Exception ("Não pode ter número!")
                                   

        except Exception:
            self.label_nome['bg']='red'
            self.label_nome.delete(0,END)
            self.deu_certo_ou_nao +=1 
            print('entrou no except1')
            print(self.deu_certo_ou_nao)    

        else:
            #self.sql.execute('INSERT INTO tabela (Nome) VALUES (?)', (self.label_nome.get(),))
            #self.texto_aux_nome("O nome foi cadastrado!")
            self.label_nome['bg']='white'
            print('O nome foi cadastrado!')
                              

        #Validando o entry do email
        try:
            self.lista = []
            for i in self.label_email.get():
                self.lista.append(i)

            if "@" in self.lista:
                pass
            else:
                raise Exception("O email deve conter o caracter '@' ")
                              
        except Exception:
            self.label_email['bg']='red'
            self.label_email.delete(0,END)
            self.deu_certo_ou_nao +=1
            print('entrou no except2')
            print(self.deu_certo_ou_nao)
                              
        else:
            #self.sql.execute('INSERT INTO tabela (Email) VALUES (?)',(self.label_email.get(),))
            #self.texto_aux_email("O email foi cadastrado!")
            self.label_email['bg']='white'
            print('O email foi cadastrado!')
                              

        #Validando o entry do nome do evento 
        try:
            self.lista = []
            for i in self.label_nome_evento.get():
                self.lista.append(i)

            for i in range(0,len(self.lista)):
                if self.lista[i].isalpha() != True:
                    raise Exception("Não pode ter número!")
            #if self.label_nome_evento.get().isalpha() == False:
                #raise Exception ("Não pode ter número!")



        except Exception:
            self.label_nome_evento['bg']='red'
            self.label_nome_evento.delete(0,END)
            self.deu_certo_ou_nao +=1
            print('entrou no except3')
            print(self.deu_certo_ou_nao)
                              
        else:
            #self.sql.execute('INSERT INTO tabela (Nome_do_Evento) VALUES (?)', (self.label_nome_evento.get(),))
            #self.texto_aux_nome_evento('O nome do evento, foi cadastrado!')
            self.label_nome_evento['bg']='white'
            print('O nome do evento, foi cadastrado!')
                              


        #Validando o entry da data
        try:
            self.lista = []
            for i in self.label_entry_data.get():
                self.lista.append(i)

            if self.lista[2] == '/' and self.lista[5] == '/':
                for i in range(0,len(self.lista)):
                        if self.lista[i].isalpha() == True:
                            raise Exception ("Não pode ter letra!")
            #if self.label_entry_data.get().isalpha() == True:
                #raise Exception ("Não pode ter letra!")

                              
        except Exception:
            self.label_entry_data['bg']='red'
            self.label_entry_data.delete(0,END)
            self.deu_certo_ou_nao +=1
            print('entrou no except4')
            print(self.deu_certo_ou_nao)

        else:
            #self.sql.execute('INSERT INTO tabela (Data_do_Evento) VALUES (?)', (self.label_entry_data.get(),))
            #self.texto_aux_data("A data do evento foi cadastrada!")
            self.label_entry_data['bg']='white'
            print('A data do evento foi cadastrada!')


        #Validando o entry do tema do evento 
        try:
            self.lista = []
            for i in self.label_entry_tema.get():
                self.lista.append(i)

            for i in range(0,len(self.lista)):
                if self.lista[i].isalpha() != True:
                        raise Exception ("Não pode ter número!")
            #if self.label_entry_tema.get().isalpha() == False:
             #   raise Exception ("Não pode ter número!")



        except Exception:
            self.label_entry_tema['bg']='red'
            self.label_entry_tema.delete(0,END)
            self.deu_certo_ou_nao +=1 
            print('entrou no except5')
            print(self.deu_certo_ou_nao)

        else:
            #self.sql.execute('INSERT INTO tabela (Tema_do_Evento) VALUES (?)', (self.label_entry_tema.get(),))
            #self.texto_aux_tema("O tema do evento foi cadastrado!")
            self.label_entry_tema['bg']='white'
            print('O tema do evento foi cadastrado!')

        #Validando o entry do local do evento 
        try:
            self.lista = []
            for i in self.label_entry_local.get():
                self.lista.append(i)

            for i in range(0,len(self.lista)):
                if self.lista[i].isalpha() != True:
                        raise Exception ("Não pode ter número!")
            #if self.label_entry_local.get().isalpha() == False:
             #   raise Exception ("Não pode ter número!")



        except Exception:
            self.label_entry_local['bg']='red'
            self.label_entry_local.delete(0,END) 
            self.deu_certo_ou_nao +=1
            print('entrou no except6')
            print(self.deu_certo_ou_nao)

        else:
            #self.sql.execute('INSERT INTO tabela (Local_do_Evento) VALUES (?)', (self.label_entry_local.get(),))
            #self.texto_aux_local.set("O nome foi cadastrado!")
            self.label_entry_local['bg']='white' 
            print('O Local foi cadastrado!')
                     
        self.deu_certo_ou_nao -= 1
        if self.deu_certo_ou_nao != 0:
            self.inserir()
        elif self.deu_certo_ou_nao == 0:

            self.sql.execute('INSERT INTO tabela (Nome) VALUES (?)', (self.label_nome.get(),))
            self.sql.execute('INSERT INTO tabela (Email) VALUES (?)', (self.label_email.get(),))
            self.sql.execute('INSERT INTO tabela (NomedoEvento) VALUES (?)', (self.label_nome_evento.get(),))
            self.sql.execute('INSERT INTO tabela (DatadoEvento) VALUES (?)', (self.label_entry_data.get(),))
            self.sql.execute('INSERT INTO tabela (TemadoEvento) VALUES (?)', (self.label_entry_tema.get(),))
            self.sql.execute('INSERT INTO tabela (LocaldoEvento) VALUES (?)', (self.label_entry_local.get(),))

            self.con.commit()

            self.label_nome.delete(0,END)
            self.label_email.delete(0,END)
            self.label_nome_evento.delete(0,END)
            self.label_entry_data.delete(0,END)
            self.label_entry_tema.delete(0,END)
            self.label_entry_local.delete(0,END)

                         
    def buscar_id_por_nome(self, nome):
        try:
            self.sql.execute('SELECT rowid FROM tabela WHERE Nome = ?', (nome,))
            resultado = self.sql.fetchone()

            if resultado:
                return resultado[0]
            else:
                return None

        except Exception as e:
            print(f"Erro durante a busca do ID: {e}")
            traceback.print_exc()
            return None


    def exclusao(self):
        try:
            nome_para_excluir = self.texto_aux_nome.get()

            id_para_excluir = self.buscar_id_por_nome(nome_para_excluir)

            if id_para_excluir is not None:
                self.sql.execute('DELETE FROM tabela WHERE rowid = ?', (id_para_excluir,))

                self.con.commit()

                self.label_nome.delete(0,END)
                self.label_nome['bg']='white'

                print(f"Registros associados ao nome '{nome_para_excluir}' excluídos com sucesso!")

            else:
                self.label_nome['bg']='red'
                print(f"Nenhum registro encontrado para o nome '{nome_para_excluir}'.")

        except Exception as e:
            print(f"Erro durante a execução de exclusao: {e}")
            traceback.print_exc()


    def consulta(self):
        try:
            self.sql.execute('SELECT * FROM tabela')
            resultados = self.sql.fetchall()

            if resultados:
                consulta_window = Toplevel(self.root)
                consulta_window.title("Consulta de Registros")

                tabela_resultados = ttk.Treeview(consulta_window, columns=(1, 2, 3, 4, 5, 6), show="headings")
                tabela_resultados.heading(1, text="Nome")
                tabela_resultados.heading(2, text="Email")
                tabela_resultados.heading(3, text="Nome do Evento")
                tabela_resultados.heading(4, text="Data do Evento")
                tabela_resultados.heading(5, text="Tema do Evento")
                tabela_resultados.heading(6, text="Local do Evento")

                for resultado in resultados:
                    tabela_resultados.insert("", "end", values=resultado)

                tabela_resultados.pack()

            else:
                print("Nenhum registro encontrado.")

        except Exception as e:
            print(f"Erro durante a execução de consulta: {e}")
            traceback.print_exc()

#aplicacao = App()
   
