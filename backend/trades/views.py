from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from src.trade_table import TradeTable


# Create your views here.
@csrf_exempt
def trade_list(request):
    trade_table = TradeTable()
    if request.method == "GET":
        response_data = {
            "trades": trade_table.trade_list,
            "open_positions": trade_table.open_positions_list,
        }

        print("Response data: ", response_data)

        return JsonResponse(response_data, safe=False)

    elif request.method == "POST":
        trade_data = json.loads(request.body)
        print("Posted trade data: ", trade_data)

        new_trade = trade_table.add_trade(trade_data)
        return JsonResponse(model_to_dict(new_trade), status=201)

    else:
        raise Exception("Unsupported method")


def trade_detail(request, pk):
    # we'll implement this later
    pass
