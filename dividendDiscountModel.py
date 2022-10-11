from calculations import *

n=1000
#stock is df
def ddmSumPrice(stock):
  #initialize stockValue
  stockValue = 0
  r = requiredReturnOnCommonStock(stock)
  
  # print("required return on common stock: ", r)
  for i in range(n):
    stockValue += expectedDividend(stock, i)/(1+r)**i
  return stockValue

def ddmBasicPrice(stock):
  perShareDividend = stock['dividend']/stock['numShares']
  r = requiredReturnOnCommonStock(stock)
  divRate = stock['divRate']

  return perShareDividend/(r-divRate)
    


