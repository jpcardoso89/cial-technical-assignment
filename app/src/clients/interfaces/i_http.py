from abc import abstractmethod


class IHttp:

    @abstractmethod
    def post(self, body, headers:dict, query_params:dict):
        pass
    
    @abstractmethod
    def get(self, url:str, headers:dict, query_params:dict):
        pass
