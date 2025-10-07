import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json
def fetch_data(companies):
        
    counter=0
    Stock=pd.DataFrame()
    for ticker in companies:
        dat = yf.Ticker(ticker)

        Apnd=pd.DataFrame(dat.history(period='1mo')).tail(1)
        try: Apnd['Company']=dat.info['shortName']
        except Exception: Apnd['Company']=ticker
        
        Apnd['Ticker']=ticker
        Stock=Stock._append(Apnd)
        
        counter+=1


    Stock["daily_return"] = (((Stock["Close"]-Stock["Open"])/Stock["Open"]) * 100).round(2).astype(np.float64)
    Stock["price_range"] = (((Stock["High"] - Stock["Low"])/Stock["Low"]) * 100).round(2).astype(np.float64)
    Stock["volatility"] = (((Stock["High"] - Stock["Low"])/Stock["Close"]) * 100).round(2).astype(np.float64)
    columns_to_drop = ["Dividends", "Stock Splits", "Open", "High", "Low", "Close"]
    Stock = Stock.drop(columns=columns_to_drop)
    Stock = Stock.reset_index()
    Stock=Stock.sort_values(by=["Ticker","Date"], ascending=[True,False]).reset_index(drop=True)

    Stock["Date"]=pd.to_datetime(Stock["Date"]).dt.date
    print(Stock)
    print("✅ Data fetch completed!")
    return Stock


