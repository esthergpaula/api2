import requests,json



def getCurrenceValueOfMoney(types):
  try:
     res = requests.get("https://api.hgbrasil.com/finance?key=c89b5f1f")
     if res.status_code==200:
        obj = json.loads(res.text)
        result = []
        for i in range(len(types)):
            result.append(obj["results"]["currencies"][types[i]]["buy"])
            pass
        return False,result
     else: 
        return True,"Api fora do ar..."   
  except Exception as e:
     return True,e


