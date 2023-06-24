from re import A
from tkinter import *
from tkinter import ttk
import psycopg2
import os
from tkinterweb import HtmlFrame #import the HTML browser
from tkhtmlview import HTMLLabel

import pandas as pd
import plotly_express as px

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from datetime import datetime

connect = psycopg2.connect(
user = 'postgres',
password = 'root',
database = 'erp_proj')
cursor = connect.cursor()
tempo = datetime.now()

App = Tk()
fontePadrao = ("Calibri", "16",)
fontePadrao1 = ("Calibri", "16", "bold")
App.title('Relatório de Vendas Diário')
App.largura = 1190
App.altura  = 680
App.largura_scr = App.winfo_screenwidth()
App.altura_scr  = App.winfo_screenheight()
App.posx = App.largura_scr/2 - App.largura/2
App.posy = App.altura_scr/2  - App.altura/2
App.geometry("%dx%d+%d+%d" % (App.largura, App.altura - 30 , App.posx, App.posy))
App.resizable(width=FALSE, height=FALSE)
# App.minsize(width=1350, height=700)
'''
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
'''

##Declaração de cores

co1 = '#FFFFFF'
co2 = '#000000'
co3 = '#11c400'
co4 = '#12BC9F'
co5 = '#2F4F4F'
co6 = '#192a2a'
App.config(bg='#000000')
titulo = Label(App, text='DASHBOARD VENDAS', width=22, height=2, relief='flat', padx=0, pady=0, fg=co1, bg='#000000')
titulo['font'] = ('Arial', '16', 'bold')
titulo.place(x=0,y=0)


frame_valor_total = Frame(App, width=270, height=100, padx=0, pady=0, relief='flat', bg=co6)
frame_valor_total.place(x=10, y=50)

# frame_valor_total = Frame(App, width=270, height=100, padx=0, pady=0, relief='flat', bg=co6)
# frame_valor_total.pack(side='top', anchor='w', pady=50, padx=34)

valor_total_nome = Label(frame_valor_total, text='Valor Total Vendido', width=15, height=1, relief='flat', padx=0, pady=0, bg=co6, fg=co1)
valor_total_nome['font'] = ('Arial', '12', 'bold')
valor_total_nome.place(x=15, y=5)

valor_total_valor = Label(frame_valor_total, text='R$ 0.000.000,00', width=15, height=1, relief='flat', padx=0, pady=0, bg=co6, fg=co4)
valor_total_valor['font'] = ('Arial', '18')
valor_total_valor.place(x=0, y=35)

valor_total_profit = Label(frame_valor_total, text='+ 101% vs mês anterior', width=20, height=1, relief='flat', padx=0, pady=0, bg=co6, fg=co3)
valor_total_profit['font'] = ('Arial', '9', 'bold')
valor_total_profit.place(x=25, y=70)

frame_qtd_itens = Frame(App, width=270, height=100, padx=0, pady=0, relief='flat', bg=co6)
frame_qtd_itens.place(x=290, y=50)

qtd_label_nome = Label(frame_qtd_itens, text='Unidades Vendida', width=15, height=1, relief='flat', padx=0, pady=0, bg=co6, fg=co1)
qtd_label_nome['font'] = ('Arial', '12', 'bold')
qtd_label_nome.place(x=15, y=5)

qtd_label_valor = Label(frame_qtd_itens, text='0.000.000.000', width=15, height=1, relief='flat', padx=0, pady=0, bg=co6, fg=co4)
qtd_label_valor['font'] = ('Arial', '18')
qtd_label_valor.place(x=0, y=35)

qtd_label_profit = Label(frame_qtd_itens, text='+ 101% vs mês anterior', width=20, height=1, relief='flat', padx=0, pady=0, bg=co6, fg=co3)
qtd_label_profit['font'] = ('Arial', '9', 'bold')
qtd_label_profit.place(x=25, y=70)

frame_gfc_vendedores = Frame(App, width=550, height=250, padx=0, pady=0, relief='flat', bg=co6)
frame_gfc_vendedores.place(x=10, y=160)

# frame_gfc_vendedores = Frame(App, width=550, height=250, padx=0, pady=0, relief='flat', bg=co6)
# frame_gfc_vendedores.pack(side=LEFT, padx=34)

