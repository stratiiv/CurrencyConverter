import json
from decimal import Decimal
from typing import Tuple
import requests


EXTERNAL_API_KEY = "8EZqkBwoYSJKzmUaA3lq53BvWNkWXTu9AhKNWaoj"


def convert_currency(from_curr: str,
                     to_curr: str,
                     amount: Decimal) -> Tuple[Decimal]:
    """Converts given currency to choosen"""
    r = requests.get("https://api.currencyapi.com/v3/latest"
                     f"?apikey={EXTERNAL_API_KEY}"
                     f"&base_currency={from_curr}"
                     f"&currencies={to_curr}")
    r.raise_for_status()
    currency_data = json.loads(r.text).get("data")
    exchange_rate = Decimal(list(currency_data.values())[0]["value"])
    return amount * exchange_rate, exchange_rate


def check_query_params(from_curr: str, to_curr: str, amount: str) -> bool:
    """Check if required GET method params are present"""
    return all([from_curr, to_curr, amount])