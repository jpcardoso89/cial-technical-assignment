import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from fastapi import FastAPI, Response, status
from src.controllers.factory import build_stock_controller
from src.clients.http_client import HttpClient
from src.clients.polygon_client import PolygonClient

app = FastAPI()

stock_controller = build_stock_controller()

@app.get("/")
def read_root():
   return {"message":"hello, world!"}

@app.get("/stock/{stock_symbol}")
def stock(stock_symbol:str, response: Response):
   try:
      stock = stock_controller.get_stock_by(stock_symbol)
      response.status_code = 200
      return stock
   except Exception as e:
      response.status_code = 500
      return {"message_error":e}
   