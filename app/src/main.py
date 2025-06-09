import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from dotenv import load_dotenv
from fastapi import FastAPI, Response, status
from src.controllers.factory import build_stock_controller


app = FastAPI()
load_dotenv()
stock_controller = build_stock_controller()

@app.get("/")
def read_root():
   return {"message":"hello, world!"}

@app.get("/stock/{stock_symbol}")
def stock(stock_symbol:str, response: Response):
   try:
      stock = stock_controller.get_stock_by(stock_symbol)
      response.status_code = status.HTTP_200_OK
      return stock
   except Exception as e:
      response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
      return {"message_error":e}
   