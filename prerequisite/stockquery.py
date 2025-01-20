import pandas as pd
import yfinance as yf

# Fetch historical data for a stock
ticker = "AAPL"
data = yf.download(ticker, start="2021-01-01", end="2025-01-01")

# Calculate moving averages
data['SMA50'] = data['Close'].rolling(window=50).mean()
data['SMA200'] = data['Close'].rolling(window=200).mean()

# Generate signals
data['Signal'] = 0
# Use .loc[] to assign values based on the condition
data.loc[data['SMA50'] > data['SMA200'], 'Signal'] = 1  # Buy Signal
data.loc[data['SMA50'] < data['SMA200'], 'Signal'] = -1  # Sell Signal

# print(data[['Close', 'SMA50', 'SMA200', 'Signal']].tail())




