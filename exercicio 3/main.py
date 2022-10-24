from data.connection import Database
from services.api import Api
from model.weather_model import Root
import json

db = Database()
api_weather = Api()

nome_city = str(input("Digite o nome de uma cidade :"))
e,con = db.connect()

ret_places=db.get_places(con,nome_city.title())

if len(ret_places)==0:
  print("Não foi encontrado nenhuma cidade ou estado com esse nome!")
elif len(ret_places)>1:#listar registros
    print("Foi encontrado mais de um registro relacionado a esse nome!")
    for i in range(len(ret_places)):
      print(f"{i} -- {ret_places[i][2]}")
    idx = int(input("Selecione uma das opções acima e digite o número correspondente : "))
    erro,res=api_weather.get_info_weather(ret_places[idx][1])
    if not erro:
      # teste local json
      #f = open('data\data.json',encoding='utf-8')
      root = Root.from_dict(json.loads(res))
      print(root.results.get_information())#mostrar info
      db.insert_history(con,root.results.temp, root.results.humidity,root.results.wind_speedy)#salvar historico  
    else:
      print(f"Erro ao buscar informações da cidade/estado {ret_places[0][2]}. Erro : {erro}") 
else:
  print(ret_places[0][1])
  erro,res=api_weather.get_info_weather(ret_places[0][1])
  if not erro:
    # teste local json
    #f = open('data\data.json',encoding='utf-8')
    root = Root.from_dict(json.loads(res))
    print(root.results.get_information()) #mostrar info
    db.insert_history(con,root.results.temp, root.results.humidity,root.results.wind_speedy) #salvar historico
  else:
    print(f"Erro ao buscar informações da cidade/estado {ret_places[0][2]}. Erro : {erro}")

 