from data.connection import Database

db = Database()
e,con = db.connect()

with open("places.txt") as file:
    for line in file:
        dados=str(line).split(';')
        if dados[4]=='State' or dados[4]=='Town':
            #print(dados[0] , dados[2])
            db.insert_place(con, dados[0], dados[2])
           
        
con.close()
del db