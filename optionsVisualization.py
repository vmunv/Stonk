import matplotlib.pyplot as plt


#call/put are option objects
#start/end are integers
def strangleVisualization(call, put, start, end):
  if call.ticker != put.ticker:
    raise Exception("Ticker for call and put are different")
  totalPremium = call.premium + put.premium
  print("\n")
  print("callStrike: ", call.strike, " putStrike: ", put.strike)
  print("callPremium: ", call.premium, " putPremium: ", put.premium)
  print("Profit range: [0,", put.strike - totalPremium, "), (",
        call.strike + totalPremium, ", infty)")
  stockPrices = []
  profits = []
  i = start
  while i <= end:
    stockPrices.append(i)
    profits.append(call.profitCurve(i) + put.profitCurve(i))
    i += 0.5
    #print("Profit for price ", i, ": ", call.profitCurve(i) + put.profitCurve(i))
  plt.title("Strangle on " + call.ticker + "\nCall: (" + str(call.strike) +
            "," + str(call.premium) + ")\nPut: (" + str(put.strike) + "," +
            str(put.premium) + ")")
  plt.plot(stockPrices, profits)
  plt.xlabel("Stock price ($)")
  plt.ylabel("Profit ($)")
  plt.show()


#x is the premium price
