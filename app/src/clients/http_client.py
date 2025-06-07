from app.src.clients.interfaces.i_http import IHttp


class HttpClient(IHttp):

    def __init__(self, base_url:str):
        self.__base_url = base_url
    
    def post(self, body, headers:dict, query_params:dict):
        pass
    
    def get(self, url:str, headers:dict, query_params:dict):
        pass