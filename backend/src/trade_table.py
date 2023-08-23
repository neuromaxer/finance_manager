from trades.models import Trade
from django.forms.models import model_to_dict
from collections import defaultdict
from typing import List
import yfinance as yf
from decimal import Decimal


class TradeTable:
    def __init__(self) -> None:
        self.trade_list = self.get_trade_list()
        self.open_positions_list = self.get_open_positions()
        print("Trade List: ", self.trade_list)

    @staticmethod
    def get_trade_list() -> List[dict]:
        return [model_to_dict(trade) for trade in Trade.objects.all()]

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

    def add_trade(self, trade_data: dict) -> None:
        # create a new trade instance
        current_price = self.get_current_price(trade_data)
        new_trade = Trade(
            symbol=trade_data["symbol"],
            quantity=int(trade_data["quantity"]),
            purchase_price=Decimal(str(trade_data["price"])),
            current_price=Decimal(str(current_price)),
            type=trade_data["type"],
            time=trade_data["time"],
        )

        # validate and save the new trade instance
        print("New trade: ", new_trade)
        new_trade.full_clean()
        new_trade.save()
        self.trade_list = self.get_trade_list()
        return new_trade

    @staticmethod
    def get_current_price(trade_data: dict):
        ticker = yf.Ticker(trade_data["symbol"])
        current_price = round(ticker.history().tail(1)["Close"].iloc[0], 3)

        print("Current price: ", current_price)
        print("Purchase price: ", Decimal(trade_data["price"]))
        return current_price
