from ast import Delete
from email import message
from itertools import count
from msilib.schema import Error
from re import A
import time
from tkinter import *
from tkinter import ttk
from tkinter import font
from unicodedata import numeric
import psycopg2
import subprocess
import os
import pickle
from pathlib import Path

connect = psycopg2.connect(
user = 'postgres',
password = 'root',
database = 'erp_proj')
cursor = connect.cursor()
App = Tk()
fontePadrao = ("Calibri", "16",)
fontePadrao1 = ("Calibri", "16", "bold")
App.title('PDV- Vendas')
App.largura = 1350
App.altura  = 700
App.largura_scr = App.winfo_screenwidth()
App.altura_scr  = App.winfo_screenheight()
App.posx = App.largura_scr/2 - App.largura/2
App.posy = App.altura_scr/50  - App.altura/50
App.geometry("%dx%d+%d+%d" % (App.largura, App.altura - 30 , App.posx, App.posy))
App.minsize(width=1350, height=700)

L1 = Frame(App)
L1["pady"] = 5
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
L20["pady"] = 20
L20.pack()
container9 = Frame(App)
container9["pady"] = 20
container9 .pack()
container10 = Frame(App)
container10.pack()
container11 =  Frame(App)
container11.pack(side=BOTTOM, fill=X)
titulo = Label(L1, text="PDV - Vendas")
titulo["font"] = ("Arial", "20", "bold")
titulo.pack()

##################################################
#       FUNÇÃO DOS BOTÕES 
##################################################
contador = 0
TotalVar = 0
listaItens = []
numcaixa = "N/A"
caixastatus = "FECHADO"
vendedorid = "N/A"
cliid = ""



qtdVar = 0

def Func_JanelaTmp():
    global numcaixa
    global caixastatus
    global vendedorid
    global cliid
    novaJanela = ""
    novaJanela = Tk()
    fontePadrao = ("Calibri", "16",)
    novaJanela.title('N° Caixa')
    novaJanela.largura = 500
    novaJanela.altura  = 620
    novaJanela.largura_scr = App.winfo_screenwidth()
    novaJanela.altura_scr  = App.winfo_screenheight()
    novaJanela.posx = App.largura_scr/2 - App.largura/2
    novaJanela.posy = App.altura_scr/2  - App.altura/2
    novaJanela.geometry("%dx%d+%d+%d" % (novaJanela.largura, novaJanela.altura - 30 , novaJanela.posx, novaJanela.posy))    
    L1 = Frame(novaJanela, bg='black')
    L1["pady"] = 5
    L1.pack()
    L2 = Frame(novaJanela)
    L2["padx"] = 20
    L2.pack()
    L3 = Frame(novaJanela)
    L3["padx"] = 20
    L3.pack()
    L4 = Frame(novaJanela)
    L4["padx"] = 20
    L4.pack()
    L5 = Frame(novaJanela)
    L5["padx"] = 20
    L5.pack()
    L6 = Frame(novaJanela)
    L6["padx"] = 20
    L6.pack()
    container9 = Frame(novaJanela)
    container9["pady"] = 20
    container9 .pack()
    container10 = Frame(novaJanela, bg='orange')
    container10.pack()
    container11 =  Frame(novaJanela)
    container11.pack(side=BOTTOM, fill=X)
    titulo = Label(L1, text="Número Caixa")
    titulo["font"] = ("Arial", "15", "bold")
    titulo.pack()


    def Func_verificar(*agrs):
        global numcaixa
        global vendedorid
        idvendVar = (Eusuario.get())
        cxnumVar = Enumcaixa.get()
        try:
            cursor = connect.cursor()
            sql_delete_query = """SELECT * from tbvendedor WHERE idvend=%s"""
            cursor.execute(sql_delete_query, (int(idvendVar),))
            rows = cursor.fetchall() 
            # print(rows[0][1])
            connect.commit()
            cursor.close()
            if rows != []:
                mensagem["text"] = "VENDEDOR " + rows[0][1] + ' CAIXA '+ cxnumVar
                vendedorid = str(rows[0][0])
                numcaixa = cxnumVar
                btnAbrirCaixa.config(state=DISABLED)
                novaJanela.destroy()
                novaJanela.quit()
            else:
                mensagem['text'] = "CAIXA OU VENDEDOR NÃO CADASTRADO!!"
        except psycopg2.Error as erro:
            print("Erro no Delete tab produto: ", erro)    
    def sair():
        quit()

    def focusEvendedor(event):
        Eusuario.focus_set()
    Lnumcaixa = Label(L2, text="Número do caixa:", font=fontePadrao)
    Lnumcaixa.pack(side=LEFT)
    Enumcaixa = Entry(L2, font=fontePadrao, width=5)
    Enumcaixa.pack(side=LEFT)
    Enumcaixa.focus_force()
    Enumcaixa.bind('<Return>', focusEvendedor)

    Lusuario = Label(L3, text='          ID Vendedor', font=fontePadrao)
    Lusuario.pack(side=LEFT, pady=10)
    Eusuario = Entry(L3, font=fontePadrao, width=5)
    Eusuario.pack(side=LEFT, pady=10)
    Eusuario.bind('<Return>', Func_verificar)

    btnVerificar = Button(L4, text='Entrar', font=fontePadrao)
    btnVerificar.pack(side=LEFT)
    btnVerificar['command'] = Func_verificar

    btnCancelar = Button(L4, text='Cancelar', font=fontePadrao)
    btnCancelar.pack(side=LEFT)
    btnCancelar['command'] = sair

    mensagem = Label(container9,)
    mensagem["font"] = ("Verdana", "20", "bold", "italic")
    mensagem.pack()


    novaJanela.mainloop()


