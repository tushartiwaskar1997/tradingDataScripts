from growwapi import GrowwAPI
import pyotp
import pandas as pd
from datetime import datetime

 
api_key = "eyJraWQiOiJaTUtjVXciLCJhbGciOiJFUzI1NiJ9.eyJleHAiOjI1NTcwNDEwMDEsImlhdCI6MTc2ODY0MTAwMSwibmJmIjoxNzY4NjQxMDAxLCJzdWIiOiJ7XCJ0b2tlblJlZklkXCI6XCI0NzdhYjBjMS00YmQwLTRmOGYtYjUwOC1iMzIxNmJkNGUwNjRcIixcInZlbmRvckludGVncmF0aW9uS2V5XCI6XCJlMzFmZjIzYjA4NmI0MDZjODg3NGIyZjZkODQ5NTMxM1wiLFwidXNlckFjY291bnRJZFwiOlwiNGM2ZWNmZGEtNDVlOC00MTlmLWJhNDctYjIxNzk3MzY3MGZiXCIsXCJkZXZpY2VJZFwiOlwiZjFkM2UyMzktMzU1Yi01NjQ5LWJkZDAtYjA1OTdkZGNhYmVmXCIsXCJzZXNzaW9uSWRcIjpcIjRiMmNlNjY4LTc4NWMtNGYyOC04NTY0LWY0YzFhNjljYWNhY1wiLFwiYWRkaXRpb25hbERhdGFcIjpcIno1NC9NZzltdjE2WXdmb0gvS0EwYkNhRlFWWTdENDd3dWxOc3NscElTbmhSTkczdTlLa2pWZDNoWjU1ZStNZERhWXBOVi9UOUxIRmtQejFFQisybTdRPT1cIixcInJvbGVcIjpcImF1dGgtdG90cFwiLFwic291cmNlSXBBZGRyZXNzXCI6XCI0OS4yMDQuMTY0Ljg5LDE3Mi43MS4xOTguNjYsMzUuMjQxLjIzLjEyM1wiLFwidHdvRmFFeHBpcnlUc1wiOjI1NTcwNDEwMDE2OTd9IiwiaXNzIjoiYXBleC1hdXRoLXByb2QtYXBwIn0.SkjwtEj67e5e7oYJEMoIWi9XWUEqDR9nmoe9DnQgMfpzRj-86cSU3CDPVmbO3KWEciS1vdmAQLFYKRt-ha1hnQ"
secret = "y6ldThW@ZX7qUPa-a_I8Old*vFm*WgqC"
 
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