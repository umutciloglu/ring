var chart = LightweightCharts.createChart(document.getElementById("chart"), {
	width: 1000,
    height: 600,
	layout: {
		backgroundColor: '#0000',
		textColor: 'rgba(255, 255, 255, 0.9)',
	},
	grid: {
		vertLines: {
			color: 'rgba(197, 203, 206, 0.5)',
		},
		horzLines: {
			color: 'rgba(197, 203, 206, 0.5)',
		},
	},
	crosshair: {
		mode: LightweightCharts.CrosshairMode.Normal,
	},
	rightPriceScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
	},
	timeScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
	},
});

var candleSeries = chart.addCandlestickSeries({
  upColor: 'rgb(56, 142, 60)',
  downColor: 'rgb(239, 83, 80)',
  borderDownColor: 'rgb(0, 0, 0) ',
  borderUpColor: 'rgb(0, 0, 0)',
  wickDownColor: 'rgb(0, 0, 0)',
  wickUpColor: 'rgb(0, 0, 0)',
});

fetch('http://127.0.0.1:5000/historical-data')
		.then(response => response.json())
		.then((response) => {
			candleSeries.setData(response);
		})

var binanceSocket = new WebSocket("wss://stream.binance.com:9443/ws/btcusdt@kline_15m")

binanceSocket.onmessage = function(event){
	var message = JSON.parse(event.data)

	candleStick = message.k

	candleSeries.update({
		time: candleStick.t / 1000,
		open: candleStick.o,
		high: candleStick.h,
		low: candleStick.l,
		close: candleStick.c
	})

}