def Func_abrirCaixa():
    global Func_JanelaTmp
    global caixastatus
    global numcaixa
    global vendedorid
    if caixastatus == "FECHADO":
        Func_JanelaTmp()
        caixastatus = 'ABERTO'
        statusvar.set("CAIXA -> ["+numcaixa+"]    |   ["+caixastatus+"]   |  VEND -> ["+vendedorid+"]     |")
        if numcaixa != "N/A" and caixastatus != "FECHADO" and vendedorid != "N/A":
            btnAdicionar.config(state=NORMAL)
            btnExcluir.config(state=NORMAL)
            Ecodbarprod.config(state=NORMAL)
            Eqtditem.config(state=NORMAL)
            mensagem['text'] = 'CAIXA ABERTO'
    else:
        pass
def Func_adicionar(*agrs):
    global codbarVar
    global TotalVar
    global contador
    global listaItens
    global qtdVar
    codbarVar = Ecodbarprod.get()
    qtdVar = int(Eqtditem.get())
    try:
        cursor = connect.cursor()
        sql_select_querry = """SELECT * FROM tbproduto WHERE codbarprod=%s"""
        cursor.execute(sql_select_querry, (codbarVar,))  
        rows = cursor.fetchall()         
        connect.commit()
        cursor.close()        
        if rows == []:
            mensagem["text"] = "PRODUTO NÃO ENCONTRADO"
        else:
            mensagem["text"] = "PRODUTO ADICIONADO"
        print('após encontrar')
        codbarprod = ''
        ncmprod = ''
        descprod = ''
        vlrunprod = ''
        unidprod = ''
        for row in rows:
            contador = contador + 1
            idprod = row[0]
            codbarprod = row[1]
            ncmprod = row[2]
            descprod = row[3]
            vlrunprod = row[4]
            unidprod = row[5]
            totalLinha = float(vlrunprod) * int(qtdVar)
            TotalVar = (TotalVar+totalLinha)
            Etotal.config(state=NORMAL)
            Etotal.delete(0, END)
            Etotal.insert(0, str(TotalVar))
            Etotal.config(state='readonly')
            print(TotalVar)
            listaItens.append([contador, codbarprod, ncmprod, descprod, float(vlrunprod), unidprod, qtdVar, totalLinha])
            print(listaItens)
            tv.insert("", 'end', text=idprod, values=(contador, codbarprod, ncmprod, descprod, vlrunprod, unidprod, qtdVar, totalLinha))
            cursor.close()    
            for selection in tv.selection(): 
                item = tv.item(selection)     
                print("ITEM: ", item['values'])    
    except psycopg2.Error as erro:
        mensagem["text"] = "Erro Produto não encontrado"
        print("Erro no select tab produto: ", erro)
        print('após print erro no select')
    Ecodbarprod.delete(0, END)
    Eqtditem.delete(0, END)
    Ecodbarprod.focus_set()
    tv_scroll.config(command=tv.yview_moveto(1))
