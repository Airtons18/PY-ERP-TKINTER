from ast import Global
from tkinter import *
import os
import pickle
import subprocess
from pathlib import Path
from datetime import datetime

global permissao
permissao = []

path_Prod = 'Perfil_CadProd.pkl'
path = Path(path_Prod)
if path.is_file():
    os.remove("Perfil_CadProd.pkl")

path_Cli = 'Perfil_CadCli.pkl'
path = Path(path_Cli)
if path.is_file():
    os.remove("Perfil_CadCli.pkl")

path_Fornec = 'Perfil_CadFornec.pkl'
path = Path(path_Fornec)
if path.is_file():
    os.remove("Perfil_CadFornec.pkl")

path_Vend = 'Perfil_CadVend.pkl'
path = Path(path_Vend)
if path.is_file():
    os.remove("Perfil_CadVend.pkl")

path_User = 'Perfil_CadUser.pkl'
path = Path(path_User)
if path.is_file():
    os.remove("Perfil_CadUser.pkl")

path_User = 'Perfil_EntMer.pkl'
path = Path(path_User)
if path.is_file():
    os.remove("Perfil_EntMer.pkl")

path_User = 'Perfil_Pdv.pkl'
path = Path(path_User)
if path.is_file():
    os.remove("Perfil_Pdv.pkl")

def SemComando():
    print("aaa")

def Func_Unpickler():
    mensagem["text"] = ""
    global obj
    global permissao
    permissao = []
    if path.is_file():
        with open('Perfil_CadProd.pkl', 'rb') as f:
            unpickler = pickle.Unpickler(f)
            obj = unpickler.load()
            permissao.append(obj)
        with open('Perfil_CadCli.pkl', 'rb') as f:
            unpickler = pickle.Unpickler(f)
            obj = unpickler.load()
            permissao.append(obj)
        with open('Perfil_CadFornec.pkl', 'rb') as f:
            unpickler = pickle.Unpickler(f)
            obj = unpickler.load()
            permissao.append(obj)
        with open('Perfil_CadVend.pkl', 'rb') as f:
            unpickler = pickle.Unpickler(f)
            obj = unpickler.load()
            permissao.append(obj)
        with open('Perfil_CadUser.pkl', 'rb') as f:
            unpickler = pickle.Unpickler(f)
            obj = unpickler.load()    
            permissao.append(obj)
        with open('Perfil_EntMer.pkl', 'rb') as f:
            unpickler = pickle.Unpickler(f)
            obj = unpickler.load()    
            permissao.append(obj)
        with open('Perfil_Pdv.pkl', 'rb') as f:
            unpickler = pickle.Unpickler(f)
            obj = unpickler.load()    
            permissao.append(obj)     

    else:
        mensagem["text"] = "** Usuário Sem permissão, Favor fazer Signon **"

def Chama_Login():
    subprocess.call("Login.py", shell=True)
    mensagem['text'] = ""

def Chama_Menu():
    pass

def Chama_Cad_Prod():
    # Func_Unpickler()
    # print(obj)
    print("CadPRO", Func_Unpickler())
    if permissao[0] == 'y':
        subprocess.call("Cad_Produto.py", shell=True)
    else:
        mensagem["text"] = "** Usuário Sem permissão no Cad Produto **"

def Chama_Cad_Cli():
    Func_Unpickler()
    print(obj)
    if permissao[1] == 'y':
        subprocess.call("Cad_Cliente.py", shell=True)
    else:
        mensagem["text"] = "** Usuário Sem permissão no Cad Cliente **"

def Chama_Cad_Fornec():
    Func_Unpickler()
    print(obj)
    if permissao[2] == 'y':
        subprocess.call("Cad_Fornecedor.py", shell=True)
    else:
        mensagem["text"] = "** Usuário Sem permissão no Cad Fornecedor**"

def Chama_Cad_Vend():
    Func_Unpickler()
    print(obj)
    if permissao[3] == 'y':
        subprocess.call("Cad_Vendedor.py", shell=True)
    else:
        mensagem["text"] = "** Usuário Sem permissão no Cad Vendedor **"

def Chama_Cad_User():
    Func_Unpickler()
    print(obj)
    if permissao[4] == 'y':
        subprocess.call("Cad_User.py", shell=True)
    else:
        mensagem["text"] = "** Usuário Sem permissão no Cad Usuario **"

def Chama_Ent_Mer():
    Func_Unpickler()
    print(obj)
    if permissao[5] == 'y':
        subprocess.call("Ent_Mer.py", shell=True)
    else:
        mensagem["text"] = "** Usuário Sem permissão no Ent Mercadoria **"

def Chama_Pdv_venda():
    Func_Unpickler()
    print(obj)
    if permissao[6] == 'y':
        subprocess.call("Pdv_venda.py", shell=True)
    else:
        mensagem["text"] = "** Usuário Sem permissão no Cad Usuario **"


def Chama_Sair():
    quit()

App=Tk()

App.title("Menu do Sistema ERP")
App.largura = 950						
App.altura  = 650						
App.largura_scr = App.winfo_screenwidth()						
App.altura_scr  = App.winfo_screenheight()						
App.posx = App.largura_scr/2 - App.largura/2						
App.posy = App.altura_scr/2  - App.altura/2 						
App.geometry("%dx%d+%d+%d" % (App.largura, App.altura - 50 , App.posx, App.posy))

def relogio():
    dia_br = ['Domingo','Segunda-Feira', 'Terça-Feira', 'Quarta-Feira',
            'Quinta-Feira', 'Sexta-Feira', 'Sábado']

    tempo = datetime.now()
    hora=tempo.strftime("%H:%M:%S")

    dia_semana = tempo.strftime("%w")
    dia = tempo.day
    mes = tempo.strftime("%m")
    ano = tempo.strftime("%Y")
    Lhora.config(text=hora)
    Lhora.after(200, relogio)
    # dia_br[dia_semana]
    Ldata.config(text=dia_br[int(dia_semana)]+" - " + str(dia)+"/"+ str(mes)+"/"+str(ano))

