import requests
import json
import pandas as pd
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns

API_KEY = "nvx0YyAuFwP430opcjKsrlHidSSItMQz"
our_stocks = ["AAPL", "OXY", "TSLA", "HPQ", "XOM"]

def getdata(ticker):
    price_url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}?serietype=line&timeseries=3600&apikey={API_KEY}"

    stock_prices = requests.get(price_url)
    stock_prices=stock_prices.json()
    raw_list=[]
    percent_changes=[]

    for date in stock_prices['historical']:
        raw_list.append(int(date['close']))
    #for i in range(len(raw_list)-1):
        #percent_changes.append((raw_list[i]-raw_list[i+1])/raw_list[i+1]*100)
    esg_url = f"https://financialmodelingprep.com/api/v4/esg-environmental-social-governance-data?symbol={ticker}&limit=1&timeseries=1&apikey={API_KEY}"

    esg_info = requests.get(esg_url)
    esg_info = esg_info.json()[0]
    return raw_list, esg_info

stock_prices =[]
for stock in our_stocks:
    a,b = getdata(stock)
    stock_prices.append({"ticker": stock, "historical": a})

df =  pd.DataFrame({item["ticker"]: item["historical"] for item in stock_prices})
print(df)

mu = expected_returns.mean_historical_return(df) 
S = risk_models.sample_cov(df)

print(mu)
print(S)






