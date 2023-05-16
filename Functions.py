from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import os
from dotenv import load_dotenv
from web import Web
import matplotlib.pyplot as plt
import pyautogui as pa
from time import sleep
import pandas as pd

class Functions():
    
    def __init__(self) -> None:
        load_dotenv()

        self._host = os.getenv('DB_HOST')
        self._user = os.getenv('DB_USER')
        self._password = os.getenv('DB_PASS')
        self._database = os.getenv('DB_NAME')
        
   
    
    def _connect_db(self):
        try:
            self._connection = mysql.connector.connect(
                host=self._host,
                user=self._user,
                password=self._password,
                database=self._database,
                charset='utf8')
        except Exception as e:
            print(f"We can't connected with the server. \033[31m ERROR!: {e} \033[m")
        else:
            self.cursor = self._connection.cursor()
       
    def _disconnect_db(self):
        self._connection.close()
        
        
    def web_scrapping(self):
        w = Web()
        
       
    def OnDoubleClick(self, event):
        self.lista_celulares.selection()
        
        for celular in self.lista_celulares.selection():
            col1, col2, col3, col4 = self.lista_celulares.item(celular, 'values')
            print(col2)
            pa.press('winleft')
            sleep(2)
            pa.typewrite('google', 0.2)
            pa.press('enter')
            sleep(0.5)
            pa.typewrite(col2, 0.1)
            pa.press('enter')
            
            
    def get_all_phones(self):
        self._connect_db()
        self.lista_celulares.delete(*self.lista_celulares.get_children())
        sql = f"SELECT * FROM celulares;"
        self.cursor.execute(sql)
        celulares = self.cursor.fetchall()
        for c in celulares:
            self.lista_celulares.insert("", END, values=c)
        self._disconnect_db()
        
    def get_per_marca(self):
        text = self.clicked.get()
        self._connect_db()
        self.lista_celulares.delete(*self.lista_celulares.get_children())
        
        sql = f"SELECT * FROM celulares WHERE marca LIKE '%{text}%' ORDER BY nome ASC;"
        self.cursor.execute(sql)
        celulares = self.cursor.fetchall()
        for c in celulares:
            self.lista_celulares.insert("", END, values=c)
        self._disconnect_db()

    def export(self):
        text = self.clickedExport.get()
        print(text)
        self._connect_db()
        sql = f"SELECT * FROM celulares ORDER BY marca ASC;"
        self.cursor.execute(sql)
        celulares = self.cursor.fetchall()
        self._disconnect_db()
        celulares = pd.DataFrame(celulares)
        
        if text == '.XLSX':
            print("excel")
            os.remove('C:/Users/57761933898/Desktop/somativa-python/celulares.xlsx')
            cel = celulares.to_excel('C:/Users/57761933898/Desktop/somativa-python/celulares.xlsx', index=False)
            
        elif text == '.CSV':
            print("csv")
            cel = celulares.to_csv('C:/Users/57761933898/Desktop/somativa-python/celulares.csv')
        
        
    
        
    
    def grafico(self):
        

        fig, ax = plt.subplots()
        modelos = []
        
        self._connect_db()
        sql = f"SELECT * FROM celulares ORDER BY preco DESC;"
        self.cursor.execute(sql)
        celulares = self.cursor.fetchall()
        self._disconnect_db()
        for celular in celulares:
            nome = celular[1][0:30]
            preco = celular[3]
            try:
                preco = preco.split(",")
                preco = preco[0]
                preco = int(str(preco).replace(".","").strip())
            except:
                print("...")
            else:
                modelos.append((nome,preco))
               
        
        precos_ordem = sorted(modelos,reverse=True)
        print(precos_ordem)

        bar_labels = [precos_ordem[0][0],precos_ordem[1][0],precos_ordem[2][0], precos_ordem[3][0]]
        counts = [precos_ordem[0][1],precos_ordem[1][1],precos_ordem[2][1], precos_ordem[3][1]]
        print(bar_labels)
        bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']

        ax.bar(bar_labels, counts, label=counts, color=bar_colors)

        ax.set_ylabel('Preço')
        ax.set_title('Celulares mais caros')
        ax.legend(title='Modelo')

        plt.show()

    