from crypt import methods
from pydoc import cli
from flask import Flask, redirect, render_template, request, flash
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

    balances = [balance for balance in balances if 'BTC' == balance['asset'] or 'ETH' == balance['asset'] or 'USDT' == balance['asset']]

    exchangeInfo = client.get_exchange_info()
    symbols = exchangeInfo['symbols']
    symbols = sorted(symbols, key = lambda i: i['symbol'])
    print(type(symbols[1]))

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

@app.route('/buy', methods=['POST'])
def buyOrder():
    orderInfo = request.form
    try:
        orderResponse = client.order_limit_buy(
        symbol=orderInfo['symbols'],
        quantity=orderInfo['quantity'],
        price=orderInfo['price'])
    except Exception as e:
        flash(e.message, 'error')

    return redirect('/')
    