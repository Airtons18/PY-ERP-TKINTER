import tkinter
from PIL import Image, ImageTk 
import psycopg2

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

connect = psycopg2.connect(
user = 'postgres',
password = 'root',
database = 'erp_proj')
cursor = connect.cursor()



from tkinter import *

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
App.config(bg='#181820')

#   Barra de Titulo do Windows
Frame_title_bar = Frame(App, height=50, bg='#181820')
Frame_title_bar.pack(fill=X)

#   Titulo Inicial
titulo_label = Label(Frame_title_bar, text="DASHBOARD VENDAS", font=("Arial bold", 16), bg='#181820', fg='#FFFFFF')
titulo_label.pack(side=LEFT, padx=34)

co1 = '#FFFFFF'
co2 = '#000000'
co3 = '#11c400'
co4 = '#12BC9F'
co5 = '#2F4F4F'
co6 = '#192a2a'

#   Corpo parte de cima
Frame_info_pequenas = Frame(App, height=100, bg='#181820')
Frame_info_pequenas.pack(pady=5, fill=X, padx=34)

##  Informações Pequenas 1
Frame_info_peq = Frame(Frame_info_pequenas, width=270, height=100)
Frame_info_peq.pack(side=LEFT)
imagem2 = PhotoImage(file='img-grafics\g_info_peq.png')
Canvas_info_peq = Canvas(Frame_info_peq, width = 270, height = 100, relief='ridge', highlightthickness=0, bg='#181820', border=0)      
Canvas_info_peq.pack()          
Canvas_info_peq.create_image(0,0, anchor=NW, image=imagem2)

#   Legendas Informações Pequenas 1
Label_desc_info_peq = Label(Frame_info_peq, text='Valor Total Vendido', width=15, height=1, relief='flat', padx=0, pady=0, bg=co6, fg=co1)
Label_desc_info_peq['font'] = ('Arial', '12', 'bold')
Label_desc_info_peq.place(x=15, y=5)
Label_total_valor = Label(Frame_info_peq, text='R$ 0.000.000,00', width=15, height=1, relief='flat',
padx=0, pady=0, bg=co6, fg=co4, font=('Arial bold', 18))
Label_total_valor.place(x=20, y=40)
Label_total_profit = Label(Frame_info_peq, text='+ 101% vs mês anterior', width=20, height=1, relief='flat', padx=0, pady=0, bg=co6, fg=co3)
Label_total_profit['font'] = ('Arial', '9', 'bold')
Label_total_profit.place(x=40, y=75)

#   Informações pequenas 2
Frame_info_peq2 = Frame(Frame_info_pequenas, width=270, height=100)
Frame_info_peq2.pack(side=LEFT, padx=10)
Canvas_info_peq2 = Canvas(Frame_info_peq2, width = 270, height = 100, relief='ridge', highlightthickness=0, bg='#181820', border=0)      
Canvas_info_peq2.pack()          
Canvas_info_peq2.create_image(0,0, anchor=NW, image=imagem2)

#   Legendas Informações Pequenas 2
Label_desc_info_unid_peq = Label(Frame_info_peq2, text='Unidade Total Vendida', width=17, height=1, relief='flat', padx=0, pady=0, bg=co6, fg=co1)
Label_desc_info_unid_peq['font'] = ('Arial', '12', 'bold')
Label_desc_info_unid_peq.place(x=15, y=5)
Label_total_unidade = Label(Frame_info_peq2, text='0.000.000.000', width=15, height=1, relief='flat',
padx=0, pady=0, bg=co6, fg=co4, font=('Arial bold', 18))
Label_total_unidade.place(x=20, y=40)
Label_total__und_profit = Label(Frame_info_peq2, text='+ 101% vs mês anterior', width=20, height=1, relief='flat', padx=0, pady=0, bg=co6, fg=co3)
Label_total__und_profit['font'] = ('Arial', '9', 'bold')
Label_total__und_profit.place(x=40, y=75)


