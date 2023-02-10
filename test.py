import requests
import time


def scrape():
    response = requests.get(URL)
    response_json = response.json()
    return float(response_json["USD"]["last"])


URL = 'https://blockchain.info/ru/ticker'
last_price = None
start_time = time.time()
while True:
    latest_price = scrape()
    current_time = time.time()
    if current_time - start_time > 3600:
        start_time = current_time
    if latest_price != last_price:
        print("Последняя цена BTC: ", latest_price)
        last_price = latest_price
