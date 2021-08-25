import pandas_datareader as web
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns

currency = "INR"
metric = "Close"

startdate = dt.datetime(2019,6,1)
enddate = dt.datetime(2020,1,1)

crypto = ['BTC', 'ETH', 'MATIC', 'XRP' , 'DOGE' , 'TRX']
colnames = []

first = True

for ticker in crypto:
    data = web.DataReader(f"{ticker}-{currency}", "yahoo", startdate, enddate)
    if first:
        merged = data[[metric]].copy()
        colnames.append(ticker)
        merged.columns = colnames
        first = False
    else:
        merged = merged.join(data[metric])
        colnames.append(ticker)
        merged.columns = colnames

plt.yscale('log') # first show linear

for ticker in crypto:
    plt.plot(merged[ticker], label=ticker)

plt.legend(loc="upper right")

plt.show()

# # Correlation Heat Map

#print(merged)

#merged = merged.pct_change().corr(method='pearson')

#sns.heatmap(merged, annot=True, cmap="coolwarm")
#plt.show()