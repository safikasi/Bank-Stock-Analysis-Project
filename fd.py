from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly
import cufflinks as cf
import datetime

%matplotlib inline

start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2016, 1, 1)

# Bank of America
BAC = data.DataReader("BAC", 'google', start, end)

# CitiGroup
C = data.DataReader("C", 'google', start, end)

# Goldman Sachs
GS = data.DataReader("GS", 'google', start, end)

# JPMorgan Chase
JPM = data.DataReader("JPM", 'google', start, end)

# Morgan Stanley
MS = data.DataReader("MS", 'google', start, end)

# Wells Fargo
WFC = data.DataReader("WFC", 'google', start, end)

# Could also do this for a Panel Object
df = data.DataReader(['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC'],'google', start, end)

# Create a list of the ticker symbols (as strings) in alphabetical order.
tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']

# Use pd.concat to concatenate the bank dataframes together to a single data frame called bank_stocks. Set the keys argument equal to the tickers list.
bank_stocks = pd.concat([BAC, C, GS, JPM, MS, WFC],axis=1,keys=tickers)

# Set the column name levels
bank_stocks.columns.names = ['Bank Ticker','Stock Info']

# Check the head of the bank_stocks dataframe
bank_stocks.head()

# max Close price for each bank's stock throughout the time period
bank_stocks.xs(key='Close',axis=1,level='Stock Info').max()

# Create a new empty DataFrame called returns. This dataframe will contain the returns for each bank's stock.
returns = pd.DataFrame()

# use pandas pct_change() method on the Close column to create a column representing this return value. Create a for loop that goes and for each Bank Stock Ticker creates this returns column and set's it as a column in the returns DataFrame.
for tick in tickers:
    returns[tick+' Return'] = bank_stocks[tick]['Close'].pct_change()
returns.head()

# Create a pairplot using seaborn of the returns dataframe.
# returns[1:]
sns.pairplot(returns[1:])

# Using this returns DataFrame, figure out on what dates each bank stock had the best and worst single day returns.
# Worst Drop (4 of them on Inauguration day)
returns.idxmin()

# Best Single Day Gain
# citigroup stock split in May 2011, but also JPM day after inauguration.
returns.idxmax()

# standard deviation of the returns
# Citigroup riskiest
returns.std() 


# Very similar risk profiles, but Morgan Stanley or BofA
returns.ix['2015-01-01':'2015-12-31'].std()

# Create a distplot using seaborn of the 2015 returns for Morgan Stanley
sns.distplot(returns.ix['2015-01-01':'2015-12-31']['MS Return'],color='green',bins=100)

# Create a distplot using seaborn of the 2008 returns for CitiGroup
sns.distplot(returns.ix['2008-01-01':'2008-12-31']['C Return'],color='red',bins=100)

sns.set_style('whitegrid')
cf.go_offline()

# Create a line plot showing Close price for each bank for the entire index of time.
for tick in tickers:
    bank_stocks[tick]['Close'].plot(figsize=(12,4),label=tick)
plt.legend()

bank_stocks.xs(key='Close',axis=1,level='Stock Info').plot()

# plotly
bank_stocks.xs(key='Close',axis=1,level='Stock Info').iplot()

# Plot the rolling 30 day average against the Close Price for Bank Of America's stock for the year 2008
plt.figure(figsize=(12,6))
BAC['Close'].ix['2008-01-01':'2009-01-01'].rolling(window=30).mean().plot(label='30 Day Avg')
BAC['Close'].ix['2008-01-01':'2009-01-01'].plot(label='BAC CLOSE')
plt.legend()

# Create a heatmap of the correlation between the stocks Close Price.
sns.heatmap(bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True)

# seaborn's clustermap to cluster the correlations together
sns.clustermap(bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True)

close_corr = bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr()
close_corr.iplot(kind='heatmap',colorscale='rdylbu')

# Use .iplot(kind='candle) to create a candle plot of Bank of America's stock from Jan 1st 2015 to Jan 1st 2016.
BAC[['Open', 'High', 'Low', 'Close']].ix['2015-01-01':'2016-01-01'].iplot(kind='candle')

# Use .ta_plot(study='sma') to create a Simple Moving Averages plot of Morgan Stanley for the year 2015.
MS['Close'].ix['2015-01-01':'2016-01-01'].ta_plot(study='sma',periods=[13,21,55],title='Simple Moving Averages')

# Use .ta_plot(study='boll') to create a Bollinger Band Plot for Bank of America for the year 2015.
BAC['Close'].ix['2015-01-01':'2016-01-01'].ta_plot(study='boll')


