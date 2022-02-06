from turtle import position
import backtrader as bt

class TestStrategy(bt.Strategy):
    def __init__(self):
        self.RSI = bt.talib.RSI(self.data, period=14)
        self.bbands = bt.indicators.BBands()
        self.dataclose = self.datas[0].close
        self.datahigh = self.datas[0].high
        self.posSize = 0.1

    def next(self):
        # if self.RSI < 30 and not self.position:
        #     self.buy(size=1)
        # if self.RSI > 70 and self.position:
        #     self.close()
        if self.dataclose <= self.bbands.lines.mid[0] and not self.position.size > 0:
            self.buy(size=self.posSize)
            print(self.position.size)
        if self.datahigh >= self.bbands.lines.top[0] - self.bbands.lines.top[0] * 0.05 and self.position.size > 0:
            self.close(size=self.posSize)

cerebro = bt.Cerebro()

data = bt.feeds.GenericCSVData(dataname='1mar2019-1apr2019-15min.csv', dtformat=2)

cerebro.adddata(data)
# cerebro.addsizer(bt.sizers.FixedSize, stake=1)

cerebro.addstrategy(TestStrategy)
cerebro.run()

cerebro.plot(style='candlestick', barup='green', bardown='red')
