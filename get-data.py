from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import config, csv, datetime

client = Client(config.API_KEY, config.API_SECRET)

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
date1 = "1"
date2 = "1"
year = 2019
i = 0

while i < 11:
    date1 = "1" + months[i] + "2019"
    date2 = "1" + months[i+1] + "2019"
    candles = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_15MINUTE,date1, date2)
    file = open(date1+"-"+date2+"-15min.csv",'w',newline='')
    candlestickWriter = csv.writer(file, delimiter=',')
    for candle in candles:
        candle[0] = candle[0] / 1000
        candlestickWriter.writerow(candle)
    file.close()
    i = i+1

# candles = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_15MINUTE, "1 jan 2019","1 feb 2019")

# # for candle in candles:
# #     timestamp = datetime.datetime.fromtimestamp(candle[0]/1000)
# #     print(timestamp.strptime())

# file = open('15-min-for-2-months.csv','w',newline='')

# candlestickWriter = csv.writer(file, delimiter=',')
# # candlestickWriter.writerow(['time','open','high','low','close','volume','close-time','quote-asset-volume'
# #                             ,'number-of-trades','taker-buy-base-asset-volume','taker-buy-quote-asset-volume','ignore'])

# for candle in candles:
#     candle[0] = candle[0] / 1000
#     candlestickWriter.writerow(candle)