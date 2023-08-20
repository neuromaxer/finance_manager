from trades.models import Trade
from django.forms.models import model_to_dict
from collections import defaultdict
from typing import List


class TradeTable:
    def __init__(self) -> None:
        self.trade_list = [model_to_dict(trade) for trade in Trade.objects.all()]
        self.open_positions_list = self.get_open_positions()
        print("Trade List: ", self.trade_list)

    def get_open_positions(self) -> List[dict]:
        open_positions = defaultdict(lambda: 0)

        for trade in self.trade_list:
            print("Trade: ", trade)
            if trade["type"] == "buy":
                open_positions[trade["symbol"]] += trade["quantity"]
            elif trade["type"] == "sell":
                open_positions[trade["symbol"]] -= trade["quantity"]
            else:
                raise Exception(f"Invalid trade type {trade['type']}")

        open_positions_list = (
            [
                {"symbol": symbol, "quantity": quantity}
                for symbol, quantity in open_positions.items()
            ]
            if open_positions
            else []
        )

        return open_positions_list
