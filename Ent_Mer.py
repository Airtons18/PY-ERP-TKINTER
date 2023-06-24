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
App.title('Entrada de Mercadoria')
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
titulo = Label(L1, text="Entrada de Mercadoria")
titulo["font"] = ("Arial", "20", "bold")
titulo.pack()
Lcodbarprod = Label(L2,text="Codigo de Barra", font=fontePadrao)
Lcodbarprod.pack(side=LEFT)
Ecodbarprod = Entry(L2,width=40,font=fontePadrao)
Ecodbarprod.pack(side=LEFT)
Lncmprod = Label(L3, text="N.C.M                ", font=fontePadrao)
Lncmprod.pack(side=LEFT)
Encmprod = Entry(L3,width=40,font=fontePadrao)
Encmprod.pack(side=LEFT)
Ldescprod = Label(L4,text="Descrição          ", font=fontePadrao)
Ldescprod.pack(side=LEFT)
Edescprod = Entry(L4,width=40,font=fontePadrao)
Edescprod.pack(side=LEFT)
Lvlrunprod = Label(L5,text="Valor Unitario   ", font=fontePadrao)
Lvlrunprod.pack(side=LEFT)
Evlrunprod = Entry(L5,width=40,font=fontePadrao)
Evlrunprod.pack(side=LEFT)
Lunidprod = Label(L6,text="Unidade             ", font=fontePadrao)
Lunidprod.pack(side=LEFT)
Eunidprod = Entry(L6,width=40,font=fontePadrao)
Eunidprod.pack(side=LEFT)
Lqtdestq = Label(L7,text="Quantidade       ", font=fontePadrao)
Lqtdestq.pack(side=LEFT)
Eqtdestq = Entry(L7,width=40,font=fontePadrao)
Eqtdestq.pack(side=LEFT)
# Lvlrtotmer = Label(L8,text="Valor Total        ", font=fontePadrao)
# Lvlrtotmer.pack(side=LEFT)
# Evlrtotmer = Entry(L8,width=40,font=fontePadrao)
# Evlrtotmer.pack(side=LEFT)
Lfornmer = Label(L9,text="Cod.Fornecedor", font=fontePadrao)
Lfornmer.pack(side=LEFT)
Efornmer = Entry(L9,width=40,font=fontePadrao)
Efornmer.pack(side=LEFT)

def Func_conta_pagar():
    global qtdestqVar
    global vlrunVar
    vlrtotVar = (int(qtdestqVar) * float(vlrunVar))
    codfornVar = (Efornmer.get())
    if codfornVar != '':
        try:
            cursor = connect.cursor() 
            sql_insert_query = """SELECT idfornec FROM tbfornec WHERE idfornec=%s"""
            cursor.execute(sql_insert_query, (int(codfornVar),))
            rows = cursor.fetchall()
            connect.commit()
            cursor.close()
            if rows != []:
                mensagem["text"] = "Fornecedor Selecionado"
                try:
                    cursor = connect.cursor() 
                    sql_insert_query = """INSERT INTO tbcontapagar(codfor, vrctpag, statusctpag) \
                    VALUES(%s, %s, %s)"""
                    cursor.execute(sql_insert_query, (int(codfornVar), vlrtotVar, "A Pagar",))
                    connect.commit()
                    cursor.close()
                    mensagem["text"] = "Conta Adicionada"
                except Exception as erro:
                    mensagem["text"] = "Erro conta_pagar 2"
                    print('Exception Func_conta_pagar: {}'.format(erro))
            else:
                mensagem['text'] = "Fornecedor não existe!"
        except Exception as erro:
            mensagem["text"] = "Erro conta_pagar 1"
            print('Exception Func_conta_pagar: {}'.format(erro))
    else:
        mensagem['text'] = 'Campo fornecedor vazio !'

def sair():
    quit()


def Func_ler_qtdestq():
    print("entrou func ler qtdestq")
    global estqantVar
    
    try:
        cursor = connect.cursor()
        sql_select_query = """SELECT qtdestq FROM tbestoque WHERE codbarprod = %s""" 
        cursor.execute(sql_select_query, (codbarVar,))
        rows = cursor.fetchall()
        if cursor.rowcount > 0:
            for col in rows: 
                estqantVar = int(col[0])
        else:
            pass
        cursor.close()
    except Exception as e:
            print('Exception: {}'.format(e))
            return "Erro na verificação estoque!"

def Func_Ler_produto():
    try:
        global contador_lido
        cursor = connect.cursor()
        sql_select_query = """SELECT * FROM tbproduto WHERE codbarprod = %s""" 
        cursor.execute(sql_select_query, (codbarVar,)) 
        contador_lido = cursor.rowcount
    except psycopg2.Error as erro:
        mensagem["text"] = "Erro select tbproduto"
        print("Erro no select tab produto: ", erro)
        print('após print erro no select')


def Func_Insert_produto():
    try:
        cursor = connect.cursor()
        sql_insert_query = """INSERT INTO tbproduto (codbarprod, ncmprod, descprod, vlrunprod, unidprod) \
        VALUES (%s,%s,%s,%s,%s)"""
        cursor.execute(sql_insert_query, (codbarVar, ncmVar, descVar, vlrunVar, unidVar))
        # cursor.execute('INSERT INTO tbproduto (codbarprod, ncmprod, descprod, vlrunprod, unidprod) \
        # VALUES (%s,%s,%s,%s,%s)',
        #         (codbarVar, ncmVar, descVar, vlrunVar, unidVar))
        connect.commit()
        cursor.close()
    except psycopg2.Error as erro:
        mensagem["text"] = "Erro Insert tbproduto"
        print("Erro no Update tab produto: ", erro)
        print('após print erro no insert')

