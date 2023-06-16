import os
from decimal import Decimal, ROUND_DOWN
from typing import Tuple
import requests


EXTERNAl_API_URL = "https://api.currencyapi.com/v3/latest"
EXTERNAL_API_KEY = os.environ.get("OPENWEATHER_KEY")


def get_exchange_rate(from_curr: str, to_curr: str) -> Decimal:
    """Gets exchange rate from external api"""
    params = {
        "apikey": EXTERNAL_API_KEY,
        "base_currency": from_curr,
        "currencies": to_curr
    }
    r = requests.get(EXTERNAl_API_URL, params=params)
    r.raise_for_status()
    data = r.json()
    exchange_rate = Decimal(data['data'][to_curr]['value'])
    return exchange_rate


def convert_currency(from_curr: str,
                     to_curr: str,
                     amount: Decimal) -> Tuple[Decimal]:
    """Converts given currency to choosen"""
    exchange_rate = get_exchange_rate(from_curr, to_curr)
    converted_amount = amount * exchange_rate
    # set precision
    converted_amount = converted_amount.quantize(Decimal("0.000000"),
                                                 rounding=ROUND_DOWN)
    return converted_amount, exchange_rate


def check_query_params(from_curr: str, to_curr: str, amount: str) -> bool:
    """Check if required GET method params are present"""
    return all([from_curr, to_curr, amount])

