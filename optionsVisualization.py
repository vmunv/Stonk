class Option:
  def __init__(self, type, strike,premium):
    self.strike = strike
    self.type = type
    self.premium = premium
  
  #x is price
  def profitCurve(self, x):
    if self.type == "call":
      if (x - self.strike - self.premium) > -1*self.premium:
        return x - self.strike - self.premium
      else:
        return -1*self.premium
    elif self.type == "put":
      if self.strike - x - self.premium > -1*self.premium:
        return self.strike - x - self.premium
      else:
        return -1*self.premium

def strangleVisualization(call, put):
  totalPremium = call.premium+put.premium
  print("\n")
  print("callStrike: ", call.strike, " putStrike: ", put.strike)
  print("callPremium: ", call.premium, " putPremium: ", put.premium)
  print("Profit range: [0,", put.strike-totalPremium, "), (", call.strike+totalPremium ,", infty)")
  for e in [49,50,51,52,53,54,55,56,57,58,59,60,61]:
    print("Profit for price ", e, ": ", call.profitCurve(e) + put.profitCurve(e))


#x is the premium price


