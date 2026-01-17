from growwapi import GrowwAPI
import pyotp
import pandas as pd
from datetime import datetime

  
api_key = "enter api key"
secret = "enter secret key"
 
access_token = GrowwAPI.get_access_token(api_key=api_key, secret=secret)
# Use access_token to initiate GrowwAPI
groww = GrowwAPI(access_token)

#end_time_in_millis = int(time.time() * 1000) # epoch time in milliseconds
#start_time_in_millis = end_time_in_millis - (24 * 60 * 60 * 1000) # last 24 hours
 
# OR
 
# you can give start time and end time in yyyy-MM-dd HH:mm:ss format.
#start_time = "2025-01-16 09:15:00"
#end_time = "2026-01-16 15:30:00"
historical_data_response = groww.get_historical_candle_data(
    trading_symbol="RELIANCE",
    exchange=groww.EXCHANGE_NSE,
    segment=groww.SEGMENT_CASH,
    start_time="2025-11-16 09:15:00",
    end_time="2025-11-20 15:30:00",
    interval_in_minutes=5 # Optional: Interval in minutes for the candle data
)
# 
# ✅ Handle different response formats safely
if isinstance(historical_data_response, dict):
    candles = historical_data_response.get("candles") \
              or historical_data_response.get("data") \
              or historical_data_response.get("payload")
else:
    candles = historical_data_response

if not candles:
    raise ValueError("No candle data received from Groww API")

# Create DataFrame
df = pd.DataFrame(
    candles,
    columns=["timestamp", "open", "high", "low", "close", "volume"]
)

# Convert timestamp to datetime
df["datetime"] = pd.to_datetime(df["timestamp"], unit="s")

# Reorder columns
df = df[["datetime", "open", "high", "low", "close", "volume"]]

# Save to Excel
file_name = "RELIANCE_Historical_Data.xlsx"
df.to_excel(file_name, index=False)

print(f"✅ Excel file created successfully: {file_name}")