def Func_deletar():
    global TotalVar
    global listaItens
    tempList = []
    # print("Antes da subtracao:", TotalVar)
    
    selected_item = tv.selection()[0] ## get selected item
    for selection in tv.selection(): 
        item = tv.item(selection)
        # tempList.append(item['values'])
        print("FIXO : ", listaItens)
        # print("TEMP  :" ,tempList)
        print("ESSE É O ITEM: ", item)
        print("INDICE: ", item['values'][0])
        indice, codbarP, ncmP, descP, vlrunitP, unitP, qtdP, totalLP = item['values'][0:8]
        tempList.append([int(indice), str(codbarP), int(ncmP), str(descP), float(vlrunitP), str(unitP), int(qtdP), float(totalLP)])
        print("MANUAL: ",tempList)
    print('LISTA ANTES: ', listaItens)
    listaItens.remove(tempList[0])
    print("DEPOIS :", tempList)
    print("LISTA DELETADA: ", listaItens)
    TotalVar = TotalVar - float(item['values'][7])
    # print("Depois da subtracao:", TotalVar)
    tv.delete(selected_item)
    Etotal.config(state=NORMAL)
    Etotal.delete(0, END)
    Etotal.insert(0, str(TotalVar))
    Etotal.config(state='readonly')
    # print(selected_item)
#     for x in len(tv.get_children()):
#         tv.insert(x, 'end', text=idprod, values=(len(tv.get_children()), codbarprod, ncmprod, descprod, vlrunprod, unidprod, qtdVar, totalLinha))       

def Func_ler_qtdestq(codproduto):
    print("entrou func ler qtdestq")
    global estqantVar
    try:
        cursor = connect.cursor()
        sql_select_query = """SELECT qtdestq FROM tbestoque WHERE codbarprod = %s""" 
        cursor.execute(sql_select_query, (codproduto,))
        rows = cursor.fetchall()
        print("TESTE", rows)
        if cursor.rowcount > 0:
            for col in rows: 
                estqantVar = int(col[0])
        else:
            pass
        cursor.close()
    except Exception as e:
            print('Exception: {}'.format(e))
            return "Erro na verificação estoque!"

def Func_Atualiza_estoque(itemqtd, codproduto):
    global qtdVar
    global estqantVar
    global fim
    print("atualiza estoque cod barra", codproduto)
    if estqantVar >= itemqtd:
        estqfinalVar = (estqantVar - itemqtd) # calcula o estoque final
        try:
            cursor = connect.cursor()
            sql_update_query = """UPDATE tbestoque SET qtdestq = %s WHERE codbarprod = %s"""
            cursor.execute(sql_update_query, (estqfinalVar, codproduto))  
            print("passou apos update estoque")        
            connect.commit()
            cursor.close()        
            mensagem["text"] = "ESTOQUE DO PRODUTO ATUALIZADO"
            fim = 1
        except psycopg2.Error as erro:
            mensagem["text"] = "Erro de Atualização"
            print("Erro no Update tab estoque: ", erro)
            print('após print erro no update')
    else:
        mensagem['text'] = "SEM ESTOQUE, item:"+codbarVar
        fim = 0


fim = 0


