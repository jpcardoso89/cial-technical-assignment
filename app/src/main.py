import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from fastapi import FastAPI
from src.controllers.factory import build_stock_controller
from src.clients.http_client import HttpClient
from src.clients.polygon_client import PolygonClient

app = FastAPI()

stock_controller = build_stock_controller()

@app.get("/")
def read_root():
   return {"message":"hello, world!"}

@app.get("/stock/{stock_symbol}")
def stock(stock_symbol:str):
   try:
      stock = stock_controller.get_stock_by(stock_symbol)
      return stock
   except Exception as e:
      return {"status":"500"}
   