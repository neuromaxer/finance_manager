from django.shortcuts import render
from .models import Trade
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import yfinance as yf 

# Create your views here.

@csrf_exempt
def trade_list(request):
    if request.method == "GET":
        trades = Trade.objects.all()
        trade_list = [model_to_dict(trade) for trade in trades]
        print(trade_list)
        return JsonResponse(trade_list, safe=False)
    
    elif request.method == "POST":
        data = json.loads(request.body)
        print("Posted data: ", data)

        # get current price from yfinance
        ticker = yf.Ticker(data['symbol'])
        current_price = ticker.history().tail(1)['Close'].iloc[0]

        print("Current price: ", current_price)
        print("Purchase price: ", float(data['price']))

        # create a new trade instance
        new_trade = Trade(symbol=data['symbol'], quantity=int(data['quantity']), purchase_price=float(data['price']), current_price=current_price)

        # validate and save the new trade instance
        try:
            new_trade.full_clean()
            new_trade.save()
            trades = Trade.objects.all()
            trade_list = [model_to_dict(trade) for trade in trades]
            print(trade_list)
            return JsonResponse(model_to_dict(new_trade), status=201)
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        

    else:
        raise Exception("Unsupported method")

def trade_detail(request, pk):
    # we'll implement this later
    pass