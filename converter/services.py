import requests
import json

EXTERNAL_API_KEY = "8EZqkBwoYSJKzmUaA3lq53BvWNkWXTu9AhKNWaoj"


def convert_currency(from_curr: str, to_curr: str, amount: float) -> float:
    r = requests.get("https://api.currencyapi.com/v3/latest"
                     f"?apikey={EXTERNAL_API_KEY}"
                     f"&base_currency={from_curr}"
                     f"&currencies={to_curr}")
    if r.status_code != 200:
        return -1
    currency_data = json.loads(r.text).get("data")
    exchange_rate = list(currency_data.values())[0]["value"]
    return amount * exchange_rate


# print(convert_currency("USD", "UAH", 22))