import sqlite3
import uuid
from datetime import datetime



class Database:
    def connect(self):
        try:
           con = sqlite3.connect("data/cotacoes.db")
           return False,con
        except Exception as e:
            return True,e
     
    def getLastQuotation(self,con):       
        cur = con.cursor()
        res = cur.execute("SELECT * FROM cotacoes where data='"+str(datetime.today().strftime('%Y-%m-%d'))+"'")
        data = res.fetchone()
        return data

    def insertQuotation(self,con,quotation_usd,quotation_eur):
        cur = con.cursor()
        data = (str(uuid.uuid4()),quotation_eur,quotation_usd,str(datetime.today().strftime('%Y-%m-%d')))
        cur.execute("INSERT INTO cotacoes(id,cotacao_euro,cotacao_dolar,data) VALUES(?,?,?,?)", data)
        con.commit()
           




