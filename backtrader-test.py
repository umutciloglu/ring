import backtrader as bt

class TestStrategy(bt.Strategy):
    def __init__(self):
        self.RSI = bt.talib.RSI(self.data, period=14)
        self.bband = bt.indicators.BBands()
        self.dataclose = self.datas[0].close

    def next(self):
        if self.RSI < 30 and not self.position:
            self.buy(size=1)
        if self.RSI > 70 and self.position:
            self.close()
        # if self.dataclose <= self.bband.lines.mid and not self.position:
        #     self.buy(size=0.1)
        # if self.dataclose >= self.bband.lines.top - self.bband.lines.top*0.05 and self.position:
        #     self.close()

cerebro = bt.Cerebro()

data = bt.feeds.GenericCSVData(dataname='1mar2019-1apr2019-15min.csv', dtformat=2)

cerebro.adddata(data)

cerebro.addstrategy(TestStrategy)
cerebro.run()

cerebro.plot()
