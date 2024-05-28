import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf


tsmc = yf.download("2330.TW", start = "2021-01-01")
 
#清理資料
#需要成交股數、開盤價、最高價、最低價、收盤價的資料
#並使用Date當作我們的索引值
 
#tsmc.index = pd.to_datetime(tsmc['Date'])
tsmc = tsmc[['Volume','Open','High','Low','Close']]
tsmc.columns = ['Volume','Open','High','Low','Close']
tsmc['Close'] = pd.to_numeric(tsmc['Close'])
print(tsmc)

#分別計算7天,15天與30天的移動平均線
tsmc['MA_7'] = tsmc['Close'].rolling(7).mean()
tsmc['MA_15'] = tsmc['Close'].rolling(15).mean()
tsmc['MA_30'] = tsmc['Close'].rolling(30).mean()

#分別計算12天,26天的指數移動平均線
tsmc['EMA_12'] = tsmc['Close'].ewm(span=12).mean()
tsmc['EMA_26'] = tsmc['Close'].ewm(span=26).mean()

#計算MACD指標
tsmc['DIF'] = tsmc['EMA_12'] - tsmc['EMA_26']
tsmc['MACD'] = tsmc['DIF'].ewm(span=9).mean()
tsmc['DIF-MACD'] = tsmc['DIF'] - tsmc['MACD']

#畫圖
fig,ax = plt.subplots(3,1,figsize=(10,10))
plt.subplots_adjust(hspace=0.8)
#圖一
tsmc['MA_7'].plot(ax=ax[0])
tsmc['MA_15'].plot(ax=ax[0])
tsmc['MA_30'].plot(ax=ax[0])
tsmc['Close'].plot(ax=ax[0])
ax[0].legend()
#圖二
tsmc['EMA_12'].plot(ax=ax[1])
tsmc['EMA_26'].plot(ax=ax[1])
tsmc['Close'].plot(ax=ax[1])
ax[1].legend()
#圖三
tsmc['DIF'].plot(ax=ax[2])
tsmc['MACD'].plot(ax=ax[2])
ax[2].fill_between(tsmc.index,0,tsmc['DIF-MACD'])
ax[2].legend()
plt.show()