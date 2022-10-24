import sqlite3
import uuid
from datetime import datetime



class Database:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def connect(self):
        try:
           con = sqlite3.connect("data/weather.db")
           return False,con
        except Exception as e:
            return True,e
     
    def get_places(self,con,place):       
        cur = con.cursor()
        res = cur.execute("SELECT * from places where name like '"+str(place)+"%'")
        data = res.fetchall()
        return data
    
    def insert_history(self,con,temp,humidity,wind_speedy):
        cur = con.cursor()
        data = (str(uuid.uuid4()),str(datetime.today().strftime('%Y-%m-%d %H:%M:%S')),float(temp),float(humidity),str(wind_speedy))
        cur.execute("INSERT INTO history_user(id,date,temp,humidity,wind_speed) VALUES(?,?,?,?,?)", data)
        con.commit()
    
    def insert_place(self,con,woeid,name):
        cur = con.cursor()
        data = (str(uuid.uuid4()),int(woeid),str(name))
        cur.execute("INSERT INTO places(id,woeid,name) VALUES(?,?,?)", data)
        con.commit()
           
           




