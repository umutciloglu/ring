from flask import Flask, render_template
from binance.client import Client
from binance.enums import *
import config, csv

#initialize flask app and binance client
app = Flask(__name__)
client = Client(config.API_KEY, config.API_SECRET)

@app.route("/")
def index():
    balances = client.get_account()['balances']

    balances = [balance for balance in balances if 'BTC' == balance['asset'] or 'ETH' == balance['asset'] or 'USDT' == balance['asset']]

    exchangeInfo = client.get_exchange_info()
    symbols = exchangeInfo['symbols']
    symbols = sorted(symbols, key = lambda i: i['symbol'])
    print(type(symbols[1]))

    return render_template("index.html", balances = balances, symbols = symbols)

@app.route("/test")
def test():
    return "route test"

@app.route('/buy')
def buyOrder():
    params = {
        'symbol': 'USDTTRY',
        'side': 'SELL',
        'type': 'LIMIT',
        'timeInForce': 'GTC',
        'quantity': 1,
        'price': 14
    }

    # info = client.get_symbol_info('USDTTRY')
    # print(info)
    orderResponse = client.create_test_order(**params)

    return orderResponse
    