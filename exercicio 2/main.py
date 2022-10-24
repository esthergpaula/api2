from utils.consumer import getCurrenceValueOfMoney
from data.connection import Database

db = Database()
err,con=db.connect()

reg = db.getLastQuotation(con)
real = float(input("digite um valor em reais:"))
if reg!=None:
    print(f"VALOR EM EURO : {real/float(reg[1])}")
    print(f"VALOR EM DÓLAR : {real/float(reg[2])}")
else:
    print("Getting quotation...")
    err,quotation=getCurrenceValueOfMoney(["USD","EUR"])
    db.insertQuotation(con,quotation[0],quotation[1])
    print(f"VALOR EM EURO : {real/float(quotation[1])}")
    print(f"VALOR EM DÓLAR : {real/float(quotation[0])}")
    
con.close() 