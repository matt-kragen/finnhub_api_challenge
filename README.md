# Finnhub Challenge

> This is a small chellenge based on the Finnhub API

## Challenge

Write a Python script to accomplish the following tasks.

Use the https://finnhub.io/ free stock quote API to query current stock prices for specific tech companies. Do not use their python package, use the `requests` package in
Python.

Get the latest price for Apple, Amazon, Netflix, Facebook, Google. Between these, find the stock that moved the most percentage points from yesterday. Call this stock most_volatile_stock.

Save the following information for the most_volatile_stock to a CSV file with the following rows (include header).

```csv
stock_symbol,percentage_change,current_price,last_close_price
AAPL, 13.2, 120.5, 150
```
