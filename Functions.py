from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import os
from dotenv import load_dotenv
from web import Web
import pyautogui as pa
from time import sleep


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
        
        

    