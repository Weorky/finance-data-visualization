# base
import numpy as np
import pandas as pd
 
# visual
import matplotlib.pyplot as plt
import mplfinance as mpf
import seaborn as sns

# time
import datetime as datetime

# data
import yfinance as yf

def stock_Kline(stock_id, start_date):
    data = yf.download(str(stock_id), start = str(start_date))
    mc = mpf.make_marketcolors(up='r', down='g', inherit=True)
    s  = mpf.make_mpf_style(base_mpf_style='yahoo', marketcolors=mc)
    kwargs = dict(type='candle', mav=(5, 10), volume=True, figratio=(16, 8), figscale=1.2, title = stock_id, style=s)
    return(mpf.plot(data, **kwargs))

stock_Kline('2330.TW', '2022-01-01')