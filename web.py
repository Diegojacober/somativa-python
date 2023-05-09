from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
import mysql.connector
import os
from dotenv import load_dotenv

class Web:
    def __init__(self):
        
        load_dotenv()

        self._host = os.getenv('DB_HOST')
        self._user = os.getenv('DB_USER')
        self._password = os.getenv('DB_PASS')
        self._database = os.getenv('DB_NAME')
        
        self.sites = ['https://www.extra.com.br/c/telefones-e-celulares/samsung?filtro=c38_m459&icid=155416',
                      'https://www.extra.com.br/c/telefones-e-celulares/apple?filtro=c38_m19&icid=155416',
                      'https://www.extra.com.br/c/telefones-e-celulares/motorola?filtro=c38_m356&icid=155416',
                      'https://www.extra.com.br/c/telefones-e-celulares/xiaomi?filtro=c38_m127789&icid=155416',
                      'https://www.extra.com.br/c/telefones-e-celulares/lg?filtro=c38_m299&icid=155416']
        self.map = {
            'celular': {
                'nome' : '/html/body/div[1]/main/div/div/div/div/div[2]/div/div[4]/div[2]/div[3]/div[1]/div[$$]/div/div/div[2]',
                
            }
        }
    
        

        for site in self.sites:
            self.driver = webdriver.Chrome()
            self.driver.get(site)
            self.abrir(site)
            sleep(3)
            self.driver.close()
        

    

    def abrir(self,site):
    
        for i in range(1, 20):
            print(i, end=' ')
            
            try:
                
                nome = self.driver.find_element(By.XPATH, self.map['celular']['nome'].replace('$$', f"{i}")).text
                celular = nome.split("\n")
                nome_celular = celular[0]
                marca = site.split("?")[0][49:].upper()
                preco = celular[4][6:14]
                
                self.add_celular(nome_celular, marca, preco, i, site)
                
            except Exception as e:
                print('erro', e)
                continue
            
            
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
        
    def tables(self):
        self._connect_db()
        sql = """DROP TABLE celulares;
            CREATE TABLE IF NOT EXISTS celulares(
            id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            nome VARCHAR(255) not null,
            marca VARCHAR(26),
            preco VARCHAR(50)
            );"""
        
        self.cursor.execute(sql)
        self._connection.commit()
        self._disconnect_db()
        
    def add_celular(self, nome, marca, preco,i, site):
    
        self._connect_db()
        if i == 1 and site == 'https://www.extra.com.br/c/telefones-e-celulares/samsung?filtro=c38_m459&icid=155416':
            self.tables()
        self.cursor = self._connection.cursor()
        sql = """INSERT INTO celulares(nome, marca, preco) values(%s, %s, %s);"""
        val = (nome, marca, preco,)
        self.cursor.execute(sql, val)
        self._connection.commit()
        self._disconnect_db()


if __name__ == "__main__":
    w = Web()

