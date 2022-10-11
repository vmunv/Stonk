import yfinance as yf

#Create list of stocks
with open('stockList.txt') as f:
  stockList = f.readlines()
  stockList = [stock.rstrip() for stock in stockList]
print(stockList)

indicators = {stock:[] for stock in stockList}


def downloadData(stock):
  data = yf.download(  

        tickers = stock,

        # use "period" instead of start/end
        period = "ytd",

        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval = "1m",

        # group by ticker (to access via data['SPY'])
        # (optional, default is 'column')
        group_by = 'ticker',

        # adjust all OHLC automatically
        # (optional, default is False)
        auto_adjust = True,

        # download pre/post regular market hours data
        # (optional, default is False)
        prepost = True,

        # use threads for mass downloading? (True/False/Integer)
        # (optional, default is True)
        threads = True,

        # proxy URL scheme use use when downloading?
        # (optional, default is None)
        proxy = None
    )

  return data

print(downloadData("AAPL"))

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