def Func_grava_vd_item():
    try:
        try:
            cursor = connect.cursor()
            sql_select_querry = """SELECT * FROM tbvdresumo ORDER BY idvdres DESC LIMIT 1"""
            cursor.execute(sql_select_querry) 
            rows1 = cursor.fetchall()
            print(rows1)
            connect.commit()
            cursor.close()
            print("select tbvdresumo teste", rows1)
            if rows1 == []:
                ultimoid = 1
            else:
                print('entro no else')
                a = rows1[0][0]
                ultimoid = int(a)
        except psycopg2.Error as erro:
            mensagem["text"] = "Erro Produto não encontrado"
            print("Erro no select tab produto: ", erro)
            print('após print erro no select')
        for linha in range(len(listaItens)):
            descitem = listaItens[linha][3]
            qtditem = listaItens[linha][6]
            vlrunitario = listaItens[linha][4]
            totalprod = listaItens[linha][7]

            cursor = connect.cursor()
            sql_select_querry = """INSERT INTO tbvditens(descvditem, idresumo, qtdvditem, vlrunvditem, vlrttvditem) \
            VALUES(%s,%s,%s,%s,%s)"""
            # sql_select_querry = """INSERT INTO tbvdresumo(totvdres, vlrrecres, trocores, vendvdres, clivdres, numcxres, dtvdres, hrvdres) \
            # VALUES(%s,%s,%s,%s,%s,%s, CURRENT_DATE, CURRENT_TIME)"""
            cursor.execute(sql_select_querry, (descitem, ultimoid, qtditem, vlrunitario, totalprod,))
            # cursor.execute(sql_select_querry, (TotalVar ,valorPagoVar ,troco ,vendvdresVar ,clivdresVar ,numcxVar ,))  
            connect.commit()
            cursor.close()               
    except psycopg2.Error as erro:
        mensagem["text"] = "Erro Produto não encontrado"
        print("Erro no select tab produto: ", erro)
        print('após print erro no select')
CountVar = 0
def Contagem():
    global CountVar
    global fim
    try:
        cursor = connect.cursor()
        sql_select_querry = """SELECT * FROM tbvdresumo ORDER BY idvdres DESC LIMIT 1"""
        cursor.execute(sql_select_querry) 
        rows1 = cursor.fetchall()
        print(rows1)
        connect.commit()
        cursor.close()
        if rows1 == []:
            CountVar = 1
        else:
            CountVar = 0
            print('entro no else')
            a = rows1[0][0]
            print("NA CONTAGEM3 ",rows1)
            print("NA CONTAGEM4 ", rows1[0][1])
            CountVar = 1 + int(a)
            fim = 3
    except psycopg2.Error as erro:
        mensagem["text"] = "Erro Produto não encontrado"
        print("Erro no select tab produto: ", erro)
        print('após print erro no select')

def Func_grava_comvenda():
    global vendedorid
    global TotalVar
    try:
        cursor = connect.cursor()
        sql_insert_querry = """INSERT INTO tbcomvenda(codvend, vrcomvenda, statuscomvenda) \
            VALUES(%s,%s,%s)"""
        cursor.execute(sql_insert_querry, (vendedorid, TotalVar*0.1, "A Pagar",)) 
        connect.commit()
        cursor.close()
    except psycopg2.Error as erro:
        mensagem["text"] = "Erro comvenda não encontrado"
        print("Erro no select tab produto: ", erro)
        print('após print erro no select')    


def Funcao_Contas_Receber():
    global TotalVar
    global cliid
    statusctrecVar = 'a receber'
    if cliid != '':
        try:
            cursor = connect.cursor() 
            sql_insert_query = """SELECT idcli FROM tbcliente WHERE idcli=%s"""
            cursor.execute(sql_insert_query, (int(cliid),))
            rows = cursor.fetchall()
            connect.commit()
            cursor.close()
            if rows != []:
                
                try:
                    cursor = connect.cursor() 
                    sql_insert_query = """INSERT INTO tbcontareceber(codcli, vrctrec, statusctrec) \
                    VALUES(%s, %s, %s)"""
                    cursor.execute(sql_insert_query, (int(cliid), TotalVar, "A Pagar",))
                    connect.commit()
                    cursor.close()
                    
                except Exception as erro:
                    mensagem["text"] = "Erro ctrec_receber 2"
                    print('Exception Func_ctrec_: {}'.format(erro))
            else:
                mensagem['text'] = "vendedor não existe!"
        except Exception as erro:
            mensagem["text"] = "Erro conta_receber 1"
            print('Exception Func_conta_receber: {}'.format(erro))
    else:
        pass



