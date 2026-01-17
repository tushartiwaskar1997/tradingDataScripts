from growwapi import GrowwAPI
import pyotp
import pandas as pd
from datetime import datetime

 
api_key = "enter api key"
secret = "enter secret key"
 
access_token = GrowwAPI.get_access_token(api_key=api_key, secret=secret)
# Use access_token to initiate GrowwAPI
groww = GrowwAPI(access_token)



historical_candles_response = groww.get_historical_candles(
    exchange=groww.EXCHANGE_NSE,
    segment=groww.SEGMENT_CASH,
    groww_symbol="NSE-WIPRO",
    start_time="2025-12-01 10:56:00",
    end_time="2025-12-24 12:00:00",
    candle_interval=groww.CANDLE_INTERVAL_MIN_30
)
print(historical_candles_response)
 