from django.shortcuts import render
from .models import Trade
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import yfinance as yf 
from collections import defaultdict
from decimal import Decimal

# Create your views here.

@csrf_exempt
def trade_list(request):
    if request.method == "GET":
        trades = Trade.objects.all()
        trade_list = [model_to_dict(trade) for trade in trades]
        print('Trade List: ', trade_list)
        open_positions = defaultdict(lambda: 0)

        for trade in trade_list:
            print("Trade: ", trade)
            if trade["type"] == "buy":
                open_positions[trade['symbol']] += trade['quantity']
            elif trade["type"] == "sell":
                open_positions[trade['symbol']] -= trade['quantity']
            else:
                raise Exception(f"Invalid trade type {trade['type']}")

        open_positions_list = [{'symbol': symbol, 'quantity': quantity} for symbol, quantity in open_positions.items()] if open_positions else []

        response_data = {
            'trades': trade_list,
            'open_positions': open_positions_list,
        }

        print("Response data: ", response_data)

        return JsonResponse(response_data, safe=False)
    
    elif request.method == "POST":
        data = json.loads(request.body)
        print("Posted data: ", data)

        # get current price from yfinance
        ticker = yf.Ticker(data['symbol'])
        current_price = round(ticker.history().tail(1)['Close'].iloc[0], 3)

        print("Current price: ", current_price)
        print("Purchase price: ", Decimal(data['price']))

        # create a new trade instance
        new_trade = Trade(
            symbol=data['symbol'], 
            quantity=int(data['quantity']),
            purchase_price=Decimal(str(data['price'])),
            current_price=Decimal(str(current_price)), 
            type=data['type'],
            time=data['time']
            )

        # validate and save the new trade instance
        print("New trade: ", new_trade)
        new_trade.full_clean()
        new_trade.save()
        trades = Trade.objects.all()
        trade_list = [model_to_dict(trade) for trade in trades]
        print(trade_list)
        return JsonResponse(model_to_dict(new_trade), status=201)
    
    

    else:
        raise Exception("Unsupported method")

def trade_detail(request, pk):
    # we'll implement this later
    pass