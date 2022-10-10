import yfinance as yf

with open('stockList.txt') as f:
    stockList = f.readlines()
    stockList = [stock.rstrip() for stock in stockList]
print(stockList)



def getStock(name):
  stock = yf.Ticker(name)

  return stock

