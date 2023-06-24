from re import A
from tkinter import *
from tkinter import ttk
import psycopg2

connect = psycopg2.connect(
user = 'postgres',
password = 'root',
database = 'erp_proj')
cursor = connect.cursor()

App = Tk()
fontePadrao = ("Calibri", "16",)
App.title('CADASTRO DE USUARIOS')
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

titulo = Label(L1, text="Cadastro de Usuarios")
titulo["font"] = ("Arial", "20", "bold")
titulo.pack()

Lusuario = Label(L2,text="Usuario  ", font=fontePadrao)
Lusuario.pack(side=LEFT)
Eusuario = Entry(L2,width=40,font=fontePadrao)
Eusuario.pack(side=LEFT)

Lsenha = Label(L3, text="Senha    ", font=fontePadrao)
Lsenha.pack(side=LEFT)
Esenha = Entry(L3,width=40,font=fontePadrao, show='*')
Esenha.pack(side=LEFT)


Checkprod = IntVar()
Checkcli = IntVar()
Checkfornec = IntVar()
Checkvend = IntVar()
Checkuser = IntVar()
Checkentrada = IntVar()
CheckEntMer = IntVar()
CheckPdv = IntVar()

def definirPermissao():
    if Checkprod.get() == 1:
        mensagem['text'] = ''
    elif Checkcli.get() == 1:
        mensagem['text'] = ''
    elif Checkfornec.get() == 1:
        mensagem['text'] = ''
    elif Checkvend.get() == 1:
        mensagem['text'] = ''
    elif Checkuser.get() == 1:
        mensagem['text'] = ''
    elif Checkentrada.get() == 1:
        mensagem['text'] = ''
    elif CheckEntMer.get() == 1:
        mensagem['text'] = ''
    elif CheckPdv.get() == 1:
        mensagem['text'] = ''


PMprod = Checkbutton(L4, text = "Cad Produto", variable=Checkprod, \
                 onvalue = 1, offvalue = 0, font=('Arial 12 bold'), command=definirPermissao)
PMprod.pack(side=LEFT)
PMcli = Checkbutton(L5, text = "Cad Cliente", variable=Checkcli, \
                 onvalue = 1, offvalue = 0, font=('Arial 12 bold'), command=definirPermissao)
PMcli.pack(side=LEFT)
PMfornec = Checkbutton(L4, text = "Cad Fornecedor", variable=Checkfornec, \
                 onvalue = 1, offvalue = 0, font=('Arial 12 bold'), command=definirPermissao)
PMfornec.pack(side=LEFT)
PMvend = Checkbutton(L5, text = "Cad Vendedor", variable=Checkvend, \
                 onvalue = 1, offvalue = 0, font=('Arial 12 bold'), command=definirPermissao)
PMvend.pack(side=LEFT)
PMuser = Checkbutton(L4, text = "Cad User", variable=Checkuser, \
                 onvalue = 1, offvalue = 0, font=('Arial 12 bold'), command=definirPermissao)
PMuser.pack(side=LEFT)
PMentrada = Checkbutton(L5, text = "Ent Mer", variable=Checkentrada, \
                 onvalue = 1, offvalue = 0, font=('Arial 12 bold'), command=definirPermissao)
PMentrada.pack(side=LEFT)

# PMEntMer = Checkbutton(L4, text = "Ent Prod", variable=CheckEntMer, \
#                  onvalue = 1, offvalue = 0, font=('Arial 12 bold'), command=definirPermissao)
# PMEntMer.pack(side=LEFT)

PMPdv = Checkbutton(L5, text = "PDV", variable=CheckPdv, \
                 onvalue = 1, offvalue = 0, font=('Arial 12 bold'), command=definirPermissao)
PMPdv.pack(side=LEFT)

print(Checkprod)


