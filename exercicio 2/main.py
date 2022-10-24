from utils.consumer import getCurrenceValueOfMoney
from data.connection import Database

db = Database()
err,con=db.connect()

reg = db.getLastQuotation(con)
real = float(input("digite um valor em reais:"))
if reg!=None:
    print(f"valor em euro : {real/float(reg[1])}")
    print(f"valor em dolar : {real/float(reg[2])}")
else:
    print("Getting quotation...")
    err,quotation=getCurrenceValueOfMoney(["USD","EUR"])
    db.insertQuotation(con,quotation[0],quotation[1])
    print(f"valor em euro : {real/float(quotation[1])}")
    print(f"valor em dolar : {real/float(quotation[0])}")
    
con.close() 
