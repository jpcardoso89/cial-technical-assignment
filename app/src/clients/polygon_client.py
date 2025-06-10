from datetime import date, datetime, timedelta

from src.clients.interfaces.i_http import IHttp
from src.models.daily_tricker_summary import DailyTickerSummary


class PolygonClient:

    def __init__(self, http: IHttp, api_key:str|None) -> None:
        self.__http = http
        self.__api_key = api_key
        self.__auth_headers = {}
        self.__yesterday: date = date.today() - timedelta(days=1)
    
    def get_daily_ticker_summary(self, symbol:str)-> DailyTickerSummary:
        headers = self.__build_auth_headers()
        self.__weekend_day()
        response = self.__http.get(f"/v1/open-close/{symbol.upper()}/{self.__yesterday.isoformat()}?adjusted=true", headers, None)
        if response.status_code == 200:
            return DailyTickerSummary(**response.body)
        
        raise Exception(f"request erro to symbol =>{symbol}")

    
    def __build_auth_headers(self) -> dict:
        self.__auth_headers = {"Authorization": f"Bearer {self.__api_key}"}
        return self.__auth_headers
    
    def __weekend_day(self):
        while not self.__yesterday.weekday() < 5:
            self.__yesterday = self.__yesterday - timedelta(days=1)
        return self.__yesterday