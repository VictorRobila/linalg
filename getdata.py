import requests
import json

API_KEY = "nvx0YyAuFwP430opcjKsrlHidSSItMQz"

def getdata(ticker):
    price_url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}?serietype=line&timeseries=3650&apikey={API_KEY}"
    
    stock_prices = requests.get(price_url)
    stock_prices=stock_prices.json()

    esg_url = f"https://financialmodelingprep.com/api/v4/esg-environmental-social-governance-data?symbol={ticker}&limit=1&timeseries=1&apikey={API_KEY}"

    esg_info = requests.get(esg_url)
    esg_info = esg_info.json()[0]
    return stock_prices, esg_info

a,b = getdata("AAPL")
print(a)
print(b)







