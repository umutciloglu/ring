var binanceSocket = new WebSocket("wss://stream.binance.com:9443/ws/btcusdt@kline_1m")
            var tradeDiv = document.getElementById('ui')
            
            binanceSocket.onmessage = function(event)
            {
                var messageObject = JSON.parse(event.data)
                tradeDiv.append(messageObject.k.o)
            }