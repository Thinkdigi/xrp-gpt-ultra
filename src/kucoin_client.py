import os
from kucoin_universal_sdk import KucoinSpotRestAPI, KucoinFuturesRestAPI

SPOT = os.getenv('SPOT_SYMBOL','XRP-USDT')
FUT  = os.getenv('FUT_SYMBOL','XRPUSDTM')

class KucoinClient:
    def __init__(self):
        self.spot = KucoinSpotRestAPI()
        self.fut  = KucoinFuturesRestAPI()
    def get_spot_price(self)->float:
        d = self.spot.get_ticker(SPOT)
        return float(d['price'])
    def get_fut_price(self)->float:
        d = self.fut.get_ticker(FUT)
        return float(d['price'])
