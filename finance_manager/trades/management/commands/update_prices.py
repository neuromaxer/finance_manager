from django.core.management.base import BaseCommand
from trades.services import StockPriceUpdater

class Command(BaseCommand):
    help = "Update prices for all trades"

    def handle(self, *args, **options):
        StockPriceUpdater.update_prices()