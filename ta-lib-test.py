# import imp
import talib,numpy
from numpy import genfromtxt

data = genfromtxt("/home/umut/Documents/binance/5min.csv", delimiter=",")

# print(data[0])

close = data[:,4]

rsi = talib.RSI(close)

bbands = talib.BBANDS(close, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)

i = 4

print('upper        middle       lower')

while i <= 50:
    print("%12f %12f %12f"%(bbands[0][i], bbands[1][i], bbands[2][i]))
    i = i + 1

# print(close)