def Func_grava_contareceber():
    global cliid
    global TotalVar
    try:
        cursor = connect.cursor()
        sql_insert_querry = """INSERT INTO tbcontareceber(codcli, vrctrec, statusctrec) \
            VALUES(%s,%s,%s)"""
        cursor.execute(sql_insert_querry, (cliid, TotalVar, "A Receber",)) 
        connect.commit()
        cursor.close()
    except psycopg2.Error as erro:
        mensagem["text"] = "Erro contareceber não encontrado"
        print("Erro no select tab produto: ", erro)
        print('após print erro no select') 

def Func_grava_item_resumo():
    global usuario
    global TotalVar
    global fim
    global listaItens
    global estqantVar
    global CountVar
    global cliid
    valorPagoVar = float(Evalreceber.get())
    troco = float(valorPagoVar)-TotalVar
    if float(valorPagoVar) > TotalVar:
        mensagem['text']  = "Troco de R$", format(troco, '.2f')
        fim = 2
    elif float(valorPagoVar) < TotalVar:
        mensagem['text'] = "Falta ainda R$", format(troco, '.2f')
        fim = 2
    elif float(valorPagoVar) == TotalVar:
        mensagem['text'] = "Pagamento Concluido! não precisa de troco!"
        troco = 0
    cursor = connect.cursor()
    sql_insert_querry = """INSERT INTO tbvdresumo(idvdres, totvdres, vlrrecres, trocores, vendvdres, clivdres, numcxres, dtvdres, hrvdres) \
    VALUES(%s,%s,%s,%s,%s,%s,%s, CURRENT_DATE, CURRENT_TIME)"""
    # cursor.execute(sql_select_querry, (descitem, ultimoid, qtditem, vlrunitario, TotalVar,))
    cursor.execute(sql_insert_querry, (CountVar,TotalVar ,valorPagoVar ,troco , vendedorid, cliid, numcaixa ,))
    connect.commit()
    cursor.close()  

def Func_vrfCli():
    global cliid
    global fim
    codclivar = int(Ecodcli.get(), base=10)
    try:
        cursor = connect.cursor()
        sql_select_querry = """SELECT * FROM tbcliente WHERE idcli=%s"""
        cursor.execute(sql_select_querry, (codclivar,)) 
        rows1 = cursor.fetchall()
        print(rows1)
        connect.commit()
        cursor.close()
        if rows1 != []:
            cliid = rows1[0][0]
            fim = 3
        else:
            mensagem['text'] = 'Cliente não encontrado!!'
    except psycopg2.Error as erro:
        mensagem["text"] = "Erro Cliente não encontrado"
        print("Erro no select tab Cliente: ", erro)
        print('após print erro no select')    

def limpaTudo():
    global TotalVar
    global listaItens
    for i in tv.get_children():
        tv.delete(i)
    Ecodbarprod.delete(0, END)
    Ecodcli.delete(0, END)
    Eqtditem.delete(0, END)
    Etotal.delete(0, END)
    TotalVar = 0
    listaItens = []
    Evalreceber.delete(0, END)
    Evalreceber.config(state=DISABLED)
    Ecodbarprod.focus_set()

