from abc import abstractmethod

from app.src.models.api_response import ApiResponse


class IHttp:

    @abstractmethod
    def post(self, body, url:str, headers:dict|None, query_params:dict|None) -> ApiResponse:
        pass
    
    @abstractmethod
    def get(self, url:str, headers:dict|None, query_params:dict|None) -> ApiResponse:
        pass