#   Frame parte dos graficos grandes
Frame_graficos = Frame(App, height=250, bg='#181820')
Frame_graficos.pack(fill=X, padx=34)

#   Frame graficos grandes 1
Frame_graficos_gfc = Frame(Frame_graficos, width=550, height=250, bg='lightblue')
Frame_graficos_gfc.pack(side=LEFT)

imagem = PhotoImage(file='img-grafics\g_grafico.png')
Canvas_graficos_gfc = Canvas(Frame_graficos_gfc, width = 550, height = 250, relief='ridge', highlightthickness=0, bg='#181820', border=0)      
Canvas_graficos_gfc.pack()          
Canvas_graficos_gfc.create_image(0,0, anchor=NW, image=imagem)

Label_desc_gfc = Label(Frame_graficos_gfc, text='Top 5 Melhores Vendedores R$', width=25, height=1, relief='flat', padx=0, pady=0, bg=co6, fg=co1)
Label_desc_gfc['font'] = ('Arial', '12', 'bold')
Label_desc_gfc.place(x=40, y=5)


Frame_graficos_gfc2 = Frame(Frame_graficos, width=550, height=250, bg='lightblue')
Frame_graficos_gfc2.pack(side=RIGHT)
Canvas_graficos_gfc = Canvas(Frame_graficos_gfc2, width = 550, height = 250, relief='ridge', highlightthickness=0, bg='#181820', border=0)      
Canvas_graficos_gfc.pack()          
Canvas_graficos_gfc.create_image(0,0, anchor=NW, image=imagem)

Label_desc_gfc2 = Label(Frame_graficos_gfc2, text='Top 5 Itens mais Vendidos', width=20, height=1, relief='flat', padx=0, pady=0, bg=co6, fg=co1)
Label_desc_gfc2['font'] = ('Arial', '12', 'bold')
Label_desc_gfc2.place(x=40, y=5)

#   
Frame_graficos_peq = Frame(App, height=250, bg='#181820')
Frame_graficos_peq.pack(fill=X, padx=34, pady=5)

# Canvas_graficos_peq = Canvas(Frame_graficos_gfc2, width = 550, height = 250, relief='ridge', highlightthickness=0, bg='#181820', border=0)      
# Canvas_graficos_peq.pack()          
# Canvas_graficos_peq.create_image(0,0, anchor=NW, image=imagem)
    
try:
        # SELECT * FROM tbvdresumo WHERE dtvdres = 'AAAA-MM-DD'
        # sql_insert_query = """SELECT SUM(totvdres) as Total_vendido_no_dia FROM tbvdresumo WHERE dtvdres = %s """
        sql_select_query3 = """SELECT SUM(totvdres) FROM tbvdresumo"""
        sql_select_query = """select vendvdres, SUM(totvdres) as Total_vendedor FROM tbvdresumo 
                    GROUP BY vendvdres
                    ORDER BY Total_vendedor DESC LIMIT 5"""

        # sql_select_query2 = """select descvditem, SUM(vlrttvditem) as Total_Valor FROM tbvditens
        #     GROUP BY descvditem
        #     ORDER BY Total_Valor DESC LIMIT 5
        # """
        sql_select_query2 = """select descvditem, SUM(qtdvditem) as Total_Valor FROM tbvditens
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
        Label_total_valor.configure(text="R$ "+str(ValorTotal))
        Label_total_unidade.configure(text=str(QtdTotal))
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
        canva1 = FigureCanvasTkAgg(figura1, Frame_graficos_gfc)
        canva1.get_tk_widget().place(x=0, y=30)

        ########## GRAFICO 2 ###############

        # valor_total_valor.configure(text="R$ "+str(ValorTotal))
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
        canva2 = FigureCanvasTkAgg(figura2, Frame_graficos_gfc2)
        canva2.get_tk_widget().place(x=0, y=30)
        

except psycopg2.Error as erro:
    # mensagem["text"] = "Erro Insert tbproduto"
    print("Erro no Update tab produto: ", erro)
    print('após print erro no insert')












App.mainloop()