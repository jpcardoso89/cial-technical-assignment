from datetime import date
from src.clients.polygon_client import PolygonClient
from src.domain.model.stock_values import StockValues
from src.domain.model.stock import Stock


class GetStockInformationBySymbol:

    def __init__(self, polygon_cli:PolygonClient):
        self.__polygon_cli = polygon_cli
        
    def execute(self, symbol:str) -> Stock:
        if symbol:
            daily = self.__polygon_cli.get_daily_ticker_summary(symbol)
            stock_values = StockValues(
                daily._open,
                daily._high,
                daily._low,
                daily._close
            )
            company = Stock(
                status="200",
                purchased_amount=daily._volume,
                purchased_status=daily._status,
                request_data=date.today(),
                company_code= daily._symbol,
                company_name="",
                stock_values=stock_values,
                performance_data=None, 
                competitors=None
            )
            return company

        raise Exception("Invalid symbol")