titulo_gfc_vendedores = Label(frame_gfc_vendedores, text='Melhores Vendedores', width=20, height=1, relief='flat', padx=0, pady=0, bg=co6, fg=co1)
titulo_gfc_vendedores['font'] = ('Arial', '12', 'bold')
titulo_gfc_vendedores.place(x=0, y=5)

frame_gfc_itens = Frame(App, width=550, height=250, padx=0, pady=0, relief='flat', bg=co6)
frame_gfc_itens.place(x=570, y=160)

# frame_gfc_itens = Frame(App, width=550, height=250, padx=0, pady=0, relief='flat', bg=co6)
# frame_gfc_itens.pack(side=RIGHT, padx=34)

titulo_gfc_itens = Label(frame_gfc_itens, text='Produtos Mais Vendidos em R$', width=30, height=1, relief='flat', padx=0, pady=0, bg=co6, fg=co1)
titulo_gfc_itens['font'] = ('Arial', '12', 'bold')
titulo_gfc_itens.place(x=0, y=5)


try:
        # SELECT * FROM tbvdresumo WHERE dtvdres = 'AAAA-MM-DD'
        # sql_insert_query = """SELECT SUM(totvdres) as Total_vendido_no_dia FROM tbvdresumo WHERE dtvdres = %s """
        sql_select_query3 = """SELECT SUM(totvdres) FROM tbvdresumo"""
        sql_select_query = """select vendvdres, SUM(totvdres) as Total_vendedor FROM tbvdresumo 
                    GROUP BY vendvdres
                    ORDER BY Total_vendedor DESC LIMIT 5"""

        sql_select_query2 = """select descvditem, SUM(vlrttvditem) as Total_Valor FROM tbvditens
            GROUP BY descvditem
            ORDER BY Total_Valor DESC LIMIT 5
        """
        sql_select_query4 = '''select SUM(qtdvditem) from tbvditens'''
        # cursor.execute(sql_insert_query, (diaVar,))
        cursor.execute(sql_select_query,)
        rows = cursor.fetchall()
        cursor.execute(sql_select_query2,)
        rows2 = cursor.fetchall()

        cursor.execute(sql_select_query3,)
        rows3 = cursor.fetchall()

        cursor.execute(sql_select_query4,)
        rows4 = cursor.fetchall()
        ValorTotal = rows3[0][0]
        QtdTotal = rows4[0][0]

        connect.commit()
        
        cursor.close()
        # rows = pd.DataFrame(rows)
        # rows = [[4, 110930.00], [3, 33535.00]]
        valor_total_valor.configure(text="R$ "+str(ValorTotal))
        qtd_label_valor.configure(text=str(QtdTotal))
        figura1 = plt.figure(figsize=(8.5, 3), dpi=65)
        ax1 = figura1.add_subplot(111)
        figura1.patch.set_facecolor('#192a2a')
        ax1.patch.set_facecolor('#192a2a')
        ax1.xaxis.label.set_color('red')
        ax1.tick_params(axis='x', colors='white', labelsize='large', grid_antialiased=True)
        ax1.tick_params(axis='y', colors='white', labelsize='large', grid_antialiased=True)
        
        ax1.tick_params(bottom=False, left=False)
        ax1.set_axisbelow(True)
        ax1.yaxis.grid(True, color='white')
        
        x = []
        y = []
        for row in range(len(rows)):
            x.append("Vendedor "+str(rows[row][0]))
            y.append(rows[row][1])   

        # hbar1 = ax1.bar(x, y, color='#12BC9F')
        hbar1 = ax1.bar(x, y)
        ax1.bar_label(hbar1, label=['.2f'] ,label_type='center', color='white', font='Arial', fontsize=16)
        canva1 = FigureCanvasTkAgg(figura1, frame_gfc_vendedores)
        canva1.get_tk_widget().place(x=0, y=30)

        ########## GRAFICO 2 ###############

        valor_total_valor.configure(text="R$ "+str(ValorTotal))
        figura2 = plt.figure(figsize=(8.5, 3), dpi=65)
        ax2 = figura2.add_subplot(111)
        figura2.patch.set_facecolor('#192a2a')
        ax2.patch.set_facecolor('#192a2a')
        ax2.xaxis.label.set_color('red')
        ax2.tick_params(axis='x', colors='white', labelsize='large', grid_antialiased=True)
        ax2.tick_params(axis='y', colors='white', labelsize='large', grid_antialiased=True)
        
        ax2.tick_params(bottom=False, left=False)
        ax2.set_axisbelow(True)
        ax2.yaxis.grid(True, color='white')
        
        x = []
        y = []
        for row in range(len(rows2)):
            x.append(str(rows2[row][0]))
            y.append(rows2[row][1])   
        print(rows3)
        # hbar2 = ax2.bar(x, y, color='#12BC9F')
        hbar2 = ax2.bar(x, y)
        ax2.bar_label(hbar2, label=['.2f'] ,label_type='center', color='white', font='Arial', fontsize=16)
        canva2 = FigureCanvasTkAgg(figura2, frame_gfc_itens)
        canva2.get_tk_widget().place(x=0, y=30)
        

