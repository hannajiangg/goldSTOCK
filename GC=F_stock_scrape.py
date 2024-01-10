import yfinance as yf
import pandas as pd

# Replace 'GC=F' with the desired stock symbol
symbol = 'GC=F'

# Download monthly historical data
stock_data = yf.download(symbol, start='2003-01-01', end='2023-12-31', interval='1mo')

# Save the data to a CSV file
stock_data.to_csv(f'{symbol}_monthly_historical_data.csv')