def Func_carregaTV(): # Lê os dados do banco e envia para treeview
    print("passou Func_carregaTV")
    tv.delete(*tv.get_children()) # Limpa a treeview 
    try:
        cursor = connect.cursor() 
        cursor.execute("SELECT id, usuario, senha, produtos, clientes, fornecedores, \
                        vendedores, colaboradores, entmer, pdv FROM tbuser ORDER BY id ASC")
        rows = cursor.fetchall()
        usuario = ''
        senha = ''
        produtos = ''
        clientes = ''
        fornecedores = ''
        vendedores = ''
        colaboradores = ''
        entmer = ''
        pdv = ''
        
        for row in rows:
            id = row[0]
            usuario = row[1]
            senha = row[2]
            produtos = row[3]
            clientes = row[4]
            fornecedores = row[5]
            vendedores = row[6]
            colaboradores = row[7]
            entmer = row[8]
            pdv = row[9]
            
            

            tv.insert("", 'end', text=id, values=(id, usuario, senha, produtos, clientes,
                                fornecedores, vendedores, colaboradores, entmer, pdv))
            cursor.close()
        
    except psycopg2.Error as erro:
        print("Erro no select tab produto: ", erro)

def Func_envia_dadoTV_tela(event): # Select da linha da tabela para Tela
    print("passou envia_dadoTV_tela")

    global idP
    global senhaP
    global PMprodP
    global PMcliP
    global PMfornecP
    global PMvendP
    global PMuserP
    global PMentradaP
    global PMEntMer
    global PMPdv
    for selection in tv.selection(): 
        item = tv.item(selection)     
        idP, senhaP, PMprodP, PMcliP, PMfornecP, PMvendP, PMuserP, PMentradaP, PMEntMerP, PMPdvP = item["values"][0:10]  
    print("idP= ", idP)
    print(item['values'][3])
    CheckprodVar = item['values'][3]
    CheckcliVar = item['values'][4]
    CheckfornecVar = item['values'][5]
    CheckvendVar = item['values'][6]
    CheckuserVar = item['values'][7]
    CheckentradaVar = item['values'][8]
    # CheckEntMerVar = item['values'][8]
    CheckPdvVar = item['values'][9]


    Eusuario.delete(0, END) 
    Esenha.delete(0, END)
    if CheckprodVar == 'y':
        PMprod.select()
    else:
        PMprod.deselect()
        mensagem['text'] = ''
    if CheckcliVar == 'y':
        PMcli.select()
    else:
        PMcli.deselect()
        mensagem['text'] = ''
    if CheckfornecVar == 'y':
        PMfornec.select()
    else:
        PMfornec.deselect()
        mensagem['text'] = ''
    if CheckvendVar == 'y':
        PMvend.select()
    else:
        PMvend.deselect()
        mensagem['text'] = ''
    if CheckuserVar == 'y':
        PMuser.select()
    else:
        PMuser.deselect()
        mensagem['text'] = ''
    if CheckuserVar == 'y':
        PMuser.select()
    else:
        PMuser.deselect()
        mensagem['text'] = ''
    if CheckentradaVar == 'y':
        PMentrada.select()
    else:
        PMentrada.deselect()
        mensagem['text'] = ''        
    if CheckPdvVar == 'y':
        PMPdv.select()
    else:
        PMPdv.deselect()
        mensagem['text'] = ''        
    global chave_banco

    chave_banco = idP 
        
    try:        
        cursor = connect.cursor()
        sql_select_query = """SELECT usuario, senha, produtos, clientes, fornecedores, \
        vendedores, colaboradores, entmer, pdv FROM tbuser WHERE id = %s""" 
        cursor.execute(sql_select_query, (chave_banco,))                    
        rows = cursor.fetchall()  
        for col in rows:  
            Eusuario.insert(0, col[0])
            Esenha.insert(0, col[1])
            Checkprod.set(0, col[2])
            Checkcli.set(0, col[3])
            Checkfornec.set(0, col[4])
            Checkvend.set(0, col[5])
            Checkuser.set(0, col[6])
            Checkentrada.set(0, col[7])
            CheckPdv.set(0, col[8])
                    
                    
            return "Carga das colunas da Tabela com sucesso!"
    except Exception as e:
        print('Exception: {}'.format(e))
        return "Erro no Select tab de cliente"

