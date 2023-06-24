from re import A
from tkinter import *
from tkinter import ttk
import psycopg2
from pycpfcnpj import cpfcnpj
# pip install cpf-cnpj-validate  
import os

# def openCadCli():
connect = psycopg2.connect(
user = 'postgres',
password = 'root',
database = 'erp_proj')
cursor = connect.cursor()

App = Tk()
fontePadrao = ("Calibri", "16",)
App.title('CADASTRO DE CLIENTES')
#
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

titulo = Label(L1, text="Cadastro de Clientes")
titulo["font"] = ("Arial", "20", "bold")
titulo.pack()

Lcpfcli = Label(L2,text="         CPF", font=fontePadrao)
Lcpfcli.pack(side=LEFT)
Ecpfcli = Entry(L2,width=40,font=fontePadrao)
Ecpfcli.pack(side=LEFT)

Lnomecli = Label(L3, text="     Nome", font=fontePadrao)
Lnomecli.pack(side=LEFT)
Enomecli = Entry(L3,width=40,font=fontePadrao)
Enomecli.pack(side=LEFT)

Ltelcli = Label(L4,text=" Telefone", font=fontePadrao)
Ltelcli.pack(side=LEFT)
Etelcli = Entry(L4,width=40,font=fontePadrao)
Etelcli.pack(side=LEFT)

Lendcli = Label(L5,text="Endereço", font=fontePadrao)
Lendcli.pack(side=LEFT)
Eendcli = Entry(L5,width=40,font=fontePadrao)
Eendcli.pack(side=LEFT)


# Lunidprod = Label(L6,text="Unidade", font=fontePadrao)
# Lunidprod.pack(side=LEFT)
# Eunidprod = Entry(L6,width=35,font=fontePadrao)
# Eunidprod.pack(side=LEFT)

#Binds para mudar campo após enter
# Ecodbarprod.focus_set()
# Ecodbarprod.bind("<Return>",lambda funct1:Encmprod.focus())
# Encmprod.bind("<Return>",lambda funct1:Edescprod.focus())
# Edescprod.bind("<Return>",lambda funct1:Evlrunprod.focus())
# Evlrunprod("<Return>",lambda funct1:Eunidprod.focus())


def Func_carregaTV(): # Lê os dados do banco e envia para treeview
    print("passou Func_carregaTV")
    tv.delete(*tv.get_children()) # Limpa a treeview 
    try:
        cursor = connect.cursor() #erro que não carregava treeview
        cursor.execute("SELECT idcli, cpfcli, nomecli, telcli, endcli FROM tbcliente ORDER BY idcli ASC")
        rows = cursor.fetchall()
        cpfcli = ''
        nomecli = ''
        telcli = ''
        endcli = ''
        
        for row in rows:
            idcli = row[0]
            cpfcli = row[1]
            nomecli = row[2]
            telcli = row[3]
            endcli = row[4]
            

            tv.insert("", 'end', text=idcli, values=(idcli, cpfcli, nomecli, telcli, endcli)) 
            cursor.close()
        
    except psycopg2.Error as erro:
        print("Erro no select tab produto: ", erro)

def Func_envia_dadoTV_tela(event): # Select da linha da tabela para Tela
    print("passou envia_dadoTV_tela")

    global idcliP
    global nomecliP

    for selection in tv.selection(): 
        item = tv.item(selection)     
        idcliP, nomecliP = item["values"][0:2]  
    print("idcliP= ", idcliP)      
    Ecpfcli.delete(0, END) 
    Enomecli.delete(0, END)
    Etelcli.delete(0, END)
    Eendcli.delete(0, END)

    global chave_banco

    chave_banco = idcliP 
        
    try:        
        cursor = connect.cursor()
        sql_select_query = """SELECT cpfcli, nomecli, telcli, endcli, idcli \
        FROM tbcliente WHERE idcli = %s""" 
        cursor.execute(sql_select_query, (chave_banco,))                    
        rows = cursor.fetchall()  
        for col in rows:  
            Ecpfcli.insert(0, col[0])
            Enomecli.insert(0, col[1])
            Etelcli.insert(0, col[2])
            Eendcli.insert(0, col[3])
                    
            return "Carga das colunas da Tabela com sucesso!"
    except Exception as e:
        print('Exception: {}'.format(e))
        return "Erro no Select tab de cliente"

