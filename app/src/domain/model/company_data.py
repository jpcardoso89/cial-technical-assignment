from datetime import date
from typing import List

from src.domain.model.competitor import Competitor
from src.domain.model.performance_data import PerformanceData
from src.domain.model.stock_values import StockValues


class CompanyData:
    def __init__(self, status: str, purchased_amount: int, purchased_status: str, 
                 request_data: date, company_code: str, company_name: str, 
                 stock_values: StockValues, performance_data: PerformanceData, 
                 competitors: List[Competitor]):
        self.status = status
        self.purchased_amount = purchased_amount
        self.purchased_status = purchased_status
        self.request_data = request_data
        self.company_code = company_code
        self.company_name = company_name
        self.stock_values = stock_values
        self.performance_data = performance_data
        self.competitors = competitors