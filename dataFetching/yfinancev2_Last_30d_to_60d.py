import yfinance as yf
import pandas as pd

# Download Reliance intraday data
df = yf.download(
    "RELIANCE.NS",
    period="90d",
    interval="5m",
    progress=False
)

# Fix MultiIndex columns
if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)

# Reset index
df.reset_index(inplace=True)

# ✅ FIX: Handle Date / Datetime column correctly
datetime_col = "Date" if "Date" in df.columns else "Datetime"

# Remove timezone info (Excel requirement)
df[datetime_col] = df[datetime_col].dt.tz_localize(None)

# Save to Excel
file_name = "RELIANCE_5_newwwwwwwmin_Historical_Data.xlsx"
df.to_excel(file_name, index=False)

print("✅ Excel file created successfully:", file_name)
