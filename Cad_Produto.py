from re import A
from tkinter import *
from tkinter import ttk
from unicodedata import numeric
import psycopg2
import subprocess
import os

connect = psycopg2.connect(
user = 'postgres',
password = 'root',
database = 'erp_proj')
cursor = connect.cursor()
App = Tk()
fontePadrao = ("Calibri", "16",)
App.title('CADASTRO DE PRODUTOS')
App.largura = 950
App.altura  = 670
App.largura_scr = App.winfo_screenwidth()
App.altura_scr  = App.winfo_screenheight()
App.posx = App.largura_scr/2 - App.largura/2
App.posy = App.altura_scr/2  - App.altura/2
App.geometry("%dx%d+%d+%d" % (App.largura, App.altura - 30 , App.posx, App.posy))
L1 = Frame(App)
L1["pady"] = 10
L1.pack()
L2 = Frame(App)
L2["padx"] = 20
L2.pack()
L3 = Frame(App)
L3["padx"] = 20
L3.pack()
L4 = Frame(App)
L4["padx"] = 20
L4.pack()
L5 = Frame(App)
L5["padx"] = 20
L5.pack()
L6 = Frame(App)
L6["padx"] = 20
L6.pack()
L7 = Frame(App)
L7["padx"] = 20
L7.pack()
L8 = Frame(App)
L8["padx"] = 20
L8.pack()
L9 = Frame(App)
L9["padx"] = 20
L9.pack()
L10 = Frame(App)
L10["padx"] = 20
L10.pack()
L11 = Frame(App)
L11["padx"] = 20
L11.pack()
L12 = Frame(App)
L12["padx"] = 20
L12.pack()
L13 = Frame(App)
L13["padx"] = 20
L13.pack()
L14 = Frame(App)
L14["padx"] = 20
L14.pack()
L15 = Frame(App)
L15["padx"] = 20 
L15.pack()
L16 = Frame(App)
L16["padx"] = 20 
L16.pack()
L17= Frame(App)
L17["padx"] = 20 
L17.pack()
L18= Frame(App)
L18["padx"] = 20 
L18.pack()
L19= Frame(App)
L19["padx"] = 20 
L19.pack()
L20 = Frame(App)
L20["pady"] = 50 
L20.pack()
container9 = Frame(App)
container9["pady"] = 20
container9 .pack()
container10 = Frame(App)
container10.pack()
titulo = Label(L1, text="Cadastro de Produtos")
titulo["font"] = ("Arial", "20", "bold")
titulo.pack()
Lcodbarprod = Label(L2,text="Codigo de Barra", font=fontePadrao)
Lcodbarprod.pack(side=LEFT)
Ecodbarprod = Entry(L2,width=40,font=fontePadrao)
Ecodbarprod.pack(side=LEFT)
Lncmprod = Label(L3, text="                N.C.M", font=fontePadrao)
Lncmprod.pack(side=LEFT)
Encmprod = Entry(L3,width=40,font=fontePadrao)
Encmprod.pack(side=LEFT)
Ldescprod = Label(L4,text="          Descrição", font=fontePadrao)
Ldescprod.pack(side=LEFT)
Edescprod = Entry(L4,width=40,font=fontePadrao)
Edescprod.pack(side=LEFT)
Lvlrunprod = Label(L5,text="   Valor Unitario", font=fontePadrao)
Lvlrunprod.pack(side=LEFT)
Evlrunprod = Entry(L5,width=40,font=fontePadrao)
Evlrunprod.pack(side=LEFT)
Lunidprod = Label(L6,text="             Unidade", font=fontePadrao)
Lunidprod.pack(side=LEFT)
Eunidprod = Entry(L6,width=40,font=fontePadrao)
Eunidprod.pack(side=LEFT)

def sair():
    #App.withdraw() esconder tela
    quit()

'''#Binds para mudar campo após enter
Ecodbarprod.focus_set()
Ecodbarprod.bind("<Return>",lambda funct1:Encmprod.focus())
Encmprod.bind("<Return>",lambda funct1:Edescprod.focus())
Edescprod.bind("<Return>",lambda funct1:Evlrunprod.focus())
Evlrunprod("<Return>",lambda funct1:Eunidprod.focus())'''
def Func_carregaTV(): # Lê os dados do banco e envia para treeview
    print("passou Func_carregaTV")
    tv.delete(*tv.get_children()) # Limpa a treeview 
    try:
        cursor = connect.cursor() #erro que não carregava treeview
        cursor.execute("SELECT idprod, codbarprod, ncmprod, descprod, vlrunprod, unidprod FROM tbproduto ORDER BY idprod ASC")
        rows = cursor.fetchall()
        codbarprod = ''
        ncmprod = ''
        descprod = ''
        vlrunprod = ''
        unidprod = ''
        for row in rows:
            idprod = row[0]
            codbarprod = row[1]
            ncmprod = row[2]
            descprod = row[3]
            vlrunprod = row[4]
            unidprod = row[5]
            tv.insert("", 'end', text=idprod, values=(idprod, codbarprod, ncmprod, descprod, vlrunprod, unidprod)) 
            cursor.close()
    except psycopg2.Error as erro:
        print("Erro no select tab produto: ", erro)
