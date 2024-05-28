import numpy
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress
import yfinance as yf

# stock_code format is 'xxxx.TW'
# start_date format is 'yyyy-mm-dd'
def trend_line(stock_code, start_date):
    df = yf.download(stock_code, start=start_date)
    df_temp = df.reset_index()

    while len(df_temp) >= 2:
        reg = linregress(x = df_temp.index, y = df_temp['Adj Close'])
        up_line = reg.intercept + reg.slope * df_temp.index
        df_temp = df_temp[df_temp['Adj Close'] < up_line]

    df["Low_Trend"] = reg.intercept + reg.slope * range(len(df))

    # 繪製收盤價和趨勢線
    df['Close'].plot(label='Adj Close Price')
    df['Low_Trend'].plot(label='Trend Line', linestyle='--')
    plt.legend()
    plt.show()

trend_line('2330.TW', '2022-01-01')