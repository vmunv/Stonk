#sift through historical data to validate whether the DDM is a valid model
from sklearn.metrics import r2_score

r2_threshold = 0.8
#function to generate points on the exponential curve between two different times
def getExpHist(hist):
  if len(hist) == 0:
    raise Exception("NO DIVIDEND HISTORY")
  
  y1 = hist[0]
  x1 = 0
  y2 = hist[-1]
  x2 = len(hist)-1

  a = y1
  b = (y2/y1)**(1/x2)
  
  return [a*b**i for i in range(len(hist))]

#counts number of descending entries from step i to step i+1 in a list
def decrementCount(list):
  acc = 0
  for i in range(len(list) - 1):
    if list[i] > list[i+1]:
      acc += 1
  return acc


#rough draft
def ddmRater(stock):
  # 0 is neutral, -1 worst, 1 best
  rating = 0
  #hist will be a list of past dividends values
  hist = stock['hist']
  #theoretical dividend hist -- in future find exp fit curve instead of first+last pts
  expHist = getExpHist(stock['hist'])
  r2 = r2_score(hist, expHist)

  #print("r2: ", r2)
  decCount =  decrementCount(stock['hist'])
  #if more than 30% of entries are decrementing, then this is worst model
  if decCount > .3*len(stock['hist']):
    return -1

  #if steadily increasing and real data close to exp growth, this is best model
  if decCount == 0 and r2 >= 0.93:
    return 1

  #decide how to penalize low r2 better
  if r2 < r2_threshold:
    rating -= 0.5
  
  return rating

    
  





# y1 = ab^0 = a

# y2 = ab^x2 --> b^x2 = y2/y1 --> b = (y2/y1)^(1/x2)

