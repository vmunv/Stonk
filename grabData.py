import yfinance as yf

#Create list of stocks
with open('stockList.txt') as f:
  stockList = f.readlines()
  stockList = [stock.rstrip() for stock in stockList]
print(stockList)

indicators = {stock:[] for stock in stockList}

def getStockHistory(name):
  stock = yf.Ticker(name)
  hist = stock.history(period="2y")
  return hist




