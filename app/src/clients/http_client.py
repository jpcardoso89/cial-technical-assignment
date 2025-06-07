from app.src.clients.interfaces.i_http import IHttp


class HttpClient(IHttp):

    def __init__(self, base_url:str, client):
        self.__base_url = base_url
        self.__client = client
    
    def post(self, body, url:str, headers:dict|None, query_params: dict|None):
        url = f"{self.__base_url}"
    
    def get(self, url:str, headers:dict|None, query_params: dict|None):
        pass