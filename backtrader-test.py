import backtrader as bt

class RSIStrategy(bt.Strategy):
    def __init__(self):
        self.RSI = bt.talib.RSI(self.data, period=14)

    def next(self):
        if self.RSI < 30 and not self.position:
            self.buy(size=0.1)
        if self.RSI > 70 and self.position:
            self.close()

cerebro = bt.Cerebro()

data = bt.feeds.GenericCSVData(dataname='15-min-for-2-months.csv', dtformat=2)

cerebro.adddata(data)

cerebro.addstrategy(RSIStrategy)
cerebro.run()

cerebro.plot()