def Func_finalizar(*agrs):
    global TotalVar
    global fim
    global listaItens
    global estqantVar
    qtdretirar = 0
    Evalreceber.config(state=NORMAL)
    print("numero de linhas: ", len(listaItens))
    print("Qtd da linha: ", listaItens[0][6])
    Evalreceber.focus_set()
    fim = 1
    if fim == 1:
        if Evalreceber.get() == "":
            pass
        else:
            valorPagoVar = float(Evalreceber.get())
            troco = float(valorPagoVar)-TotalVar
        if float(valorPagoVar) > TotalVar:
            mensagem['text']  = "Troco de R$", format(troco, '.2f')
            Ecodcli.focus_set()
            if Ecodcli.get() != '':
                fim = 2
            else:
                mensagem['text'] = 'Inserir id do cliente !'
        elif float(valorPagoVar) < TotalVar:
            mensagem['text'] = "Dinheiro faltando R$", format(troco, '.2f')
            fim = 1
        elif float(valorPagoVar) == TotalVar:
            mensagem['text'] = "Pagamento Concluido! não precisa de troco!"
            troco = 0
            Ecodcli.focus_set()
            if Ecodcli.get() != '':
                fim = 2
            else:
                mensagem['text'] = 'Inserir o id do cliente !'

    if fim == 2:
        Func_vrfCli()
        pontuacao = 0
    if fim == 3:
        for linha in range(len(listaItens)):
            codproduto = (listaItens[linha][1])
            itemqtd = (listaItens[linha][6])
            totalprod = (listaItens[linha][7])
            Func_ler_qtdestq(codproduto)
            print("DENTRO DO ULTIMO PASSO")
            print("linha", codproduto, itemqtd)
            Contagem()
            if estqantVar >= itemqtd:
                pontuacao = pontuacao + 1
            else:
                mensagem['text'] = "ITEM SEM ESTOQUE"
        if len(listaItens) == pontuacao:
            for linha in range(len(listaItens)):
                print('TAMANHO LISTA', len(listaItens))
                codproduto = (listaItens[linha][1])
                itemqtd = (listaItens[linha][6])
                totalprod = (listaItens[linha][7])    
                Func_ler_qtdestq(codproduto)        
                Func_Atualiza_estoque(itemqtd, codproduto)
                # Func_grava_vd_item()
            Func_grava_contareceber()
            Func_grava_comvenda()
            Func_grava_item_resumo()
            Func_grava_vd_item()
            limpaTudo()

def Func_procuraCliente(*args):
    pass

                
def focusEqtd(event):
    Eqtditem.focus_set()

def focusCodcli(event):
    Ecodcli.focus_set()

# ##################################################
Lcodbarprod = Label(L3, text='Código de Barra:', font=fontePadrao)
Lcodbarprod.pack(side=LEFT)
Ecodbarprod = Entry(L3, font=fontePadrao, width=15)
Ecodbarprod.pack(side=LEFT)
Ecodbarprod.bind("<Return>", focusEqtd)

Lqtditem = Label(L3, text='  Qtd:', font=fontePadrao)
Lqtditem.pack(side=LEFT)
Eqtditem = Entry(L3, font=fontePadrao, width=9)
Eqtditem.pack(side=LEFT)
Eqtditem.bind('<Return>', Func_adicionar)

Ltotal = Label(L3, text="VALOR TOTAL:.R$", bg='light green', font=fontePadrao)
Ltotal.pack(side=LEFT)
Etotal = Entry(L3, font=fontePadrao1, bg='red', width=9, state="readonly")
Etotal.pack(side=LEFT)

Lvalreceber = Label(L4, font=fontePadrao,text='VALOR A RECEBER:.R$')
Lvalreceber.pack(side=LEFT, anchor='e')
Evalreceber = Entry(L4, font=fontePadrao, width=9, state=DISABLED)
Evalreceber.pack(side=LEFT, anchor='e')
Evalreceber.bind('<Return>', focusCodcli)

# Lcodvend = Label(L3, font=fontePadrao, text='Cód Vend: ')
# Lcodvend.pack(side=LEFT)
# Ecodvend = Entry(L3, font=fontePadrao, width=9)
# Ecodvend.pack(side=LEFT)

Lcodcli = Label(L4, font=fontePadrao, text='   Cód Cliente:')
Lcodcli.pack(side=LEFT)
Ecodcli = Entry(L4, font=fontePadrao, width=9)
Ecodcli.pack(side=LEFT)
Ecodcli.bind('<Return>', Func_finalizar)

