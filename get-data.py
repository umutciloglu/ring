from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import config, csv, datetime

client = Client(config.API_KEY, config.API_SECRET)

candles = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_15MINUTE, "1 jan 2019","1 feb 2019")

# for candle in candles:
#     timestamp = datetime.datetime.fromtimestamp(candle[0]/1000)
#     print(timestamp.strptime())

file = open('15-min-for-2-months.csv','w',newline='')

candlestickWriter = csv.writer(file, delimiter=',')
# candlestickWriter.writerow(['time','open','high','low','close','volume','close-time','quote-asset-volume'
#                             ,'number-of-trades','taker-buy-base-asset-volume','taker-buy-quote-asset-volume','ignore'])

for candle in candles:
    candle[0] = candle[0] / 1000
    candlestickWriter.writerow(candle)