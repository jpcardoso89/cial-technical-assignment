class ApiResponse:

    def __init__(self, status_code:int, body:dict|None):
        self.__status_code = status_code
        self.__body = body