import talib,numpy
from numpy import genfromtxt

data = genfromtxt("../5min.csv", delimiter=",")

# print(data[0])

close = data[:,4]

rsi = talib.RSI(close)

print(rsi[:250])

# print(close)