except psycopg2.Error as erro:
    # mensagem["text"] = "Erro Insert tbproduto"
    print("Erro no Update tab produto: ", erro)
    print('após print erro no insert')


def Rdv_val_total_no_dia():
    try:
        # SELECT * FROM tbvdresumo WHERE dtvdres = 'AAAA-MM-DD'
        sql_select_query3 = """SELECT SUM(totvdres) FROM tbvdresumo"""
        sql_select_query = """select vendvdres, SUM(totvdres) as Total_vendedor FROM tbvdresumo 
                    GROUP BY vendvdres
                    ORDER BY Total_vendedor DESC LIMIT 5"""

        sql_select_query2 = """select descvditem, SUM(vlrttvditem) as Total_Valor FROM tbvditens
            GROUP BY descvditem
            ORDER BY Total_Valor DESC LIMIT 5
        """
        # cursor.execute(sql_insert_query, (diaVar,))
        cursor.execute(sql_select_query,)
        rows = cursor.fetchall()
        cursor.execute(sql_select_query2,)
        rows2 = cursor.fetchall()
        cursor.execute(sql_select_query3,)
        rows3 = cursor.fetchall()
        Select1Var = cursor.fetchall()
        ValorTotal = rows3[0][0]
        connect.commit()
        cursor.close()
        # rows = pd.DataFrame(rows)
        # rows = [[4, 110930.00], [3, 33535.00]]
        x = []
        y = []
        for row in range(len(rows)):
            x.append("Vendedor "+str(rows[row][0]))
            y.append(rows[row][1])
        print('X:', x)
        print('Y:', y)
        fig = px.bar(x=x, y=y, text=y)
        fig.update_xaxes(showgrid=True, ticks="outside")
        fig.layout.update({'title': 'Total de Vendas'})
        # fig.show()
        # fig.write_image("img-grafics\Grafico1.png")
        fig.write_image("img-grafics\Grafico1.png", scale=1, width=400, height=230)
        x = []
        y = []
        for row in range(len(rows2)):
            x.append(str(rows2[row][0]))
            y.append(rows2[row][1])
        print('X:', x)
        print('Y:', y)
        fig = px.bar(x=x, y=y, text=(y))
        fig.update_xaxes(showgrid=True, ticks="outside")
        fig.layout.update({'title': 'Produtos Mais Vendidos'})
        # fig.show()
        fig.write_image("img-grafics\Grafico2.png", scale=1, width=400, height=230)
        # x = []
        # y = []
        # for row in range(len(rows)):
        #     x.append("Vendedor "+str(rows[row][0]))
        #     y.append(rows[row][1])   

        # plt.bar(x=x, y=y)
        # plt.show()



        ####
        
        # fig.write_html('meuRelatorio.html')
    except psycopg2.Error as erro:
        # mensagem["text"] = "Erro Insert tbproduto"
        print("Erro no Update tab produto: ", erro)
        print('após print erro no insert')

##############################################################
##############################################################
##############################################################

def Func_Pesquisar():
    # if EdiaSelecionado.get() == '' and EmesSelecionado.get() == '' and EanoSelecionado.get() == '':

    #     Rdv_val_total_no_dia()
    # else:
    #     dia = EdiaSelecionado.get()
    #     mes = EmesSelecionado.get()
    #     ano = EanoSelecionado.get()
    #     Rdv_val_total_no_dia()
    Rdv_val_total_no_dia()


# btnSomarDias = Button(L6)
# btnSomarDias['text'] = 'PESQUISAR'
# btnSomarDias['font'] = ('Calibri', '20', 'bold')
# btnSomarDias['width'] = 13
# btnSomarDias['command'] = Func_Pesquisar
# btnSomarDias.pack(side=LEFT, pady=10, padx=10)





App.mainloop()