import math
#t is years
def expectedDividend(stock, t):
  dividend = stock['dividend']
  shares = stock['numShares']
  divRate = stock['divRate']
  
  perShareDividend = dividend/shares
  return perShareDividend * (1 + divRate)**t

def retentionRatio(stock):
  netIncome = stock['netIncome']
  dividend = stock['dividend']

  return (netIncome - dividend)/netIncome

def ROE(stock):
  netIncome = stock['netIncome']
  startEquity = stock['startEquity']
  endEquity = stock['endEquity']
  meanEquity = (startEquity + endEquity)/2
  print("ROE: ", netIncome/meanEquity)
  return netIncome/meanEquity
  

def requiredReturnOnCommonStock(stock):
  d0 = stock['dividend']/stock['numShares']
  
  p0 = stock['price']
  g = retentionRatio(stock) * ROE(stock)
  
  return ((d0 * (1+g))/p0) + g

