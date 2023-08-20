import yfinance as yf

from .models import Trade

class StockPriceUpdater:
    @staticmethod
    def update_prices():
        symbols = Trade.objects.values_list('symbol', flat=True).distinct()
        data = yf.download(tickers=list(symbols), period='1d', interval='1m')
        for symbol in symbols:
            price = data['Close'][symbol][-1]
            Trade.objects.filter(symbol=symbol).update(current_price=price)