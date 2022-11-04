import requests
import json
import csv

api_key = "YOUR KEY HERE"
symbols = ["AAPL", "AMZN", "NFLX", "META", "GOOGL"]

def get_stock_data(symbol):
    url = "https://finnhub.io/api/v1/quote?symbol=" + symbol
    headers = {'X-Finnhub-Token': api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    data['symbol'] = symbol
    return data

data_set = map(get_stock_data, symbols)
most_volatile_stock = max(data_set, key=lambda x: x['dp'])

stock_symbol = most_volatile_stock['symbol']
percentage_change = most_volatile_stock['dp']
current_price = most_volatile_stock['c']
last_close_price = most_volatile_stock['pc']

header = ['stock_symbol', 'percentage_change', 'current_price', 'last_close_price']
data = [stock_symbol, percentage_change, current_price, last_close_price]

with open('mv_stock.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
