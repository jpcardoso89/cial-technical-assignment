import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

import requests

from fastapi import FastAPI
from src.clients.http_client import HttpClient
from src.clients.polygon_client import PolygonClient

app = FastAPI()


@app.get("/")
def read_root():
   return {"message":"hello, world!"}