def Func_envia_dadoTV_tela(event): # Select da linha da tabela para Tela
    print("passou envia_dadoTV_tela")
    global idprodP
    global descprodP
    for selection in tv.selection(): 
        item = tv.item(selection)     
        idprodP, descprodP = item["values"][0:2]  
    print("idprodP= ",idprodP)
    Ecodbarprod.delete(0, END) 
    Encmprod.delete(0, END)
    Edescprod.delete(0, END)
    Evlrunprod.delete(0, END)
    Eunidprod.delete(0, END)
    global chave_banco
    chave_banco = idprodP 
    try:        
        cursor = connect.cursor()
        sql_select_query = """SELECT codbarprod, ncmprod, descprod, vlrunprod, unidprod, idprod \
        FROM tbproduto WHERE idprod = %s""" 
        cursor.execute(sql_select_query, (chave_banco,))                    
        rows = cursor.fetchall()  
        for col in rows:  
            Ecodbarprod.insert(0, col[0])
            Encmprod.insert(0, col[1])
            Edescprod.insert(0, col[2])
            Evlrunprod.insert(0, col[3])
            Eunidprod.insert(0, col[4])
            return "Carga das colunas da Tabela com sucesso!"
    except Exception as e:
        print('Exception: {}'.format(e))
        return "Erro no Select tab de produto"
def Func_cadastrar():
    print('entrou cad_produto')
    codbarVar = Ecodbarprod.get()

    if str(codbarVar) == "":
        mensagem["text"] = "CODIGO EM BRANCO?"
        return
    elif len(str(codbarVar)) > 13:
                mensagem["text"] = "Cod Barras SOBRANDO DIGITO"
                return
    else:
        if len(str(codbarVar)) < 1:
                mensagem["text"] = "COD. Barras FALTA DIGITO"
                return

    ncmVar = Encmprod.get()
    if str(ncmVar) == "":
        mensagem["text"] = "NCM EM BRANCO"
        return
    elif len(str(ncmVar)) > 8:
                mensagem["text"] = "NCM SOBRANDO DIGITO"
                return
    else:
        if len(str(ncmVar)) < 1:
                mensagem["text"] = "NCM FALTA DIGITO"
                return

    descVar = Edescprod.get()

    if descVar == "":
        mensagem["text"] = "Descrição em Branco ?"
        
        return
    else:
        if len(descVar) > 30:
            mensagem["text"] = "Nome maior que 30 caracteres ?"
            
            return

    vlrunVar = Evlrunprod.get()
    vlrunVar = vlrunVar.replace(',' , '.')
    print(vlrunVar) 
    if vlrunVar == "":
        mensagem["text"] = "Valor em Branco ?"
        return

    unidVar = Eunidprod.get()
    if unidVar == "":
        mensagem["text"] = "Unidade em Branco ?"
        return
    else:
        if len(descVar) > 10:
            mensagem["text"] = "Unidade maior que 10 caracteres ?"
            return

    try:        
            cursor = connect.cursor()
            sql_select_query = """SELECT * FROM tbproduto WHERE codbarprod = %s""" 
            cursor.execute(sql_select_query, (codbarVar,))                 
            rows = cursor.fetchall()
            print(rows)
            if rows != []:
                mensagem['text'] = 'COD. Barras Já Cadastrado !!'
                Ecodbarprod.focus_set()
                return
    except Exception as e:
            print('Exception: {}'.format(e))
            return "Erro na verificação de duplicidade do cod barra!"
    try:
        cursor = connect.cursor() 
        cursor.execute('INSERT INTO tbproduto (codbarprod, ncmprod, descprod, vlrunprod, unidprod) \
                      VALUES (%s,%s,%s,%s,%s)',
                      (codbarVar, ncmVar, descVar, vlrunVar, unidVar))
        connect.commit()
        cursor.close()
        mensagem["text"] = "PRODUTO CADASTRADO"
    except Exception as erro:
        mensagem["text"] = "Erro no Cadastro"
        print('Exception: {}'.format(erro))
        raise Exception(erro)
    try:
        cursor = connect.cursor()
        cursor.execute('INSERT INTO tbestoque (codbarprod, qtdestq) \
                    VALUES (%s, %s)',
                    (codbarVar, 0),)       
        connect.commit()
        cursor.close()        
    except psycopg2.Error as erro:
        mensagem["text"] = "Erro no insert tbestoque"
        print("Erro no Insert tab estoque: ", erro)
        print('após print erro no update')
    Ecodbarprod.delete(0, END) #limpa os campo
    Encmprod.delete(0, END) 
    Edescprod.delete(0, END)
    Evlrunprod.delete(0, END)
    Eunidprod.delete(0, END)
    Func_carregaTV() 
