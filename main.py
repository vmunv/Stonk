from grabData import *
from dividendDiscountModel import *
from dividendDiscountModelRater import *

JPM = {'dividend' : 4*3.027*10**9, 'netIncome' : 46.503*10**9, 'numShares': 3.027*10**9, 'divRate' : .111, 'startEquity' : 279.354*10**9, 'endEquity' : 294.127*10**9, 'price' : 158.35, 'hist' : [0.9,0.9,0.9,0.9,0.9,0.9,0.9,1,1,1,1,1]}

KO = {'dividend' : 7.252*10**9, 'netIncome' : 9.771*10**9, 'numShares': 4.34*10**9, 'divRate' : .04, 'startEquity' : 21.284*10**9, 'endEquity' : 24.86*10**9, 'price' : 57.9069, 'hist' : [0.41, 0.41, 0.41, 0.41, 0.42, 0.42, 0.42, 0.42, 0.44, 0.44,0.44]}

print("ddm sum price model of KO: ", ddmSumPrice(KO))

print("ddm basic price model of KO: ", ddmBasicPrice(KO))

print("ddm sum price model of JPM: ", ddmSumPrice(JPM))

print("ddm basic price model of JPM: ", ddmBasicPrice(JPM))

#print("getExpHist: ", getExpHist([0.9, 0.9, 0.9, 1.0, 1.1, 1.2, 1.2, 1.2]))

print("KO rating from ddmRater: ", ddmRater(KO))

print("JPM rating from ddmRater: ", ddmRater(JPM))
