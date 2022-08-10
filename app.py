from crypt import methods
from pydoc import cli
from flask import Flask, redirect, render_template, request, flash, jsonify
from binance.client import Client
from binance.enums import *
import config, csv

#initialize flask app and binance client
app = Flask(__name__)
app.secret_key = b'ausdha7dtas7dasi'
client = Client(config.API_KEY, config.API_SECRET)

@app.route("/")
def index():
    balances = client.get_account()['balances']

    balances = [balance for balance in balances if balance['asset'] in ['BTC', 'ETH', 'USDT']]

    symbols = ['BTCUSDT', 'ETHUSDT']

    return render_template("index.html", balances = balances, symbols = symbols)

@app.route("/testBuy")
def test():
    orderResponse = client.create_test_order(
    symbol='BTCUSDT',
    side=SIDE_BUY,
    type=ORDER_TYPE_LIMIT,
    timeInForce=TIME_IN_FORCE_GTC,
    quantity=100,
    price='30000')

    return orderResponse

#route to buy a symbol with given amount and price from the form
@app.route('/buy', methods=['POST'])
def buyOrder():
    orderInfo = request.form
    try:
        client.order_limit_buy(
        symbol=orderInfo['symbols'],
        quantity=orderInfo['quantity'],
        price=orderInfo['price'])
    except Exception as e:
        flash(e.message, 'error')

    return redirect('/')

@app.route('/sell',methods=['POST'])
def sellOrder():
    orderInfo = request.form
    try:
        client.order_limit_sell(
            symbol=orderInfo['symbols'],
            quantity=orderInfo['quantity'],
            price=orderInfo['price'])
    except Exception as e:
        flash(e.message, 'Error')
        
    return redirect('/')

#route that fetches and stores initial historical data
@app.route('/historical-data')
def historicalData():
    candles = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_15MINUTE, "1 week ago UTC")

    processedCandles = []

    for candle in candles:
        candleStick = { 
            "time": candle[0]/1000, 
            "open": candle[1], 
            "high": candle[2], 
            "low": candle[3], 
            "close": candle[4] 
        }

        processedCandles.append(candleStick)

    
    return jsonify(processedCandles)