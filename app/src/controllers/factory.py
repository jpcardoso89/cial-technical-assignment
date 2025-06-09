import requests
from src.controllers.stock import StockController
from src.domain.use_cases.stock_information import GetStockInformationBySymbol
from src.clients.polygon_client import PolygonClient
from src.clients.http_client import HttpClient


def build_stock_controller():
    http = HttpClient(base_url="https://api.polygon.io", client=requests)
    polygon_cli = PolygonClient(http=http, api_key="xpto")
    use_case = GetStockInformationBySymbol(polygon_cli)
    controller = StockController(use_case)
    return controller
