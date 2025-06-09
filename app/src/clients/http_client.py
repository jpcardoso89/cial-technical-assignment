from datetime import date, datetime, timedelta
import requests
from src.clients.interfaces.i_http import IHttp
from src.models.api_response import ApiResponse


class HttpClient(IHttp):

    def __init__(self, base_url:str, client):
        self.__base_url = base_url
        self.__client = client
    
    def post(self, body, url:str, headers:dict|None, query_params: dict|None) -> ApiResponse | None:
        pass
    
    def get(self, url:str, headers:dict|None, query_params: dict|None) -> ApiResponse:
        url = f"{self.__base_url}{url}"
        response = self.__client.get(url, headers=headers, params=query_params)
        return ApiResponse(response.status_code, response.json())
    