def Func_cadastrar():
    print('entrou cad_usuario')

    usuarioVar = Eusuario.get()
    senhaVar = Esenha.get()
    CheckprodVar = Checkprod.get()
    CheckcliVar = Checkcli.get()
    CheckfornecVar = Checkfornec.get()
    CheckvendVar = Checkvend.get()
    CheckuserVar = Checkuser.get()
    CheckentradaVar = Checkentrada.get()
    CheckPdvVar = CheckPdv.get()

    if Checkprod.get() == 1:
        CheckprodVar = 'y'
    else:
        CheckprodVar = 'n'
    if Checkcli.get() == 1:
        CheckcliVar = 'y'
    else:
        CheckcliVar = 'n'
    if Checkfornec.get() == 1:
        CheckfornecVar = 'y'
    else:
        CheckfornecVar = 'n'
    if Checkvend.get() == 1:
        CheckvendVar = 'y'
    else:
        CheckvendVar = 'n'
    if Checkuser.get() == 1:
        CheckuserVar = 'y'
    else:
        CheckuserVar = 'n'
    if Checkentrada.get() == 1:
        CheckentradaVar = 'y'
    else:
        CheckentradaVar = 'n'
    if CheckPdv.get() == 1:
        CheckPdvVar = 'y'
    else:
        CheckPdvVar = 'n'
    try:        
        cursor = connect.cursor()
        sql_select_query = """SELECT usuario FROM tbuser WHERE usuario = %s""" 
        cursor.execute(sql_select_query, (usuarioVar,))                 
        rows = cursor.fetchall()
        print(rows)
        if rows != []:
            mensagem['text'] = 'Usuario Já Cadastrado !!'
            Eusuario.focus_set()
            return
    except Exception as e:
        print('Exception: {}'.format(e))
        return "Erro na verificação de duplicidade do usuario!"
    if usuarioVar == "":
       mensagem["text"] = "Usuario em Branco !"
       Eusuario.focus_set()
       return
    else:
         if len(usuarioVar) > 40:
            mensagem["text"] = "Usuario maior que 40 caracteres !"
            Eusuario.focus_set()
            return
    
    if senhaVar == "":
       mensagem["text"] = "Senha em Branco !"
       Eusuario.focus_set()
       return
    else:
         if len(usuarioVar) > 10:
            mensagem["text"] = "senha maior que 10 caracteres ?"
            Eusuario.focus_set()
            return
    try:
        cursor = connect.cursor() 
        sql_insert_querry = 'INSERT INTO tbuser(usuario, senha, produtos, clientes, fornecedores, \
        vendedores, colaboradores, entmer, pdv) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql_insert_querry, (usuarioVar, senhaVar, CheckprodVar, \
        CheckcliVar, CheckfornecVar, CheckvendVar, CheckuserVar, CheckentradaVar, CheckPdvVar),)
        connect.commit()
        cursor.close()
        mensagem["text"] = "Cliente cadastrado"
    except Exception as erro:
        mensagem["text"] = "Erro no Cadastro"
        print('Exception: {}'.format(erro))
        raise Exception(erro)
    Func_carregaTV()
    Eusuario.delete(0, END) #limpa os campo
    Esenha.delete(0, END)

     

def Func_alterar():
    global usuarioVar
    usuarioVar = Eusuario.get()
    senhaVar = Esenha.get()
    CheckprodVar = Checkprod.get()
    CheckcliVar = Checkcli.get()
    CheckfornecVar = Checkfornec.get()
    CheckvendVar = Checkvend.get()
    CheckuserVar = Checkuser.get()
    CheckentradaVar = Checkentrada.get()    
    CheckPdvVar = CheckPdv.get()


    if Checkprod.get() == 1:
        CheckprodVar = 'y'
    else:
        CheckprodVar = 'n'
    if Checkcli.get() == 1:
        CheckcliVar = 'y'
    else:
        CheckcliVar = 'n'
    if Checkfornec.get() == 1:
        CheckfornecVar = 'y'
    else:
        CheckfornecVar = 'n'
    if Checkvend.get() == 1:
        CheckvendVar = 'y'
    else:
        CheckvendVar = 'n'
    if Checkuser.get() == 1:
        CheckuserVar = 'y'
    else:
        CheckuserVar = 'n'
    if Checkentrada.get() == 1:
        CheckentradaVar = 'y'
    else:
        CheckentradaVar = 'n'
    if CheckPdv.get() == 1:
        CheckPdvVar = 'y'
    else:
        CheckPdvVar = 'n'
   
    if usuarioVar == "":
       mensagem["text"] = "Usuario em Branco ?"
       Eusuario.focus_set()
       return
    else:
         if len(usuarioVar) > 40:
            mensagem["text"] = "Usuario maior que 40 caracteres ?"
            Eusuario.focus_set()
            return
    
    if senhaVar == "":
       mensagem["text"] = "senha em Branco ?"
       Eusuario.focus_set()
       return
    else:
         if len(senhaVar) > 10:
            mensagem["text"] = "senha maior que 10 caracteres ?"
            Eusuario.focus_set()
            return 

    try:
        cursor = connect.cursor()
        # sql_update_query = """UPDATE tbuser SET usuario = %s, senha = %s WHERE id = %s"""
