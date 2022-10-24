from typing import List
from typing import Any
from dataclasses import dataclass
import json


@dataclass
class Forecast:
    date: str
    weekday: str
    max: int
    min: int
    description: str
    condition: str

    @staticmethod
    def from_dict(obj: Any) -> 'Forecast':
        _date = str(obj.get("date"))
        _weekday = str(obj.get("weekday"))
        _max = int(obj.get("max"))
        _min = int(obj.get("min"))
        _description = str(obj.get("description"))
        _condition = str(obj.get("condition"))
        return Forecast(_date, _weekday, _max, _min, _description, _condition)

@dataclass
class Results:
    temp: int
    date: str
    time: str
    condition_code: str
    description: str
    currently: str
    cid: str
    city: str
    img_id: str
    humidity: int
    wind_speedy: str
    sunrise: str
    sunset: str
    condition_slug: str
    city_name: str
    forecast: List[Forecast]

    @staticmethod
    def from_dict(obj: Any) -> 'Results':
        _temp = int(obj.get("temp"))
        _date = str(obj.get("date"))
        _time = str(obj.get("time"))
        _condition_code = str(obj.get("condition_code"))
        _description = str(obj.get("description"))
        _currently = str(obj.get("currently"))
        _cid = str(obj.get("cid"))
        _city = str(obj.get("city"))
        _img_id = str(obj.get("img_id"))
        _humidity = int(obj.get("humidity"))
        _wind_speedy = str(obj.get("wind_speedy"))
        _sunrise = str(obj.get("sunrise"))
        _sunset = str(obj.get("sunset"))
        _condition_slug = str(obj.get("condition_slug"))
        _city_name = str(obj.get("city_name"))
        _forecast = [Forecast.from_dict(y) for y in obj.get("forecast")]
        return Results(_temp, _date, _time, _condition_code, _description, _currently, _cid, _city, _img_id, _humidity, _wind_speedy, _sunrise, _sunset, _condition_slug, _city_name, _forecast)
    
    def __get_media_min_temp(self) ->float:
        media = 0
        for i, val in enumerate(self.forecast):
            media+=val.min
        media = media/len(self.forecast)
        return media 

    def __get_media_max_temp(self) ->float:   
        media = 0
        for i, val in enumerate(self.forecast):
            media+=val.max
        media = media/len(self.forecast)
        return media 

    def get_information(self) -> str:
        res = "------------------DADOS---------------------\n"
        res += f"Temperatura : {self.temp} C°\n"
        res += f"Data : {self.date} - {self.time}\n"
        res += f"Descrição Tempo : {self.description}\n"
        res += f"Corrente : {self.currently}\n"
        res += f"Umidade : {self.humidity}%\n"
        res += f"Velocidade do vento : {self.wind_speedy}\n"
        res += f"Nascer do sol : {self.sunrise}\n"
        res += f"Pôr do sol : {self.sunset}\n"
        res += f"Condição de tempo atual : {self.condition_slug}\n"
        res += f"Médias das temperaturas máxima semanal : {self.__get_media_max_temp()} C°\n"
        res += f"Médias das temperaturas mínima semanal {self.__get_media_min_temp()} C°"
        return res

@dataclass
class Root:
    by: str
    valid_key: bool
    results: Results
    execution_time: float
    from_cache: bool

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _by = str(obj.get("by"))
        _valid_key = bool(obj.get("valid_key"))
        _results = Results.from_dict(obj.get("results"))
        _execution_time = float(obj.get("execution_time"))
        _from_cache = bool(obj.get("from_cache"))
        return Root(_by, _valid_key, _results, _execution_time, _from_cache)


