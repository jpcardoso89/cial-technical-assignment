from datetime import date
from typing import List

from src.domain.model.competitor import Competitor
from src.domain.model.performance_data import PerformanceData
from src.domain.model.stock_values import StockValues


class Stock:
    def __init__(self, status: str, purchased_amount: float|None, purchased_status: str|None, 
                 request_data: date, company_code: str|None, company_name: str|None, 
                 stock_values: StockValues|None, performance_data: PerformanceData|None, 
                 competitors: List[Competitor]|None):
        self.status = status
        self.purchased_amount = purchased_amount
        self.purchased_status = purchased_status
        self.request_data = request_data
        self.company_code = company_code
        self.company_name = company_name
        self.stock_values = stock_values
        self.performance_data = performance_data
        self.competitors = competitors
    
    def to_dict(self)-> dict:
        return {
            "status":self.status,
            "purchased_amount":self.purchased_amount,
            "purchased_status":self.purchased_status,
            "request_data":self.request_data.isoformat(),
            "company_code":self.company_code,
            "company_name":self.company_name,
            "stock_values":self.stock_values.__dict__,
            "performance_data":self.performance_data,
            "competitors":self.competitors,
        }