# 'INSERT INTO tbuser(usuario, senha, produtos, clientes, fornecedores,vendedores, colaboradores)
        sql_insert_querry = 'UPDATE tbuser SET usuario = %s, senha = %s, produtos = %s, clientes = %s, \
        fornecedores = %s, vendedores = %s, colaboradores = %s, entmer = %s, pdv = %s WHERE id = %s'
        cursor.execute(sql_insert_querry, (usuarioVar, senhaVar, CheckprodVar, \
        CheckcliVar, CheckfornecVar, CheckvendVar, CheckuserVar, CheckentradaVar, CheckPdvVar, chave_banco),)
        # cursor.execute(sql_update_query, (usuarioVar, senhaVar, chave_banco))           
        connect.commit()
        cursor.close()
        mensagem["text"] = "Cliente atualizado"
        print('após atualizado') 
    except psycopg2.Error as erro:
        mensagem["text"] = "Erro de Atualização"
        print("Erro no Update tab Cliente: ", erro)
        print('após print erro no update')
    
    Func_carregaTV()

    Eusuario.delete(0, END)
    Esenha.delete(0, END)
    

def Func_block():
    mensagem["text"] = "Não permitido!"

def Func_excluir():
    print("passou Func_excluir")

    try:
            cursor = connect.cursor()
            sql_delete_query = """DELETE FROM tbuser WHERE id = %s"""
            cursor.execute(sql_delete_query, (chave_banco,))
            connect.commit()
            cursor.close()
            mensagem["text"] = "usuario deletado"
    except psycopg2.Error as erro:
            print("Erro no Delete tab Cliente: ", erro)           
    
    Func_carregaTV()

def sair():
    #App.withdraw() esconder tela
    quit()

caduser = Button(L20)
caduser["text"] = "CADASTRAR"
caduser["font"] = ("Calibri", "20","bold")
caduser["width"] = 10
caduser["command"] = Func_cadastrar
caduser.pack(side=LEFT)

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
mensagem["font"] = ("Verdana", "20", "italic", "bold" )
mensagem.pack()

lblselect= Label(container10, text="Selecione um registro abaixo para Incluir, Alterar ou Excluir",
font=fontePadrao, width=50)
lblselect.pack(side=LEFT)

frame = Frame(App)
frame.pack(pady=20)

tv = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), show='headings', height=10)
tv.pack(side=LEFT)

tv.heading(1, text="ID ")
tv.column("#1",minwidth=0,width=100, anchor='center')
tv.heading(2, text="usuario")
tv.column("#2",minwidth=0,width=100, anchor='center')
tv.heading(3, text="senha")
tv.column("#3",minwidth=0,width=100, anchor='center')
tv.heading(4, text="P")
tv.column("#4",minwidth=0,width=20, anchor='center')
tv.heading(5, text="C")
tv.column("#5",minwidth=0,width=20, anchor='center')
tv.heading(6, text="F")
tv.column("#6",minwidth=0,width=20, anchor='center')
tv.heading(7, text="V")
tv.column("#7",minwidth=0,width=20, anchor='center')
tv.heading(8, text="CO")
tv.column("#8",minwidth=0,width=20, anchor='center')
tv.heading(9, text="EM")
tv.column("#9",minwidth=0,width=22, anchor='center')
tv.heading(10, text="PDV")
tv.column("#10",minwidth=0,width=24, anchor='center')


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