from ast import If, Try
import subprocess
from tkinter import *
from winreg import QueryInfoKey
import psycopg2
import pickle

connect = psycopg2.connect(
user = 'postgres',
password = 'root',
database = 'erp_proj')
cursor = connect.cursor()

App = Tk()

App.title("LOGIN DB")
App.largura = 300						
App.altura  = 300
App.largura_scr = App.winfo_screenwidth()						
App.altura_scr  = App.winfo_screenheight()						
App.posx = App.largura_scr/2 - App.largura/2						
App.posy = App.altura_scr/2  - App.altura/2 						
App.geometry("%dx%d+%d+%d" % (App.largura, App.altura - 50 , App.posx, App.posy))
App.configure(bg='#ADD8E6')
Luser = Label(App, text = "Username")
Luser.place(x = 10, y = 10)
Euser = Entry(App, bd = 10)
Euser.place(x = 70,y = 10)
Lpass = Label(App, text = "Password")
Lpass.place(x = 10,y = 50)
Epass = Entry(App, bd = 10, show= "*")
Epass.place(x = 70,y = 50)


mensagem = Label(App, text = "", font=16, fg='red',bg='#ADD8E6')
mensagem.place(x = 70,y = 100) #90

def sair():
    #App.withdraw() esconder tela
    quit()


def login():
    try:
        cursor = connect.cursor()
        usernameVar = Euser.get()  
        passdigitVar = Epass.get()      
                
        Query1 = "SELECT usuario, senha, produtos, clientes, fornecedores, vendedores, colaboradores, entmer, pdv FROM tbuser WHERE usuario = %s"
        cursor.execute(Query1 , (usernameVar,))
        rows = cursor.fetchall()
        if cursor.rowcount == 0:  
            mensagem["text"] = "Usuário não Encontrado"
        else:  
            for row in rows:
                print("Usuario = ", row[0], )
                print("Senha   = ", row[1])
                print(rows)
                passwuserVar = row[1]

                VarCadProd = row[2]
                VarCadCli = row[3]
                VarCadFornec = row[4]
                VarCadVend = row[5]
                VarCadUser = row[6]
                VarEntMer = row[7]
                VarPdv = row[8]             

                Perfil_CadProd = VarCadProd
                Perfil_CadCli = VarCadCli
                Perfil_CadFornec = VarCadFornec
                Perfil_CadVend = VarCadVend
                Perfil_CadUser = VarCadUser
                Perfil_EntMer = VarEntMer
                Perfil_Pdv = VarPdv

                with open('Perfil_CadProd.pkl', 'wb') as f:
                    pickle.dump(Perfil_CadProd, f)
                
                with open('Perfil_CadCli.pkl', 'wb') as f:
                    pickle.dump(Perfil_CadCli, f)
                
                with open('Perfil_CadFornec.pkl', 'wb') as f:
                    pickle.dump(Perfil_CadFornec, f)
                
                with open('Perfil_CadVend.pkl', 'wb') as f:
                    pickle.dump(Perfil_CadVend, f)
                
                with open('Perfil_CadUser.pkl', 'wb') as f:
                    pickle.dump(Perfil_CadUser, f)

                with open('Perfil_EntMer.pkl', 'wb') as f:
                    pickle.dump(Perfil_EntMer, f)
                
                with open('Perfil_Pdv.pkl', 'wb') as f:
                    pickle.dump(Perfil_Pdv, f)                 

                if passdigitVar == passwuserVar:
                    App.destroy()
                else:
                    mensagem["text"] = "Senha Invalida"
                          
    except Exception as erro:
        print(erro)
        Euser.delete(0, END) 
        Epass.delete(0, END) 
        print("passou delete Entries ")

botao = Button(App, text="PROCESSAR",command=login) #antes era Func_enviar_mensagem  no comand ...
botao.place(x=100, y=140) # 120

botaox = Button(App, text="Sair",command=sair) #antes era Func_enviar_mensagem  no comand ...
botaox.place(x=190, y=140) #120

App.mainloop()