def Func_cadastrar():
    print('entrou cad_cliente')

    cpfcliVar = (Ecpfcli.get())
    nomecliVar = Enomecli.get()
    telcliVar = Etelcli.get()
    endcliVar = Eendcli.get()

    #Verifica se o CPF está em branco
    if cpfcliVar == '':
        mensagem["text"] = "CPF está em branco!"
        Ecpfcli.focus_set()
        return
    elif cpfcnpj.validate(cpfcliVar) == False:
        #Utiliza uma biblioteca para verificar se o CPF é válido
        mensagem["text"] = "CPF Não está Válido !!"
        Ecpfcli.focus_set()
        return
    
    #Verifica se o nome está em branco!
    if nomecliVar == "":
        mensagem["text"] = "Nome em branco !"
        Enomecli.focus_set()
        return
    else:
        #Verifica se o nome é maior que 60 letras
        if len(nomecliVar) > 60:
            mensagem["text"] = "Nome maior que 60 caracteres ?"
            Enomecli.focus_set()

    #Verifica se o número de telefone está em branco
    if len(str(telcliVar)) == 0:
        mensagem["text"] = "Número de Telefone em branco!"
        Etelcli.focus_set()
        return
    elif len(str(telcliVar)) < 10:
        #Verifica se o número de telefone é menor que 10
        mensagem['text'] = "Número de Telefone faltando !"
        Etelcli.focus_set()
        return
    elif len(str(telcliVar)) > 10:
        #Verifica se o número de telefone é maior que 10
        mensagem['text'] = "Número de Telefone a mais que o normal !"
        Etelcli.focus_set()
        return
    
    if endcliVar == "":
        mensagem['text'] = "Endereço em branco!"
        Eendcli.focus_set()
        return
    elif len(endcliVar) > 60:
        mensagem['text'] = "Endereço tem mais de 60 caracteres!"
        Eendcli.focus_set()
        return

    #Faz um select procurando se já existe o CPF Cadastrado
    #Se tiver então é duplicado e não pode ser USADO !!!
    try:        
        cursor = connect.cursor()
        sql_select_query = """SELECT cpfcli FROM tbcliente WHERE cpfcli = %s""" 
        cursor.execute(sql_select_query, (cpfcliVar,))                 
        rows = cursor.fetchall()
        print(rows)
        if rows != []:
            mensagem['text'] = 'CPF Já Cadastrado !!'
            Ecpfcli.focus_set()
            return
    except Exception as e:
        print('Exception: {}'.format(e))
        return "Erro na verificação de duplicidade do cpf!"
    #Realiza o cadastro no Banco de Dados
    try:
        cursor = connect.cursor() 
        sql_insert_query = """INSERT INTO tbcliente(cpfcli, nomecli, telcli, endcli) \
                    VALUES(%s, %s, %s, %s)"""
        cursor.execute(sql_insert_query, (cpfcliVar, nomecliVar, telcliVar, endcliVar,))
        connect.commit()
        cursor.close()
        mensagem["text"] = "Cliente cadastrado"
    except Exception as erro:
        mensagem["text"] = "Erro no Cadastro"
        print('Exception: {}'.format(erro))
        
        raise Exception(erro)


    Ecpfcli.delete(0, END) #limpa os campo
    Enomecli.delete(0, END) 
    Etelcli.delete(0, END)
    Eendcli.delete(0, END)

    Func_carregaTV() 

