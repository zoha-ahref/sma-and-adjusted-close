import yfinance as yf
import datetime as dt
import pandas as pd
from pandas_datareader import data as pdr


yf.pdr_override()

stock = input("Enter a stock ticker symbol: ")
print(stock)

start_year = 2020
start_month = 1
start_day = 1

start = dt.datetime(start_year, start_month, start_day)
now = dt.datetime.now()

df = pdr.get_data_yahoo(stock, start, now)


ma = 50
sma = "Sma_" + str(ma)
df[sma]= df.iloc[:, 4].rolling(window=ma).mean()
df = df.iloc[ma:]

count_higher = 0
count_lower = 0

for i in df.index:
    # print(df["Adj Close"][i]) #GET adjested close values for stoc
    # print(df[sma][i]) #get simple moving average values
    if(df["Adj Close"][i] > df[sma][i]):
        print("The Close is higher")
        count_higher += 1
    else:
        print("The Close is lower")
        count_lower += 1
print(count_higher)
print(count_lower)