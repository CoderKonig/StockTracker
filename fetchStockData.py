import yfinance as yf
import pandas as pd

#  list of top 10 stocks
stock_tickers = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", 
    "META", "NVDA", "SPY", "NFLX", "DIS"
]

# Dictionary to hold data for each stock
stock_data = {}

# Fetch data for each stock and store it
for ticker in stock_tickers:
    stock_data[ticker] = yf.download(ticker, start="2010-01-01", end="2023-12-31")['Close']
    print(f"Downloaded data for {ticker}")

# Combine data into a single DataFrame
all_stocks_data = pd.DataFrame(stock_data)
print(all_stocks_data.head())
