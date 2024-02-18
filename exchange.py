import requests
import os
import logging
from dateutil.parser import parse

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

ER_TOKEN = os.getenv('ER_TOKEN')

def get_all_exchange_rates_erapi(src):
    url = f"https://open.er-api.com/v6/latest/{src}"
    data = requests.get(url).json()
    if data["result"] == "success":
        last_updated_datetime = parse(data["time_last_update_utc"])
        exchange_rates = data["rates"]
    return last_updated_datetime, exchange_rates


def convert_currency_erapi(src, dst, amount):
    last_updated_datetime, exchange_rates = get_all_exchange_rates_erapi(src)
    return last_updated_datetime, exchange_rates[dst] * int(amount)


if __name__ == "__main__":
    source_currency = 'EUR'
    destination_currency = 'USD'
    amount = 100
    last_updated_datetime, exchange_rate = convert_currency_erapi(source_currency, destination_currency, amount)
    print("Last updated datetime:", last_updated_datetime)
    print(f"{amount} {source_currency} = {exchange_rate} {destination_currency}")