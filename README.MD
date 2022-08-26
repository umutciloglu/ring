<h1>Ring</h1>
<p>This is an algo trading bot for binance that has a web UI. Note that right now this bot is far away from being finished and usable</p>
<h1>How to use </h1>
<p>Before starting to use the bot first download dependencies using

<code>$ pip install -r requirements.txt</code>

After you have install the dependincies you can use the bot right away but to accsess cli u must build the cli by going to your installation directory and calling

<code>$ sudo python CLI/setup.py develop</code>

After you have built the cli simply calling <code>$ ring run</code> would suffice.

If you want you can add <code>-d</code> flag and start the program on debug mode which is recommended if you plan to do any changes</p>

<h1>Backtesting</h1>
<p>For backtesting you can change the cerebro in backtraderTest.py and then call 

<code>$ ring backtest</code>

to run plot your current strategy results.

Don't forget to change the current feed of the cerebro as it's a local file not present at the repo.</p>