def Func_Atualiza_produto():
    print("entrou func atualiza produto")
    try:
        cursor = connect.cursor()
        print("antes fazer update do produto ncm=", ncmVar)
        sql_update_query = """UPDATE tbproduto SET ncmprod = %s, descprod = %s, vlrunprod = %s, unidprod = %s WHERE codbarprod = %s"""
        cursor.execute(sql_update_query, (ncmVar, descVar, vlrunVar, unidVar, codbarVar))           
        connect.commit()
        #mensagem["text"] = "ESTOQUE DO PRODUTO ATUALIZADO"
        cursor.close()        
        print('após produto atualizado')        
    except psycopg2.Error as erro:
        mensagem["text"] = "Erro de Atualização"
        print("Erro no Update tab produto: ", erro)
        print('após print erro no update')

# atualiza estoque
def Func_Atualiza_estoque():
    global estqantVar
    print("atualiza estoque cod barra", codbarVar)
    estqfinalVar = (estqantVar + int(qtdestqVar)) # calcula o estoque final
    try:
        cursor = connect.cursor()
        sql_update_query = """UPDATE tbestoque SET qtdestq = %s WHERE codbarprod = %s"""
        cursor.execute(sql_update_query, (estqfinalVar,codbarVar))  
        print("passou apos update estoque")        
        connect.commit()
        cursor.close()        
        mensagem["text"] = "ESTOQUE DO PRODUTO ATUALIZADO"
    except psycopg2.Error as erro:
        mensagem["text"] = "Erro de Atualização"
        print("Erro no Update tab estoque: ", erro)
        print('após print erro no update')

# inclui estoque
def Func_Inclui_estoque():
    print("atualiza estoque cod barra", codbarVar)
    try:
        cursor = connect.cursor()
        cursor.execute('INSERT INTO tbestoque (codbarprod, qtdestq) \
                      VALUES (%s, %s)',
                      (codbarVar, qtdestqVar)) 
        print("passou apos insert estoque")        
        connect.commit()
        cursor.close()        
        mensagem["text"] = "ESTOQUE DO PRODUTO ATUALIZADO"
    except psycopg2.Error as erro:
        mensagem["text"] = "Erro no insert tbestoque"
        print("Erro no Insert tab estoque: ", erro)
        print('após print erro no update')

def Func_dar_entrada():
    #Definindo as Globais  
    global codbarVar
    global ncmVar 
    global descVar
    global vlrunVar
    global unidVar 
    global estqfinalVar 
    global qtdestqVar
    global estqantVar
 
    # movendo as variaveis
    codbarVar = Ecodbarprod.get()
    ncmVar = Encmprod.get()
    descVar = Edescprod.get()
    vlrunVar = Evlrunprod.get() 
    unidVar = Eunidprod.get()
    qtdestqVar = Eqtdestq.get()

    if str(codbarVar) == "":
        mensagem["text"] = "COD. BARRAS EM BRANCO?"
        return
    elif len(str(codbarVar)) > 3:
                mensagem["text"] = "COD. BARRAS MAIOR QUE 13 DIGITOS?"
                return
    else:
        if len(str(codbarVar)) < 3:
                mensagem["text"] = "COD. BARRAS MENOR QUE 13 DIGITOS?"
                return
    ncmVar = Encmprod.get()
    if str(ncmVar) == "":
        mensagem["text"] = "NCM EM BRANCO"
        return
    elif len(str(ncmVar)) > 8:
                mensagem["text"] = "NCM MAIOR QUE 8 DIGITOS?"
                return
    else:
        if len(str(ncmVar)) < 1:
                mensagem["text"] = "NCM MENOR QUE 8 DIGITOS?"
                return
    descVar = Edescprod.get()
    if descVar == "":
        mensagem["text"] = "Descrição em Branco ?"        
        return
    else:
        if len(descVar) > 30:
            mensagem["text"] = "DESCRIÇÃO GRANDE, DIMINUA"            
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
        if len(unidVar) > 10:
            mensagem["text"] = "UNIDADE GRANDE, ABREVIE"
            return
     
    # Chama funcao de leitura do produto
    Func_Ler_produto()
  
    #if cursor.rowcount > 0: 
    if contador_lido > 0:   # o produto já existe
        cursor = connect.cursor()
        # Chama funcao de leitura de estoque Anterior
        Func_ler_qtdestq() 

        # Chama funcao de atualizar produto      
        Func_Atualiza_produto()

        # Chama função atualiza estoque
        Func_Atualiza_estoque()  
        Func_conta_pagar()
        
    else: # o produto não existe
        # Chama função Insert Produto
        Func_Insert_produto()   
    
        # Chama função inclui estoque
        Func_Inclui_estoque() 
        Func_conta_pagar()
    


entmer = Button(L20)
entmer["text"] = "DAR ENTRADA"
entmer["font"] = ("Calibri", "20","bold")
entmer["width"] = 15
entmer["command"] = Func_dar_entrada
entmer.pack(side=LEFT)

Espaco1= Label(L20, text="  ",
font=fontePadrao, width=2,)
Espaco1.pack(side=LEFT)

bntsair = Button(L20)
bntsair["text"] = "SAIR"
bntsair["font"] = ("Calibri", "20","bold")
bntsair["width"] = 10
bntsair["command"] = sair
bntsair.pack(side=LEFT)

mensagem = Label(container9,)
mensagem["font"] = ("Verdana", "20", "bold", "italic")
mensagem.pack()

frame = Frame(App)
frame.pack(pady=20)

App.mainloop()