btnAdicionar = Button(L5)
btnAdicionar['text'] = 'ADICIONAR'
btnAdicionar['font'] = ("Calibri", "20","bold")
btnAdicionar['width'] = 10
btnAdicionar['command'] = Func_adicionar
btnAdicionar.pack(side=LEFT, pady=10, padx=10)

btnExcluir = Button(L5)
btnExcluir['text'] = 'EXCLUIR'
btnExcluir['font'] = ("Calibri", "20","bold")
btnExcluir['width'] = 10
btnExcluir['command'] = Func_deletar
btnExcluir.pack(side=LEFT, pady=10, padx=10)

btnAbrirCaixa = Button(L5)
btnAbrirCaixa['text'] = 'ABRIR CAIXA'
btnAbrirCaixa['font'] = ("Calibri", "20","bold")
btnAbrirCaixa['width'] = 10
btnAbrirCaixa['command'] = Func_abrirCaixa
btnAbrirCaixa['bg'] = 'light blue'
btnAbrirCaixa.pack(side=LEFT, pady=10, padx=10)
# Espaco1 = Label(L5, text='                                                          \
#          ', font=fontePadrao)
# Espaco1.pack(side=LEFT)


btnFinalizar = Button(L5)
btnFinalizar['text'] = 'FECHAR VENDA'
btnFinalizar['font'] = ("Calibri", "20","bold")
btnFinalizar['width'] = 13
btnFinalizar['command'] = Func_finalizar
btnFinalizar.pack(side=LEFT, pady=10, padx=10)
App.bind('<End>', Func_finalizar)


btnAdicionar.config(state=DISABLED)
btnExcluir.config(state=DISABLED)
Ecodbarprod.config(state=DISABLED)
Eqtditem.config(state=DISABLED)
##########################################################    
mensagem = Label(container9,)
mensagem["font"] = ("Verdana", "20", "bold", "italic")
mensagem.pack()
# lblselect= Label(container10, text="Selecione um produto abaixo para Alterar ou Excluir",
# font=fontePadrao, width=50)
# lblselect.pack(side=LEFT)
frame = Frame(App)
frame.pack(padx=10)
statusvar = StringVar()
statusvar.set("CAIXA -> [N/A]    |   [FECHADO]   |  VEND -> [N/A]     |")
sbar = Label(container11, textvariable=statusvar, font=('Arial 12'), relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM, fill=X)

tv_scroll = Scrollbar(L1)
tv_scroll.pack(side=RIGHT, fill=Y)


tv = ttk.Treeview(L1, yscrollcommand=tv_scroll.set ,columns=(1, 2, 3, 4, 5, 6, 7, 8), show='headings', height=18)
tv.pack(side=LEFT, fill=X)
tv_scroll.config(command=tv.yview, troughcolor='blue')
tv.heading(1, text="N° Items")
tv.column("#1",minwidth=100, width=167, anchor='center')
tv.heading(2, text="Codigo de Barra")
tv.column("#2",minwidth=100, width=167, anchor='center')
tv.heading(3, text="NCM")
tv.column("#3",minwidth=100, width=167, anchor='center')
tv.heading(4, text="Descrição")
tv.column("#4",minwidth=100, width=167, anchor='center')
tv.heading(5, text="Valor Unitário")
tv.column("#5",minwidth=100, width=167, anchor='center')
tv.heading(6, text="Unidade")
tv.column("#6",minwidth=100, width=167, anchor='center')
tv.heading(7, text="Qtd")
tv.column("#7",minwidth=100, width=167, anchor='center')
tv.heading(8, text="Total")
tv.column("#8",minwidth=100, width=170, anchor='center')
# sb = Scrollbar(frame, orient=VERTICAL)
# sb.pack(side=RIGHT, fill=Y)
# tv.config(yscrollcommand=sb.set)
# sb.config(command=tv.yview)
tv.bind("<<TreeviewSelect>>")





style = ttk.Style()
style.theme_use("default")
style.map("Treeview")
App.mainloop()
    