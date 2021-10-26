from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import config, csv, datetime

client = Client(config.API_KEY, config.API_SECRET)

candles = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_1DAY, "1 year ago UTC")

# for candle in candles:
#     timestamp = datetime.datetime.fromtimestamp(candle[0]/1000)
#     print(timestamp.strptime())

file = open('1day.csv','w',newline='')

candlestickWriter = csv.writer(file, delimiter=',')
candlestickWriter.writerow(['time','open','high','low','close','volume','close-time','quote-asset-volume'
                            ,'number-of-trades','taker-buy-base-asset-volume','taker-buy-quote-asset-volume','ignore'])

for candle in candles:
    candlestickWriter.writerow(candle)