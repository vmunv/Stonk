import yfinance as yf
from polygon import RESTClient
import pandas as pd

api_key = 'YwkLX7WPkOSqUS4CTt_kRJp0pCJBz8gG'

client = RESTClient(api_key)
print(client)

#Create list of stocks
with open('stockList.txt') as f:
  stockList = f.readlines()
  stockList = [stock.rstrip() for stock in stockList]
print("stockList: ", stockList)

indicators = {stock: [] for stock in stockList}

#####################
# Using polygon api #
#####################


def getStockDF(ticker):
  minuteData = client.get_aggs(ticker,
                                           multiplier=1,
                                           timespan='minute',
                                           from_='2022-09-01',
                                           to='2022-09-02')
  #print(resp)
  #return 1
  df = pd.DataFrame(minuteData)
  df['Date'] = df['timestamp'].apply(lambda x: pd.to_datetime(x*1000000))
  df = df.set_index('Date')
  #df['date'] = pd.to_datetime(df['t'], unit='ms')
  return df


################
# Using YF api #
################


def getStockPrice(ticker):
  stock = yf.Ticker(ticker)
  latest_price = stock.history(period='1d')['Close'][0]
  return round(latest_price, 2)


def downloadData(stock):
  data = yf.download(
    tickers=stock,

    # use "period" instead of start/end
    period="ytd",

    # fetch data by interval (including intraday if period < 60 days)
    # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    # (optional, default is '1d')
    interval="1m",

    # group by ticker (to access via data['SPY'])
    # (optional, default is 'column')
    group_by='ticker',

    # adjust all OHLC automatically
    # (optional, default is False)
    auto_adjust=True,

    # download pre/post regular market hours data
    # (optional, default is False)
    prepost=True,

    # use threads for mass downloading? (True/False/Integer)
    # (optional, default is True)
    threads=True,

    # proxy URL scheme use use when downloading?
    # (optional, default is None)
    proxy=None)

  return data


#print(downloadData("AAPL"))
"""
Our strategy to valuate a stock + how much we should buy:

1. Value the stock with a formula
2. Forecast future price movements to create buy/sell orders-
  - Let c be an integer that describes how confident we in future price (low means high confidence in downtrend, vice versa)
  - Higher risk -> scaling c down
  - Market + beta influences c
3. Execute trades


types of variables:
  per stock:
  - 
  
"""
'''
def getStockHistory(name):
  stock = yf.Ticker(name)
  hist = stock.history(period="2y")
  return hist
'''
