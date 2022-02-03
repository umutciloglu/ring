from crypt import methods
from pydoc import cli
from flask import Flask, render_template, request
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

@app.route('/buy', methods=['POST'])
def buyOrder():
    print(request.form)
    orderInfo = request.form

    orderResponse = client.order_limit_buy(
    symbol=orderInfo['symbols'],
    quantity=orderInfo['quantity'],
    price=orderInfo['price'])

    return orderResponse
    