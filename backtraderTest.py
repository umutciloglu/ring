from turtle import position
import backtrader as bt

class TestStrategy(bt.Strategy):
    def __init__(self):
        self.RSI = bt.talib.RSI(self.data, period=14)
        self.bbands = bt.indicators.BBands()
        self.dataclose = self.datas[0].close
        self.datahigh = self.datas[0].high
        self.posSize = 0.1
        self.direction = True

    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def next(self):
        if self.dataclose >= self.bbands.lines.bot and not self.direction:
            self.direction = True
        # if self.RSI < 30 and not self.position:
        #     self.buy(size=1)
        # if self.RSI > 70 and self.position:
        #     self.close()
        if self.dataclose <= self.bbands.lines.mid and not self.position and self.direction:
            self.buy(size=self.posSize)
            # print(self.position.size)
        if self.datahigh >= self.bbands.lines.top and self.position:
            # self.log('Top Band: %.2f Close: %.2f High: %.2f' % (self.bbands.lines.top[0] - self.bbands.lines.top[0] * 0.05, self.dataclose[0],self.datahigh[0]))
            self.close(size=self.posSize)
        if self.dataclose <= self.bbands.lines.bot:
            self.close(size = self.posSize)
            self.direction = False

def run():
    cerebro = bt.Cerebro()

    data = bt.feeds.GenericCSVData(dataname='1mar2019-1apr2019-15min.csv', dtformat=2, compression=15, timeframe=bt.TimeFrame.Minutes)

    cerebro.adddata(data)
    # cerebro.addsizer(bt.sizers.FixedSize, stake=1)

    cerebro.addstrategy(TestStrategy)
    cerebro.run()

    cerebro.plot(style='candlestick', barup='green', bardown='red')