def Func_alterar():
    global codbarVar
    codbarVar = int(Ecodbarprod.get())
    ncmVar = int(Encmprod.get())
    descVar = Edescprod.get()
    vlrunVar = float(Evlrunprod.get()) 
    unidVar = Eunidprod.get()
    try:
        cursor = connect.cursor()
        sql_update_query = """UPDATE tbproduto SET codbarprod = %s,ncmprod = %s, descprod = %s, vlrunprod = %s, unidprod = %s WHERE idprod = %s"""
        cursor.execute(sql_update_query, (codbarVar, ncmVar, descVar, vlrunVar, unidVar, chave_banco))           
        connect.commit()
        cursor.close()        
        mensagem["text"] = "PRODUTO ATUALIZADO"
        print('após atualizado')        
    except psycopg2.Error as erro:
        mensagem["text"] = "Erro de Atualização"
        print("Erro no Update tab produto: ", erro)
        print('após print erro no update')     
    Func_carregaTV()
    Ecodbarprod.delete(0, END)
    Encmprod.delete(0, END)
    Edescprod.delete(0, END)
    Evlrunprod.delete(0, END)
    Eunidprod.delete(0, END)
def Func_excluir():
    print("passou Func_excluir")
    try:
            cursor = connect.cursor()
            sql_delete_query = """DELETE FROM tbproduto WHERE idprod = %s"""
            cursor.execute(sql_delete_query, (chave_banco,))
            connect.commit()
            cursor.close()
            mensagem["text"] = "PRODUTO EXCLUIDO"
    except psycopg2.Error as erro:
            print("Erro no Delete tab produto: ", erro)           
    Func_carregaTV()
cadcli = Button(L20)
cadcli["text"] = "CADASTRAR"
cadcli["font"] = ("Calibri", "20","bold")
cadcli["width"] = 10
cadcli["command"] = Func_cadastrar
cadcli.pack(side=LEFT)
Espaco1= Label(L20, text="  ",
font=fontePadrao, width=2,)
Espaco1.pack(side=LEFT)
bntalterar = Button(L20)
bntalterar["text"] = "ATUALIZAR"
bntalterar["font"] = ("Calibri", "20","bold")
bntalterar["width"] = 10
bntalterar["command"] = Func_alterar
bntalterar.pack(side=LEFT)
Espaco2= Label(L20, text="  ",
font=fontePadrao, width=2)
Espaco2.pack(side=LEFT)
bntexcluir = Button(L20)
bntexcluir["text"] = "EXCLUIR"
bntexcluir["font"] = ("Calibri", "20","bold")
bntexcluir["width"] = 10
bntexcluir["command"] = Func_excluir
bntexcluir.pack(side=LEFT)
Espaco3= Label(L20, text="  ",
font=fontePadrao, width=2)
Espaco3.pack(side=LEFT)
bntsair = Button(L20)
bntsair["text"] = "SAIR"
bntsair["font"] = ("Calibri", "20","bold")
bntsair["width"] = 10
bntsair["command"] = sair
bntsair.pack(side=LEFT)

##########################################################    
mensagem = Label(container9,)
mensagem["font"] = ("Verdana", "20", "bold", "italic")
mensagem.pack()
lblselect= Label(container10, text="Selecione um produto abaixo para Alterar ou Excluir",
font=fontePadrao, width=50)
lblselect.pack(side=LEFT)
frame = Frame(App)
frame.pack(pady=20)
tv = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5, 6), show='headings', height=10)
tv.pack(side=LEFT)
tv.heading(1, text="ID produto")
tv.column("#1",minwidth=0,width=100)
tv.heading(2, text="Codigo de Barra")
tv.column("#2",minwidth=0,width=100)
tv.heading(3, text="NCM")
tv.column("#3",minwidth=0,width=100)
tv.heading(4, text="Descrição")
tv.column("#4",minwidth=0,width=100)
tv.heading(5, text="Valor Unitário")
tv.column("#5",minwidth=0,width=100)
tv.heading(6, text="Unidade")
tv.column("#6",minwidth=0,width=100)
sb = Scrollbar(frame, orient=VERTICAL)
sb.pack(side=RIGHT, fill=Y)
tv.config(yscrollcommand=sb.set)
sb.config(command=tv.yview)
tv.bind("<<TreeviewSelect>>", Func_envia_dadoTV_tela) 
Func_carregaTV()
style = ttk.Style()
style.theme_use("default")
style.map("Treeview")
App.mainloop()
    