def Func_alterar():
    global cpfcliVar
    cpfcliVar = Ecpfcli.get()
    nomecliVar = Enomecli.get()
    telcliVar = Etelcli.get()
    endcliVar = Eendcli.get()

    #Verifica se o CPF está em branco
    if cpfcliVar == '':
        mensagem["text"] = "CPF está em branco!"
        Ecpfcli.focus_set()
        return
    elif cpfcnpj.validate(cpfcliVar) == False:
        #Utiliza uma biblioteca para verificar se o CPF é válido
        mensagem["text"] = "CPF Não está Válido !!"
        Ecpfcli.focus_set()
        return
    
    #Verifica se o nome está em branco!
    if nomecliVar == "":
        mensagem["text"] = "Nome em branco !"
        Enomecli.focus_set()
        return
    else:
        #Verifica se o nome é maior que 60 letras
        if len(nomecliVar) > 60:
            mensagem["text"] = "Nome maior que 60 caracteres ?"
            Enomecli.focus_set()

    #Verifica se o número de telefone está em branco
    if len(str(telcliVar)) == 0:
        mensagem["text"] = "Número de Telefone em branco!"
        Etelcli.focus_set()
        return
    elif len(str(telcliVar)) < 12:
        #Verifica se o número de telefone é menor que 10
        mensagem['text'] = "Número de Telefone faltando !"
        Etelcli.focus_set()
        return
    elif len(str(telcliVar)) > 10:
        #Verifica se o número de telefone é maior que 10
        mensagem['text'] = "Número de Telefone a mais que o normal !"
        Etelcli.focus_set()
        return
    
    if endcliVar == "":
        mensagem['text'] = "Endereço em branco!"
        Eendcli.focus_set()
        return
    elif len(endcliVar) > 60:
        mensagem['text'] = "Endereço tem mais de 60 caracteres!"
        Eendcli.focus_set()
        return

    try:
        cursor = connect.cursor()
        sql_update_query = """UPDATE tbcliente SET cpfcli = %s, nomecli = %s, telcli = %s, \
                        endcli = %s WHERE idcli = %s"""
        cursor.execute(sql_update_query, (cpfcliVar, nomecliVar, telcliVar, endcliVar, chave_banco))           
        connect.commit()
        cursor.close()        
        mensagem["text"] = "Cliente atualizado"
        print('após atualizado')        
    except psycopg2.Error as erro:
        mensagem["text"] = "Erro de Atualização"
        print("Erro no Update tab Cliente: ", erro)
        print('após print erro no update')     
    
    Func_carregaTV()
    
    Ecpfcli.delete(0, END)
    Enomecli.delete(0, END)
    Etelcli.delete(0, END)
    Eendcli.delete(0, END)

def Func_block():
    mensagem["text"] = "Não permitido!"

def Func_excluir():
    print("passou Func_excluir")

    try:
            cursor = connect.cursor()
            sql_delete_query = """DELETE FROM tbcliente WHERE idcli = %s"""
            cursor.execute(sql_delete_query, (chave_banco,))
            connect.commit()
            cursor.close()
            mensagem["text"] = "Cliente deletado"
    except psycopg2.Error as erro:
            print("Erro no Delete tab Cliente: ", erro)           
    
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

btnSair = Button(L20)
btnSair["text"] = "SAIR"
btnSair["font"] = ("Calibri", "20","bold")
btnSair["width"] = 10
btnSair["command"] = App.quit
btnSair.pack(side=LEFT)

##########################################################    
mensagem = Label(container9, text="")
mensagem["font"] = ("Verdana", "20", "italic", "bold")
mensagem.pack()

lblselect= Label(container10, text="Selecione um registro abaixo para Incluir, Alterar ou Excluir",
font=fontePadrao, width=50)
lblselect.pack(side=LEFT)

frame = Frame(App)
frame.pack(pady=20)

tv = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5), show='headings', height=10)
tv.pack(side=LEFT)

tv.heading(1, text="ID cliente")
tv.column("#1",minwidth=0,width=100)
tv.heading(2, text="CPF")
tv.column("#2",minwidth=0,width=100)
tv.heading(3, text="Nome")
tv.column("#3",minwidth=0,width=100)
tv.heading(4, text="Telefone")
tv.column("#4",minwidth=0,width=100)
tv.heading(5, text="Endereço")
tv.column("#5",minwidth=0,width=100)
# tv.heading(6, text="Unidade")
# tv.column("#6",minwidth=0,width=100)

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