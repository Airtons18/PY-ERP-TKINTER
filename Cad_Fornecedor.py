from tkinter import *
import psycopg2
from tkinter import ttk


connect = psycopg2.connect(
user = 'postgres',
password = 'root',
database = 'erp_proj')
cursor = connect.cursor()

App = Tk()
fontePadrao = ("Calibri", "16",)
App.title('CADASTRO DE FORNECEDOR')

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
L21 = Frame(App)
L21["pady"] = 50 
L21.pack()

container9 = Frame(App)
container9["pady"] = 20
container9.pack()

container10 = Frame(App)
container10.pack()

titulo = Label(L1, text="CADASTRO DO FORNECEDOR")
titulo["font"] = ("Arial", "20", "bold")
titulo.pack()

Lnomefornec = Label(L2,text="NOME DO FORNECEDOR", font=fontePadrao)
Lnomefornec.pack(side=LEFT)
Enomefornec = Entry(L2,width=40,font=fontePadrao)
Enomefornec.pack(side=LEFT)


def Func_carregaTV(): # Lê os dados do banco e envia para treeview
    print("passou Func_carregaTV")
    tv.delete(*tv.get_children()) # Limpa a treeview 
    try:
        cursor = connect.cursor() #erro que não carregava treeview
        cursor.execute("SELECT  idfornec, nomefornec FROM Tbfornec ORDER BY idfornec ASC")
        rows = cursor.fetchall()
        nomefornec = ''
       
      
        
        for row in rows:
            idfornec = row[0]
            nomefornec = row[1]
           
            

            tv.insert("", 'end', text=idfornec, values=(idfornec, nomefornec)) 
            cursor.close()
        
    except psycopg2.Error as erro:
        print("Erro no select tab produto: ", erro)

def Func_envia_dadoTV_tela(event): # Select da linha da tabela para Tela
    print("passou envia_dadoTV_tela")

    global idfornecP
    global nomefornecP

    for selection in tv.selection(): 
        item = tv.item(selection)     
        idfornecP, nomefornecP = item["values"][0:2]  
    print("idfornecP= ",idfornecP)      
    Enomefornec.delete(0, END)
   

    global chave_banco

    chave_banco = idfornecP
     
    try:        
        cursor = connect.cursor()
        sql_select_query = """SELECT nomefornec \
        FROM Tbfornec WHERE idfornec = %s""" 
        cursor.execute(sql_select_query, (chave_banco,))                    
        rows = cursor.fetchall()
        for col in rows:
            Enomefornec.insert(0, col[0])
          
                    
            return "Carga das colunas da Tabela com sucesso!"
    except Exception as e:
        print('Exception: {}'.format(e))
        return "Erro no Select tab de fornecedor"

def Func_cadastrar():
    print('entrou cad_fornecedor')

    nomefornecVar = Enomefornec.get()
    
    if nomefornecVar == "":
            mensagem["text"] = "Nome em Branco ?"
            Enomefornec.focus_set()
            return
    else:
         if len(nomefornecVar) > 60:
            mensagem["text"] = "Nome maior que 40 caracteres ?"
            Enomefornec.focus_set()
            return

    try:
        cursor = connect.cursor()
        QUERY_INSERT = """INSERT INTO tbfornec(nomefornec) VALUES (%s)"""
        RECORD_INSERT = (nomefornecVar)
        cursor.execute(QUERY_INSERT ,(RECORD_INSERT,))
        connect.commit()
        cursor.close()
        mensagem["text"] = "FORNECEDOR CADASTRADO"
    except Exception as erro:
        mensagem["text"] = "Erro no Cadastro"
        print('Exception: {}'.format(erro))
        raise Exception(erro)
       
    if nomefornecVar == "":
            mensagem["text"] = "Nome em Branco ?"
            Enomefornec.focus_set()
            return
    else:
         if len(nomefornecVar) > 60:
            mensagem["text"] = "Nome maior que 40 caracteres ?"
            Enomefornec.focus_set()
            return
        
    Enomefornec.delete(0, END) #limpa os campo
   

    Func_carregaTV()

def Func_alterar():
    global nomefornecVar
    nomefornecVar = Enomefornec.get()


    if nomefornecVar == "":
            mensagem["text"] = "Nome em Branco ?"
            Enomefornec.focus_set()
            return
    else:
         if len(nomefornecVar) > 60:
            mensagem["text"] = "Nome maior que 40 caracteres ?"
            Enomefornec.focus_set()
            return

    try:
        cursor = connect.cursor()
        sql_update_query = """UPDATE Tbfornec SET nomefornec = %s WHERE idfornec = %s"""
        cursor.execute(sql_update_query, (nomefornecVar, chave_banco))           
        connect.commit()
        cursor.close()
        mensagem["text"] = "fornecedor atualizado"
        print('após atualizado')   
    except psycopg2.Error as erro:
        mensagem["text"] = "Erro de Atualização"
        print("Erro no Update tab produto: ", erro)
        print('após print erro no update')     
    
    Func_carregaTV()
    
    Enomefornec.delete(0, END)

def Func_excluir():
    print("passou Func_excluir")

    try:
            cursor = connect.cursor()
            sql_delete_query = """DELETE FROM tbfornec WHERE idfornec = %s"""
            cursor.execute(sql_delete_query, (chave_banco,))
            connect.commit()
            cursor.close()
            mensagem["text"] = "fornecedor deletado"
    except psycopg2.Error as erro:
            print("Erro no Delete tab fornecedor: ", erro)           
    
    Func_carregaTV()

def sair():
    #App.withdraw() esconder tela
    quit()



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

Espaco2= Label(L20, text="  ",
font=fontePadrao, width=2)
Espaco2.pack(side=LEFT)


botaosair = Button(L20)
botaosair["text"] = "SAIR"
botaosair["font"] = ("calibre", "20", "bold")
botaosair["width"] = 10
botaosair["command"] = sair
botaosair.pack(side=LEFT)

##########################################################    
mensagem = Label(container9,  text="")
mensagem["font"] = ("Verdana", "20", "italic","bold")
mensagem.pack()

lblselect= Label(container10, text="Selecione um registro abaixo para Incluir, Alterar ou Excluir",
font=fontePadrao, width=50)
lblselect.pack(side=LEFT)

frame = Frame(App)
frame.pack(pady=20)

tv = ttk.Treeview(frame, columns=(1, 2), show='headings', height=10)
tv.pack(side=LEFT)

tv.heading(1, text="ID FORNEC")
tv.column("#1",minwidth=0,width=100)
tv.heading(2, text="NOME")
tv.column("#2",minwidth=0,width=100)

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
  