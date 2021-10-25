from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import config, csv

client = Client(config.API_KEY, config.API_SECRET)

candles = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_5MINUTE, "1 month ago UTC")

file = open('5min.csv','w',newline='')

candlestickWriter = csv.writer(file, delimiter=',')


for candle in candles:
    candlestickWriter.writerow(candle)