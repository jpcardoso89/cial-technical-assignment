from src.domain.use_cases.stock_information import GetStockInformationBySymbol


class StockController:

    def __init__(self, get_stock:GetStockInformationBySymbol) -> None:
        self._get_stock = get_stock

    def get_stock_by(self, symbol:str):
        if symbol:
            stock = self._get_stock.execute(symbol)
            return stock.__dict__
        raise Exception("Invalid symbol")
