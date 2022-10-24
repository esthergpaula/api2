import requests

class Api:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def get_info_weather(self,woeid):
        req = requests.get("https://api.hgbrasil.com/weather?key=656f571e&woeid="+str(woeid))
        try:
            if req.status_code==200:
                return False,req.text
            else:
               return True,str(req.status_code)+"; Erro no servidor."
        except Exception as e:
            return True,e
             