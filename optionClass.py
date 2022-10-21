import matplotlib.pyplot as plt
import math


class Option:

  def __init__(self, ticker, type, strike, premium):
    self.ticker = ticker
    self.strike = strike
    self.type = type
    self.premium = premium

  #x is price
  def profitCurve(self, x):
    if self.type == "call":
      if (x - self.strike - self.premium) > -1 * self.premium:
        return x - self.strike - self.premium
      else:
        return -1 * self.premium
    elif self.type == "put":
      if self.strike - x - self.premium > -1 * self.premium:
        return self.strike - x - self.premium
      else:
        return -1 * self.premium

  def printProfitCurve(self):
    start = math.floor(.88 * self.strike)
    end = math.floor(1.15 * self.strike)
    i = start
    stockPrices = []
    profits = []
    while i <= end:
      stockPrices.append(i)
      profits.append(self.profitCurve(i))
      i += 0.5
    plt.plot(stockPrices, profits)
    plt.title(self.ticker + " " + self.type + " option profit")
    plt.xlabel("Stock price")
    plt.ylabel("Profit")
    plt.show()