Ldata = Label(App, text='00/00/0000', font=("Verdana 12 bold"))
Ldata.pack(side="bottom", anchor='sw')

Lhora = Label(App, text="00:00:00", font=("Verdana 18 bold"))
Lhora.pack(side="bottom" ,anchor="sw")
relogio()

menubar = Menu(App)

menu_Signon = Menu(menubar, tearoff=False, background='yellow')
menu_Signon.add_command(label="Signon",command=Chama_Login,font=20)
menu_Signon.add_separator()
menu_Signon.add_command(label="Sair",command=App.quit,font=20)
menubar.add_cascade(label="Signon",menu=menu_Signon)

menu_CadProd=Menu(menubar,tearoff=0)
menu_CadProd.add_command(label="Cad Produtos",command=Chama_Cad_Prod)
menu_CadProd.add_separator()
menu_CadProd.add_command(label="Sair ",command=App.quit)
menu_CadProd.add_separator()
menu_CadProd.add_command(label="Menu",command=Chama_Menu)
menubar.add_cascade(label="Cad Produtos",menu=menu_CadProd)

menu_CadClie=Menu(menubar,tearoff=0)
menu_CadClie.add_command(label="Cad Clientes",command=Chama_Cad_Cli)
menu_CadClie.add_separator()
menu_CadClie.add_command(label="Sair",command=App.quit)
menubar.add_cascade(label="Cad Clientes",menu=menu_CadClie)

menu_CadForn=Menu(menubar,tearoff=0)
menu_CadForn.add_command(label="Cad Fornecedores",command=Chama_Cad_Fornec)
menu_CadForn.add_separator()
menu_CadForn.add_command(label="Sair",command=App.quit)
menubar.add_cascade(label="Cad Fornecedores",menu=menu_CadForn)

menu_CadVend=Menu(menubar,tearoff=0)
menu_CadVend.add_command(label="Cad Vendedores",command=Chama_Cad_Vend)
menu_CadVend.add_separator()
menu_CadVend.add_command(label="Sair",command=App.quit)
menubar.add_cascade(label="Cad Vendedores",menu=menu_CadVend)

menu_CadUser=Menu(menubar,tearoff=0)
menu_CadUser.add_command(label="Cad Usuários",command=Chama_Cad_User)
menu_CadUser.add_separator()
menu_CadUser.add_command(label="Sair",command=App.quit)
menubar.add_cascade(label="Cad Usuários",menu=menu_CadUser)


menu_EntrMerc=Menu(menubar,tearoff=0)
menu_EntrMerc.add_command(label="Entr Produtos",command=Chama_Ent_Mer)
menu_EntrMerc.add_separator()
menu_EntrMerc.add_command(label="Sair",command=App.quit)
menubar.add_cascade(label="Entr Produtos",menu=menu_EntrMerc)

menu_Pdv=Menu(menubar,tearoff=0)
menu_Pdv.add_command(label="PDV - Vendas",command=Chama_Pdv_venda)
menu_Pdv.add_separator()
menu_Pdv.add_command(label="Sair",command=App.quit)
menubar.add_cascade(label="PDV",menu=menu_Pdv)

menu_Relat=Menu(menubar,tearoff=0)
menu_Relat.add_command(label="Relatório Diário Vendas",command=Chama_Cad_Prod)
menu_Relat.add_command(label="Relatório Mensal Vendas",command=Chama_Cad_Prod)
menu_Relat.add_command(label="Relatório Semestral de Vendas",command=Chama_Cad_Prod)
menu_Relat.add_separator()
menu_Relat.add_command(label="Sair",command=App.quit)
menubar.add_cascade(label="Relatórios",menu=menu_Relat)

menu_Grafico=Menu(menubar,tearoff=0)
menu_Grafico.add_command(label="Gráfico Diário Vendas",command=Chama_Cad_Prod)
menu_Grafico.add_command(label="Gráfico Mensal Vendas",command=Chama_Cad_Prod)
menu_Grafico.add_command(label="Gráfico Semestral de Vendas",command=Chama_Cad_Prod)
menu_Grafico.add_separator()
menu_Grafico.add_command(label="Sair",command=App.quit)
menubar.add_cascade(label="Gráficos",menu=menu_Grafico)

menu_Financeiro=Menu(menubar,tearoff=0)
menu_Financeiro.add_command(label="Contas a Pagar",command=Chama_Cad_Prod)
menu_Financeiro.add_command(label="Contas a Receber",command=Chama_Cad_Prod)
menu_Financeiro.add_command(label="Valor>>>",command=Chama_Cad_Prod)
menu_Financeiro.add_separator()
menu_Financeiro.add_command(label="Sair",command=App.quit)
menubar.add_cascade(label="Financeiro",menu=menu_Financeiro)

menu_Manut=Menu(menubar,tearoff=0)
menu_Manut.add_command(label="Backup",command=Chama_Cad_Prod)
menu_Manut.add_separator()
menu_Manut.add_command(label="Sair",command=App.quit)
menubar.add_cascade(label="Manutenção",menu=menu_Manut)

menu_Sair=Menu(menubar,tearoff=0)
menu_Sair.add_command(label="Sair",command=Chama_Sair)
menubar.add_cascade(label="Sair",menu=menu_Sair)

mensagem = Label(App, text = "", font=16, fg='red')
mensagem.place(x = 70,y = 90)

App.config(menu=menubar)
App.mainloop()
