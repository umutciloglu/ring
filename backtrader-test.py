import backtrader as bt

cerebro = bt.Cerebro()

data = bt.feeds.GenericCSVData(dataname='15-min-for-2-months.csv', dtformat=2)

cerebro.adddata(data)

cerebro.run()

cerebro.plot()