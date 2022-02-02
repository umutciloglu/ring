from flask import Flask, render_template
from binance.spot import Spot
import config, csv

#initialize flask app and binance client
app = Flask(__name__)
client = Spot(key=config.API_KEY, secret=config.API_SECRET)

@app.route("/")
def index():
    balances = client.account()['balances']

    balances = [balance for balance in balances if 'BTC' == balance['asset'] or 'ETH' == balance['asset'] or 'USDT' == balance['asset']]

    return render_template("index.html", balances = balances)

@app.route("/test")
def test():
    return "route test"