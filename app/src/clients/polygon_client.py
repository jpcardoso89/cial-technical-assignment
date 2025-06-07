from datetime import date
from app.src.clients.interfaces.i_http import IHttp
from app.src.models.daily_tricker_summary import DailyTickerSummary


class PolygonClient:

    def __init__(self, http: IHttp, api_key:str) -> None:
        self.__http = http
        self.__api_key = api_key
    
    def get_daily_ticker_summary(self, _date:date, symbol:str)-> DailyTickerSummary:
        pass